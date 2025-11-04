from google.adk.agents.llm_agent import Agent, LlmAgent
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

def get_current_time():
    """Returns the current date and time as a string."""   
    return datetime.now().isoformat()   

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    tools=[get_current_time],
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge. if the user asks about the time use the get_current_time tool to get the current time.',
)

