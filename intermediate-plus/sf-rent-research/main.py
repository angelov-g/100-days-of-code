import requests
from bs4 import BeautifulSoup

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22" \
             "usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%" \
             "3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22" \
             "isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%" \
             "3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%" \
             "3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22" \
             "fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22" \
             "value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22" \
             "beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

FORM_URL = "https://forms.gle/R2jZbbr9BSiLwQRp9"

HEADERS = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/109.0.0.0 Safari/537.36"
}

response = requests.get(ZILLOW_URL, headers=HEADERS)
zillow_page = response.text

soup = BeautifulSoup(zillow_page, "html.parser")

# Find all list items
apartments = soup.findAll(name="li", class_="ListItem-c11n-8-85-1__"
                                            "sc-10e22w8-0 srp__sc-wtsrtn-0 jhnswL with_constellation")

# Remove the ads which appear as apartments
for apartment in apartments:
    if apartment.get("data-test") is not None:
        apartments.remove(apartment)

addresses = []
prices = []
links = []

for apartment in apartments:
    # For some reason the website limits the number of apartments to return on request. Gives timeout for rest.
    if apartment.getText() == "":
        pass
    else:
        addresses.append(apartment.address.getText())
        prices.append(apartment.span.getText().split("+")[0])
        # Not all links include the domain
        links.append("https://www.zillow.com" + (apartment.a.get("href").split("https://www.zillow.com"))[-1])
