from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


check_user = input("Enter Github user: ")
my_url = "https://github.com/" + check_user + "?tab=repositories"
Client = uReq(my_url)

html_page = Client.read()
Client.close()

soup_page = soup(html_page, "html.parser")

repos = soup_page.findAll('li', {'class': 'col-12 d-block width-full py-4 border-bottom public source'})

repos_len = len(repos)

for i in range(repos_len):

    print(repos[i].a.text)
    print(repos[i].p.text)
    print("---------------------------------------------------------------------------")


print("Number of Repositories:", repos_len)

