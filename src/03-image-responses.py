import os
import dotenv
import base64
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

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Path to the image
image_path = os.path.join("assets", "image", "planogram-01.jpeg")

# Getting the Base64 string
base64_image = encode_image(image_path)

# Using the responses API with image input
response = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "system",
            "content": "You are a helpful assistant specialized in OCR and analyzing image understanding."
        },
        {
            "role": "user",
            "content": [
                { "type": "input_text", "text": "Please describe provided image(s)." },
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    temperature=0.7,
    top_p=1.0,
    max_output_tokens=4000
)

print(response.output_text)