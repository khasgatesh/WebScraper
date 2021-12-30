import requests
from bs4 import BeautifulSoup

req=requests.get("https://www.indiabix.com/aptitude/problems-on-trains/038002")

interview=requests.get("https://www.indiabix.com/placement-papers/accenture/6735")

soup1=BeautifulSoup(req.content,"html.parser")

soup=BeautifulSoup(req.content,"html.parser")

cards=soup.find_all('div','bix-div-container')

# for card in cards:
#     file1=open('indiabix.txt','a')
#     file1.write(card.text) 


soup1=BeautifulSoup(interview.content,"html.parser")

interviewDetail=soup1.find_all('div','div-top-left')
interviewContent=soup1.find_all('div','div-paper-data')

for i in interviewDetail:
    file2=open('interview.txt','a')
    file2.write(i.text)

for i in interviewContent:
    file3=open('interview.txt','a')
    file3.write(i.text)