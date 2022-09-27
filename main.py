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
    header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

    response = requests.get(link, headers=header)

    soup = BeautifulSoup(response.content, "lxml")


    price = soup.find("span", attrs={'class': 'a-offscreen'})
    price = str(price)
    try:
        title = soup.find("span",attrs={"id": 'productTitle'})
        title_value = title.string
 
        title_string = title_value.strip().replace(',', '')
           
    except AttributeError:
 
        title_string = "NA"
 
        print("product Title = ", title_string)
    try:
        price = soup.find("span", attrs={'class': 'offscreen'}).string.strip().replace(',', '')
        # we are omitting unnecessary spaces
        # and commas form our string
    except AttributeError:
        price = "NA"
    

    discount = soup.find("span", attrs={'class': 'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'})
    
    
    return {"Title":title_string,"Price":price,"Discount":discount}