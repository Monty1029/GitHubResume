"""
Tutorial - Passing variables

This tutorial shows you how to pass GET/POST variables to methods.
"""

import os.path

import cherrypy

import urllib, json


class WelcomePage:

    @cherrypy.expose
    def index(self):
        # Ask for the user's name.
        return '''
            <form action="greetUser" method="GET">
            What is your name?
            <input type="text" name="name" />
            <input type="submit" />
            </form>'''

    @cherrypy.expose
    def greetUser(self, name=None):
        # CherryPy passes all GET and POST variables as method parameters.
        # It doesn't make a difference where the variables come from, how
        # large their contents are, and so on.
        #
        # You can define default parameter values as usual. In this
        # example, the "name" parameter defaults to None so we can check
        # if a name was actually specified.

        url = "https://api.github.com/users/" + name
        response = urllib.urlopen(url)
        data = json.loads(response.read())

        if data["name"]:
            # Greet the user!
            return "Name: %s" % data["name"]
        else:
            if data["name"] is None:
                # No name was specified
                return 'Please enter your name <a href="./">here</a>.'
            else:
                return 'No, really, enter your name <a href="./">here</a>.'

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(WelcomePage())
