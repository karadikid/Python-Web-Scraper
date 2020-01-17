import click
import scraper
import db_functions

@click.command()
@click.option('--h_tag', default="h3", help='Heading TAG Number, default h3')
@click.option('--link_tag', default="li a", help='Link TAG, default li a')
@click.option('--text_tag', default="li", help='Text TAG, default li')
@click.option('--target_url', default="https://owasp.org/www-project-top-ten/",
              help='URL to scrape, default https://owasp.org/www-project-top-ten/')

def scrape(h_tag, link_tag, text_tag, target_url):
    """A Program to Scrape a website"""
    url = target_url
    target = scraper.create_target(target_url)
    page = scraper.get_page(target)
    soup = scraper.get_soup(page)
    headings = scraper.get_heading(soup, h_tag)
    text = scraper.get_texts(soup, text_tag)
    links = scraper.get_links(soup, link_tag)
    db_functions.create_scrape(url, h_tag, text_tag, link_tag)
    db_functions.create_result(url, headings, text, links)
    db_functions.print_scrape(url)
    db_functions.print_records(url)

    # # Print Tests DELETE
    # scraper.print_headings(headings)
    # scraper.print_text(text)
    # scraper.print_links(links)

if __name__ == '__main__':
    scrape()