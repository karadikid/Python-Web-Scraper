import data_model


# Create Recordsets
def create_scrape(url, heading_tag, text_tag, link_tag):
    scrape_record = data_model.Scrape(url=url, heading_tag=heading_tag, text_tag=text_tag, link_tag=link_tag)
    scrape_record.save()
    return scrape_record

def create_result(url, tag, headings, text, links):
    result_record = data_model.Results(url=url, tag=tag, headings=headings, text=text, links=links)
    result_record.save()
    return result_record

# Read: (.get() and .select()) get = 1 record, select = multiple
def get_scrape(url):
    result = data_model.Scrape.select().where(data_model.Scrape.url == url).execute()
    return result

def select_results(url):
    results = data_model.Results.select().where(data_model.Results.url == url).execute()
    return results

# Update
def update_scrape(url):
    update_query = data_model.Scrape.update().where(data_model.Scrape.url == url)
    update_query.execute()
    return 

# Delete
def delete_scrape(url):
    delete_query = data_model.Scrape.delete().where(data_model.Scrape.url == url).execute()
    return delete_query

def delete_results(url):
    delete_results = data_model.Results.delete().where(data_model.Results.url == url).execute()
    return delete_results

# Print results
def print_scrape(url):
    scrape = get_scrape(url)
    print(list(scrape))
    return

def print_records(url):
    results = select_results(url)
    print(list(results))
    return

