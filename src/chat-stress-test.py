import os
import dotenv
from openai import AzureOpenAI
import re
import time

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

# Read questions from file
questions = []
with open("assets/list-of-questions.txt", "r") as file:
    for line in file:
        match = re.search(r'question \d+: (.*)', line.strip())
        if match:
            questions.append(match.group(1))

total_time = 0
results = []

# Process each question
for i, question in enumerate(questions, 1):
    print(f"\n{'=' * 80}")
    print(f"Processing Question {i}/{len(questions)}: {question}")
    print(f"{'-' * 80}")
    
    start_time = time.time()
    
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
                "content": question
            }
        ],
        temperature=1.0,
        top_p=1.0,
        max_output_tokens=4000
    )
    
    end_time = time.time()
    duration = end_time - start_time
    total_time += duration
    
    results.append({
        "question": question,
        "time": duration
    })
    
    print(f"Response to Question {i} (took {duration:.2f} seconds):")
    print(f"{'-' * 80}")
    print(response.output_text)
    print(f"{'=' * 80}")

# Print summary
print("\nSUMMARY:")
print(f"{'-' * 80}")
print(f"Total questions processed: {len(questions)}")
print(f"Total time: {total_time:.2f} seconds")
print(f"Average time per question: {total_time/len(questions):.2f} seconds")
print("\nIndividual question times:")
for result in results:
    print(f"  - {result['question'][:50]}{'...' if len(result['question']) > 50 else ''}: {result['time']:.2f} seconds")