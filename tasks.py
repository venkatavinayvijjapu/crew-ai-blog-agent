from crewai import Task
from tools import tool
from agents import *

# Research task
research_task = Task(
  description=(
    "Research and identify key insights on {topic} to create a compelling blog post."
    "Focus on structuring the content with an engaging introduction, detailed pros and cons,"
    "and a practical project or code example if applicable."
    "Ensure the final output is informative, well-organized, and provides value to the reader."
  ),
  expected_output='A well-structured blog post with an introduction, pros and cons, and a project or code example, if relevant.',
  tools=[tool],  # Specify relevant research and writing tools
  agent=blog_researcher,  # Using the modified blog researcher agent
)


# Writing task with language model configuration
write_task = Task(
  description=(
    "Create a detailed blog post on {topic}."
    "Include an engaging introduction, a balanced analysis of pros and cons,"
    "and a practical project or code example if applicable."
    "The blog should be clear, informative, and engaging, making the content accessible to readers of all levels."
  ),
  expected_output='A markdown-formatted blog post on {topic}, including an introduction, pros and cons, and a project or code example if relevant.',
  tools=[tool],  # Specify necessary writing, research, and code tools
  agent=blog_writer,  # Using the tailored blog writer agent
  async_execution=False,
  output_file='Crew_output.md'  # Specify the output file name
)
