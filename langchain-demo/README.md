# Incident Triage Copilot reference application

This application reads an operational incident report and returns a validated JSON assessment. LangChain provides the model and prompt interface. Pydantic defines the response contract. Deterministic application policy decides when human review is mandatory.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

On Windows PowerShell, activate with `.venv\\Scripts\\Activate.ps1`.

Add your own key and a supported model name to `.env`. Never commit that file.

## Run without an API key

```bash
python -m incident_copilot.cli data/single-incident.txt --mock
python -m incident_copilot.evaluate --mock
python -m unittest discover -s tests -v
```

## Run with a model

```bash
python -m incident_copilot.cli data/single-incident.txt
python -m incident_copilot.evaluate
```

The evaluation command makes one model call per case. Review the dataset before running it against a paid API.

## Teaching sequence

1. `demo_steps/01_first_model_call.py`
2. `demo_steps/02_prompt_roles.py`
3. `demo_steps/03_schema_contract.py`
4. `src/incident_copilot/`
5. `src/incident_copilot/evaluate.py`
