from peewee import *
from datetime import date

#Database.connect
db = PostgresqlDatabase('people', user='postgres', 
                        password='', host='localhost', port='5432')

class BaseModel(Model):

#Meta in classes is Meta information or settings
    class Meta:
            database = db

# Database table properties
class Scrape(BaseModel):
    id = IdentityField()
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)
    url = CharField()
    heading_tag = CharField()
    text_tag = CharField()
    link_tag = CharField()

class Results(BaseModel):
    url = CharField()
    text_tag = CharField()
    headings = CharField()
    text = CharField()
    links = CharField()

# Connect to DB
def db_connect():
    db_connection = db.connect()
    return db_connection

# Initialize database
def db_initialize():
    db_connect()
    db_drop_table(Scrape)
    db_drop_table(Results)
    db_create_table(Scrape)
    db_create_table(Results)

# Drop table
def db_drop_table(table_name):
    db.drop_tables([table_name])
    return

# Create table
def db_create_table(table_name):
    db.create_tables([table_name])
    return 

# Create Recordsets
def create_scrape(url, heading_tag, text_tag, link_tag):
    scrape_record = Scrape(url=url, heading_tag=heading_tag, text_tag=text_tag, link_tag=link_tag)
    scrape_record.save()
    return scrape_record

def create_result(url, headings, text, links):
    result_record = Results(url=url, headings=headings, text=text, links=links)
    result_record.save()
    return result_record

# Read: (.get() and .select()) get = 1 record, select = multiple
def get_scrape(url):
    result = Scrape.get(Scrape.url == url)
    print(result)
    return result

def select_results(url):
    results = Results.select(Results.url == url)
    for result in results:
        print(result)
    return results

# Update
def update_scrape(url):
    update_query = Scrape.update().where(Scrape.url == url)
    update_query.execute()
    return 

# Delete
def delete_scrape(url):
    delete_query = Scrape.delete().where(Scrape.url == url)

# Print results
print(f"Karadi was born on {karadi.birthday}")
print(f"Maddy is a {maddy.animal_type}")

