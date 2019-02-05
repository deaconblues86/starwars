from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Table,
    exc
)

from sqlalchemy.types import(
    PickleType,
    Integer,
    String
)


def db_connect(user, pw, host):
    url = f'mysql://{user}:{pw}@{host}'
    print(url)
    engine = create_engine(url)
    try:
        engine.execute("CREATE DATABASE starwars")

    # If DB exists we're cool
    except exc.ProgrammingError:
        pass

    engine.execute("USE starwars")
    return engine


def db_close(engine):
    engine.dispose()


def create_char_table(engine):
    metadata = MetaData()

    characters = Table(
        'characters',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(30), nullable=False),
        Column('height', String(30), nullable=False),  # Setting to string to handle non integer values from API
        Column('hair_color', String(30), nullable=False),
        Column('skin_color', String(30), nullable=False),
        Column('eye_color', String(30), nullable=False),
        Column('birth_year', String(30), nullable=False),
        Column('gender', String(30), nullable=False),
        Column('films', String(240), nullable=False),
        Column('url', String(60), nullable=False),
    )

    characters.create(engine, checkfirst=True)

    return characters


def drop_table(engine, table):
    engine.execute("USE starwars")
    table.drop(engine)


def insert_character(engine, character_table, char_obj):
    insert_stmt = character_table.insert().values(
        id=char_obj.id,
        name=char_obj.name,
        height=char_obj.height,
        hair_color=char_obj.hair_color,
        skin_color=char_obj.skin_color,
        eye_color=char_obj.eye_color,
        birth_year=char_obj.birth_year,
        gender=char_obj.gender,
        films=char_obj.films,
        url=char_obj.url
        )

    engine.execute(insert_stmt)
