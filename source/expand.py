from source.generator import generate, get_prompt, get_tokens

def expand(text):
    prompt = get_prompt('expander.txt').replace('<text>', text)
    result = generate(prompt)
    output = {"result": result, "tokens": get_tokens()}
    return output

