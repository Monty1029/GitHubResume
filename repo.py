import urllib, json
from urllib2 import urlopen, Request

class Repo:

    data = []
    repoName = ""
    creationDate = ""

    def __init__(self, name=None):
        self.name = name
        global data
        url = "https://api.github.com/users/" + name + "/repos"
        token = "TOKEN"
        request = Request(url)
        request.add_header('Authorization', 'token %s' % token)
        response = urlopen(request)
        data = json.loads(response.read())

    def getRepoName(self):
        global repoName
        return repoName

    def getCreationDate(self):
        global creationDate
        return creationDate

    def setRepoName(self, repoNumber=None):
        global repoName
        repoName = data[repoNumber]["name"]

    def setCreationDate(self, repoNumber=None):
        global creationDate
        creationDate = data[repoNumber]["created_at"]