"""
Tests for Telegram Bot API Tool
==============================

Comprehensive test suite for the Telegram tool covering:
- Basic functionality
- Error handling
- API method mapping
- Parameter validation
- Response formatting
- Environment variable handling
"""

import json
import os
import tempfile
from unittest.mock import Mock, patch

import pytest
import responses
from strands_telegram import telegram


class TestTelegramTool:
    """Test suite for the Telegram tool."""

    def setup_method(self):
        """Set up test environment."""
        self.test_token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
        self.test_chat_id = "123456789"
        self.base_url = f"https://api.telegram.org/bot{self.test_token}"

    @patch.dict(os.environ, {"TELEGRAM_BOT_TOKEN": ""})
    def test_missing_token_error(self):
        """Test error when bot token is missing."""
        result = telegram(action="send_message", chat_id=self.test_chat_id, text="test")

        assert result["status"] == "error"
        assert "Bot Token not provided" in result["content"][0]["text"]

    @responses.activate
    @patch.dict(
        os.environ, {"TELEGRAM_BOT_TOKEN": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}
    )
    def test_send_message_success(self):
        """Test successful message sending."""
        # Mock successful API response
        responses.add(
            responses.POST,
            f"{self.base_url}/sendMessage",
            json={"ok": True, "result": {"message_id": 123, "text": "test"}},
            status=200,
        )

        result = telegram(
            action="send_message", chat_id=self.test_chat_id, text="test message"
        )

        assert result["status"] == "success"
        assert "send_message successful" in result["content"][0]["text"]
        assert "telegram_response" in result
        assert result["telegram_response"]["message_id"] == 123

    @responses.activate
    @patch.dict(
        os.environ, {"TELEGRAM_BOT_TOKEN": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}
    )
    def test_send_message_with_keyboard(self):
        """Test sending message with inline keyboard."""
        responses.add(
            responses.POST,
            f"{self.base_url}/sendMessage",
            json={"ok": True, "result": {"message_id": 124}},
            status=200,
        )

        keyboard = [
            [{"text": "Button 1", "callback_data": "btn1"}],
            [{"text": "Button 2", "callback_data": "btn2"}],
        ]

        result = telegram(
            action="send_message",
            chat_id=self.test_chat_id,
            text="Choose option:",
            inline_keyboard=keyboard,
        )

        assert result["status"] == "success"

        # Check that keyboard was included in request
        request_data = json.loads(responses.calls[0].request.body)
        assert "reply_markup" in request_data
        reply_markup = json.loads(request_data["reply_markup"])
        assert reply_markup["inline_keyboard"] == keyboard

    @responses.activate
    @patch.dict(
        os.environ, {"TELEGRAM_BOT_TOKEN": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}
    )
    def test_send_photo_with_file_path(self):
        """Test sending photo from file path."""
        responses.add(
            responses.POST,
            f"{self.base_url}/sendPhoto",
            json={"ok": True, "result": {"message_id": 125}},
            status=200,
        )

        # Create temporary image file
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp_file:
            tmp_file.write(b"fake image data")
            tmp_file_path = tmp_file.name

        try:
            result = telegram(
                action="send_photo",
                chat_id=self.test_chat_id,
                file_path=tmp_file_path,
                text="Test photo",
            )

            assert result["status"] == "success"
        finally:
            # Clean up temporary file
            os.unlink(tmp_file_path)

    @responses.activate
    @patch.dict(
        os.environ, {"TELEGRAM_BOT_TOKEN": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}
    )
    def test_send_photo_with_url(self):
        """Test sending photo from URL."""
        responses.add(
            responses.POST,
            f"{self.base_url}/sendPhoto",
            json={"ok": True, "result": {"message_id": 126}},
            status=200,
        )

        result = telegram(
            action="send_photo",
            chat_id=self.test_chat_id,
            file_url="https://example.com/photo.jpg",
            text="Photo from URL",
        )

        assert result["status"] == "success"

    @responses.activate
    @patch.dict(
        os.environ, {"TELEGRAM_BOT_TOKEN": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}
    )
    def test_send_poll(self):
        """Test creating a poll."""
        responses.add(
            responses.POST,
            f"{self.base_url}/sendPoll",
            json={"ok": True, "result": {"message_id": 127, "poll": {}}},
            status=200,
        )

        result = telegram(
            action="send_poll",
            chat_id=self.test_chat_id,
            question="What's your favorite color?",
            options=["Red", "Blue", "Green", "Yellow"],
        )

        assert result["status"] == "success"

        # Verify poll parameters
        request_data = json.loads(responses.calls[0].request.body)
        assert request_data["question"] == "What's your favorite color?"
        assert json.loads(request_data["options"]) == ["Red", "Blue", "Green", "Yellow"]

    @responses.activate
    @patch.dict(
        os.environ, {"TELEGRAM_BOT_TOKEN": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}
    )
    def test_get_me(self):
        """Test getting bot information."""
        bot_info = {
            "id": 123456789,
            "is_bot": True,
            "first_name": "TestBot",
            "username": "test_bot",
        }

        responses.add(
            responses.POST,
            f"{self.base_url}/getMe",
            json={"ok": True, "result": bot_info},
            status=200,
        )

        result = telegram(action="get_me")

        assert result["status"] == "success"
        assert result["telegram_response"] == bot_info

    @responses.activate
    @patch.dict(
        os.environ, {"TELEGRAM_BOT_TOKEN": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}
    )
    def test_telegram_api_error(self):
        """Test handling of Telegram API errors."""
        responses.add(
            responses.POST,
            f"{self.base_url}/sendMessage",
            json={
                "ok": False,
                "error_code": 400,
                "description": "Bad Request: chat not found",
            },
            status=200,
        )

        result = telegram(action="send_message", chat_id="invalid_chat_id", text="test")

        assert result["status"] == "error"
        assert "chat not found" in result["content"][0]["text"]
        assert result["error_code"] == 400

    @responses.activate
    @patch.dict(
        os.environ, {"TELEGRAM_BOT_TOKEN": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}
    )
    def test_http_error(self):
        """Test handling of HTTP errors."""
        responses.add(
            responses.POST,
            f"{self.base_url}/sendMessage",
            body="Internal Server Error",
            status=500,
        )

        result = telegram(action="send_message", chat_id=self.test_chat_id, text="test")

        assert result["status"] == "error"
        assert "HTTP error: 500" in result["content"][0]["text"]

    def test_invalid_action(self):
        """Test error for invalid action."""
        with patch.dict(os.environ, {"TELEGRAM_BOT_TOKEN": self.test_token}):
            result = telegram(action="invalid_action")

            assert result["status"] == "error"
            assert "Unknown action: invalid_action" in result["content"][0]["text"]

    @responses.activate
    @patch.dict(
        os.environ, {"TELEGRAM_BOT_TOKEN": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}
    )
    def test_custom_api_call(self):
        """Test custom API method call."""
        responses.add(
            responses.POST,
            f"{self.base_url}/customMethod",
            json={"ok": True, "result": {"custom": "response"}},
            status=200,
        )

        result = telegram(
            action="custom",
            method="customMethod",
            custom_params={"param1": "value1", "param2": "value2"},
        )

        assert result["status"] == "success"

    def test_custom_action_missing_method(self):
        """Test custom action without method parameter."""
        with patch.dict(os.environ, {"TELEGRAM_BOT_TOKEN": self.test_token}):
            result = telegram(action="custom")

            assert result["status"] == "error"
            assert "method parameter required" in result["content"][0]["text"]

    @responses.activate
    @patch.dict(
        os.environ, {"TELEGRAM_BOT_TOKEN": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}
    )
    def test_download_file_missing_path(self):
        """Test download_file without file_path parameter."""
        result = telegram(action="download_file")

        assert result["status"] == "error"
        assert "file_path parameter required" in result["content"][0]["text"]

    @responses.activate
    @patch.dict(
        os.environ, {"TELEGRAM_BOT_TOKEN": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}
    )
    def test_download_file_success(self):
        """Test successful file download."""
        file_content = b"test file content"

        responses.add(
            responses.GET,
            f"https://api.telegram.org/file/bot{self.test_token}/path/to/file.txt",
            body=file_content,
            status=200,
        )

        result = telegram(
            action="download_file", custom_params={"file_path": "path/to/file.txt"}
        )

        assert result["status"] == "success"
        assert "File downloaded successfully" in result["content"][0]["text"]
        assert result["file_data"] == file_content

    def test_api_key_parameter_override(self):
        """Test that api_key parameter overrides environment variable."""
        custom_token = "987654:XYZ-custom-token"

        with patch.dict(os.environ, {"TELEGRAM_BOT_TOKEN": self.test_token}):
            with patch("strands_telegram.telegram_tool.requests.post") as mock_post:
                mock_post.return_value.status_code = 200
                mock_post.return_value.json.return_value = {"ok": True, "result": {}}

                telegram(
                    action="send_message",
                    chat_id=self.test_chat_id,
                    text="test",
                    api_key=custom_token,
                )

                # Verify the custom token was used in the URL
                expected_url = f"https://api.telegram.org/bot{custom_token}/sendMessage"
                mock_post.assert_called_once()
                assert mock_post.call_args[0][0] == expected_url


class TestTelegramIntegration:
    """Integration tests for Telegram tool with Strands Agent."""

    def test_tool_import(self):
        """Test that the tool can be imported correctly."""
        from strands_telegram import telegram

        assert callable(telegram)

    def test_package_metadata(self):
        """Test package metadata accessibility."""
        import strands_telegram

        assert hasattr(strands_telegram, "__version__")
        assert strands_telegram.get_version() == "1.0.0"

        info = strands_telegram.get_info()
        assert info["name"] == "strands-telegram"
        assert "telegram" in info["description"].lower()


if __name__ == "__main__":
    pytest.main([__file__])
