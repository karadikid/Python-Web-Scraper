import click
import scraper
# import data_model

@click.command()
@click.option('--h_tag', default="h3", help='Heading TAG Number, default h3')
@click.option('--link_tag', default="li a", help='Link TAG, default li a')
@click.option('--text_tag', default="li", help='Text TAG, default li')
@click.option('--target_url', default="https://owasp.org/www-project-top-ten/",
              help='URL to scrape, default https://owasp.org/www-project-top-ten/')

def scrape(h_tag, link_tag, text_tag, target_url):
    """A Program to Scrape a website"""
    # url = target_url
    target = scraper.create_target(target_url)
    page = scraper.get_page(target)
    soup = scraper.get_soup(page)
    headings = scraper.get_heading(soup, h_tag)
    text = scraper.get_texts(soup, text_tag)
    links = scraper.get_links(soup, link_tag)
    # data_model.create_scrape(target, h_tag, text_tag, link_tag)
    # data_model.create_result(target, headings, text, links)
    # data_model.print_scrape(url)
    # data_model.print_records(url)

    # Print Tests DELETE
    scraper.print_headings(headings)
    scraper.print_text(text)
    scraper.print_links(links)

if __name__ == '__main__':
    scrape()