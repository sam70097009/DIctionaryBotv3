from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

app = Flask(__name__)

def get_word_definition(word):
    timestamp = time.strftime('%H:%M')
    web = requests.get('https://prpm.dbp.gov.my/Cari1?keyword=' + word)
    data = web.content
    soup = BeautifulSoup(data, features="html.parser")
    tag = soup.find_all("div", "tab-pane fade in active")
    definitions = [i.text for i in tag]
    return definitions, timestamp

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/definition', methods=['POST'])
def definition():
    word = request.form['word']
    definitions, timestamp = get_word_definition(word)
    
    if definitions:
        show_thanks = request.form.get('answer') == 'yes'  
        show_regret = request.form.get('answer') == 'no' 
        return render_template('index.html', definitions=definitions, word=word, timestamp=timestamp, show_thanks=show_thanks, show_regret=show_regret)
    else:
        return render_template('index.html', word=word, error=True)


if __name__ == '__main__':
    app.run(debug=True)
