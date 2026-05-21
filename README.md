# Local LLM Insight Extractor & Summarizer

A structured text summarization and insight extraction pipeline built using Python, **LangChain Core (LCEL)**, and local open-source LLMs via **Ollama**.

## 🚀 Overview

This project demonstrates how to orchestrate local large language models to extract structured insights and summaries from unstructured text. By utilizing **LangChain Expression Language (LCEL)**, the pipeline decouples prompt engineering from model invocation, allowing for seamless switches between local models (like `gemma3:270m` or `mistral`) and cloud APIs (like Google Gemini).

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Framework:** LangChain Core (LCEL syntax)
- **LLM Orchestration:** Ollama (Local Execution) & LangChain Google GenAI (Cloud ready)
- **Environment Management:** Python-dotenv

## 🏗️ Architecture

The pipeline follows a modern, declarative LCEL structure:
`Data Input -> PromptTemplate Injection -> LLM Processing (Ollama/Gemma) -> Output Stream`

This structure ensures that the data is fed cleanly into the model while enforcing formatting boundaries to capture specific blocks (Short Summary and Key Facts) without conversational filler.

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/juliaDiasOliv/langchain-lcel-summarizer.git
cd langchain-lcel-summarizer
