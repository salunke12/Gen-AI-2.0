from crewai import Crew, Process
from agents import news_researcher, news_writer
from task import research_task, writing_task

# Formatting the tech focused crew with some enhanced configurations 
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Start the task execution process with enhanced feedback 
result = crew.kickoff(inputs={'topic': 'AI in healthcare'}) # FIXED: Changed 'input' to 'inputs'
print(result)