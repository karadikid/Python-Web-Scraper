import requests
from bs4 import BeautifulSoup


# target = "https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_Top_10.html"
# target ="https://gamefaqs.gamespot.com/top10/3133-the-top-10-most-psychotic-characters-in-gaming"
target = "http://yoga.ommygod.com"
# target = "https://www.centurymartialarts.com/shop/weapons/kamas/"
newURL = f"http://localhost:8050/render.html?url={target}"

res = requests.get('https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_Top_10.html')
soup = BeautifulSoup(res.text,"lxml")
event_containers = soup.find_all('div', class_ = "col-xs-12 col-sm-6 col-md-8")
base_url = 'https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/'

for tag in event_containers:
    link = base_url + tag.a['href']
    soup = BeautifulSoup(requests.get(link).text,"lxml")
    location = ', '.join(list(soup.select_one('div.event-add').stripped_strings)[1:-1])
    print('Title:', tag.h3.text)
    print('Date:', tag.select_one('div.date').text)
    print('Link:', link)
    print('Location:', location)