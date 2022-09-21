from source.generator import generate, get_tokens, get_prompt
import asyncio

loop = asyncio.get_event_loop()

def essay (prompt):
    result = loop.run_until_complete(write(prompt))
    output = {"result": result, "tokens": get_tokens()}
    return output

 
def main_points (topic):
    prompt = get_prompt("outline.txt").replace('<topic>',topic)
    text = generate(prompt, temp=0.5)
 
    points = []
    lines = ('1. Thesis:' + text).splitlines()
 
    for i in lines:
        if i[3:10] == 'Thesis:':
            points.append([i[11:]])
 
        if i[3:11] == 'Example:':
            points[-1].append(i[12:])
    return points

async def body (point):
    prompt = get_prompt("expander.txt").replace('<text>',(point[0] + ' ' + point[1]))
    text = generate(prompt).strip()
    return text


async def intro (topic):
    prompt = get_prompt('introduction.txt').replace('<topic>',topic)
    text = generate(prompt).strip()
    return text


async def conclusion (intro):
    prompt = get_prompt('conclusion.txt').replace('<intro>',intro)
    text = generate(prompt).strip()
    return text

 
def key_ideas (text, topic):
    prompt=get_prompt('ideas.txt').replace('<text>',text).replace('<topic>',topic)
    output = '-' + generate(prompt, max_tokens=200, model='davinci')
    ideas = [l.replace('- ','-') for l in output.splitlines()]
    return ideas

async def write (topic):
    intro_task = asyncio.create_task(intro(topic))
    points = main_points(topic)
    bodies_tasks=[asyncio.create_task(body(p)) for p in points]
    [await task for task in bodies_tasks]
    bodies = [task.result() for task in bodies_tasks]
    await intro_task
    i = intro_task.result()
    b = '\n\n'.join(bodies)
    c = await conclusion(i)
    essay = '\n\n'.join([topic,i,b,c])
    return essay

#prompt = "Benefits of keto diet"
#print(essay(prompt)['result'])