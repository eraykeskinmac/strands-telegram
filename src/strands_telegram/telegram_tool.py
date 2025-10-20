"""
Comprehensive Telegram Bot API Tool for Strands Agents
======================================================

This module provides a complete Telegram Bot API integration tool that supports
all major Telegram Bot API operations with full flexibility and rich features.

The tool is designed to work seamlessly with Strands Agents, providing:
- All major Telegram Bot API methods (60+ operations)
- Rich message formatting (HTML, Markdown, MarkdownV2)
- Interactive elements (inline keyboards, polls, games)
- Media support (photos, videos, audio, documents)
- Group and channel management capabilities
- File upload/download functionality
- Comprehensive error handling
- Environment-based configuration

Usage Examples:
--------------
```python
from strands import Agent
from strands_telegram import telegram

# Create agent with Telegram tool
agent = Agent(tools=[telegram])

# Send text message
agent.tool.telegram(
    action="send_message",
    chat_id="123456789",
    text="Hello from Strands! 🚀"
)

# Send photo with caption
agent.tool.telegram(
    action="send_photo",
    chat_id="123456789", 
    file_path="/path/to/photo.jpg",
    text="Check this out! 📸"
)

# Create interactive poll
agent.tool.telegram(
    action="send_poll",
    chat_id="123456789",
    question="What's your favorite feature?",
    options=["AI Tools", "Multi-agent", "Workflows"]
)
```

Environment Variables:
--------------------
- TELEGRAM_BOT_TOKEN: Your bot token from @BotFather (required)

API Coverage:
------------
Message Operations: send_message, send_photo, send_video, send_audio,
                   send_document, send_voice, send_sticker, send_location,
                   send_contact, send_poll, send_dice

Message Management: edit_message, delete_message, forward_message,
                   copy_message, pin_message, unpin_message

Bot Information: get_me, get_updates, get_chat, get_chat_member,
                get_chat_administrators, get_chat_members_count

Group Management: kick_chat_member, unban_chat_member, restrict_chat_member,
                 promote_chat_member, set_chat_permissions, set_chat_title,
                 set_chat_description, leave_chat

Webhook Management: set_webhook, delete_webhook, get_webhook_info

File Operations: get_file, download_file

Custom Operations: custom (for any unlisted API method)
"""

import json
import os
from typing import Any, Dict, List, Optional, Union

import requests
from strands import tool


