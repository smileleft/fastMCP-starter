# first_server.py
from fastmcp import FastMCP
import asyncio

mcp = FastMCP(name="my first mcp server")

print("First FastMCP server is created.")

@mcp.tool()
def greet(name: str) -> str:
  """simple greeting"""
  return f"Hello, {name}!"

@mcp.tool()
def add(a: int, b: init) -> int:
  """add two numbers."""
  return a + b

print("tool 'greet' and 'add' is added.")
  
