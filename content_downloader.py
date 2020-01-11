import requests
from bs4 import BeautifulSoup
import json
class Project:
    titlu=""
    callName=""
    codDepunere=""
    anIncepere=""
    anIncheiere=""
    role=""
    coordInstitution=""
    projectPartners=""
    affiliation=""
    website=""
    abstract=""
    def __init__(self,
                titlu="",
                callName="",
                codDepunere="",
                anIncepere="",
                anIncheiere="",
                role="",
                coordInstitution="",
                projectPartners="",
                affiliation="",
                website="",
                abstract=""):
        self.titlu=titlu
        self.callName=callName
        self.codDepunere=codDepunere
        self.anIncepere=anIncepere
        self.anIncheiere=anIncheiere
        self.role=role
        self.coordInstitution=coordInstitution
        self.projectPartners=projectPartners
        self.affiliation=affiliation
        self.website=website
        self.abstract=abstract
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=False, indent=4)
urls = []
with open('links.txt', 'r') as links:
    urls=links.readlines()
for url in urls:
    url = url.replace('\n','')
    name = url.split("/")[-1]
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    lenProject=len(soup.find_all(class_='table-validate-projects'))
    projectList=[]
    for i in range(0,lenProject):
        titlu=soup.find_all(class_='table-validate-projects')[i].find('label',class_='pTitlu').get_text()
        callName=soup.find_all(class_='table-validate-projects')[i].find('div',class_='project-title').find('span').find('label').get_text()
        codDepunere=soup.find_all(class_='table-validate-projects')[i].find('span',class_='projectID').find('label').get_text()
        anIncepere=soup.find_all(class_='table-validate-projects')[i].find_all('span',class_='projectID')[1].label.get_text()
        anIncheiere=soup.find_all(class_='table-validate-projects')[i].find_all('span',class_='projectID')[1].find_all('label')[1].get_text()
        role=soup.find_all(class_='table-validate-projects')[i].find('span',class_='option-title').label.get_text()
        coordInstitution=soup.find_all(class_='table-validate-projects')[i].find_all('div',class_='project-info row')[1].label.get_text()
        projectPartners=soup.find_all(class_='table-validate-projects')[i].find_all('div',class_='project-info row')[2].label.get_text()
        affiliation=soup.find_all(class_='table-validate-projects')[i].find_all('div',class_='project-info row')[3].label.get_text()
        website=soup.find_all(class_='table-validate-projects')[i].find_all('div',class_='project-info row')[4].a.get_text()
        abstract=soup.find_all(class_='table-validate-projects')[i].find_all('div',class_='project-info row')[5].find('div',class_='expand').get_text()
        newProject=Project(titlu,
            callName,
            codDepunere,
            anIncepere,
            anIncheiere,
            role,
            coordInstitution,
            projectPartners,
            affiliation,
            website,
            abstract)
        #print(newProject.toJSON())
        projectList.append(newProject)
    JSON="[\n"
    for x in projectList:
        JSON=JSON+str(x.toJSON())+",\n"
    JSON=JSON[:-2]+"\n]"
    #print(JSON)
    with open(f'jsons//{name}.txt', 'w') as outfile:
        outfile.write(JSON)
    print(f'{name} descarcat')
print('All good... done :D')