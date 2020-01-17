import click
import scraper

@click.command()
@click.option('--h_tag', default="h3", help='Heading TAG Number, default h3')
@click.option('--link_tag', default="li a", help='Link TAG, default a')
@click.option('--text_tag', default="li", help='Text TAG, default p')
@click.option('--target', default="https://owasp.org/www-project-top-ten/",
              help='URL to scrape, default https://owasp.org/www-project-top-ten/')

def scrape(h_tag, link_tag, text_tag, target):
    """A Program to Scrape a website"""
    target = scraper.create_target(target)
    page = scraper.get_page(target)
    soup = scraper.get_soup(page)
    headings = scraper.get_heading(soup, h_tag)
    text = scraper.get_texts(soup, text_tag)
    links = scraper.get_links(soup, link_tag)
    scraper.print_headings(headings)
    scraper.print_text(text)
    scraper.print_links(links)

if __name__ == '__main__':
    scrape()