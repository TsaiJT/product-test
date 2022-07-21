# built-in
import uuid

# 3rd
from sqlalchemy import create_engine, Integer, Column, Sequence, String, DateTime, Boolean, Table, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# module
from flask_app import app


Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(String(255), primary_key=True)
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



