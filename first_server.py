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
  
