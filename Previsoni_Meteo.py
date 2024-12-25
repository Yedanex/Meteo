import requests
from bs4 import BeautifulSoup

city = input("Enter City Name : ")
city_formatted = city.lower().replace(" ", "-")

url = f"https://www.timeanddate.com/weather/italy/{city_formatted}"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

try:
    temperature = soup.find("div", class_="h2").get_text(strip=True)
    description = soup.find("div", class_="h2").find_next("p").get_text(strip=True)

    print(f"Weather in {city} ")
    print(f"Temperature in {city} : {temperature}")
    print(f"Conditions : {description}")

except AttributeError:
    print("Please check the city name and try again.")
