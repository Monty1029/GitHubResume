import os.path
import cherrypy
import urllib, json
import operator
from urllib2 import urlopen, Request
from requests.auth import HTTPBasicAuth

from user import User
from repo import Repo
from documentCreator import DocumentCreator


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

        url = "https://api.github.com/users/" + name + "/repos"
        token = "TOKEN"
        request = Request(url)
        request.add_header('Authorization', 'token %s' % token)
        response = urlopen(request)
        data = json.loads(response.read())

        if data[0]["name"] is None:
            return 'Please enter your GitHub username <a href="./">here</a>.'

        allRepos = []
        user = User(name)
        repoIndex = 0
        output = ""
        
        for x in data:
            repo = Repo(name)
            repo.setRepoName(repoIndex)
            repo.setLang(repoIndex)
            repo.setCreationDate(repoIndex)
            repo.setStars(repoIndex)
            allRepos.append(repo)
            repoIndex += 1

        print len(allRepos)

        if (len(allRepos) <= 5):
            for x in allRepos:
                output += x.getRepoName() + " "
        else:
            allRepos = sorted(allRepos)
            allRepos = list(reversed(allRepos))
            del allRepos[5:]
            for x in allRepos:
                output += x.getRepoName() + " "

        dc = DocumentCreator(name, user, allRepos)
        dc.buildDoc()

        return "Your GitHub Resume is complete!"

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(WelcomePage())
