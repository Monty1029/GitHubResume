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
        self.stars = 0
        global data
        url = "https://api.github.com/users/" + name + "/repos"
        token = "TOKEN"
        request = Request(url)
        request.add_header('Authorization', 'token %s' % token)
        response = urlopen(request)
        data = json.loads(response.read())

    def __cmp__(self, other):
        if (self.stars > other.stars):
            return 1
        elif (self.stars < other.stars):
            return -1
        else:
            return 0

    def getRepoName(self):
        return self.repoName

    def setRepoName(self, repoNumber=None):
        self.repoName = data[repoNumber]["name"]

    def getCreationDate(self):
        return self.creationDate

    def setCreationDate(self, repoNumber=None):
        self.creationDate = data[repoNumber]["created_at"]

    def getStars(self):
        return self.stars

    def setStars(self, repoNumber=None):
        self.stars = data[repoNumber]["stargazers_count"]