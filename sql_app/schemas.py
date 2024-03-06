from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    email: str
    country : str
    firstname: str
    surname: str
    address: str
    zip: int
    city:str
    telephone_number: str
    pin_number: int


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
