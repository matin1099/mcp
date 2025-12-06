import asyncio
import nest_asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

nest_asyncio.apply()  # for jupyter!
def user_input(tool:str):
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))
    result  =  session.call_tool(tool,arguments={'a':firstNumber, 'b':secondNumber})
    print(f"answer for {tool} is {result.content[0].text}")

async def main():
    server_parameters = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    async with stdio_client(server_parameters) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f'\t- {tool.name}: {tool.description}')
            # chosen_tool = str(input("Select tool: "))
            # user_input(chosen_tool)

            result  = await session.call_tool("add_two_number", arguments={'a':2, 'b':3})
            print(f'Answer: {result.content[0].text}')
if __name__ == "__main__":
    asyncio.run(main())