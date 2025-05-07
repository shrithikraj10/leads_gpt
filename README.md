Folder Structure:
leads_gpt/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Entry point for FastAPI app
│   ├── api/                    # Route definitions
│   │   ├── __init__.py
│   │   ├── routes_upload.py    # Upload & parse CSV
│   │   ├── routes_generate.py  # Generate messages
│   ├── core/                   # Core configs & logic
│   │   ├── __init__.py
│   │   ├── config.py           # Environment variables, settings
│   ├── services/               # Business logic, integrations
│   │   ├── __init__.py
│   │   ├── parser.py           # Lead parsing from CSV
│   │   ├── prompt_engine.py    # GPT prompt and response handling
│   ├── models/                 # Pydantic models (Request/Response)
│   │   ├── __init__.py
│   │   ├── lead.py
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py
│   │   ├── file_utils.py
│   │   ├── logger.py
│   └── templates/              # If using Jinja2 (optional)
│       └── index.html
├── .env                        # Secrets (API keys etc.)
├── requirements.txt
├── README.md
├── .gitignore
