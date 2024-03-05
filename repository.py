import requests
import json
 
 
 
 
# Steg 1:
# • Lag et script som henter ut informasjon om en Github bruker eller organ- isasjon Vi ønsker at du tar inn et brukernavn/organisasjonsnavn som input og printer ut følgende til terminalen:
# – En liste over hvilke repoer personen/organisasjonen har. Her er vi interessert i følgende felter fra json strukturen du får fra APIet:
# ∗ navn på repo (name)
# ∗ url til repo (html_url)
# ∗ beskrivelse av repo (description) ∗ temaer (topics)
# ∗ lisens navn (license -> name)
# ∗ programmerinsspråk (language)
# • Om repoet er en fork, trenger du ikke inkludere det
# • Om noen av feltene er tomme, kan du f.eks. legge inn en plassholder
# Vi forventer en tekstlig representasjon av informasjonen, som er strukturert på en måte som gjør den lett å lese
 
navn = input("Hva er navnet på github brukeren/organisasjon:  ")
 
 
def repository_sub_info(repo_dict:dict, sub_name:str):
    return repo_dict[sub_name]
 
 
g = requests.get(f"https://api.github.com/users/{navn}")
print(g.status_code)
data = g.json()
data_js = json.dumps(data)
# print(data_js)
 
    
 
 
repo = requests.get(f"https://api.github.com/users/{navn}/repos")
repo_data = repo.json()
repo_list = []
 
 
for repo_dict in repo_data:
    print(repo_dict)
#     repository_dict = {
#         'name': repository_sub_info(repo_dict,'name'),
#         'html-url': repository_sub_info(repo_dict,'html_url'),
#         'description': repository_sub_info(repo_dict,'description'),
#         'topics': repository_sub_info(repo_dict, 'topics'),
#         'license': repository_sub_info(repo_dict, 'license'),
#         'language': repository_sub_info(repo_dict, 'language'),
#                        }
#     repo_list.append(repository_dict)
# print(repo_list)