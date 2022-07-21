# built-in
import uuid

# 3rd
from sqlalchemy import create_engine, Integer, Column, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# module
from flask_app import app

def generate_uuid():
    return uuid.uuid4().hex

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(String(255), primary_key=True, default=generate_uuid)
    name = Column(String(255), nullable=False)
    code = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    size = Column(String(255), nullable=False)
    unit_price = Column(Integer, nullable=False)
    inventory = Column(Integer, nullable=False)
    color = Column(String(255), nullable=False)
    create_at = Column(DateTime, server_default=func.now(), index=True)



engine = create_engine(app.config["POSTGRES_DATABASE_URI"])

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)



