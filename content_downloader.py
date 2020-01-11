import requests
from bs4 import BeautifulSoup
import json
class Project:
    title= ""
    callName=""
    codDepunere=""
    anIncepere=""
    anIncheiere=""
    role=""
    coordInstitution=""
    projectPartners=""
    affiliation=""
    website=""
    authorFirstName = ""
    authorLastName = ""
    authorPosition = ""
    authorInstitution = ""
    authorRoles = ""
    authorCountry = ""
    abstract=""
    def __init__(self,
                title="",
                callName="",
                codDepunere="",
                anIncepere="",
                anIncheiere="",
                role="",
                coordInstitution="",
                projectPartners="",
                affiliation="",
                website="",
                authorFirstName = "",
                authorLastName = "",
                authorPosition = "",
                authorInstitution = "",
                authorRoles = "",
                authorCountry = "",
                abstract=""):
        self.title=title
        self.callName=callName
        self.codDepunere=codDepunere
        self.anIncepere=anIncepere
        self.anIncheiere=anIncheiere
        self.role=role
        self.coordInstitution=coordInstitution
        self.projectPartners=projectPartners
        self.affiliation=affiliation
        self.website=website
        self.authorFirstName = authorFirstName
        self.authorLastName = authorLastName
        self.authorPosition = authorPosition
        self.authorInstitution = authorInstitution
        self.authorRoles = authorRoles
        self.authorCountry = authorCountry
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
    tmp = ""
    if soup.find(class_='profile-dash col-md-9').h3.find( 'label', {"a:localid": "firstName"}) is not None:
        authorFirstName = soup.find(class_='profile-dash col-md-9').h3.find( 'label', {"a:localid": "firstName"}).get_text()

    if soup.find(class_='profile-dash col-md-9').h3.find( 'label', {"a:localid": "lastName"}) is not None:
        authorLastName = soup.find(class_='profile-dash col-md-9').h3.find( 'label', {"a:localid": "lastName"}).get_text()

    if soup.find(class_='profile-dash col-md-9').h5.find('label',{"a:localid":"instPosition"}) is not None:
        authorPosition = soup.find(class_='profile-dash col-md-9').h5.find('label',{"a:localid":"instPosition"}).get_text()

    if soup.find(class_='profile-dash col-md-9').h5.find('label',{"a:localid":"instNume"}) is not None:
        authorInstitution = soup.find(class_='profile-dash col-md-9').h5.find('label',{"a:localid":"instNume"}).get_text()
    if soup.find(class_='roles-list')is not None:
        if soup.find(class_='roles-list').find('label',{"a:localid":"roles"})is not None:
            authorRoles = soup.find(class_='roles-list').find('label',{"a:localid":"roles"}).get_text().replace(' ','').split("|")

    if soup.find(class_='profile-lowInfo').find('label',{"a:localid":"idTaraLucru"})is not None:
        authorCountry = soup.find(class_='profile-lowInfo').find('label',{"a:localid":"idTaraLucru"}).get_text()

    for i in range(0,lenProject):
        title=soup.find_all(class_='table-validate-projects')[i].find('label', class_='pTitlu').get_text()
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
        newProject=Project(title,
                           callName,
                           codDepunere,
                           anIncepere,
                           anIncheiere,
                           role,
                           coordInstitution,
                           projectPartners,
                           affiliation,
                           website,
                           authorFirstName,
                           authorLastName ,
                           authorPosition ,
                           authorInstitution ,
                           authorRoles ,
                           authorCountry ,
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