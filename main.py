import click
import scraper
import db_functions

@click.command()
@click.option('--h_tag', default="h3", help='Heading TAG Number, default h3')
@click.option('--link_tag', default="a", help='Link TAG, default li a')
@click.option('--text_tag', default="p", help='Text TAG, default li')
@click.option('--target_url', default="https://owasp.org/www-project-top-ten/",
              help='URL to scrape, default https://owasp.org/www-project-top-ten/')

def scrape(h_tag, link_tag, text_tag, target_url):
    """A Program to Scrape a website"""
    url = target_url
    target = scraper.create_target(target_url)
    page = scraper.get_page(target)
    soup = scraper.get_soup(page)
    headings = scraper.get_heading(soup, h_tag)
    texts = scraper.get_texts(soup, text_tag)
    db_functions.create_scrape(url, h_tag, text_tag, link_tag)
    for h in headings:
        db_functions.create_result(url, h_tag, h, '', link_tag)
    for t in texts:
        db_functions.create_result(url, text_tag, '', t, link_tag)
    links = scraper.get_links(soup, link_tag)
    for l in links:
        db_functions.create_result(url, link_tag, '', '', l)
    db_functions.print_scrape(url)
    db_functions.print_records(url)

    # # Print Tests DELETE
    # scraper.print_headings(headings)
    # scraper.print_text(text)
    # scraper.print_links(links)

if __name__ == '__main__':
    scrape()