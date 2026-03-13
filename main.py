from fastmcp import FastMCP
from datetime import datetime
import random


def create_mcp():
    mcp = FastMCP("Utility MCP Server")

    @mcp.tool()
    def add(a: float, b: float) -> float:
        return a + b

    @mcp.tool()
    def subtract(a: float, b: float) -> float:
        return a - b

    @mcp.tool()
    def multiply(a: float, b: float) -> float:
        return a * b

    @mcp.tool()
    def divide(a: float, b: float):
        if b == 0:
            return "Division by zero not allowed"
        return a / b

    @mcp.tool()
    def current_time() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @mcp.tool()
    def random_number(min: int, max: int) -> int:
        return random.randint(min, max)

    return mcp


# expose server object
mcp = create_mcp()


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000
    )