:tocdepth: 2

==============
Second News App
==============

A step-by-step guide to publishing a simple news application that uses a SQL database

This tutorial will walk you through the process of building a simple news application that uses a database.
You will get hands-on experience in every stage of the development process, writing Python, HTML and JavaScript while recording it in Git's
version control system.

******************
What you will make
******************

By the end of this lesson, you will publish an interactive database and map
of notices of foreclosure in Maryland zip codes over the past two years.
You will do this with data published by the state at `https://opendata.maryland.gov/Housing/Maryland-Notices-of-Intent-to-Foreclose-by-Zip-Cod/ftsr-vapt <https://opendata.maryland.gov/Housing/Maryland-Notices-of-Intent-to-Foreclose-by-Zip-Cod/ftsr-vapt>`_

*****************
About the authors
*****************

This guide was designed by Derek Willis for the News Applications class at the University of Maryland's Philip Merrill College of Journalism.

**********************
Prelude: Prerequisites
**********************

Before you can begin, your computer needs the following tools installed and working.

1. An account at `GitHub.com <https://www.github.com>`_
2. A browser. That's it! (We'll be using GitHub's Codespaces.)

***********************
Act 1: Hello Codespaces
***********************

Start at the `GitHub URL for your version of this repository <https://github.com/NewsAppsUMD/second-news-app-umd-{yourusername}>`_

Click the green button and choose "Open in a codespace". You should see something like this:

.. image:: /_static/codespaces.png

The browser is divided into three sections: on the left is a file explorer, listing all of the files in this repository. The top right shows whatever file you're currently viewing or editing, defaulting to README.md. The bottom right shows the terminal, where we'll run commands.

The codespace will be connected to your repository in the `the NewsApps organization on GitHub <https://github.com/NewsAppsUMD/>`_.

Open up the README by clicking on README.md on the left side and type something in it. Maybe change the heading like:

.. code-block:: markdown

    # My Second News App

Make sure to save it. You'll see on the left that there's a yellow "M" next to README.md, meaning you've made some edits. Let's double-check that in the terminal:

.. code-block:: bash

    $ git status

You should see something like this:

.. image:: /_static/git_status.png

If so, we can add and commit it:

.. code-block:: bash

    $ git add README.md

Log its creation with Git's ``commit`` command. You can include a personalized message after the ``-m`` flag.

.. code-block:: bash

    $ git commit -m "First commit"

Now, finally, push your commit up to GitHub.

.. code-block:: bash

    $ git push origin main

Reload your repository on GitHub and see your handiwork.

******************
Act 2: Hello Flask
******************

Use pip on the command line to install `Flask <https://palletsprojects.com/p/flask/>`_, the Python "microframework" we'll use to put together our website.

.. code-block:: bash

    $ pip install Flask

Create a new file called ``app.py`` where we will configure Flask.

.. code-block:: bash

    # in the terminal:
    $ touch app.py

Open ``app.py`` with your code editor and import the Flask basics. This is the file that will serve as your
application's "backend," routing data to the appropriate pages.

.. code-block:: python

    from flask import Flask
    app = Flask(__name__)  # Note the double underscores on each side!

Next we will configure Flask to make a page at your site's root URL.

Configure Flask to boot up a test server when you run ``app.py`` like so:

.. code-block:: python
    :emphasize-lines: 4-6

    from flask import Flask
    app = Flask(__name__)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

.. note::

    You're probably asking, "What the heck is ``if __name__ == '__main__'``?" The short answer: It's just one of the weird things in Python you have to memorize. But it's worth the brain space because it allows you to run any Python script as a program.

    Anything indented inside that particular ``if`` clause is executed when the script is called from the command line. In this case, that means booting up your web site using Flask's built-in ``app.run`` function.

Don't forget to save your changes. Then run ``app.py`` on the command-line and open up your browser to `localhost:5000 <http://localhost:5000>`_

.. code-block:: bash

    $ python app.py

Here's what you should see. A website with nothing to show.

.. image:: /_static/hello-flask-404.png

