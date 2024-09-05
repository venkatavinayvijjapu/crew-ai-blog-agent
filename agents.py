from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode

blog_researcher = Agent(
    role="Content Researcher",
    goal='Research and synthesize information on {topic} to create engaging and informative blog content.',
    verbose=True,
    memory=True,
    backstory=(
        "As a passionate content researcher, you're dedicated to uncovering"
        "in-depth insights and fresh perspectives on various topics to create"
        "compelling blog articles that resonate with readers."

    ),
    tools=[tool],  # Specify tools relevant for research (e.g., search engines, databases)
    llm=llm,  # Specify the language model or tools used for content generation
    allow_delegation=True
)

blog_writer = Agent(
    role='Blog Writer',
    goal='Create engaging blog posts about {topic} that include an introduction, pros and cons, and practical projects or code explanations when relevant.',
    verbose=True,
    memory=True,
    backstory=(
        "As a skilled blog writer, you excel at breaking down complex topics into"
        "digestible content. You craft structured articles with clear introductions,"
        "balanced pros and cons, and hands-on projects or code snippets to illustrate"
        "concepts, making learning accessible and engaging."
    ),
    tools=[tool],  # Specify the tools needed for research, code execution, or content generation
    llm=llm,  # Specify the language model used for content and code generation
    allow_delegation=False
)
