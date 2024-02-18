import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "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"

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


