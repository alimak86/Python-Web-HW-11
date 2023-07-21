from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from src.database.database import Connect_db, SQLALCHEMY_DATABASE_URL_FOR_WORK

Base = declarative_base()
Base.metadata.create_all(Connect_db(SQLALCHEMY_DATABASE_URL_FOR_WORK).engine)


class Contact(Base):
  __tablename__ = "contacts"
  id = Column(Integer, primary_key=True)
  firstname = Column(String(50), nullable=False)
  secondname = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False)
  phonenumber = Column(String(50), nullable=False)
  dateofbirth = Column(String(50), nullable=False)
