from typing import List, Union

from sqlalchemy.orm import Session, subqueryload
from src.database.models import Contact
from src.schemas import ContactModel, ResponseContactModel


class Get_Contacts:

  def __init__(self, skip, limit, db):
    self.skip = skip
    self.limit = limit
    self.db = db

  async def __call__(self) -> List[Contact]:
    return self.db.query(Contact).offset(self.skip).limit(self.limit).all()


class Create_Contact:

  def __init__(self, body, db):
    self.body = body
    self.db = db

  async def __call__(self) -> Contact:
    new_contact = Contact(
      firstname=self.body.firstname,
      secondname=self.body.secondname,
      email=self.body.email,
      phonenumber=self.body.phonenumber,
      dateofbirth=self.body.dateofbirth,
    )
    self.db.add(new_contact)
    self.db.commit()
    self.db.refresh(new_contact)
    return new_contact


class Get_Contact:

  def __init__(self, contact_id, db):
    self.contact_id = contact_id
    self.db = db

  async def __call__(self) -> Contact:
    return self.db.query(Contact).filter(Contact.id == self.contact_id).first()


class Get_Contact_by_Name:

  def __init__(self, contact_name: str, db: Session):
    self.contact_name = contact_name
    self.db = db

  async def __call__(self) -> List[Contact]:
    return self.db.query(Contact).filter(
      Contact.firstname == self.contact_name).all()

class Get_Contact_by_Second_Name:

  def __init__(self, contact_name: str, db: Session):
    self.contact_name = contact_name
    self.db = db

  async def __call__(self) -> List[Contact]:
    return self.db.query(Contact).filter(
      Contact.secondname == self.contact_name).all()

class Get_Contact_by_Email:

  def __init__(self, email: str, db: Session):
    self.email = email
    self.db = db

  async def __call__(self) -> List[Contact]:
    return self.db.query(Contact).filter(
      Contact.email == self.email).all()


class Update_Contact:

  def __init__(self, contact_id, body, db):
    self.contact_id = contact_id
    self.body = body
    self.db = db

  async def __call__(self) -> Union[Contact, None]:
    contact = self.db.query(Contact).filter(
      Contact.id == self.contact_id).first()
    if contact:
      contact.firstname = self.body.firstname,
      contact.secondname = self.body.secondname,
      contact.email = self.body.email,
      contact.phonenumber = self.body.phonenumber,
      contact.dateofbirth = self.body.dateofbirth,
      self.db.commit()
    return contact


class Remove_Contact:

  def __init__(self, contact_id, db):
    self.contact_id = contact_id
    self.db = db

  async def __call__(self) -> Union[Contact, None]:
    contact = self.db.query(Contact).filter(
      Contact.id == self.contact_id).first()
    if contact:
      self.db.delete(contact)
      self.db.commit()
    return contact
