import requests
from bs4 import BeautifulSoup

# DEFAULT URLs
# Target URL to scrape
target_url="https://owasp.org/www-project-top-ten/"

# Splash URL from docker local container including port
splash_url = "http://localhost:8050/render.html?url="

# target splash_url+target_url

def create_target(target_url, splash_url="http://localhost:8050/render.html?url="):
    target = f"{splash_url}{target_url}"
    return target

# Request object
def get_page(target):
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
    return page

# soup object
def get_soup(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

# TAG Arguments
# Heading TAG
def choose_heading_tag(heading_tag):
    heading_tag = "h3"
    return heading_tag

# Text TAG
def choose_text_tag(text_tag):
    text_tag = "p"
    return text_tag

# Link TAG
def choose_link_tag(link_tag):
    link_tag = "a"
    return link_tag

# Select Elements
# Select Headings Object
def get_heading(soup, heading_tag):
    headings = soup.select(f"{heading_tag}")
    return headings

# Select Text TAG Object
def get_texts(soup, text_tag):
    texts = soup.select(f"{text_tag}")
    return texts
# Select Link TAG Object
def get_links(soup, link_tag):
    links = soup.select(f"{link_tag}")
    return links


## Print Elements
# URLs
def print_links(links):
    for l in links:
        print(l)

## Headings
def print_headings(headings):
    for h in headings:
        print(h)

### Text
def print_text(texts):
    for t in texts:
        print(t)