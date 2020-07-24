# HTML: templates/index.html

For the most part, this is just regular HTML.

On line 10, I do need to explicitly state which stylesheet I want to pull in, since I'm using an external stylesheet.

Of note is, I'm **not** using Bootstrap or jQuery here. It's just a lot of code that I really don't need. Instead, I made my own CSS classes.

We'll go over the CSS classes later.

The specific syntax that I'm using for the `href` is different than you might use for Apache or Nginx, though. Since we're using Flask, we need to specify that our stylesheet is a static object.

```
href="{{ url_for('static', filename='css/style.css') }}"
```

The next interesting thing comes in line 23, where I create the form.

I need to explicitly state the method that this form is operating in: POST. You should also give your form a name. It's a good idea to also explicitly state the encoding type (`>multipart/form-data`), though this isn't entirely necessary.

The rest of the form is constructed as you'd otherwise construct a form.

To inform the form that I want to make the POST request, I need to explicitly mention that the button type at the bottom of the form (line 36) should be a submit button.

```
<button type="submit" class="btn btn_kenyon">Submit</button>
```

Below, from lines 42-44, Flask is going to fill in the processed variables that I just returned in the Python script. Enclose the variable names in double-curly-braces for Flask to take control of that HTML chunk.

Finally, we're to this very text that you're reading right now!

CSS: static/css/style.css

You might've noticed that in the HTML, there isn't any inline style! That's because I've crammed it all into one CSS document, created a bunch of CSS classes, then referred to those classes here.

Notice how in this HTML document, there's classes that you've never seen, like `btn_kenyon`? That's surely not in Bootstrap!

Well, if you look at style.css, you'll find that on line 55, there's a class called `btn_kenyon`. Every time I refer to that class in this HTML document, I'll get the style that's inside of those curly braces.

There are some cases where class precedence will cause issues. This means that two classes will be called for one asset that have overlapping properties.

To avoid issues and definitively choose the style that we want, we can use the `!important` suffix on our CSS style attributes. It's important (pun not intended) to note that, you should use the `!important` suffix very sparingly, because there's no super-important suffix.

Having a `!important` suffix will not overturn your inline CSS or header CSS. For context, your HTML will look for inline css first (you know, the `style="attribute: value;"` stuff). If it can't find any, then it'll check in the head for a non-linked stylesheet (so, if you wrote `<style>p {font-family: 'Roboto Mono', monospace;}</style>`, it'd choose that next. Finally, if it can't find any CSS inline or in the head, then it'll refer to external stylesheets.

You can also overwrite default styles. Notice in style.css how I've redefined the style for headings, paragraphs, labels, and links.

Lastly, you can use a @media tag to choose what happens when certain responsiveness actions occur. Try to shrink and expand this webpage horizontally (along the x-axis). Notice how <a href="#">link colors</a> and background colors change when you go above and beyond 700px. That's the job of the @media tags, like on line 69.
