from peewee import *
from datetime import date

#mongoose.connect
db = PostgresqlDatabase('people', user='postgres', 
                        password='', host='localhost', port='5432')

class BaseModel(Model):

#Meta in classes is Meta information or settings
    class Meta:
            database = db

# Database table properties
class Person(BaseModel):
    id = IdentityField()
    name = CharField()
    birthday = DateField()

class Pet(BaseModel):
    id = IdentityField()
    name = CharField()
    animal_type = CharField()
    owner = ForeignKeyField(Person, to_field='id', on_delete='cascade')

# Connect to database
db.connect()

# Drop table
db.drop_tables([Person], cascade=True)
db.drop_tables([Pet], cascade=True)

# Create table
db.create_tables([Person])
db.create_tables([Pet])

# Instantiate object of class or first row of Person table
karadi = Person(name='Karadi', birthday=date(1990, 11, 18))


# Save new object or instance
karadi.save()

#Create and save instance of pet
maddy = Pet(name='Maddy', animal_type='Dawg', owner=karadi.id)
maddy.save()

# Read: (.get() and .select()) get = 1 record, select = multiple
karadi = Person.get(Person.name == 'Karadi')
print(karadi)

people = Person.select()

for person in people:
    print(person.name)

# Update:
karadi.birthday = date(1111, 11, 11)
karadi.save()

# Delete
karadi.delete_instance()

# Print results
print(f"Karadi was born on {karadi.birthday}")
print(f"Maddy is a {maddy.animal_type}")

