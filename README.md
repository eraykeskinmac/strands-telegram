# Strands Telegram

[![PyPI version](https://badge.fury.io/py/strands-telegram.svg)](https://badge.fury.io/py/strands-telegram)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Comprehensive Telegram Bot API integration for Strands Agents**

A complete Telegram Bot API tool that provides seamless integration with Strands Agents, supporting all major Telegram Bot API operations with full flexibility and rich features.

## 🚀 Features

### 📨 **Message Operations**
- **Text Messages**: Send rich text with HTML/Markdown formatting
- **Media Support**: Photos, videos, audio, documents, voice messages
- **Interactive Elements**: Polls, dice games, location sharing, contact cards
- **Message Management**: Edit, delete, forward, copy, pin/unpin messages

### 🎮 **Interactive Features**
- **Inline Keyboards**: Create interactive button menus
- **Custom Keyboards**: Reply keyboards with custom layouts
- **Callback Queries**: Handle button press events
- **Rich Media**: Stickers, animations, and multimedia content

### 👥 **Group & Channel Management**
- **User Management**: Kick, ban, unban, promote users
- **Permissions**: Set chat permissions and restrictions
- **Administration**: Manage chat settings, photos, descriptions
- **Member Info**: Get chat members, administrators, and statistics

### 🔧 **Bot Management**
- **Webhook Support**: Set up and manage webhooks
- **Bot Information**: Get bot details and configuration
- **Updates Handling**: Retrieve and process bot updates
- **File Operations**: Upload, download, and manage files

## 📦 Installation

```bash
pip install strands-telegram
```

## 🤖 Bot Setup

Before using this tool, you need to create a Telegram bot and get an API token:

### 1. Create a Telegram Bot

1. **Open Telegram** and search for `@BotFather`
2. **Start a chat** with BotFather by clicking `/start`
3. **Create new bot** with `/newbot` command
4. **Choose a name** for your bot (e.g., "My Awesome Bot")
5. **Choose a username** for your bot (must end with "bot", e.g., "myawesomebot")
6. **Save the token** - BotFather will give you a token like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`

### 2. Configure Bot Settings (Optional)

You can customize your bot using BotFather commands:
- `/setdescription` - Set bot description
- `/setcommands` - Set bot commands menu
- `/setprivacy` - Enable/disable privacy mode for groups
- `/setjoingroups` - Allow bot to be added to groups

### 3. Get Your Bot Token

The token from BotFather is your `TELEGRAM_BOT_TOKEN`. Keep it secure!

### 4. Set Environment Variable

```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
```

### 📚 Official Documentation

- **Telegram Bots Guide:** https://core.telegram.org/bots
- **Telegram Bot API:** https://core.telegram.org/bots/api
- **Full Telegram API:** https://core.telegram.org/api

## 🛠️ Usage

### Quick Start

```python
from strands import Agent
from strands_telegram import telegram

# Create agent with Telegram tool
agent = Agent(tools=[telegram])

# Send a message
agent.tool.telegram(
    action="send_message",
    chat_id="@username",
    text="Hello from Strands! 🚀"
)
```

### Environment Setup

```bash
# Set your Telegram Bot Token (get from @BotFather)
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
```

### Advanced Examples

#### Interactive Keyboard
```python
# Send message with inline keyboard
agent.tool.telegram(
    action="send_message",
    chat_id="123456789",
    text="Choose an option:",
    inline_keyboard=[
        [{"text": "Option 1", "callback_data": "opt1"}],
        [{"text": "Option 2", "callback_data": "opt2"}]
    ]
)
```

#### Send Photo with Caption
```python
# Send photo from local file
agent.tool.telegram(
    action="send_photo",
    chat_id="123456789",
    file_path="/path/to/photo.jpg",
    text="Check out this amazing photo! 📸"
)

# Send photo from URL
agent.tool.telegram(
    action="send_photo",
    chat_id="123456789",
    file_url="https://example.com/photo.jpg",
    text="Photo from the web 🌐"
)
```

#### Create Poll
```python
# Create a poll
agent.tool.telegram(
    action="send_poll",
    chat_id="123456789",
    question="What's your favorite Strands feature?",
    options=["AI Tools", "Multi-agent", "Workflows", "All of them!"]
)
```

#### Group Management
```python
# Promote user to admin
agent.tool.telegram(
    action="promote_chat_member",
    chat_id="-100123456789",
    user_id=987654321
)

# Set chat permissions
agent.tool.telegram(
    action="set_chat_permissions",
    chat_id="-100123456789",
    permissions={
        "can_send_messages": True,
        "can_send_media_messages": False
    }
)
```

## 📋 Supported Actions

### Message Operations
- `send_message` - Send text messages
- `send_photo` - Send photos
- `send_video` - Send videos  
- `send_audio` - Send audio files
- `send_document` - Send documents
- `send_voice` - Send voice messages
- `send_sticker` - Send stickers
- `send_location` - Send location coordinates
- `send_contact` - Send contact information
- `send_poll` - Create polls
- `send_dice` - Send dice animations

### Message Management
- `edit_message` - Edit message text
- `delete_message` - Delete messages
- `forward_message` - Forward messages
- `copy_message` - Copy messages
- `pin_message` - Pin messages
- `unpin_message` - Unpin messages

### Bot Information
- `get_me` - Get bot information
- `get_updates` - Get bot updates
- `get_chat` - Get chat information
- `get_chat_member` - Get chat member info
- `get_chat_administrators` - Get chat administrators

### Webhook Management
- `set_webhook` - Set webhook URL
- `delete_webhook` - Delete webhook
- `get_webhook_info` - Get webhook information

### Group/Channel Management
- `kick_chat_member` - Remove members
- `unban_chat_member` - Unban members
- `restrict_chat_member` - Restrict members
- `promote_chat_member` - Promote to admin
- `set_chat_permissions` - Set permissions
- `set_chat_title` - Change chat title
- `set_chat_description` - Set description
- `leave_chat` - Leave chat

### File Operations
- `get_file` - Get file information
- `download_file` - Download files

## 🔒 Security & Best Practices

### Token Security
- **Never hardcode tokens** in your code
- **Use environment variables** for bot tokens
- **Rotate tokens regularly** for production use

### Error Handling
The tool provides comprehensive error handling:
```python
result = agent.tool.telegram(action="send_message", chat_id="invalid", text="test")
if result["status"] == "error":
    print(f"Error: {result['content'][0]['text']}")
```

### Rate Limiting
- Telegram has rate limits (30 messages/second to different chats)
- The tool handles basic rate limiting
- For high-volume bots, implement additional rate limiting

## 🌟 Integration with Strands Agents

This tool is designed to work seamlessly with Strands Agents:

```python
from strands import Agent
from strands_telegram import telegram

# Agent with Telegram capabilities
agent = Agent(
    system_prompt="You are a helpful Telegram bot assistant.",
    tools=[telegram]
)

# Agent can now use Telegram in conversations
response = agent("Send a welcome message to the user")
```

## 📚 API Reference

### telegram(action, **kwargs)

**Parameters:**
- `action` (str): The Telegram API action to perform
- `chat_id` (str|int): Target chat ID or username
- `text` (str): Message text content  
- `parse_mode` (str): Text parsing mode (HTML, Markdown, MarkdownV2)
- `file_path` (str): Local file path for uploads
- `file_url` (str): URL for remote files
- `inline_keyboard` (List[List[Dict]]): Inline keyboard markup
- Additional parameters specific to each action

**Returns:**
- `Dict` with status and response content

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### Development Setup
```bash
git clone https://github.com/yourusername/strands-telegram
cd strands-telegram
pip install -e ".[dev]"
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [Strands Agents Documentation](https://strandsagents.com)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [PyPI Package](https://pypi.org/project/strands-telegram/)
- [GitHub Repository](https://github.com/yourusername/strands-telegram)

## 📞 Support

- Create an issue on GitHub for bug reports
- Join our community discussions for questions
- Check the Strands Agents documentation for integration help

---

**Made with ❤️ for the Strands Agents community**