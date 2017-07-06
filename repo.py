import urllib, json


class Repo:

    response = ""
    data = []

    def __init__(self, name=None):
        self.name = name
        global response
        global data
        url = "https://api.github.com/users/" + self.name + "/repos"
        response = urllib.urlopen(url)
        data = json.loads(response.read())

    def getRepoName(self):
        output = ""
        for x in data:
            output += "<br>%s" % x["name"]

        return "Repositories: " + output

    def getCreationDate(self):
        output = ""

        for x in data:
            output += "<br>%s" % x["created_at"]

        return "Creation Date: " + output