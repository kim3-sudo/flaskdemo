from flask import Flask, request, render_template
import sys

app = Flask(__name__)

@app.route('/flaskdemo')
def indexpage():
	return render_template('./index.html')

@app.route('/flaskdemo', methods=['POST'])
def index():
	if request.method == 'POST':
		# Get the name from the HTML form
		name = request.form.get('name', False)
		# Do processing on the name
		processed_name = name.upper()

		# Get the alignment from the HTML form
		align = request.form.get('alignment', False)

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
	#	output = execute('./request.py')

	# Return the Flask rendering template
	return render_template('index.html',processed_name=processed_name, processed_align=processed_align)

if __name__ == '__main__':
	app.run
