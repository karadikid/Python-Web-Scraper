import click
import scraper

@click.command()
@click.option('--h_tag', default="h3", help='Heading TAG Number, default h3')
@click.option('--link_tag', default="a", help='Link TAG, default a')
@click.option('--text', default="li", help='Text TAG, default p')
@click.option('--url', default="p",
              help='URL to scrape, default https://owasp.org/www-project-top-ten/')
def scrape(count, name):
    """A Program to Scrape a website"""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()