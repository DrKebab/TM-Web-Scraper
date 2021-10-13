import requests
from bs4 import BeautifulSoup
import pandas

raw_page = requests.get("https://www.trademe.co.nz/a/property/residential/rent/canterbury/christchurch-city")
content = raw_page.content

parsed_page = BeautifulSoup(content, 'html.parser')

listings = parsed_page.find_all("div",{"class":"tm-property-premium-listing-card__details"})
#price = listings[0].find_all("div",{"class":"tm-property-search-card-price-attribute__price"})
#print(price)

list_of_dir = []
for listing in listings:
    temp_dic = {}
    addy = listing.find("tm-property-search-card-listing-title").text
    price = listing.find("div",{"class":"tm-property-search-card-price-attribute__price"}).text
    b_and_b = listing.find("ul",{"class":"tm-property-search-card-attribute-icons__features"}).text
    temp_dic.update({"Street Address":addy})
    temp_dic.update({"Weekly Rental Cost":price})
    temp_dic.update({"# of Bedrooms and Bathrooms":b_and_b})
    list_of_dir.append(temp_dic)

formatted_data = pandas.DataFrame(list_of_dir)
formatted_data.to_csv("output.csv")