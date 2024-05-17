import requests
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


url = "https://news.ycombinator.com/"
response = requests.get(url)
html_content = response.text


soup = BeautifulSoup(html_content, "html.parser")
titlelines = soup.find_all('span', class_='titleline')
for titleline in titlelines:
    hyperlink_tag = titleline.find('a')
    title = hyperlink_tag.text
    link = hyperlink_tag['href']
    print(f"Title: {title}\nLink: {link}\n")
