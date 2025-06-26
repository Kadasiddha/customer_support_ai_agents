# customer_support_ai_agents
Multi-agent support system using CrewAI, memory, and live documentation scraping to generate high-quality, QA-reviewed responses to customer inquiries.

# 🤖 CrewAI Customer Support Automation with Memory

This project uses [CrewAI](https://github.com/joaomdmoura/crewai) to simulate a realistic customer support workflow powered by AI agents. It handles customer inquiries using a two-agent team — a **Support Representative Agent** and a **Support QA Specialist** — to provide accurate, well-sourced, and human-like support responses.

It also utilizes the CrewAI memory feature and web scraping tools to refer to live documentation, ensuring the responses are grounded and up-to-date.

---

## 📌 What It Does

- Accepts a customer's support inquiry.
- Uses an AI agent to research and write a high-quality, friendly response.
- A QA agent reviews and enhances the response based on internal quality standards.
- Automatically scrapes official CrewAI documentation for accurate answers.
- Outputs a final, Markdown-formatted reply ready to be sent.
- Stores the result in a local `.md` file for review or publication.

---

## 🧠 Agents Involved

### 1. **Support Representative Agent**
- Gathers information from CrewAI documentation.
- Crafts a clear, friendly, and thorough response to the customer's inquiry.
- Makes no assumptions and references all sources used.

### 2. **Support QA Specialist**
- Reviews the support agent’s draft.
- Ensures clarity, completeness, factual accuracy, and brand tone.
- Makes final improvements for delivery readiness.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/crewai-support-automation.git
cd crewai-support-automation

2. Install Dependencies

pip install crewai crewai-tools openai markdown2


3. Set API Credentials
Make sure to export or load your Mistral/OpenAI-compatible credentials:

I have used mistral api key. You can use OpenAI as well.

export OPENAI_API_KEY="your-mistral-api-key"
export OPENAI_API_BASE="https://api.mistral.ai/v1"
export OPENAI_MODEL_NAME="mistral-small"

If using a .env file, use:

OPENAI_API_KEY=your-mistral-api-key
OPENAI_API_BASE=https://api.mistral.ai/v1
OPENAI_MODEL_NAME=mistral-small

python3 support_agents.py

Example input (inside the script):

inputs={
  "customer": "ABC Inc",
  "person": "Kadasiddha Kullolli",
  "inquiry": "I'm looking for guidance on setting up a Crew in CrewAI, particularly on how to add memory to the crew. Could you walk me through the steps or share best practices for enabling memory within a Crew setup?"
}


📄 Output
Markdown response saved as: blog_post.md

Ready to be sent or copy-pasted into a support tool or email


🧩 Tools Used
ScrapeWebsiteTool – Pulls content from CrewAI Docs

crewai-tools – Adds scraping, search, and other smart capabilities

memory=True – Retains conversational context throughout the crew


✅ Example Use Cases
Automating Tier 1 or Tier 2 customer support

Training simulations for new support staff

Internal QA evaluations for support teams

Scaling technical documentation support


📝 License
MIT License © 2025 [Kadasiddha Kullolli]

🙌 Acknowledgements
CrewAI

Mistral AI

Markdown2
