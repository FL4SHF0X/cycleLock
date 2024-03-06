from sqlalchemy import Boolean, Column, Integer, String

from sql_app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    country = Column(String)
    firstname = Column(String)
    surname = Column(String)
    address = Column(String)
    zip = Column(Integer)
    city = Column(String)
    telephone_number = Column(String)
    pin_number = Column(Integer)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

