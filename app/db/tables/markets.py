import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import ARRAY

metadata = sqlalchemy.MetaData()

markets_table = sqlalchemy.Table(
    'markets',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String),
	Column('code', String),
	Column('country', String),
	Column('currency', String),
	Column('timezone', String),
	Column('isopen', Boolean),
	Column('active_tickers', Integer),
	Column('update_tickers', Integer)
)