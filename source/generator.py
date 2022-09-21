import openai
import os

openai.api_key = os.getenv('OPENAI_KEY')
tokens_spent = 0
paths = {"prompts": os.path.join(os.getcwd(), 'prompts')}

def generate (prompt, max_tokens = 400, temp = 0.7, model = "davinci"):
    global tokens_spent

    model = "text-davinci-002" if model == 'davinci' else f"text-{model}-001"
    response = openai.Completion.create(prompt=prompt, max_tokens=max_tokens, stop='STOP', engine=model, temperature=temp)

    tokens_spent += tokens(prompt + response["choices"][0]["text"])
    return response["choices"][0]["text"]

def tokens (str):
    return int(len(str) / 4)

def get_tokens():
    global tokens_spent
    output = tokens_spent
    tokens_spent = 0
    return output

def get_prompt (filename):
    with open(os.path.join(paths['prompts'],filename), 'r') as file:
        prompt = file.read()
    return prompt



