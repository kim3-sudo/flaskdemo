# Python: app.py

We start by importing the libraries that we need:

```
from flask import Flask, request, render_template
import sys
```

Then, we name the Flask app explicitly. It's possible to use the implicit naming, but it can obscure readibility and sometimes, it just screws up because you mislabeled something. It's just good to have as a sanity check.

```
app = Flask(__name__)
```

Now, we return the blank HTML page, without anything filled. Because we're not expecting any content, we're just going to leave the method empty. You can link to any .html file in the templates directory. I'm also laying out which path I'll access my Flask app at: documentroot/flaskdemo.

```
@app.route('flaskdemo')
	def indexpage():
	return render_template('./index.html')
```

Now, when I do enter some material onto the page and make a POST request, I want to be able to read it, so that's what the material is from lines 10-40.

This should all be fairly self-explanatory - it's just a Python function with some web stuff in it.

On line 12:

```
if request.method =='POST':
```

I do want to make sure that someone isn't trying to run a GET request, otherwise my Python code will freak out and not work properly. If a GET request is made, the function will just return empty variables.

In line 14:

```
name = request.form.get('name', False)
```

I'm grabbing an element from the HTML by the element name (not to be confused with the element ID - they're not the same thing!

I need to specify a default value (in this case, False), otherwise my Python interpreter won't be able to execute the full function, and Flask will freak and throw a 400 error (bad request).

This function comes from the request class, which is part of the Flask library.

I'm doing the same thing with the alignment element.

In lines 32-34, I print some stuff to the console - this is just regular Python after all. I do need to specify where I'm making my prints to, the system console - that's why I need to load the sys library.

Finally, in line 37, I return the render template with the variables:

```
return render_template('index.html',processed_name=processed_name, processed_align=processed_align)
```

I'm returning the same variables into the same HTML document, but I've put some special sauce in the HTML document that will let me read those Flask variables.
