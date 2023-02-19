import os
import openai

MAX_TOKENS = 3000

class GptApi:
    openai.api_key = ''

    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_text(self, prompt):
        openai.api_key = self.api_key
        response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0,
                                            max_tokens=MAX_TOKENS)
        return response

    def generate_text_only_answer(self, prompt):
        openai.api_key = self.api_key
        response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0,
                                            max_tokens=MAX_TOKENS)
        return response["choices"][0]["text"]

    def generate_image(self, prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
