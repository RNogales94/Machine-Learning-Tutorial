from flask import Flask, request
from translate import Translator

app = Flask(__name__)
translator = Translator(to_lang="en")


@app.route('/')
def index():
    return 'Hello world!'


@app.route('/translate', methods=['POST'])
def translate():
    text = request.json['text']
    print(text)
    text_translated = translator.translate(text)
    return text_translated


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
