from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import requests

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://en.wikipedia.org/wiki/SpaceX")

wikipedia_xpath="/html/body/div[3]/div[3]/div[5]/div[1]/table[1]/tbody/tr[9]/td/div/ul/li[1]/a[1]"
wikipedia_spacexCEO=driver.find_element("xpath",wikipedia_xpath).text
driver.quit()

query="""query{
  company {
    ceo
  }
}
"""
response=requests.post("https://api.spacex.land/graphql/", json={'query':query})
print(response.status_code)
api_spacexCEO=response.json()

print("CEO SpaceX menurut Wikipedia",wikipedia_spacexCEO)
print('CEO SpaceX menurut api.spacex.land/graphql',api_spacexCEO)
print("Apakah CEO SpaceX pada wikipedia sama dengan api.spacex.land ?")
print(wikipedia_spacexCEO==api_spacexCEO["data"]["company"]["ceo"])
