import asyncio
import os
from pathlib import Path
from typing import Annotated

from agent_framework import tool, Agent
from agent_framework.azure import AzureOpenAIResponsesClient
from azure.identity.aio import AzureCliCredential
from pydantic import Field


async def main():
    os.system("cls" if os.name == "nt" else "clear")

    script_dir = Path(__file__).parent
    file_path = script_dir / "data.txt"

    with file_path.open("r") as file:
        data = file.read() + "\n"

    user_prompt = input(
        f"Here is the expenses data in your file:\n\n{data}\n\nWhat would you like me to do with it?\n\n"
    )

    await process_expenses_data(user_prompt, data)


async def process_expenses_data(prompt, expenses_data):
    credential = AzureCliCredential()

    async with Agent(
        client=AzureOpenAIResponsesClient(
            credential=credential,
            deployment_name=os.getenv("MODEL_DEPLOYMENT_NAME"),
            project_endpoint=os.getenv("PROJECT_ENDPOINT"),
        ),
        instructions="""You are an AI assistant for expense claim submission.
At the user's request, create an expense claim and use the plug-in function to send an email to expenses@contoso.com with the subject 'Expense Claim' and a body that contains itemized expenses with a total.
Then confirm to the user that you've done so. Don't ask for any more information from the user, just use the data provided to create the email.""",
        tools=[submit_claim],
    ) as agent:
        try:
            prompt_messages = [f"{prompt}: {expenses_data}"]
            response = await agent.run(prompt_messages)
            print(f"\n# Agent:\n{response}")
        except Exception as e:
            print(e)
        finally:
            await credential.close()


@tool(approval_mode="never_require")
def submit_claim(
    to: Annotated[str, Field(description="Who to send the email to")],
    subject: Annotated[str, Field(description="The subject of the email.")],
    body: Annotated[str, Field(description="The text body of the email.")],
):
    print("\nTo:", to)
    print("Subject:", subject)
    print(body, "\n")


if __name__ == "__main__":
    asyncio.run(main())
