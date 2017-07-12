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
        self.lang = ""
        global data
        url = "https://api.github.com/users/" + name + "/repos"
        token = "fd672c7370710e401e94bbcc97f7ab073ec3e928"
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

    def getLang(self):
        return self.lang

    def setLang(self, repoNumber=None):
        self.lang = data[repoNumber]["language"]

    def getCreationDate(self):
        return self.creationDate

    def setCreationDate(self, repoNumber=None):
        self.creationDate = data[repoNumber]["created_at"]
        self.creationDate = self.creationDate[:10]

    def getStars(self):
        return self.stars

    def setStars(self, repoNumber=None):
        self.stars = data[repoNumber]["stargazers_count"]