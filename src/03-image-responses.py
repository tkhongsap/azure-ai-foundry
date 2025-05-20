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

# Directory containing the images
image_dir = os.path.join("assets", "image")

# Get all image files in the directory
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Process each image
for image_file in image_files:
    print(f"Processing {image_file}...")
    image_path = os.path.join(image_dir, image_file)
    
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
                    { "type": "input_text", "text": f"Please describe the image: {image_file}" },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ],
        temperature=0.3,
        top_p=1.0,
        max_output_tokens=4000
    )
    
    print(f"\nResults for {image_file}:")
    print(response.output_text)
    print("\n" + "-"*50 + "\n")