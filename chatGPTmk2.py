from pyChatGPT import ChatGPT
import openai

openai.organization = "org-VImW1GPOrIrZZDPBxHpb9YTQ"


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')


def gpt3_completion(prompt, engine='text-davinci-003',
                    temp=0.7, top_p=1.0, tokens=400,
                    freq_pen=0.5, pres_pen=0.5, stop=None):
    if stop is None:
        stop = ['King Julian', 'USER']
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop
    )
    text = response['choices'][0]['text'].strip()
    return text


if __name__ == '__main__':
    conversation = list()
    while True:
        user_input = input('')
        response = gpt3_completion(user_input)
        print(response)
