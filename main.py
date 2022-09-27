
from curses import meta
import requests
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


    price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '')
    title = soup.find("span",attrs={"id": 'productTitle'})
    title_value = title.string
 
    title_string = title_value.strip().replace(',', '')
    print(title_string)
    # price = price.split()[0]
    discount = soup.find("span", attrs={'class': 'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'}).string.strip().replace(',', '')
    # except AttributeError:
    #     try:
    #         rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
    #     except:
    #         rating = "NA"
    
    return {"Title":title_string,"Price":price,"Discount":discount}