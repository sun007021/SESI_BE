from sqlalchemy.orm import registry
from sqlalchemy import MetaData, Table, Column, Integer, Float, create_engine, String, Date
from users import Users

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

users = Table(
    'users', metadata,
    Column(name='id', type_=Integer, primary_key=True),
    Column(name='email', type_=String(255), unique=True, nullable=False),
    Column(name='password', type_=String, nullable=False),
    Column(name='name', type_=String, nullable=False),
    Column(name='sex', type_=String(1), nullable=False),
    Column(name='birth', type_=Date, nullable=False),
    Column(name='address', type_=String, nullable=False)
)

users_mapper = mapper_registry.map_imperatively(Users, users, properties={
    '_id': users.c.id,
    'email': users.c.email,
    'password': users.c.password,
    'name': users.c.name,
    'sex': users.c.sex,
    'birth': users.c.birth,
    'address': users.c.address
})

engine = create_engine('postgresql://sesiadmin:sesi1234@localhost:5432/sesidb')
metadata.create_all(engine)
