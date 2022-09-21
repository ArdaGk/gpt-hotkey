from source.generator import generate, get_prompt, get_tokens

def qa(text):
    prompt = get_prompt('qa.txt').replace("<text>", text)
    result = generate(prompt)
    output = {"result": result, "tokens": get_tokens()}
    return output
