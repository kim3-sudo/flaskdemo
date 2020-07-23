from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def indexpage():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def form_post():
	text = request.form['text']
	processed_text = text.upper()
	return processed_text

