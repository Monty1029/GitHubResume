from docx import Document

from user import User
from repo import Repo

class DocumentCreator:

    def __init__(self, name=None, user=None, allRepos=None):
        self.name = name
        self.user = user
        self.allRepos = allRepos
    
    def buildDoc(self):
        doc = Document()
        doc.add_heading(self.user.getName(self.name) + " (" + self.name + ")", level = 1)
        doc.add_paragraph("Followers: " + self.user.getFollowers(self.name)).add_run().font.bold = True
        doc.add_heading("Bio", level = 2)
        doc.add_paragraph(self.user.getBio(self.name))
        doc.add_heading("Organizations", level = 2)
        doc.add_paragraph(self.user.getOrganizations(self.name))
        doc.add_heading("Projects", level = 2)
        repoIndex = 0
        for x in self.allRepos:
            doc.add_paragraph(x.getRepoName())
            doc.add_paragraph(x.getCreationDate())
            doc.add_paragraph("Language: " + x.getLang())
            doc.add_paragraph("Stars: " + str(x.getStars()))
        doc.save('example.docx')