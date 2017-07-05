import os.path
import cherrypy
import urllib, json
from user import User


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

        user = User(name)
        output = user.getName() + "<br>" + user.getBio() + "<br>" + str(user.getFollowers()) + "<br>" + user.getOrganizations() + "<br>" + user.getPublicRepos()
        return output

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(WelcomePage())
