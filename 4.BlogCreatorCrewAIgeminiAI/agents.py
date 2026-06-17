from crewai import Agent
from tools import tool
from dotenv import load_dotenv
import os

load_dotenv()

# CrewAI (via LiteLLM) specifically looks for the GEMINI_API_KEY environment variable. 
# This line ensures it's set using your existing GOOGLE_API_KEY.
os.environ["GEMINI_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Use the native CrewAI string format instead of LangChain's wrapper
gemini_llm = "gemini/gemini-3.1-flash-lite"

## Create a senior researcher agent 
news_researcher = Agent(
    role='Senior Researcher',
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could change "
        "the world."
    ),
    tools=[tool],
    llm=gemini_llm,  # Passing the LiteLLM string directly
    allow_delegation=True
)

## Creating the writer agent responsible for the new blog 
news_writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=gemini_llm,  # Passing the LiteLLM string directly
    allow_delegation=False
)