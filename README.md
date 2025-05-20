# Azure AI Foundry

A Python-based project for working with Azure OpenAI services and capabilities, providing simple examples and tools for text completion, chat interactions, and image analysis.

## Project Overview

Azure AI Foundry is a toolkit that demonstrates how to integrate with Azure OpenAI services using Python. It provides a collection of example scripts that showcase various capabilities including:

- Setting up and authenticating with Azure OpenAI services
- Generating text responses using chat completions
- Processing and analyzing images with multimodal models
- Performance testing for Azure OpenAI API endpoints

This project serves as a starting point for developers looking to leverage Azure's AI capabilities in their applications.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- An Azure account with access to Azure OpenAI services
- Azure OpenAI API key and endpoint

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/azure-ai-foundry.git
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

## File-by-File Descriptions

### `src/00-api-setup-and-auth.py`

**Description:** Demonstrates how to set up and authenticate with Azure OpenAI using API keys.

**Role:** This is the foundational script for establishing connection to Azure OpenAI services.

**How to run:**
```bash
python src/00-api-setup-and-auth.py
```

**What it does:**
- Loads environment variables from `.env` file
- Initializes the Azure OpenAI client
- Displays your configuration details
- Lists available models in your deployment
- Tests authentication with a basic completion request

### `src/02-chat-responses.py`

**Description:** Shows how to generate text responses using the Azure OpenAI API.

**Role:** Provides a simple example of using the responses API for chat-based completions.

**How to run:**
```bash
python src/02-chat-responses.py
```

**What it does:**
- Sets up a chat completion request with a system and user message
- Sends the request to the Azure OpenAI API
- Prints the response text

### `src/03-image-responses.py`

**Description:** Demonstrates how to process and analyze images using Azure OpenAI multimodal capabilities.

**Role:** Shows how to encode images and use them as input for the AI model.

**How to run:**
```bash
python src/03-image-responses.py
```

**What it does:**
- Reads all image files from the `assets/image` directory
- Encodes each image as a Base64 string
- Sends each image to the Azure OpenAI API for analysis
- Prints the AI's description of each image

### `src/chat-stress-test.py`

**Description:** A utility for testing the performance of Azure OpenAI API with multiple queries.

**Role:** Helps evaluate response times and reliability of the API under load.

**How to run:**
```bash
python src/chat-stress-test.py
```

**What it does:**
- Reads a list of questions from `assets/list-of-questions.txt`
- Sends each question to the Azure OpenAI API
- Measures and records the response time for each query
- Provides a summary of total and average processing times

## Execution Flow

The components in this project typically follow this workflow:

1. **Setup and Authentication** (`00-api-setup-and-auth.py`): This is the first step for any interaction with Azure OpenAI. It initializes the client and verifies your credentials.

2. **Feature Utilization**: After authentication, you can use any of the feature examples:
   - **Text Generation** (`02-chat-responses.py`): For generating text responses.
   - **Image Analysis** (`03-image-responses.py`): For processing and analyzing images.
   - **Performance Testing** (`chat-stress-test.py`): For evaluating API performance.

Each script is independent and demonstrates a specific capability, but they all share the same authentication and setup pattern.

## Example Use Cases

### Case 1: Simple Question Answering System

Use `02-chat-responses.py` as a template to create a question-answering system. Modify the user prompt to ask different questions or adjust the system message to change the assistant's behavior.

### Case 2: Image Content Analysis

Use `03-image-responses.py` to analyze the content of images. This can be adapted for use cases like:
- Product image recognition
- Document OCR
- Visual content moderation

### Case 3: API Performance Evaluation

Use `chat-stress-test.py` to evaluate the performance of your Azure OpenAI deployment:
- Test with different question sets to see how response times vary
- Adjust the model parameters to find the optimal balance between quality and speed
- Monitor performance across different times of day to identify patterns