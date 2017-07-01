import os.path

import cherrypy

import urllib, json


class WelcomePage:

    @cherrypy.expose
    def index(self):
        
        return '''
            <form action="displayResult" method="GET">
            What is your GitHub username?
            <input type="text" name="name" />
            <input type="submit" />
            </form>'''

    @cherrypy.expose
    def displayResult(self, name=None):
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

        output = ""

        if data["name"]:
            # Greet the user!
            output += "Name: %s" % data["name"]
        else:
            if data["name"] is None:
                # No name was specified
                return 'Please enter your GitHub username <a href="./">here</a>.'
            else:
                return 'Please enter your GitHub username <a href="./">here</a>.'

        output += "<br>Number of Followers: %s" % data["followers"]

        output += "<br>Organizations:"

        organizations_url = url + "/orgs"
        response = urllib.urlopen(organizations_url)
        data = json.loads(response.read())

        for x in data:
            output += " %s" % x["login"]

        return output

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(WelcomePage())
