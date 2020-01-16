import requests
from bs4 import BeautifulSoup

# URLS
# Target URL to scrape
target_url="https://owasp.org/www-project-top-ten/"

# Splash URL from docker local container including port
splash_url = "http://localhost:8050/render.html?url="

# target splash_url+target_url
target = f"{splash_url}{target_url}"

# TAG Arguments
# Heading TAG
heading_tag = "h3"

# Text TAG
text_tag = "li"

# Link TAG
link_tag = "li a"

# Request object
try:
    page = requests.get(target,timeout=3)
    page.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("Oops: Something Else",err)

# soup object
soup = BeautifulSoup(page.content, 'html.parser')

# Select Elements
# Select Headings Object
headings = soup.select(f"{heading_tag}")

# Select Text TAG Object
texts = soup.select(f"{text_tag}")

# Select Link TAG Object
links = soup.select(f"{link_tag}")

## Print Elements
# URLs
# for l in links:
#     print(l)

## Headings
# for h in headings:
#     print(h)

### Text
# for t in texts:
#     print(t)