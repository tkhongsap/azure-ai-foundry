import os
import dotenv
from openai import AzureOpenAI

dotenv.load_dotenv()

endpoint = "https://ai-totrakoolk6076ai346198185670.openai.azure.com/"
model_name = os.getenv("AZURE_OPENAI_MODEL_NAME")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_API_VERSION")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

# Using the responses API instead of chat.completions
response = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?"
        }
    ],
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    max_output_tokens=4000
)

print(response.output_text)