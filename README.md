# Hallucination Detection API

This repository contains a microservice API for detecting hallucinations in AI-generated responses using the Vectara model.

## Overview

The Hallucination Detection API is designed to evaluate the faithfulness of an AI-generated response to a given context. It uses the Vectara model to assess whether the response contains information not present in or contradictory to the provided context.

## Prerequisites

- Python 3.7+
- Poetry (Python package manager)
- Docker (for containerization and deployment)
- FastAPI

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/vectara-hallucination-api.git
   cd vectara-hallucination-api
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

## Usage

### Running the API locally

1. Start the uvicorn server:
   ```
   poetry run uvicorn app:app --host 0.0.0.0 --port 8000
   ```

2. The API will be available at `http://localhost:8000`.
3. You can access the interactive API documentation at `http://localhost:8000/docs`.

### API Endpoints

#### POST /evaluate

Evaluates the faithfulness of a response to a given context.

**Request Body:**
```json
{
  "context": "Your context text here",
  "response": "The response to evaluate"
}
```

**Response:**
```json
{
  "score": 0.85
}
```

The score ranges from 0 to 1, where 1 indicates perfect faithfulness and 0 indicates complete hallucination.

### Example Usage

You can use the interactive API documentation at `http://localhost:8000/docs` to test the API directly in your browser.

Alternatively, you can use `curl` or any HTTP client. Here's an example using `curl`:

```bash
curl -X 'POST' \
  'http://localhost:8000/evaluate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "context": "Climate change is a significant global challenge that requires immediate action. The Intergovernmental Panel on Climate Change (IPCC) has reported that human activities are the primary driver of global warming.",
  "response": "According to the provided context, the IPCC has stated that human activities are the main cause of global warming, and climate change is a major worldwide issue that needs to be addressed urgently."
}'
```

## Docker Commands

### Building the Docker Image

To build the Docker image:

```
make build
```

### Running the API Locally with Docker

To run the API locally using Docker:

```
make run
```

The API will be available at `http://localhost:5000`.

### Deploying the API

To build and deploy the API:

```
make deploy
```

This command will build a Docker image, tag it, and push it to the specified ECR repository.

### Cleaning Up

To remove the local Docker image:

```
make clean
```

## Testing

To run the unit tests:

```
poetry run python -m unittest test_app.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate.

## License

[Specify your license here]

