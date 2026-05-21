from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
laptops = []

response = requests.get(url)
response.encoding = "utf-8"
doc = BeautifulSoup(response.text, "html.parser")

containers = doc.find_all("div", class_="card-body")

for item in containers:
    name_el   = item.find("a", class_="title")
    price_el  = item.find("h4", class_="price")
    rating_el = item.find("p", attrs={"data-rating": True})
    review_el = item.find("p", class_="review-count")

    laptops.append({
        "name":    name_el["title"]          if name_el   else "N/A",
        "price":   price_el.text.strip()     if price_el  else "N/A",
        "rating":  rating_el["data-rating"]  if rating_el else "N/A",
        "reviews": review_el.text.strip()    if review_el else "N/A"
    })

df = pd.DataFrame(laptops)
print(df.head())
df.to_excel("laptops.xlsx", index=False)
print("Done.", len(laptops), "laptops exported.")