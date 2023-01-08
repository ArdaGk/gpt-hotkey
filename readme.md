## Setup
1. pip install -r requirements.txt
2. Rename .env.example to .env
3. Enter the openai api token inside .env
4. python3 main.py


## How it works?
Copying a text into the clipboard will trigger a GPT-3 completion. Each predefined prompt can be assigned to a key pattern, if a text is copied after a key pattern, the text inside the clipboard will be inserted into the prompt and sent to gpt-3. As soon as text generation is complete, the content of the clipboard will be replaced with the output.

## Example
Target text:
```"Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. (Wikipedia)" ``` 

prompts/paraphrase.txt
```
Sentence: <text>
Paraphrased:
```
After the text is highlighted, pressing "Ctrl x3 and Ctrl+C" will copy the text into the clipboard, replace the \<text\> with the actual text, and send it to GPT-3. The output will automatically be copied into the clipboard.

Result (Ctrl+V):
```Docker is a set of PaaS products that use virtualization to deliver software in containers.```

