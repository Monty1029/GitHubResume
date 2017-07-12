import urllib, json
from urllib2 import urlopen, Request

class User:

    def __init__(self, name=None):
        self.name = name
        
    def callAPI(self, url):
        token = "d3cfc92d830f70979286fdf9e0781c4f2d24df0a"
        request = Request(url)
        request.add_header('Authorization', 'token %s' % token)
        response = urlopen(request)
        data = json.loads(response.read())
        return data    

    def getName(self, name=None):

        output = ""
        url = "https://api.github.com/users/" + self.name

        data = self.callAPI(url)
        name = data["name"]
        output += "%s" % name

        return output

    def getBio(self, name=None):
        output = ""
        url = "https://api.github.com/users/" + self.name
        data = self.callAPI(url)
        if data["bio"] is not None:
            bio = data["bio"]
            output += "%s" % bio

        return output

    def getFollowers(self, name=None):
        url = "https://api.github.com/users/" + self.name
        data = self.callAPI(url)
        return str(data["followers"])

    def getOrganizations(self, name=None):
        url = "https://api.github.com/users/" + self.name + "/orgs"
        data = self.callAPI(url)

        output = ""

        for x in data:
            output += "%s\n" % x["login"]

        return output