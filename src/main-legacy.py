import requests
from bs4 import BeautifulSoup

# URLs
# https://www.owasp.org/index.php/Top_10-2017_Top_10 - EXPIRED WHILE WORKING!
# https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_Top_10.html

# Splash URL Proxy for Full Scraping Functionality in Docker 
# Docker command docker run -p 8050:8050 -p 5023:5023 scrapinghub/splash
# New URL http://localhost:8050/render.html?url=http://example.com/

target = "https://owasp.org/www-project-top-ten/"
# target ="https://gamefaqs.gamespot.com/top10/3133-the-top-10-most-psychotic-characters-in-gaming"
# target = "http://yoga.ommygod.com"
# target = "https://www.centurymartialarts.com/shop/weapons/kamas/"
newURL = f"http://localhost:8050/render.html?url={target}"

# Requests response object and status_code
page = requests.get(newURL)
page.status_code

#Soup usage of requests page response object
soup = BeautifulSoup(page.content, 'html.parser')

# BS4 Pretty output
# print(soup.prettify())

# Print children and tags
# print(list(soup.children))

# Iterate over children
# print([type(item) for item in list(soup.children)])

# Access Tags from BS4 objects above
# html = list(soup.children)[2]
# print(html)

# Children inside HTML TAG
# body = list(html)[3]

# Further nested to <p> Tag 3 deep
# p_tag = list(body)

# Sample select query
# select = BeautifulSoup(select, "div p")
# select.get_text()

# Sample find_all('<tag>') from DOM
# for t in soup.find_all('dd'):
#     print(t)

#Success!
headings = soup.select('h3')
texts = soup.select('p')
urls = soup.select('a')

for u in urls:
    print(u)

for h in headings:
    print(h)

for t in texts:
    print(t)

