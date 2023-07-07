import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import ARRAY

metadata = sqlalchemy.MetaData()

exchanges_table = sqlalchemy.Table(
    'exchanges',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String),
	Column('code', String),
	Column('country', String),
	Column('currency', String),
	Column('countryIso2', String),
	Column('countryIso3', String),
	Column('OperatingMIC', String)
)