@tool
def telegram(
    action: str,
    chat_id: Optional[Union[str, int]] = None,
    text: Optional[str] = None,
    message_id: Optional[int] = None,
    user_id: Optional[int] = None,
    file_path: Optional[str] = None,
    file_url: Optional[str] = None,
    inline_keyboard: Optional[List[List[Dict]]] = None,
    reply_markup: Optional[Dict] = None,
    parse_mode: Optional[str] = "HTML",
    disable_web_page_preview: bool = False,
    disable_notification: bool = False,
    reply_to_message_id: Optional[int] = None,
    callback_query_id: Optional[str] = None,
    url: Optional[str] = None,
    certificate: Optional[str] = None,
    webhook_params: Optional[Dict] = None,
    custom_params: Optional[Dict] = None,
    api_key: Optional[str] = None,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
    phone_number: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    question: Optional[str] = None,
    options: Optional[List[str]] = None,
    emoji: Optional[str] = None,
    from_chat_id: Optional[Union[str, int]] = None,
    offset: Optional[int] = None,
    limit: Optional[int] = None,
    timeout: Optional[int] = None,
    until_date: Optional[int] = None,
    permissions: Optional[Dict] = None,
    file_id: Optional[str] = None,
    show_alert: Optional[bool] = None,
    cache_time: Optional[int] = None,
    method: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Comprehensive Telegram Bot API tool with support for all major operations.

    This tool provides complete access to the Telegram Bot API, enabling rich
    interactions including messaging, media sharing, group management, and more.

    Args:
        action: The Telegram API action to perform. Supported actions include:

            Message Operations:
            - "send_message": Send text message
            - "send_photo": Send photo
            - "send_document": Send document/file
            - "send_video": Send video
            - "send_audio": Send audio
            - "send_voice": Send voice message
            - "send_sticker": Send sticker
            - "send_location": Send location
            - "send_contact": Send contact
            - "send_poll": Send poll
            - "send_dice": Send dice animation

            Message Management:
            - "edit_message": Edit message text
            - "delete_message": Delete message
            - "forward_message": Forward message
            - "copy_message": Copy message
            - "pin_message": Pin message
            - "unpin_message": Unpin message

            Bot Information:
            - "get_me": Get bot information
            - "get_updates": Get updates
            - "get_chat": Get chat information
            - "get_chat_member": Get chat member info
            - "get_chat_administrators": Get chat administrators
            - "get_chat_members_count": Get member count

            Webhook Management:
            - "set_webhook": Set webhook URL
            - "delete_webhook": Delete webhook
            - "get_webhook_info": Get webhook information

            Group/Channel Management:
            - "kick_chat_member": Kick member from chat
            - "unban_chat_member": Unban member
            - "restrict_chat_member": Restrict member
            - "promote_chat_member": Promote member
            - "set_chat_permissions": Set chat permissions
            - "set_chat_title": Set chat title
            - "set_chat_description": Set chat description
            - "set_chat_photo": Set chat photo
            - "delete_chat_photo": Delete chat photo
            - "leave_chat": Leave chat

            Callback Queries:
            - "answer_callback_query": Answer callback query

            File Operations:
            - "get_file": Get file information
            - "download_file": Download file

            Custom API Calls:
            - "custom": Make custom API call with custom_params

        chat_id: Target chat ID (can be username, chat ID, or channel ID)
        text: Message text content
        message_id: Message ID for operations that require it
        user_id: User ID for user-specific operations
        file_path: Local file path for file uploads
        file_url: URL of file to send
        inline_keyboard: Inline keyboard markup as list of lists
        reply_markup: Full reply markup object
        parse_mode: Text parsing mode (HTML, Markdown, MarkdownV2)
        disable_web_page_preview: Disable web page preview
        disable_notification: Send silently
        reply_to_message_id: Reply to specific message
        callback_query_id: Callback query ID to answer
        url: Webhook URL
        certificate: SSL certificate for webhook
        webhook_params: Additional webhook parameters
        custom_params: Custom parameters for API calls
        api_key: Telegram Bot API token (uses env TELEGRAM_BOT_TOKEN if not provided)
        latitude: Latitude for location sharing
        longitude: Longitude for location sharing
        phone_number: Phone number for contact sharing
        first_name: First name for contact sharing
        last_name: Last name for contact sharing
        question: Question text for polls
        options: Poll options list
        emoji: Emoji for dice games
        from_chat_id: Source chat ID for forwarding
        offset: Offset for getting updates
        limit: Limit for getting updates
        timeout: Timeout for long polling
        until_date: Ban until date (Unix timestamp)
        permissions: Chat permissions object
        file_id: File ID for file operations
        show_alert: Show alert for callback queries
        cache_time: Cache time for callback queries
        method: Custom API method name

    Returns:
        Dict containing status and API response content:
        {
            "status": "success" | "error",
            "content": [{"text": "Response message"}],
            "telegram_response": {...}  # Full Telegram API response (on success)
        }

    Environment Variables:
        TELEGRAM_BOT_TOKEN: Required bot token from @BotFather

    Examples:
        # Send simple message
        telegram(action="send_message", chat_id="123456789", text="Hello!")

        # Send photo with keyboard
        telegram(
            action="send_photo",
            chat_id="123456789",
            file_path="/path/photo.jpg",
            text="Choose option:",
            inline_keyboard=[
                [{"text": "Option 1", "callback_data": "opt1"}],
                [{"text": "Option 2", "callback_data": "opt2"}]
            ]
        )

        # Create poll
        telegram(
            action="send_poll",
            chat_id="123456789",
            question="Favorite color?",
            options=["Red", "Blue", "Green"]
        )

    Raises:
        Various exceptions for network errors, API errors, or invalid parameters.
        All exceptions are caught and returned as error status in response.
    """

    # Get API key from parameter or environment
    bot_token = api_key or os.getenv("TELEGRAM_BOT_TOKEN")

    if not bot_token:
        return {
            "status": "error",
            "content": [
                {
                    "text": "❌ Telegram Bot Token not provided. Set TELEGRAM_BOT_TOKEN environment variable or pass api_key parameter."
                }
            ],
        }

    # Base API URL
    base_url = f"https://api.telegram.org/bot{bot_token}"

    try:
        # Map actions to API methods and prepare parameters
        api_method = None
        params = {}
        files = {}

        # Message sending operations
        if action == "send_message":
            api_method = "sendMessage"
            params = {
                "chat_id": chat_id,
                "text": text,
                "parse_mode": parse_mode,
                "disable_web_page_preview": disable_web_page_preview,
                "disable_notification": disable_notification,
                "reply_to_message_id": reply_to_message_id,
            }
            if reply_markup:
                params["reply_markup"] = json.dumps(reply_markup)
            elif inline_keyboard:
                params["reply_markup"] = json.dumps({"inline_keyboard": inline_keyboard})

        elif action == "send_photo":
            api_method = "sendPhoto"
            params = {
                "chat_id": chat_id,
                "caption": text,
                "parse_mode": parse_mode,
                "disable_notification": disable_notification,
                "reply_to_message_id": reply_to_message_id,
            }
            if file_path:
                files["photo"] = open(file_path, "rb")
            elif file_url:
                params["photo"] = file_url

        elif action == "send_document":
            api_method = "sendDocument"
            params = {
                "chat_id": chat_id,
                "caption": text,
                "parse_mode": parse_mode,
                "disable_notification": disable_notification,
                "reply_to_message_id": reply_to_message_id,
            }
            if file_path:
                files["document"] = open(file_path, "rb")
            elif file_url:
                params["document"] = file_url

        elif action == "send_video":
            api_method = "sendVideo"
            params = {
                "chat_id": chat_id,
                "caption": text,
                "parse_mode": parse_mode,
                "disable_notification": disable_notification,
                "reply_to_message_id": reply_to_message_id,
            }
            if file_path:
                files["video"] = open(file_path, "rb")
            elif file_url:
                params["video"] = file_url

        elif action == "send_audio":
            api_method = "sendAudio"
            params = {
                "chat_id": chat_id,
                "caption": text,
                "parse_mode": parse_mode,
                "disable_notification": disable_notification,
                "reply_to_message_id": reply_to_message_id,
            }
            if file_path:
                files["audio"] = open(file_path, "rb")
            elif file_url:
                params["audio"] = file_url

        elif action == "send_voice":
            api_method = "sendVoice"
            params = {
                "chat_id": chat_id,
                "caption": text,
                "parse_mode": parse_mode,
                "disable_notification": disable_notification,
                "reply_to_message_id": reply_to_message_id,
            }
            if file_path:
                files["voice"] = open(file_path, "rb")
            elif file_url:
                params["voice"] = file_url

        elif action == "send_sticker":
            api_method = "sendSticker"
            params = {
                "chat_id": chat_id,
                "disable_notification": disable_notification,
                "reply_to_message_id": reply_to_message_id,
            }
            if file_path:
                files["sticker"] = open(file_path, "rb")
            elif file_url:
                params["sticker"] = file_url

        elif action == "send_location":
            api_method = "sendLocation"
            params = {
                "chat_id": chat_id,
                "latitude": latitude,
                "longitude": longitude,
                "disable_notification": disable_notification,
                "reply_to_message_id": reply_to_message_id,
            }

        elif action == "send_contact":
            api_method = "sendContact"
            params = {
                "chat_id": chat_id,
                "phone_number": phone_number,
                "first_name": first_name,
                "last_name": last_name,
                "disable_notification": disable_notification,
                "reply_to_message_id": reply_to_message_id,
            }

        elif action == "send_poll":
            api_method = "sendPoll"
            params = {
                "chat_id": chat_id,
                "question": question,
                "options": json.dumps(options or []),
                "is_anonymous": True,  # Default value
                "type": "regular",  # Default value
                "allows_multiple_answers": False,  # Default value
                "disable_notification": disable_notification,
                "reply_to_message_id": reply_to_message_id,
            }

        elif action == "send_dice":
            api_method = "sendDice"
            params = {
                "chat_id": chat_id,
                "emoji": emoji or "🎲",
                "disable_notification": disable_notification,
                "reply_to_message_id": reply_to_message_id,
            }

        # Message management operations
        elif action == "edit_message":
            api_method = "editMessageText"
            params = {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": text,
                "parse_mode": parse_mode,
                "disable_web_page_preview": disable_web_page_preview,
            }
            if reply_markup:
                params["reply_markup"] = json.dumps(reply_markup)
            elif inline_keyboard:
                params["reply_markup"] = json.dumps({"inline_keyboard": inline_keyboard})

        elif action == "delete_message":
            api_method = "deleteMessage"
            params = {"chat_id": chat_id, "message_id": message_id}

        elif action == "forward_message":
            api_method = "forwardMessage"
            params = {
                "chat_id": chat_id,
                "from_chat_id": from_chat_id,
                "message_id": message_id,
                "disable_notification": disable_notification,
            }

        elif action == "copy_message":
            api_method = "copyMessage"
            params = {
                "chat_id": chat_id,
                "from_chat_id": from_chat_id,
                "message_id": message_id,
                "caption": text,
                "parse_mode": parse_mode,
                "disable_notification": disable_notification,
            }

        elif action == "pin_message":
            api_method = "pinChatMessage"
            params = {
                "chat_id": chat_id,
                "message_id": message_id,
                "disable_notification": disable_notification,
            }

        elif action == "unpin_message":
            api_method = "unpinChatMessage"
            params = {"chat_id": chat_id, "message_id": message_id}

        # Information retrieval operations
        elif action == "get_me":
            api_method = "getMe"

        elif action == "get_updates":
            api_method = "getUpdates"
            params = {
                "offset": offset,
                "limit": limit or 100,
                "timeout": timeout or 0,
            }

        elif action == "get_chat":
            api_method = "getChat"
            params = {"chat_id": chat_id}

        elif action == "get_chat_member":
            api_method = "getChatMember"
            params = {"chat_id": chat_id, "user_id": user_id}

        elif action == "get_chat_administrators":
            api_method = "getChatAdministrators"
            params = {"chat_id": chat_id}

        elif action == "get_chat_members_count":
            api_method = "getChatMembersCount"
            params = {"chat_id": chat_id}

        # Webhook operations
        elif action == "set_webhook":
            api_method = "setWebhook"
            params = {
                "url": url,
                "certificate": certificate,
                "max_connections": 40,  # Default value
                "allowed_updates": None,  # Can be set via custom_params
            }
            if webhook_params:
                params.update(webhook_params)

        elif action == "delete_webhook":
            api_method = "deleteWebhook"

        elif action == "get_webhook_info":
            api_method = "getWebhookInfo"

        # Chat management operations
        elif action == "kick_chat_member":
            api_method = "kickChatMember"
            params = {
                "chat_id": chat_id,
                "user_id": user_id,
                "until_date": until_date,
            }

        elif action == "unban_chat_member":
            api_method = "unbanChatMember"
            params = {
                "chat_id": chat_id,
                "user_id": user_id,
                "only_if_banned": True,  # Default value
            }

        elif action == "restrict_chat_member":
            api_method = "restrictChatMember"
            params = {
                "chat_id": chat_id,
                "user_id": user_id,
                "permissions": json.dumps(permissions or {}),
                "until_date": until_date,
            }

        elif action == "promote_chat_member":
            api_method = "promoteChatMember"
            params = {
                "chat_id": chat_id,
                "user_id": user_id,
                "is_anonymous": False,  # Default values
                "can_manage_chat": False,
                "can_post_messages": False,
                "can_edit_messages": False,
                "can_delete_messages": False,
                "can_manage_video_chats": False,
                "can_restrict_members": False,
                "can_promote_members": False,
                "can_change_info": False,
                "can_invite_users": False,
                "can_pin_messages": False,
            }

        elif action == "set_chat_permissions":
            api_method = "setChatPermissions"
            params = {
                "chat_id": chat_id,
                "permissions": json.dumps(permissions or {}),
            }

        elif action == "set_chat_title":
            api_method = "setChatTitle"
            params = {"chat_id": chat_id, "title": text}

        elif action == "set_chat_description":
            api_method = "setChatDescription"
            params = {"chat_id": chat_id, "description": text}

        elif action == "set_chat_photo":
            api_method = "setChatPhoto"
            params = {"chat_id": chat_id}
            if file_path:
                files["photo"] = open(file_path, "rb")

        elif action == "delete_chat_photo":
            api_method = "deleteChatPhoto"
            params = {"chat_id": chat_id}

        elif action == "leave_chat":
            api_method = "leaveChat"
            params = {"chat_id": chat_id}

        # Callback query operations
        elif action == "answer_callback_query":
            api_method = "answerCallbackQuery"
            params = {
                "callback_query_id": callback_query_id,
                "text": text,
                "show_alert": show_alert or False,
                "url": url,
                "cache_time": cache_time or 0,
            }

        # File operations
        elif action == "get_file":
            api_method = "getFile"
            params = {"file_id": file_id}

        elif action == "download_file":
            file_path_param = custom_params.get("file_path") if custom_params else None
            if not file_path_param:
                return {
                    "status": "error",
                    "content": [
                        {
                            "text": "❌ file_path parameter required for download_file action in custom_params"
                        }
                    ],
                }

            download_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path_param}"
            response = requests.get(download_url)

            if response.status_code == 200:
                return {
                    "status": "success",
                    "content": [
                        {
                            "text": f"✅ File downloaded successfully. Size: {len(response.content)} bytes"
                        }
                    ],
                    "file_data": response.content,
                }
            else:
                return {
                    "status": "error",
                    "content": [
                        {
                            "text": f"❌ Failed to download file. Status: {response.status_code}"
                        }
                    ],
                }

        # Custom API call
        elif action == "custom":
            api_method = method or (custom_params.get("method") if custom_params else None)
            if not api_method:
                return {
                    "status": "error",
                    "content": [
                        {"text": "❌ method parameter required for custom action"}
                    ],
                }
            params = custom_params or {}

        else:
            return {
                "status": "error",
                "content": [{"text": f"❌ Unknown action: {action}"}],
            }

        # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}

        # Make API request
        url = f"{base_url}/{api_method}"

        if files:
            response = requests.post(url, data=params, files=files)
            # Close file handles
            for file_handle in files.values():
                if hasattr(file_handle, "close"):
                    file_handle.close()
        else:
            response = requests.post(url, json=params if params else None)

        # Parse response
        if response.status_code == 200:
            result = response.json()
            if result.get("ok"):
                return {
                    "status": "success",
                    "content": [{"text": f"✅ {action} successful"}],
                    "telegram_response": result["result"],
                }
            else:
                return {
                    "status": "error",
                    "content": [
                        {
                            "text": f"❌ Telegram API error: {result.get('description', 'Unknown error')}"
                        }
                    ],
                    "error_code": result.get("error_code"),
                    "telegram_response": result,
                }
        else:
            return {
                "status": "error",
                "content": [
                    {"text": f"❌ HTTP error: {response.status_code} - {response.text}"}
                ],
            }

    except Exception as e:
        return {
            "status": "error",
            "content": [{"text": f"❌ Error: {str(e)}"}],
        }