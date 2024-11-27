import pandas as p
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r=requests.get(url)

soup=BeautifulSoup(r.content,'html.parser')

#scrapping title,rating and reviews
titles=soup.find_all('div',class_="f8qK5m") #display titles 
'''ratings=soup.find_all('div',class_='_3LWZlK') # dispaly ratings
reviews=soup.find_all('span',class_='_2_R_DZ') # display reviews
prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")


mratings=[]
mreviews=[]
mprices=[]'''
mtitles=[]

for title,rating,review,price in zip(titles):
    mtitles.append(titles.text)
'''mratings.append(rating.text)
    mreviews.append(review.text)
    mprices.append(price.text)'''


# saving data in csv
data1={'mtitles':mtitles}
model=p.DataFrame(data=data1)

model.to_csv("mobilesdata.csv")
