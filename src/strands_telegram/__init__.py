"""
Strands Telegram - Comprehensive Telegram Bot API integration for Strands Agents
==============================================================================

This package provides a complete Telegram Bot API tool that integrates seamlessly
with Strands Agents, supporting all major Telegram Bot API operations.

Key Features:
- Complete Telegram Bot API coverage (60+ methods)
- Rich message formats (HTML, Markdown, media)
- Interactive elements (keyboards, polls, games)
- Group and channel management
- File upload/download capabilities
- Webhook support
- Comprehensive error handling

Quick Start:
-----------
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

Environment Setup:
-----------------
Set your Telegram Bot Token (get from @BotFather):
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
```

For more examples and documentation, visit:
https://github.com/strands-agents/strands-telegram
"""

from .telegram import telegram

__version__ = "1.0.0"
__author__ = "Strands Community"
__email__ = "community@strandsagents.com"

__all__ = ["telegram"]


# Package metadata
def get_version():
    """Get package version."""
    return __version__


def get_info():
    """Get package information."""
    return {
        "name": "strands-telegram",
        "version": __version__,
        "description": "Telegram Bot API integration for Strands Agents",
        "author": __author__,
        "email": __email__,
        "url": "https://github.com/eraykeskinmac/strands-telegram",
    }
