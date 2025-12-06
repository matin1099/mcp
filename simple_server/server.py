from mcp.server.fastmcp import FastMCP
import sys
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",
    port=8050,
)

@mcp.tool()
def add_two_number(a:int,b:int)->int:
    return int(a+b)

@mcp.tool()
def subtract_two_number(a:int,b:int)->int:
    return int(a-b)

@mcp.tool()
def multiply_two_number(a:int,b:int)->int:
    return int(a*b)

@mcp.tool()
def divide_two_number(a:int,b:int)-> str | int:
    if b == 0:
        return "Cannot divide by zero"
    else:
        return int(a/b)


if __name__ == "__main__":
    transport = 'stdio'
    if transport == 'stdio':
        print("run server with standard transport.",file=sys.stderr)
        mcp.run(transport="stdio")
    elif transport == 'sse':
        print("run server with sse transport.",file=sys.stderr)
        mcp.run(transport="sse")

    else:
        raise ValueError(f"transport must be 'stdio' or 'sse' but got {transport}",file=sys.stderr)