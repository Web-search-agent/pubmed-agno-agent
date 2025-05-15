import os
from agno.agent import Agent
from agno.tools.pubmed import PubmedTools
from agno.models.openai import OpenAIChat
from agno.models.perplexity import Perplexity
from agno.models.huggingface import HuggingFace
from agno.models.xai import xAI
from agno.models.groq import Groq

agent = Agent(model=Groq(id="llama-3.3-70b-versatile"), tools=[PubmedTools()], show_tool_calls=True)
agent.print_response("Tell me about Funda Meric Bernstam.")
