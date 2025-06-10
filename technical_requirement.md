# Technical Requirements

## Input Methods
- Accepts `POST` requests at `/chat`
- JSON payload: `{ "message": "your query here" }`

## AI Components
- Hugging Face Transformers API
- Model used: `google/flan-t5-small`

## Data Sources
- User-provided messages
- Hugging Face API-generated responses

## API Integrations
- Hugging Face API:
  - Used for generating AI responses.
  - Called via `requests.post` with Bearer token authentication.
