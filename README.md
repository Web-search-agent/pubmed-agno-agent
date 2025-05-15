# PubMed tool in Agno Framework

This repository demonstrates how to use the Agno framework for working with various language models and tools.

## Prerequisites

- Python 3.8 or higher
- Agno framework installed

## Setup

1. Clone this repository
2. Install the dependencies:

```
pip install agno
```

3. Set up your API keys as environment variables:

```
export GROQ_API_KEY="your_groq_api_key_here"
```

For other models, you may need to set their respective API keys:
```
export OPENAI_API_KEY="your_openai_api_key_here"
export PERPLEXITY_API_KEY="your_perplexity_api_key_here"
export HUGGINGFACE_API_KEY="your_huggingface_api_key_here"
export XAI_API_KEY="your_xai_api_key_here"
```

## Changing Models

You can easily change the model by modifying the `model` parameter when initializing the Agent. The example currently uses Groq's `llama-3.3-70b-versatile`, but you can switch to other supported models:

```python
agent = Agent(model=OpenAIChat(id="gpt-4"), tools=[PubmedTools()], show_tool_calls=True)

agent = Agent(model=Perplexity(id="sonar-medium-online"), tools=[PubmedTools()], show_tool_calls=True)

agent = Agent(model=HuggingFace(id="mistralai/mixtral-8x7b"), tools=[PubmedTools()], show_tool_calls=True)

agent = Agent(model=xAI(id="grok-1"), tools=[PubmedTools()], show_tool_calls=True)
```


