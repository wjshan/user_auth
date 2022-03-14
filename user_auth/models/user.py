import datetime

from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int = Field(primary_key=True)
    create_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.utcnow())
    user_name: str
    password: str
    alias: str
