
from litellm import completion
import os


# Set the OpenAI API key


#This is the only function that needs to be changed
def generate_response(user_text, model, api_key):
    # Set the OpenAI API key
    if(model == "openai/gpt-4o"):
        os.environ["OPENAI_API_KEY"] = api_key
    elif(model == "gemini/gemini-2.5-flash"):
        print("wa")
        os.environ["GOOGLE_API_KEY"] = 'AIzaSyCtKXYBJHqD3R0a1L2hlPDw5SF9zMzapr8'

    messages = [{ "content": user_text,"role": "user"}]
    response = completion(model=model, messages=messages)
    return response['choices'][0]['message']['content']

#dummy response when just doing UI testing
def generate_response2(user_text, model, api_key):
    print(f"Model: {model}, API Key: {api_key}")
    responses = {
        "hello": "Hi there! How can I help?",
        "how are you": "I'm just a bot, but I'm functioning well!",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(user_text.lower(), "I don't understand.")