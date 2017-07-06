import urllib, json


class User:

    def __init__(self, name=None):
        self.name = name
        
    def callAPI(self, url):
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        return data    

    def getName(self, name=None):

        output = ""
        url = "https://api.github.com/users/" + self.name

        data = self.callAPI(url)

        if data["name"]:
            name = data["name"]
            output += " %s" % name
        else:
            if data["name"] is None:
                return 'Please enter your GitHub username <a href="./">here</a>.'
            else:
                return 'Please enter your GitHub username <a href="./">here</a>.'

        return "Name: " + output

    def getBio(self, name=None):
        output = ""
        url = "https://api.github.com/users/" + self.name
        data = self.callAPI(url)
        if data["bio"] is not None:
            bio = data["bio"]
            output += " %s" % bio

        return "Bio: " + output

    def getFollowers(self, name=None):
        url = "https://api.github.com/users/" + self.name
        data = self.callAPI(url)
        return "Followers: " + str(data["followers"])

    def getOrganizations(self, name=None):
        url = "https://api.github.com/users/" + self.name + "/orgs"
        data = self.callAPI(url)

        output = ""

        for x in data:
            output += " %s" % x["login"]

        return "Organizations: " + output