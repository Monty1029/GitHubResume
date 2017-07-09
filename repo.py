import urllib, json
from urllib2 import urlopen, Request

class Repo:

    data = []
    repoName = ""
    creationDate = ""

    def __init__(self, name=None):
        self.name = name
        self.repoName = ""
        self.creationDate = ""
        global data
        url = "https://api.github.com/users/" + name + "/repos"
        token = "TOKEN"
        request = Request(url)
        request.add_header('Authorization', 'token %s' % token)
        response = urlopen(request)
        data = json.loads(response.read())

    def getRepoName(self):
        return self.repoName

    def getCreationDate(self):
        return self.creationDate

    def setRepoName(self, repoNumber=None):
        self.repoName = data[repoNumber]["name"]

    def setCreationDate(self, repoNumber=None):
        self.creationDate = data[repoNumber]["created_at"]