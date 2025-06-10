
# Design Thinking Process

## Empathize
Users like developers or businesses want to integrate AI chat into their products without building LLMs from scratch.

## Define
The problem is the lack of an easy-to-use backend API that can bridge user input and a powerful AI model seamlessly.

## Ideate
We chose to build a Flask-based REST API that sends user queries to Hugging Face models and returns responses.

## Prototype
The prototype is a single Flask route `/chat` accepting JSON payload, logging input/output, and returning AI results.

## Test
Testing will include:
- Sending various inputs
- Handling edge cases (missing data, API failures)
- Validating logs and outputs

## References
- https://huggingface.co/docs/api-inference
- https://flask.palletsprojects.com/
