from fastmcp import FastMCP
from datetime import datetime
import random

mcp = FastMCP("Utility MCP Server")

# Tool 1
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b


# Tool 2
@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b


# Tool 3
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b


# Tool 4
@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        return "Division by zero not allowed"
    return a / b


# Tool 5
@mcp.tool()
def current_time() -> str:
    """Get current system time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Tool 6
@mcp.tool()
def random_number(min: int, max: int) -> int:
    """Generate random number"""
    return random.randint(min, max)


if __name__ == "__main__":
    mcp.run(transport='streamable-http',host="0.0.0.0",port=8000)
