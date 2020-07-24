# About Flask vs. Apache/Nginx

Like Apache or Nginx, Flask is a type of web server. Apache handles PHP quite well with support for Node.js, and Nginx handles Node.js and PHP well. However, Flask is designed to handle Python.

Flask's web server works in a fundamentally different way - it's designed to serve HTML that's delivered through a Python script - you can't deliver just HTML without any Python. Your templates folder is somewhat similar to the `/var/www/html` for Apache or `/var/www/nginx-default` for Nginx.

So, you could just have a server without Apache, Nginx, or any other web server installed, and then just use Python and Flask to serve your webpages.
