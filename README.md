# reserarch-physics

## Research and analysis of scientific articles; formulator and validator of hypotheses

## Objective

To create a system of expert agents to search for relevant articles on a given topic, perform scientific analysis of the content, validate the hypotheses included in the body of the articles, create a knowledge base in graphs, and generate new hypotheses.

## Directory Structure

scientific_agents_poc/
├── app/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── reader_agent.py
│   │   └── extractor_agent.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── document_service.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main_routes.py
│   ├── static/
│   ├── templates/
│   │   └── index.html
│   └── app.py
├── data/
│   ├── uploads/
│   └── processed/
├── .env
├── requirements.txt
└── run.py
