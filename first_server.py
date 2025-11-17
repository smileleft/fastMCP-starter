# first_server.py
from fastmcp import FastMCP
from fastmcp import Client
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


async def test_server_locally():
    print("\n--- testing local server ---")
    # client for local server object.
    client = Client(mcp)

    # Use async client.
    async with client:
        # call 'greet' tool 
        greet_result = await client.call_tool("greet", {"name": "FastMCP 사용자"})
        print(f"greet resut: {greet_result}")

        # call 'add' tool 
        add_result = await client.call_tool("add", {"a": 5, "b": 7})
        print(f"add result: {add_result}")

        # read 'config' resource 
        config_data = await client.read_resource("data://config")
        print(f"config resource: {config_data}")

        # read user profile with template
        user_profile = await client.read_resource("users://101/profile")
        print(f"profile of user 101: {user_profile}")

        # 'summarize' 프롬프트 구조 얻기(여기서 LLM 호출을 실행하지 않음)
        prompt_messages = await client.get_prompt("summarize", {"text": "이것은 일부 텍스트입니다."})
        print(f"요약 프롬프트 구조: {prompt_messages}")