Next we'll put a page there. Our goal is to publish the complete list of people who died during the riots using a template. We will call that template "index.html".

Before we do that, return to your command-line interface and stop your webserver by hitting the combination of ``CTRL-C``. You should now again at the standard command-line interface.

Now in ``app.py`` import ``render_template``, a Flask function we can use to combine data with HTML to make a webpage.

.. code-block:: python
    :emphasize-lines: 2

    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

Then create a function called ``index`` that returns our rendered ``index.html`` template.

.. code-block:: python
    :emphasize-lines: 5-8

    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

Now use one of Flask's coolest tricks, the ``app.route`` decorator, to connect that function with the root URL of our site, ``/``.

.. code-block:: python
    :emphasize-lines: 5

    from flask import Flask
    from flask import render_template
    app = Flask(__name__)

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        # Fire up the Flask test server
        app.run(debug=True, use_reloader=True)

Return to your command line and create a directory to store your templates in `the default location Flask expects <https://flask.palletsprojects.com/en/2.2.x/quickstart/#rendering-templates>`_.

.. code-block:: bash

    $ mkdir templates

Next create the ``index.html`` file we referenced in ``app.py``. This is the HTML file where your will lay out your webpage.

.. code-block:: bash

    $ touch templates/index.html

Open it up in your text editor and write something clever.

.. code-block:: html

    Hello World!

Now restart your Flask server.

.. code-block:: bash

    $ python app.py

Head back to your browser and visit your site again. You should see the contents of your template displayed on the page.

.. image:: /_static/hello-flask-hello-world.png

We're approaching the end of this act, so it's time to save your work by returning to the
command line and committing these changes to your Git repository.

.. note::

    To get the terminal back up, you will either need to quit out of ``app.py`` by hitting ``CTRL-C``, or open a second terminal and do additional work there. If you elect to open a second terminal, which is recommended, make sure to check into the virtualenv by repeating the ``. bin/activate`` part of :ref:`activate`. If you choose to quit out of ``app.py``, you will need to turn it back on later by calling ``python app.py`` where appropriate.

    As we progress through this lesson, you will need to continually do this to switch between the server and terminal. We no longer be instructing to do it each time from here on.

I bet you remember how from above. But here's a reminder.

.. code-block:: bash

    $ git add . # Using "." is a trick that will quickly stage *all* files you've changed.
    $ git commit -m "Flask app.py and first template"

Push it up to GitHub and check out the changes there.

.. code-block:: bash

    $ git push origin main

Congratulations, you've made a real web page with Flask. Now to put something useful in it.

Start over in your ``templates/index.html`` file with a bare-bones HTML document.

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
        </head>
        <body>
            <h1>Maryland Notices of Foreclosure by Zip Code</h1>
        </body>
    </html>

Commit the changes to your repository, if only for practice.

.. code-block:: bash

    $ git add templates/index.html
    $ git commit -m "Real HTML"
    $ git push origin main

*******************
Act 3: Hello SQLite
*******************

When you’re Serious About Data (which we are, of course), you store your data in a database, not an Excel spreadsheet or CSV file. They’re faster and more flexible.

Our database is going to be a SQLite database, which is perfect and wonderful because it’s just a file. If I want to send you my database, I can just send it to you via email or Dropbox or whatever - no playing around with installing things or servers or anything like this. Think of it like a small upgrade to a CSV file.

To create our new SQLite database, we’re going to start with a CSV file. First, make a directory to store our data file.

.. code-block:: bash

    $ mkdir static

Download `the comma-delimited file <https://raw.githubusercontent.com/NewsAppsUMD/second-news-app-umd/main/docs/_static/foreclosures_by_month.csv>`_ that will be the backbone of our application and save it in the static directory as ``foreclosures_by_month.csv``. Now we'll install the tools necessary to turn it into a SQLite database, namely `sqlite-utils`.
Then we'll create the database from the CSV file:

.. code-block:: bash

    $ cd static
    $ wget https://raw.githubusercontent.com/NewsAppsUMD/second-news-app-umd/main/docs/_static/foreclosures_by_month.csv
    $ cd ..

