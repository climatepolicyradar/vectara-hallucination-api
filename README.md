# Hallucination Detection API

This repository contains a microservice API for detecting hallucinations in AI-generated responses using the Vectara model.

## Overview

The Hallucination Detection API is designed to evaluate the faithfulness of an AI-generated response to a given context. It uses the Vectara model to assess whether the response contains information not present in or contradictory to the provided context.

## Prerequisites

- Python 3.7+
- Poetry (Python package manager)
- Docker (for containerization and deployment)

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

1. Start the Flask server:
   ```
   poetry run flask run --host=0.0.0.0
   ```

2. The API will be available at `http://localhost:5000`.

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

Using `httpie`:

```
http POST http://localhost:5000/evaluate \
    context="Climate change is a significant global challenge that requires immediate action. The Intergovernmental Panel on Climate Change (IPCC) has reported that human activities are the primary driver of global warming." \
    response="According to the provided context, the IPCC has stated that human activities are the main cause of global warming, and climate change is a major worldwide issue that needs to be addressed urgently."
```

## Deployment

To deploy the API:

```
make deploy
```

This command will build a Docker image and deploy it according to the configuration in your Makefile.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Specify your license here]

