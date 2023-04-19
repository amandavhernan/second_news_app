import os
from peewee import *
from census import Census
from app import *
db = SqliteDatabase('foreclosures.db')
census_api_key = os.environ.get('09ab3b0e03c1394c8a2b4459460427ab6f0a1c59')
c = Census(census_api_key)

# get all the zips from the Notices
all_zips = (Notice.select(Notice.zip).distinct())

# create a new table for the zip codes and owner_occupied figures
class ZipCode(Model):
    zipcode = CharField()
    owner_occupied = IntegerField(null = True)

    class Meta:
        database = db

# create that table if it doesn't already exist
db.create_tables([ZipCode])

# create a container to put my data in
rows_to_insert = []

# loop over our zip codes, retrieving Census data where possible
for zip in all_zips:
    print(zip.zip)
if zip.zip != "No Zip Code":
    owner_occupied = c.acs5.state_zipcode(('NAME', 'B25003_002E'), '24', zip.zip)
    if owner_occupied and 'B25003_002E' in owner_occupied[0]:
        rows_to_insert.append({"zipcode": zip.zip, "owner_occupied": int(owner_occupied[0]['B25003_002E'])})

# insert the data we've collected
ZipCode.insert_many(rows_to_insert).execute()