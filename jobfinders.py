import requests
from bs4 import BeautifulSoup
import pprint

def oppHunter(jobtitle):
    res = requests.get('https://in.linkedin.com/jobs/search?keywords='+jobtitle)
    soup = BeautifulSoup(res.text, 'html.parser')
    element =soup.select("a.result-card__full-card-link")
    links = []
    jobs = []

    i=0

    for i in range(len(element)):
        job = element[i].get_text()
        href = element[i].get('href')
        jobs.append(job)
        links.append(href)
        i+=1


    zipped_list = list(zip(jobs,links))
    return zipped_list



print(oppHunter('Data Science'))