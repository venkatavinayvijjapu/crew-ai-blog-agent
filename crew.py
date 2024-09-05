from crewai import Crew,Process
from tasks import research_task,write_task
from agents import blog_researcher,blog_writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Crew AI'})
print(result)