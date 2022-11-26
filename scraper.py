import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract():
    headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url = "https://www.jumia.co.ke/all-products/"
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'info')
    
    for item in divs:
        product_name = item.find('h3', class_ = "name").text.strip()
        product_price = item.find('div', class_ ="prc").text.strip()
        rating = item.find('div', class_='stars _s').text.replace('\n', '')
        
        products = {
            'product_name': product_name,
            'product_price':product_price,
            'rating': rating
        }
        product_list.append(products)
    return 

product_list =[]


c = extract()
transform(c)
df = pd.DataFrame(product_list)
print(df.head(5))
df.to_csv('products.csv')
