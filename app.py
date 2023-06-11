from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

# Create an empty list to store the chat history
chat_history = []

def get_word_definition(word):
    try:
        timestamp = time.strftime('%H:%M')
        web = requests.get('https://prpm.dbp.gov.my/Cari1?keyword=' + word)
        data = web.content
        soup = BeautifulSoup(data, features="html.parser")
        tag = soup.find_all("div", "tab-pane fade in active")
        definitions = [i.text for i in tag]
        return definitions, timestamp
    except Exception as e:
        # Handle the error here, for example, print an error message
        print(f"An error occurred: {str(e)}")
        return None, None

@app.route('/')
def index():
    # Add initial bot message to the chat history
    if len(chat_history) == 0:
        timestamp = time.strftime('%H:%M')
        initial_bot_message = {
            'content': 'Welcome to DictionaryBot! How can I assist you today?',
            'sender': 'bot',
            'timestamp': timestamp
        }
        chat_history.append(initial_bot_message)

    return render_template('index.html', chat_history=chat_history)

@app.route('/definition', methods=['POST'])
def definition():
    word = request.form['word']
    definitions, timestamp = get_word_definition(word)

    if definitions:
        # Append user's message to the chat history
        user_message = {'content': word, 'sender': 'user', 'timestamp': timestamp}
        chat_history.append(user_message)

        # Append bot's response to the chat history
        bot_response = {'content': definitions, 'sender': 'bot', 'timestamp': timestamp}
        chat_history.append(bot_response)

        return render_template('index.html', chat_history=chat_history, timestamp=timestamp)
    else:
        # Append user's message to the chat history
        user_message = {'content': word, 'sender': 'user', 'timestamp': timestamp}
        chat_history.append(user_message)

        # Append bot's response with error message to the chat history
        bot_response = {'content': 'Sorry, I couldn\'t find a definition for that word.', 'sender': 'bot', 'timestamp': timestamp}
        chat_history.append(bot_response)

        return render_template('index.html', chat_history=chat_history, timestamp=timestamp, error=True)

if __name__ == '__main__':
    app.run(debug=True)
