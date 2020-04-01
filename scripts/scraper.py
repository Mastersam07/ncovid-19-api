from bs4 import BeautifulSoup
import requests

url = "https://futa.edu.ng/"
response = requests.get("https://covid19.ncdc.gov.ng")
content = BeautifulSoup(response.content, "html.parser")

print(content)
