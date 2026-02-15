# Web Searcher Agent (with Firecrawl)

## Overview
This is a Python-based web searcher agent that uses the Firecrawl library to fetch, analyze, and synthesize web information as concise, well-rounded answers to user queries.

## Usage
```
python main.py "Your search query here"
```
Example:
```
python main.py "What are the latest advances in renewable energy storage?"
```

## Installation
1. Clone this repository
2. Install requirements:
```
pip install -r requirements.txt
```
3. Set your Firecrawl API key (and OpenAI key if needed) in a `.env` file:
```
FIRECRAWL_API_KEY=your_key_here
OPENAI_API_KEY=your_openai_key_here
```

## Files
- `main.py` — Entry point, handles CLI, output, errors.
- `searcher.py` — Core coordination of search, fetch, summarize.
- `firecrawl_client.py` — Encapsulates Firecrawl web queries.
- `summarizer.py` — Synthesis and summarization logic.
- `utils.py` — Text cleaning, deduplication, etc.
- `requirements.txt` — Required dependencies.
- `README.md` — This guide!

## Notes
- Handles no results and ambiguous queries with clear error messages.
- Easily extensible and cleanly structured.
