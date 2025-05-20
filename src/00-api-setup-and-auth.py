"""
Azure OpenAI API Setup and Authentication
-----------------------------------------
This script demonstrates how to:
1. Set up and authenticate with Azure OpenAI using API keys
2. Check available models in your deployment
3. Display basic endpoint and authentication information
"""

import os
import dotenv
from openai import AzureOpenAI

# Load environment variables from .env file
dotenv.load_dotenv()

# Azure OpenAI configuration
endpoint = "https://ai-totrakoolk6076ai346198185670.openai.azure.com/"
model_name = os.getenv("AZURE_OPENAI_MODEL_NAME")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_API_VERSION")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

# Display configuration details
print("Azure OpenAI Configuration:")
print("--------------------------")
print(f"Endpoint: {endpoint}")
print(f"API Version: {api_version}")
print(f"Deployment: {deployment}")
print(f"Model: {model_name}")
print("--------------------------\n")

# List available models
print("Available Models:")
print("--------------------------")
models = client.models.list()
for model in models:
    print(f"ID: {model.id}")
    print(f"Created: {model.created}")
    print(f"Object: {model.object}")
    print()

# Test authentication with a basic completion
print("Testing Authentication with Basic Completion:")
print("--------------------------")
try:
    response = client.responses.create(
        model=deployment,
        input=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, who are you?"}
        ],
        temperature=1.0,
        top_p=1.0,
        max_output_tokens=800
    )
    print("Authentication successful!")
    print(f"Response: {response.output_text}\n")
except Exception as e:
    print(f"Authentication failed: {e}")
