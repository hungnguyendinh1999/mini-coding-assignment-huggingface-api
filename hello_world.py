from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
import requests

 # Load environment variables from a .env file
load_dotenv("keys.env")
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

# Set up InferenceClient
repo_id = "mistralai/Mistral-7B-v0.1"

llm_client = InferenceClient( #InferenceClient is a Python client making HTTP calls to HF's APIs
    model = repo_id,
    timeout = 120,
    token = huggingface_api_key
)

# Call LLM text generation using InferenceClient
def call_llm(inference_client: InferenceClient, prompt: str):
    data = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100},
        "task": "text-generation"
    }
    response = inference_client.post(
        json=data
    )
    return response.json()[0]["generated_text"]


# 2. Use Hugging Face's inference API ("gpt2")
api_url = "https://api-inference.huggingface.co/models/gpt2"

def generate_hello_world(prompt: str):
    response = requests.post(
        api_url, 
        headers={"Authorization": f"Bearer {huggingface_api_key}"},
        json={"inputs": prompt})
    
    if response.status_code == 200:
        generated_text = response.json()[0]['generated_text']
        print(generated_text)
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # First way to call APIs
    prompt = "Hello World, this is a test of the HuggingFace API. The response should be"
    # generate_hello_world(prompt)
    print("---")
    
    # Second way is to use InferenceClient by huggingface
    response = call_llm(llm_client, prompt)
    print(response)
