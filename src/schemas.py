from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class ResponseContactModel(BaseModel):
  id: int = Field(default=1, ge=1)
  firstname: str = Field(max_length=50)
  secondname: str = Field(max_length=50)
  email: str = Field(max_length=50)
  phonenumber: str = Field(max_length=50)
  dateofbirth: str = Field(max_length=50)


class ContactModel(BaseModel):
  firstname: str = Field(max_length=50)
  secondname: str = Field(max_length=50)
  email: str = Field(max_length=50)
  phonenumber: str = Field(max_length=50)
  dateofbirth: str = Field(max_length=50)


class ContactModelFullName(BaseModel):
  firstname: str = Field(max_length=50)
  secondname: str = Field(max_length=50)
