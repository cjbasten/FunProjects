import requests
import bs4


# Download the page
res = requests.get('https://bananarepublic.gap.com/browse/product.do?vid=1&pid=261885002&searchText=denim+jacket')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
print(soup)
# jacketElem = soup.find_all("div", class_="panel_no-space buy-box")
# testElem = soup.find_all("div", class_="swatches swatches_dimension")
# print(testElem)
# print(jacketElem)