.. code-block:: bash

    $ pip install sqlite-utils
    $ sqlite-utils insert foreclosures.db notices static/foreclosures_by_month.csv --csv

Add both the CSV and database file to your git repository.

.. code-block:: bash

    $ git add static
    $ git commit -m "Added CSV source data and db file"
    $ git push origin main

Once upon a time there were databases, and there was SQL, and there were people who loved writing SQL. SQL is cool, SQL is great!

Then everyone else was invented, and they didn’t like writing SQL, they just liked writing Python. So the Gods invented ORMs, which basically mean “instead of writing SQL you’ll just write Python and the ORM will talk to the database for you.”

Now everyone can be happy, sort of.

There are a handful of ORMs that work for Python, and plenty that work with Flask. We'll use one called Peewee, because, well, it's small:

.. code-block:: bash

    $ pip install peewee

Next we will open up ``app.py`` in your code editor and add the import needed to use it:

.. code-block:: python
    :emphasize-lines: 3

    from flask import Flask
    from flask import render_template
    from peewee import *
    app = Flask(__name__)

    @app.route("/")
    def index():
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Now we need to tell Flask about our database and its notices table. Every table is called a Model, and we use that model to play around with its associated table from Python. (Although we only have one table in this case, so we’ll only have one model).

Going back to our code - right after we make our Flask app with app = Flask(__name__), you’ll want to tell Peewee everything important about the database and its tables. It’ll look like this:

.. code-block:: python
    :emphasize-lines: 6-15

    from flask import Flask
    from flask import render_template
    from peewee import *
    app = Flask(__name__)

    db = SqliteDatabase('foreclosures.db')

    class Notice(Model):
        id = IntegerField(unique=True)
        zip = CharField()
        month = DateField()
        notices = IntegerField()

        class Meta:
            database = db

Let’s take it line-by-line to get an idea of what’s going on (or a-few-lines by a-few-lines).

First off, you tell the app where to find the database and have Peewee read it. Then we tell Peewee about the notices table.

We need to tell the model several things:

    * Its name. In this case, we’re calling it Notice, because it’s… a list of notices.
    * The columns and their datatypes. We also add a "unique=True" to the id column because no two values of that column are the same.
    * The Meta class just makes explicit which database the notices table is in (we could use multiple databases) and the table name (in case we want to change it).

Fire up the server if it isn't running and give your page a refresh to make sure you don’t have any typos or other little issues, and then we’ll charge ahead to actually using this model.

We don’t know how to make our database talk to the web page yet, so we’re going to cheat a little bit. Let’s edit the /index route to make it print something out:

.. code-block:: python
    :emphasize-lines: 20

    from flask import Flask
    from flask import render_template
    from peewee import *
    app = Flask(__name__)

    db = SqliteDatabase('foreclosures.db')

    class Notice(Model):
        id = IntegerField(unique=True)
        zip = CharField()
        month = DateField()
        notices = IntegerField()

        class Meta:
            table_name = "notices"
            database = db

    @app.route("/")
    def index():
        print("Total number of notices is", Notice.select().count())
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Refresh the page and you’ll see… nothing changed? But pop on over to your command line, and you’ll see a secret little line hiding in the debug output.

When you use print in the Flask app, it doesn’t print to the web page. That’s the render_template part. Instead, print prints to the command line. It’s totally useless for showing things to the user, but a nice cheat to check things and help us debug.

Where’d that 11488 come from? Notice.select().count()! We used our model - Notice - to visit the database, build a new query, and count the number of rows in the table.

Because we’re using an Peewee, we write Python, not SQL. Peewee takes care of the translation to SQL and just gives us the result.

For example, we can do a WHERE query - filtering our data - by using get or where. Retrieving a single records might look like this:

.. code-block:: python

    >>> zip = Notice.get(zip == '20906')
    >>> zip.id
    3949

To play around a little, let’s try to find a specific zip code and month and print out its number of notices. We can use `where` to do that as well:

