import click
import scraper

@click.command()
@click.option('--h_tage', default="H3", help='Heading TAG Number, default H3')
@click.option('--url', prompt='URL',
              help='URL to scrape, default https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_Top_10.html')
def scrape(count, name):
    """A Program to Scrape a website"""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()