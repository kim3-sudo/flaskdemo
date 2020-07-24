# Flask Demo

Just a simple interactive Python/Flask demo.

This demo's purpose is to show how to move data from a HTML form into your Python script, then regurgitate it back into HTML in a modified form.

To install it, clone the repository onto your computer or server:

`git clone https://github.com/kim3-sudo/flaskdemo.git`

Make sure you have Python 3, pip, flask, and sys installed:

`pip3 install flask`
`pip3 install sys`

Then, if you're on your local computer, run `flask run` while in the root directory of the repository (the same directory as app.py). In your web browser on the same machine, go to localhost:5000/flaskdemo or whatever the localhost assignment is for your computer.

If you're on a server, run `flask run --host=0.0.0.0` while in the root directory of the repository (the same directory as app.py). In the web browser on a different device, go to navigate to the IP address of the server on port 5000, and add `/flaskdemo` to the end. It should look like `1.2.3.4:5000/flaskdemo` where `1.2.3.4` is replaced with your server's IP address.
