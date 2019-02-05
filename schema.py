from sqlalchemy import (
    MetaData,
    Column,
    Table,
    Integer,
    String
)

metadata = MetaData()

characters = Table(
    'characters',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), nullable=False),
    Column('height', Integer, nullable=False),
    Column('hair_colr', String(30), nullable=False),
    Column('skin_color', String(30), nullable=False),
    Column('eye_color', String(30), nullable=False),
    Column('birth_year', String(30), nullable=False),
    Column('gender', String(30), nullable=False),
    Column('film', String(30), nullable=False),
    Column('url', String(60), nullable=False),
)
