# Azure AI Foundry Scripts

This directory contains Python scripts for working with Azure OpenAI services and capabilities. These scripts demonstrate various ways to interact with Azure AI services including authentication, chat completions, image analysis, and performance testing.

## Scripts Overview

### 00-api-setup-and-auth.py

This script demonstrates how to set up and authenticate with Azure OpenAI services. It covers:

- Loading environment variables from a `.env` file
- Configuring and initializing the Azure OpenAI client
- Displaying connection and configuration details
- Listing available models in your deployment
- Testing authentication with a basic completion request
- Error handling for authentication failures

**Usage:**
```bash
python 00-api-setup-and-auth.py
```

### 02-chat-responses.py

This script shows how to use the Azure OpenAI responses API for chat completions. It:

- Sets up the Azure OpenAI client
- Creates a simple chat request with system and user messages
- Uses the responses API to generate a text response
- Prints the generated response

**Usage:**
```bash
python 02-chat-responses.py
```

### 03-image-responses.py

This script demonstrates how to use Azure OpenAI for image analysis and understanding. It:

- Loads and processes images from the `assets/image` directory
- Encodes images to base64 format for API transmission
- Uses the responses API with multimodal inputs (both text and image)
- Provides specialized OCR and image understanding prompts
- Prints the AI's description/analysis of each image

**Usage:**
```bash
python 03-image-responses.py
```

### chat-stress-test.py

This script performs stress testing on the Azure OpenAI chat service to measure performance metrics. It:

- Reads a list of questions from `assets/list-of-questions.txt`
- Processes each question through the Azure OpenAI service
- Times and records the response duration for each question
- Calculates performance metrics (total time, average time per question)
- Provides a detailed summary of performance results

**Usage:**
```bash
python chat-stress-test.py
```

## Prerequisites

Before running these scripts, ensure:

1. You have an Azure OpenAI service set up in Azure
2. You've created a `.env` file in the root directory with:
   ```
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_API_VERSION=your_api_version
   AZURE_OPENAI_DEPLOYMENT=your_deployment_name
   AZURE_OPENAI_MODEL_NAME=your_model_name
   ```
3. You've installed the required dependencies with `pip install -r requirements.txt`

## Additional Notes

- The image processing script (`03-image-responses.py`) requires images to be placed in the `assets/image` directory
- The stress test script (`chat-stress-test.py`) requires a `list-of-questions.txt` file in the `assets` directory
- All scripts use the same Azure OpenAI endpoint and authentication method for consistency