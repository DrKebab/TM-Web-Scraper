import requests     #Captures data of webpage
from bs4 import BeautifulSoup       #Interperates data collected by requests
import pandas       #General data processing tools 

raw_page = requests.get("https://www.trademe.co.nz/a/property/residential/rent/canterbury/christchurch-city")      #Creates variable containing raw data
content = raw_page.content      #Extracts just page content to variable

parsed_page = BeautifulSoup(content, 'html.parser')     #Interperates the page's HTML

listings = parsed_page.find_all("div",{"class":"tm-property-premium-listing-card__details"})        #Finds and extracts div containing individual listings to list

list_of_dir = []        #Creates blank list for below interation loop
for listing in listings:        #Interates through list of property data
    temp_dic = {}       
    addy = listing.find("tm-property-search-card-listing-title").text       #Finds street address data, removes HTML code leaving just text
    price = listing.find("div",{"class":"tm-property-search-card-price-attribute__price"}).text     
    b_and_b = listing.find("ul",{"class":"tm-property-search-card-attribute-icons__features"}).text     #Number of bed and bathrooms
    temp_dic.update({"Street Address":addy})        #Adds dictionary entry containing datatype and street address data
    temp_dic.update({"Weekly Rental Cost":price})
    temp_dic.update({"# of Bedrooms and Bathrooms":b_and_b})
    list_of_dir.append(temp_dic)        #Adds the list containing 3 above dictionaries of individual property to list of all properties 

formatted_data = pandas.DataFrame(list_of_dir)      #Converts list into dataframe
formatted_data.to_csv("output.csv")     #Saves dataframe as CSV file