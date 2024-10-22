# **Mini-coding assignment (API Integration) using Hugging Face API**

## **Overview**
This Python application demonstrates how to interact with the Hugging Face API to generate creative text based on a given prompt. In this case, it's a createive "Hello World" message.

API calls to GPT-2 and Mistral-7B-v0.1 models from Hugging Face are done via 2 similar methods:
1. `InferenceClient`: a Python client making HTTP calls to HuggingFace's APIs.
2. Manually use `requests` library to make HTTP calls to HuggingFace's inference APIs.

The API key is securely stored in a separate file and loaded into the script using the `python-dotenv` package to prevent exposing sensitive data.

[**Quick-start video for Hugging Face**](https://www.youtube.com/watch?v=1AUjKfpRZVo)


## **Steps took to Integrate the Hugging Face API**

1. **Create a Hugging Face Account**:
- Go to [Hugging Face](https://huggingface.co/) and create an account.
- Navigate to your [profile settings](https://huggingface.co/settings/tokens) and generate an API token. Save this token locally because you won't be able to see it again on HuggingFace.

2. **Install Necessary Libraries**:
- `requests` for making HTTP calls
- `python-dotenv` for managing API keys from a `.env` file
- `huggingface_hub` to access its tool kit

3. **Set Up Environment File**:

Create a `.env` file (e.g., the code references `keys.env`) to securely store your Hugging Face API token. The format of the `.env` file should look like this:

```
HUGGINGFACE_API_KEY=your-huggingface-api-key
```

4. **Wrote Python Code**:

To summarize the Python code consists of:
- Reading the API key from the `.env` file.
- Sending a POST request to Hugging Face’s model using the API (or via InferenceClient).
- Retrieving and displaying the generated creative text.

5. **Others**:
- Ensure `*.env` file (and any other secrets) is added to [`.gitignore`](.gitignore) to prevent it from being published to Git repositories.
- Exported the list of required libraries to [`requirements.txt`](requirements.txt)

## **How to Run the Application**

### **1. Setup**
- Clone the repository containing the script or download the code.
- Create a `.env` file (e.g., the Python code references `keys.env`) in the root directory and add your Hugging Face API token as follows:
```
HUGGINGFACE_API_KEY=your-huggingface-api-key
```

### **2. Install Dependencies**

Ensure you have Python installed and the necessary dependencies:

```bash
pip install -r requirements.txt
```

### **3. Run the Application**
To generate the creative text, simply run the Python script:

```bash
python hello_world.py
```

### **Expected Output**
When you run the script, you should see output like this:

```
Hello World, this is a test of the HuggingFace API. The response should be a list of 100 random images.

# 👋 Welcome to the HuggingFace API!

This is a simple API that allows you to access the HuggingFace API.
...
```

## **Notes**
*___To Change the model___*: The models being used in the script are GPT-2 and Mistral v0.1, but you can change the model by modifying the API URL (`api_url`) for the `generate_hello_world()` method, or by modifying the model ID (`repo_id`) for the `call_llm()` method. For example, you could use a different model hosted on Hugging Face, such as `gpt-3.5-turbo` if available.

*___To Change the Prompt___*: The input prompt can be adjusted under the `if __name__ == "__main__":` line, called `prompt`.

## **Reflection**
Initially, I wanted to use OpenAI's API with GPT4. However, I realized that it was not free, after I had taken quite some time looking at its documentation. I had to switch to Hugging Face APIs.

I know of another method to use HuggingFace models through the `transformers` library (using `pipeline`). But I wanted to try an elementary approach and a HuggingFace Hub client approach. I encountered a challenge in reading through the documentations for InferenceClient, but it basically models after OpenAI's APIs so that there is easy integration between the two. Otherwise, interacting with the Hugging Face API was a smooth experience, allowing me to use text-generation with minimal setup.

I am also very aware that using powerful models require many resources, from cloud processing capabilities to server costs and API costs. For future projects, this knowledge is definitely useful. I can confidently start LLM projects and build simple POC quickly using smaller models, before building a fuller prototype. I can also design and implement AI with more caution.