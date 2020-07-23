from flask import Flask, request, render_template
import sys
import request

app = Flask(__name__)

@app.route('/flaskdemo')
def indexpage():
	return render_template('index.html')

@app.route('/flaskdemo', methods=['POST'])
def form_post():
	# Get the name from the HTML form
	name = request.form.get['name']
	# Do processing on the name
	processed_name = request.args.get('name')

	# Get the alignment from the HTML form
	align = request.form.get['alignment']

	# Do processing on the alignment
	if (align == 'rebel'):
		processed_align = 'Rebel Alliance'
	elif (align == 'empire'):
		processed_align = 'Galactic Empire'
	elif (align == 'other'):
		processed_align = 'Other'
	else:
		processed_align = 'Error'

	# Print some stuff to the console for the lolz
	print('Here\'s what I got:', file=sys.stdout)
	print(name, file=sys.stdout)
	print(align, file=sys.stdout)

	# Prepare the data to send back to HTML
	output = execute('./request.py')

	# Return the Flask rendering template
	return render_template('index.html',output=output)
