import requests

import lxml
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()

@app.get("/")
def root():
  return {"Welcome": "Hello, World"}



@app.get("/product_details")
def profile(link: str):
# url = input("Please enter the URL of the product: ")
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

    response = requests.get(link, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    soup2 = BeautifulSoup(soup.prettify(), "html.parser")
    

    title = soup2.find('span',{'class':'a-size-large product-title-word-break'}).text
    title = title.strip()
    print("product Title = ", title)
    
    price = soup2.find('span',{'class':'a-offscreen'}).text
    price = price.strip()[1:]
    

    discount = soup.find("span", {'class': 'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'}).text
    discount = discount.strip()
    
    return {"Title":title,"Price":price, "Discount":discount}