.. code-block:: python
    :emphasize-lines: 21-22

    from flask import Flask
    from flask import render_template
    from peewee import *
    app = Flask(__name__)

    db = SqliteDatabase('foreclosures.db')

    class Notice(Model):
        id = IntegerField(unique=True)
        zip = CharField()
        month = DateField()
        notices = IntegerField()

        class Meta:
            table_name = "notices"
            database = db

    @app.route("/")
    def index():
        print("Total number of notices is", Notice.select().count())
        notice = Notice.select().where(Notice.id==3963).get()
        print(f"Zip code {notice.zip} had {notice.notices} in {notice.month}")
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Make sure to save ``app.py``. Then reload the page and check the output in the terminal - remember, we're not showing anything on the page yet.

What comes back from the database is that one row where Notice.id==3963 - we only got one because we asked for .get(). It works just like a normal variable, kind of like a dictionary that you don’t need ['whatever'] for. Instead, you can just ask for each column with a period.

Since zip is the column with the zip code in it, we can just ask for notice.zip and it will print right out.

If we want to get fancier, we can also select multiple rows with .where().

.. code-block:: python
    :emphasize-lines: 23-25

    from flask import Flask
    from flask import render_template
    from peewee import *
    app = Flask(__name__)

    db = SqliteDatabase('foreclosures.db')

    class Notice(Model):
        id = IntegerField(unique=True)
        zip = CharField()
        month = DateField()
        notices = IntegerField()

        class Meta:
            table_name = "notices"
            database = db

    @app.route("/")
    def index():
        print("Total number of notices is", Notice.select().count())
        notice = Notice.select().where(Notice.id==3963).get()
        print(f"Zip code {notice.zip} had {notice.notices} in {notice.month}")
        notices_20906 = Notice.select().where(Notice.zip=='20906')
        for notice in notices_20906:
            print(notice.notices)
        template = 'index.html'
        return render_template(template)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Save app.py, reload the index page and check the terminal again. Lots of printing!

We’ve been flexing our sweet new Peewee ORM, testing our skills at querying and counting and WHEREing without WHEREs, but how about we actually make this useful? In the next section we’ll take a look at how we can put this data on the actual web page.

*****************
Act 4: Hello HTML
*****************

Let's edit our index template so that we're sending some information from the database directly to the page. We'll replace the print statements in our app.py and add some variables to the template:

.. code-block:: python
    :emphasize-lines: 20, 22

    from flask import Flask
    from flask import render_template
    from peewee import *
    app = Flask(__name__)

    db = SqliteDatabase('foreclosures.db')

    class Notice(Model):
        id = IntegerField(unique=True)
        zip = CharField()
        month = DateField()
        notices = IntegerField()

        class Meta:
            table_name = "notices"
            database = db

    @app.route("/")
    def index():
        notice_count = Notice.select().count()
        template = 'index.html'
        return render_template(template, count = notice_count)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Now, in the template file, let's add our `count` variable to the template and clean things up:

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
        </head>
        <body>
            <h1>Maryland Notices of Foreclosure by Zip Code</h1>
            <p>There are {{ count }} records in the database.</p>
        </body>
    </html>

Sending a single integer to our template is pretty easy, but so is sending a whole mess of things! Let’s send those notices from the 20906 ZIP code.

.. code-block:: python
    :emphasize-lines: 21, 23

    from flask import Flask
    from flask import render_template
    from peewee import *
    app = Flask(__name__)

    db = SqliteDatabase('foreclosures.db')

    class Notice(Model):
        id = IntegerField(unique=True)
        zip = CharField()
        month = DateField()
        notices = IntegerField()

        class Meta:
            table_name = "notices"
            database = db

    @app.route("/")
    def index():
        notice_count = Notice.select().count()
        notices_20906 = Notice.select().where(Notice.zip=='20906')
        template = 'index.html'
        return render_template(template, count = notice_count, notices = notices_20906)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Save that, and then we'll update the template:

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
        </head>
        <body>
            <h1>Maryland Notices of Foreclosure by Zip Code</h1>
            <p>There are {{ count }} records in the database.</p>
            {% for notice in notices %}
               <p>{{ notice.month }}: {{ notice.notices }}</p>
            {% endfor %}
        </body>
    </html>

