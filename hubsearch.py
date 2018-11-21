from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


check_user = input("Enter Github user: ")
my_url = "https://github.com/" + check_user + "?tab=repositories"
Client = uReq(my_url)

html_page = Client.read()
Client.close()

soup_page = soup(html_page, "html.parser")

repos = soup_page.findAll('li', {'class': 'col-12 d-block width-full py-4 border-bottom public source'})
repo_des = soup_page.findAll('p', {'class': 'col-9 d-inline-block text-gray mb-2 pr-4'})
repos_fork = soup_page.findAll('li', {'class': 'col-12 d-block width-full py-4 border-bottom public fork'})

repos_len = len(repos)
repos_fork_len = len(repos_fork)

print()
print('Repositories:')

for r in range(repos_len):

    print(repos[r].a.text)
    print(repo_des[r].text)
    print("---------------------------------------------------------------------------")

print()
if repos_fork_len == 0:
    print()
else:
    print('Forks:')

for f in range(repos_fork_len):
    print(repos_fork[f].a.text)
    print(repo_des[f].text)
    print("---------------------------------------------------------------------------")


print("Number of Repositories:", repos_len, "|", repos_fork_len, "Forks")

