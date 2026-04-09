# 🍽️ Restaurant Name Generator

A generative AI web app that creates **unique restaurant names and themed menus** based on cuisine type — built end-to-end with LangChain, Groq API, and Streamlit.

🔗 **[Live Demo →](https://restaurant-name-generator-2opxgbmycvpo6td2xf8dvk.streamlit.app/)**

---

## What It Does

Enter a cuisine type (e.g., *Italian*, *Japanese*, *Mexican*) and the app:
1. Generates a creative, fancy restaurant name using an LLM
2. Instantly produces 5 unique menu items tailored to that restaurant

All in one seamless, interactive UI — no technical knowledge required.

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | `llama-3.1-8b-instant` via Groq API |
| Chaining | LangChain (Runnable syntax) |
| Frontend | Streamlit |
| Deployment | Streamlit Cloud |
| Language | Python |

---

## Architecture

```
User Input (Cuisine Type)
        ↓
PromptTemplate → LangChain Chain → Groq LLM
        ↓
  Restaurant Name
        ↓
PromptTemplate → LangChain Chain → Groq LLM
        ↓
    Menu Items
        ↓
Streamlit UI Display
```

Two sequential LangChain chains are used:
- **Chain 1** — Takes cuisine type → generates a restaurant name
- **Chain 2** — Takes that restaurant name → generates 5 contextual menu items

---

## Project Structure

```
Restaurant-Name-Generator/
├── main.py              # Streamlit frontend and UI logic
├── langchainhelp.py     # LangChain chains and Groq LLM integration
├── requirements.txt     # Python dependencies
└── .gitignore
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- A [Groq API key](https://console.groq.com/)

### Installation

```bash
git clone https://github.com/Khushipratibha/Restaurant-Name-Generator.git
cd Restaurant-Name-Generator
pip install -r requirements.txt
```

### Running Locally

Add your Groq API key to `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_api_key_here"
```

Then run:

```bash
streamlit run main.py
```

---

## Key Design Decisions

- **Groq over OpenAI** — Chose Groq for significantly lower latency inference on open-source models
- **Sequential chaining** — Used LangChain's Runnable pipe syntax (`prompt | llm`) for clean, modular chain composition
- **Prompt optimization** — Constrained prompts to return structured outputs (single name, comma-separated list) to make parsing reliable without post-processing overhead

---

## Dependencies

```
langchain
langchain-groq
streamlit
```

---

## Author

**Pratibha Yadav**
B.Tech CSE-AI @ IGDTUW
[GitHub](https://github.com/Khushipratibha) · [LinkedIn](https://www.linkedin.com/in/khushipratibha/)
