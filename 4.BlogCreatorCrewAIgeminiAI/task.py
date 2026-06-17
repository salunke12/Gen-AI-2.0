from crewai import Task
from tools import tool 
from agents import news_researcher, news_writer

## Research task
research_task = Task(
    description=(
        "Identify the big trends in {topic}. "
        "Focus on identifying Pros and cons and the overall narrative. "
        "Your final report should clearly articulate the key points, "
        "its market opportunities, and potential risks."
    ),
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends',
    tools=[tool],
    agent=news_researcher  # FIXED: Changed from 'agents' and removed trailing comma
)

# Writing task
writing_task = Task(
    description=(
        "Compose an insightful article on {topic}. "
        "Focus on the latest trends and how it is impacting the industry. "
        "This article should be easy to understand, engaging and positive."
    ),
    expected_output='A 4 paragraph article on {topic} advancements formatted as markdown',
    tools=[tool],
    agent=news_writer,  # FIXED: Changed from 'agents' and removed trailing comma
    async_execution=False,
    output_file='new-blog-post.md'
)