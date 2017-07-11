import os.path
import cherrypy
from cherrypy.lib import static
import urllib, json
import operator
from urllib2 import urlopen, Request
from requests.auth import HTTPBasicAuth

from user import User
from repo import Repo
from documentCreator import DocumentCreator


localDir = os.path.dirname(__file__)
absDir = os.path.join(os.getcwd(), localDir)

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
        token = "c94b5c2e5de3a12911aa2802d8267ebcd114d65a"
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

        allRepos = sorted(allRepos)
        allRepos = list(reversed(allRepos))

        if (len(allRepos) > 5):
            del allRepos[5:]

        dc = DocumentCreator(name, user, allRepos)
        dc.buildDoc()

        return """
        <html><body>
            <h2>Your GitHub Resume is complete!</h2>
            <a href='download'>Download Now</a>
        </body></html>
        """

    @cherrypy.expose
    def download(self):
        path = os.path.join(absDir, "example.docx")
        return static.serve_file(path, "application/x-download",
                                 "attachment", os.path.basename(path))

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    import sys
    import os
    port = os.environ['PORT']
    print(port)
    cherrypy.config.update({
                            'server.socket_host': '0.0.0.0',
                            'server.socket_port': int(port),
                           })
    cherrypy.quickstart(WelcomePage())
