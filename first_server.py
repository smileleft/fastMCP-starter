# first_server.py
from fastmcp import FastMCP
import asyncio

APP_CONFIG = {"theme": "dark", "version": "1.1", "feature_flags": ["new_dashboard"]}

USER_PROFILES = {
    101: {"name": "Alice", "status": "active"},
    102: {"name": "Bob", "status": "inactive"},
}

mcp = FastMCP(name="my first mcp server")

print("First FastMCP server is created.")

@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: int) -> dict:
    """Search User Profile with User ID."""
    return USER_PROFILES.get(user_id, {"error": "cannot find user."})

@mcp.resource("data://config")
def get_config() -> dict:
  """application config"""
  return APP_CONFIG

@mcp.tool()
def greet(name: str) -> str:
  """simple greeting"""
  return f"Hello, {name}!"

@mcp.tool()
def add(a: int, b: init) -> int:
  """add two numbers."""
  return a + b

print("tool 'greet' and 'add' is added.")


@mcp.prompt("summarize")
async def summarize_prompt(text: str) -> list[dict]:
    """prompt for summarize requested text"""
    return [
        {"role": "system", "content": "당신은 요약에 능숙한 유용한 조수입니다."},
        {"role": "user", "content": f"다음 텍스트를 요약해 주세요:\n\n{text}"}
    ]

print("Prompt 'summarize' added.")


