# Azure AI Foundry

A Python-based project for working with Azure OpenAI services, providing examples for text generation, chat, and multimodal vision capabilities using the Azure OpenAI API.

## Features

- Azure OpenAI API authentication and model discovery
- Text and chat generation using the responses API
- Image analysis and OCR using multimodal capabilities
- Performance testing and benchmarking
- Comprehensive examples for different use cases

## Project Structure

```
azure-ai-foundry/
├── assets/
│   ├── image/             # Sample images for multimodal analysis
│   ├── list-of-questions.txt # Sample questions for stress testing
│   └── note.md            # Reference notes about Azure CLI
├── src/
│   ├── 00-api-setup-and-auth.py  # Setup and authentication example
│   ├── 02-chat-responses.py      # Basic chat responses example
│   ├── 03-image-responses.py     # Image analysis example
│   └── chat-stress-test.py       # Performance testing script
├── .env.example           # Template for environment variables
└── requirements.txt       # Project dependencies
```

## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure OpenAI services
- Azure OpenAI deployment with appropriate models
- API access to Azure OpenAI service

## Getting Started

1. Clone this repository
   ```bash
   git clone https://github.com/tkhongsap/azure-ai-foundry.git
   cd azure-ai-foundry
   ```

2. Create a `.env` file with your Azure OpenAI credentials:
   ```
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_API_VERSION=2025-03-01-preview
   AZURE_OPENAI_MODEL_NAME=gpt-4.1
   AZURE_OPENAI_DEPLOYMENT=gpt-4.1
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the example scripts in the `src` directory

## Example Scripts

### Authentication and API Setup

The `00-api-setup-and-auth.py` script demonstrates:
- Setting up the Azure OpenAI client
- Authenticating with your API key
- Listing available models in your deployment
- Testing API connectivity with a basic completion

Run this script first to verify your setup:
```bash
python src/00-api-setup-and-auth.py
```

### Chat Responses

The `02-chat-responses.py` script shows how to:
- Create a simple chat interaction
- Generate responses from the model
- Configure parameters like temperature and token limits

Run the script:
```bash
python src/02-chat-responses.py
```

### Image Analysis

The `03-image-responses.py` script demonstrates:
- Processing and encoding images for the API
- Sending images for analysis
- Getting detailed descriptions of image content
- Batch processing multiple images

Ensure you have images in the `assets/image/` directory, then run:
```bash
python src/03-image-responses.py
```

### Performance Testing

The `chat-stress-test.py` script provides:
- Batch processing of multiple questions
- Performance measurement for API calls
- Timing statistics for response generation
- Summary reports of API performance

Run the performance test:
```bash
python src/chat-stress-test.py
```

## Dependencies

This project relies on the following Python packages:
- azure-ai-projects
- azure-identity
- openai
- azure-ai-inference
- azure-search-documents
- azure-ai-evaluation
- azure-monitor-opentelemetry
- python-dotenv

## Troubleshooting

- If you encounter authentication errors, verify your API key and endpoint in the `.env` file
- Ensure your Azure OpenAI deployment is active and the model specified exists
- Check that your API version is compatible with the features you're trying to use
- If image processing fails, ensure the image format is supported (JPG, JPEG, PNG)
- For performance issues, consider adjusting the number of tokens or batch size