Refresh, and you should be good to go! If not, make sure you matched up the variable names from app.py to the template.

We can't (shouldn't) put every zip code on the same page - we should make a page for each zip code! Let's do that. We'll use the zip code itself as the `slug` in the url.

To build our detail page, we need a new route in app.py. This is going to be a special route, since the end of the URL can change - /zipcode/20906 is different from /zipcode/21012. To accomplish this we add a variable into our route.

.. code-block:: python
    :emphasize-lines: 23-27

    from flask import Flask
    from flask import render_template
    from peewee import *
    app = Flask(__name__)

    db = SqliteDatabase('foreclosures.db')

    class Notice(Model):
        id = IntegerField(unique=True)
        zip = CharField()
        month = DateField()
        notices = IntegerField()

        class Meta:
            table_name = "notices"
            database = db

    @app.route("/")
    def index():
        notice_count = Notice.select().count()
        notices_20906 = Notice.select().where(Notice.zip=='20906')
        template = 'index.html'
        return render_template(template, count = notice_count, notices = notices_20906)

    @app.route('/zipcode/<slug>')
    def detail(slug):
        zipcode = slug
        notices = Notice.select().where(Notice.zip==slug)
        total_notices = Notice.select(fn.SUM(Notice.notices).alias('sum')).where(Notice.zip==slug).scalar()
        return render_template("detail.html", zipcode=zipcode, notices=notices, notices_count=len(notices), total_notices = total_notices)

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)

Now anything can do into the part after /zipcode/. If we want to find 20906, we’ll check out /zipcode/20906. But first we need to create detail template!

.. code-block:: bash

    $ touch templates/detail.html

Let's make it look good and show off our data:

.. code-block:: html

    <!doctype html>
    <html>
      <head>
        <title>Zip code: {{ zipcode }}</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
      </head>
      <body>
          <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="/">Zip Codes</a>
          </nav>
          <div class="jumbotron">
            <div class="container">
              <h1 class="display-4">{{ zipcode }}</h1>
              <p class="lead">This zip code has {{ notices_count }} records and {{ total_notices }} total notices.</p>
            </div>
          </div>
        </div>
      </body>
    </html>

Save both app.py and the detail template, make sure the app is running and check out one of your zipcode urls (like /zipcode/20906).

Now let's generate a list of zip codes that can link to the detail pages from the index template. First we'll need to send a list of all zip codes to the template by adding that to app.py:

.. code-block:: python
    :emphasize-lines: 22, 24

    from flask import Flask
    from flask import render_template
    from peewee import *
    app = Flask(__name__)

    db = SqliteDatabase('foreclosures.db')

    class Notice(Model):
        id = IntegerField(unique=True)
        zip = CharField()
        month = DateField()
        notices = IntegerField()

        class Meta:
            table_name = "notices"
            database = db

    @app.route("/")
    def index():
        notice_count = Notice.select().count()
        all_zips = (Notice.select(Notice.zip).distinct())
        template = 'index.html'
        return render_template(template, count = notice_count, all_zips = all_zips)

    @app.route('/zipcode/<slug>')
    def detail(slug):
        zipcode = slug
        notices = Notice.select().where(Notice.zip==slug)
        return render_template("detail.html", zipcode=zipcode, notices=notices, notices_count=len(notices))

    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True)


Then we can plug those zip codes in and build URLs.

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
        </head>
        <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="/">Maryland Foreclosure Notices by Zip Code</a>
        </nav>
          <div class="jumbotron">
            <div class="container">
                <h1>Maryland Notices of Foreclosure by Zip Code</h1>
                <p>There are {{ count }} records in the database.</p>
                <h3>Zip Codes</h3>
                <ul>
                    {% for zip in all_zips %}
                        <li><a href="/zipcode/{{ zip.zip }}">{{ zip.zip }}</a></li>
                    {% endfor %}
                </ul>
            </div>
        </div>
        </body>
    </html>

Now, let's think about visualizing this data.
