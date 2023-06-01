import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder='.', template_folder='.')
openai.api_key = 'KEY' #Ommited for security reasons

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a cooking and recipe assistant. Refuse to answer any question not related to cooking, food, nutrients, or meal prep."},
            {"role": "user", "content": message},
        ],
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    reply = response.choices[0].message.content.strip()

    return jsonify({'message': reply})

if __name__ == '__main__':
    app.run()
