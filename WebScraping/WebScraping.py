print("Importing libraries")
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
# driver = webdriver.Chrome("C:\\Web Automation\\chromedriver.exe")
print("Done, Execution begins") 
path = "C:\\Web Automation\\chromedriver.exe"
# chromedriver = 'C:\\Users\\grayson\\Downloads\\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument('window-size=1200x600') 
 
driver = webdriver.Chrome(executable_path=path, options=options)


products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
print("Loading Webpage. . . ")
# driver.get("https://www.flipkart.com/search?q=smartphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off")
driver.get("https://www.flipkart.com/search?q=tv+32+inches&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+32+inches%7CTVs&requestId=d0242c5e-e984-498e-8733-870239213e64&as-backfill=on")
# ₹
print("Fetching data")
i = 1
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34'})
    products.append(name.text)
    prices.append(str(price.text).strip('₹'))
    ratings.append(rating.text) 
    print(i)
    i = i + 1
print("Saving it to the file")
df = pd.DataFrame({'Product Name':products,'Price In INR':prices,'Rating':ratings}) 
df.to_csv('F:\\products.csv', index=False, encoding='utf-8')
print("Closing browser")
driver.quit()
print("Done")