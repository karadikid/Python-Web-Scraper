# Python Web Scraper
This application uses Python to scrape a url.  The user can offer multiple option including the URL, at <TAG> for Headings, Text, and Links respectively.  If entered with zero options it uses defaults.  The application also inserts the records into an SQL database for searching or printing.  By default it scrapes the URL from a local proxy named "Splash" from ScrapingHub and the selects the results sets for both the scrapes settings and scrape results.

## Docker Configuration
This is optional, if not using Docker, change splash_url from Scraper.py to "".

*No Docker*
```python
splash_url = ""
```
### Docker Install
```
brew cask install docker
```
### First Time Run
Got to Spotlight by pressing "Command + Space" on OSX and typing 'Docker'
Accept elevated privileges for the Docker Engine and Networking Agent
Open Terminal Window and Run:

### Docker Image Pull and Launch
```
docker pull scrapinghub/splash && docker run -p 8050:8050 -p 5023:5023 scrapinghub/splash
```
### Postgres SQL Install and Configuration
Install
```
brew install postgresql
```
Services Start/Stop
```
brew services start postgresql
brew services stop postgresql.
```
Create Database for Scraping
```
createdb Scraper
```
To initialize database, uncomment the code in data_model.py
```python
# data_model.py
# Function for initialization
db_initialize()
```
From Terminal run
```
python data_model.py
```
Then recomment out the initialize command.
```
# data_model.py
# Function for initialization
# db_initialize()
```

## Python Run

```
❯ python main.py --help
Usage: main.py [OPTIONS]

  A Program to Scrape a website

Options:
  --h_tag TEXT       Heading TAG Number, default h3
  --link_tag TEXT    Link TAG, default a
  --text_tag TEXT    Text TAG, default p
  --target_url TEXT  URL to scrape, default https://owasp.org/www-project-top-
                     ten/
  --help             Show this message and exit.

❯ python main.py --h_tag h3 --link_tag=a --text_tag=p --target_url https://gamefaqs.gamespot.com/top10/3133-the-top-10-most-psychotic-characters-in-gaming
```

## Technologies
1. Python3
1. Requests
1. BeautifulSoup
1. Click
1. peewee and psycopg2
1. Docker
1. Postgresql

## Bonus

Once you have the command line version working consider the following bonuses:

1. Get Update and Delete working
1. Build a user interface with [tkinter](https://docs.python.org/3/library/tk.html), [pygame](https://www.pygame.org/), or [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
1. Use web scraping to pull data from a webpage using [requests](https://2.python-requests.org/en/master/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[Project Requirements](https://git.generalassemb.ly/dc-wdi-python-django/python-command-line-project)

