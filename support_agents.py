# warning control
import warnings
warnings.filterwarnings('ignore')

# core imports
import os
from utils import get_openai_api_key
from crewai import Agent, Task, Crew

# API key and model setup
openai_api_key = get_openai_api_key()
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["OPENAI_MODEL_NAME"] = "mistral-small"
os.environ["OPENAI_API_BASE"]="https://api.mistral.ai/v1"


# Define agents
support_agent = Agent(
    role="Support Representative Agent",
	goal="Deliver exceptional customer service by being the most approachable, empathetic, and solution-oriented support representative on your team. Ensure every interaction leaves the customer feeling heard, valued, and satisfied.",
	backstory=(
		"You are a Customer Support Agent at CrewAI (https://crewai.com), currently assisting {customer}, one of the company’s most valued clients."
        "Your responsibility is to deliver exceptional support by providing clear, complete, and accurate responses."
        "Avoid making assumptions—base your answers on facts, documentation, and available data."
        "Ensure that the customer feels fully supported, heard, and confident in every interaction."
	),
	allow_delegation=False,
	verbose=True
)
support_qa_agent = Agent(
	role="Support QA Specialist",
	goal="Establish yourself as the most reliable and detail-oriented Quality Assurance agent on your team by consistently upholding the highest standards in support evaluation and feedback. Your dedication ensures exceptional customer experiences and continuous improvement across the support team.",
	backstory=(
		"You are part of the Quality Assurance team at CrewAI (https://crewai.com), currently reviewing a support interaction for {customer}, a highly valued client. Your role is to ensure that the support representative delivers responses that are complete, accurate, and helpful—without making assumptions. You are responsible for upholding the highest standards of support quality by carefully evaluating the interaction and providing objective, constructive feedback that helps maintain excellence in customer service."
	),
	verbose=True
)

from crewai_tools import SerperDevTool, \
                         ScrapeWebsiteTool, \
                         WebsiteSearchTool


docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
)

inquiry_resolution = Task(
    description=(
        "{customer} has submitted a critical request: {inquiry}"
        "The request was made by {person} from {customer}."
        "Leverage all available context and knowledge to deliver the most accurate, thorough, and helpful response possible."
        "Your goal is to ensure the customer receives a complete and precise answer that fully addresses their needs."
    ),
    expected_output=(
	    "Craft a clear, comprehensive, and friendly response that fully addresses all aspects of the customer’s inquiry."
        "Your answer should reference any resources, tools, or documentation used—including external data or solutions—demonstrating transparency and reliability."
        "Make sure the response is complete, leaves no follow-up questions, and reflects a helpful and approachable tone throughout."
    ),
	tools=[docs_scrape_tool],
    agent=support_agent,
)

quality_assurance_review = Task(
    description=(
        "Review the response drafted by the Senior Support Representative for {customer}'s inquiry."    
        "Ensure the reply is complete, factually accurate, and aligned with the high standards of customer support quality."
        "Confirm that every aspect of the customer's inquiry is clearly and thoroughly addressed in a helpful, professional, and friendly tone."
        "Verify that the response is well-supported with appropriate references or sources, leaving no room for ambiguity or follow-up questions."
    ),
    expected_output=(
        "A final, polished, and informative response that is ready to be shared with the customer."
        "The response should thoroughly address the customer’s inquiry, incorporating all necessary improvements and feedback."
        "Maintain a friendly, professional tone—reflecting our company’s relaxed and approachable style, without being overly formal."
    ),
    agent=support_qa_agent,
)
# Run the crew
crew = Crew(
    agents=[support_agent, support_qa_agent],
    tasks=[inquiry_resolution, quality_assurance_review],
    verbose=True,
    memory=True
)

inputs={
  "customer": "ABC Inc",
  "person": "Kadasiddha Kullolli",
  "inquiry": "I'm looking for guidance on setting up a Crew in CrewAI, particularly on how to add memory to the crew. Could you walk me through the steps or share best practices for enabling memory within a Crew setup?"
}

result = crew.kickoff(inputs=inputs)

# Display result as Markdown
try:
    from markdown2 import markdown
    from IPython.display import display, HTML

    display(HTML(markdown(str(result))))
except ImportError:
    print("\nMarkdown2 or IPython not available. Output below:\n")
    print(result)

# Save to file
with open("blog_post.md", "w", encoding="utf-8") as f:
    f.write(str(result))  # Safe fix for CrewOutput object

print("\n✅ Blog post saved .md")
