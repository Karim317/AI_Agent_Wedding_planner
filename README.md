# AI Wedding Planner

A multi-agent wedding planning application built with LangChain, OpenAI, Tavily, and Streamlit. It turns a structured wedding brief into a client-ready plan covering venue and vendor research, budget allocation, timelines, risks, and tradeoffs.

## Features

- Interactive Streamlit planning dashboard
- Structured brief for date, location, guests, budget, style, priorities, traditions, and constraints
- Main LangChain planning agent with two delegated research subagents
- Live web research through Tavily
- Markdown plan preview and download
- Optional API key entry in the Streamlit sidebar
- Saved in-session run history

## Project Structure

```text
.
├── app.py                      # Streamlit web application
├── main.py                     # Interactive command-line entry point
├── agents.py                   # Main-agent delegation and subagents
├── model.py                    # OpenAI chat model configuration
├── tools.py                    # Tavily web-search tool
├── prompts.py                  # Wedding-planner system and user prompts
├── pyproject.toml              # uv project and dependency configuration
├── uv.lock                     # Locked dependency versions
├── .python-version             # Python 3.11
└── src/ai_weddingplanner/
    └── __init__.py             # Installed-package entry module
```

## Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/) (recommended)
- OpenAI API key
- Tavily API key

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Karim317/AI_Agent_Wedding_planner.git
cd AI_Agent_Wedding_planner
```

### 2. Install dependencies

Using `uv`:

```bash
uv sync
```

Or create a virtual environment and install with `pip`:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Environment Variables

Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

| Variable | Required | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | Yes | Authentication for the `gpt-5-nano` model used by the planner and subagents |
| `TAVILY_API_KEY` | Yes | Authentication for live vendor, venue, and market web searches |

The repository does not currently contain a `.env.example` file. Do not commit `.env` or real API keys.

You can also configure these values in Streamlit's sidebar or through Streamlit secrets. In Streamlit Cloud, add `OPENAI_API_KEY` and `TAVILY_API_KEY` to the app's secrets.

## Usage

### Run the Streamlit application

```bash
uv run streamlit run app.py
```

Open the local URL printed by Streamlit. Complete the wedding brief, add API keys if they are not already configured, and select **Generate wedding plan**.

Use **Load sample brief** in the sidebar to populate example values for a Chicago wedding.

### Run the command-line interface

```bash
uv run python main.py
```

Enter the wedding requirements at the prompt. The main agent delegates research to subagents and prints the synthesized result.

Example input:

```text
Modern 120-person wedding in Chicago, budget USD 35,000–65,000, indoor-outdoor venue, vegetarian menu, live acoustic music, and a blend of western ceremony and family tea ceremony.
```

## How It Works

```text
Streamlit or CLI
  -> structured requirements
  -> WEDDING_PLANNER_AGENT_PROMPT
  -> MainWeddingPlannerAgent
      -> delegate_to_subagent1
      -> delegate_to_subagent2
          -> Tavily web search
  -> synthesized wedding plan
```

The generated plan can include:

- Executive summary
- Venue and vendor recommendations
- Budget allocation
- Wedding-day timeline
- Planning risks and tradeoffs
- Open questions

## Notes

- The primary model is configured in `model.py` as `gpt-5-nano`.
- API quotas, account access, and Tavily availability may affect results.
- The Streamlit app stores completed runs only in the current browser session.
- One subagent delegation currently calls `sub_agent1` in `delegate_to_subagent2`; review `agents.py` if separate subagent behavior is intended.
