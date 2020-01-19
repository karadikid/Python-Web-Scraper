from peewee import *
from datetime import date, datetime

#Database.connect
db = PostgresqlDatabase('Scraper', user='postgres', 
                        password='', host='localhost', port='5432')

class BaseModel(Model):

#Meta in classes is Meta information or settings
    class Meta:
            database = db

# Database table properties
class Scrape(BaseModel):
    id = IdentityField()
    timestamp = DateTimeField(default=datetime.now)
    url = CharField()
    heading_tag = CharField()
    text_tag = CharField()
    link_tag = CharField()

class Results(BaseModel):
    url = CharField()
    tag = CharField(null = True)
    headings = CharField(null = True,max_length=30000)
    text = CharField(null = True,max_length=30000)
    links = CharField(null = True,max_length=30000)

# Connect to database
db.connect()

# Connect to DB
def db_connect():
    db_connection = db.connect()
    return db_connection

# Initialize database
def db_initialize():
    db_drop_table(Scrape)
    db_drop_table(Results)
    db_create_table(Scrape)
    db_create_table(Results)
    return

# Drop table
def db_drop_table(table_name):
    db.drop_tables([table_name])
    return


# Create table
def db_create_table(table_name):
    db.create_tables([table_name])
    return 

# Function for initialization
# db_initialize()
