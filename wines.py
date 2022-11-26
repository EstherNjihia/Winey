# import all the necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

## extract, transform and load processes
def extract(page):
    headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url ="https://www.thewineshopkenya.com/product-category/red-wines/" + "page/" +str(page)+"/?v=be7f575c3bc9"
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, "html.parser")
    #r.status_code
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = "sh-woo-post-content-container")
    
    for item in divs:
        title = item.find('h2', class_ = "woocommerce-loop-product__title").text.strip()
        additional_info = item.find('p').text.strip()
        price = item.find('span', class_ = 'price').text.strip()
        
        wine ={
            'Title': title,
            'additional_info': additional_info,
            'Price': price
        }
        wine_list.append(wine)
           
    return


wine_list =[]
for i in range(0,14):
    c = extract(0)
    transform(c)
    
df = pd.DataFrame(wine_list)
df.to_csv('wines.csv')
      