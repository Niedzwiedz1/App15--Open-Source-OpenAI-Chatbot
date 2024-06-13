import openai
import os

class Chatbot:
    def __init__(self):

        api_pass = os.getenv('OPENAI_API_KEY')
        openai.api_key = api_pass

    def get_response(self, user_query):
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",  # Specify the appropriate chat-based model
            messages=[{"role": "user", "content": user_query}],
            max_tokens=100,
            temperature=0.5
        ).choices[0].message['content']
        return response

if __name__ == "__main__":
    bot = Chatbot()
    response = bot.get_response(user_query="napisz mi wiersz o Martynie")
    print(response)


