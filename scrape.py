from bs4 import BeautifulSoup
import requests

url = input("Enter the URL you would like to scrape: ")

page = requests.get(url)

data = page.text

soup = BeautifulSoup(data, "html.parser")

links_with_index = []

for link in soup.find_all("a"):
    if link.get("href") is not None:
        if "index.html" in link.get("href"):
            links_with_index.append(link.get("href"))
try:
    links_file = open("links.txt", "w")

    for link in links_with_index:
        links_file.write(link + "\n")

    links_file.close()
    print("Links written to file")
except IOError:
    print("Error opening or writing to file")