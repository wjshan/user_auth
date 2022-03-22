import datetime
import typing

from sqlmodel import SQLModel, Field, Relationship
import typing as tp
import ipaddress
from sqlalchemy import UniqueConstraint

if tp.TYPE_CHECKING:
    from .user import User


class LoginToken(SQLModel, table=True):
    __tablename__:str = "login_tokens" # type: ignore
    __table_args__ = (UniqueConstraint("token"),)
    id: int = Field(primary_key=True)
    token: str  # 校验token
    expired_in: typing.Optional[datetime.datetime]  # 过期时间
    user_id: int = Field(foreign_key="user.id")  # 关联用户
    user: User = Relationship(back_populates="tokens")


class LoginLog(SQLModel, table=True):
    __tablename__:str = "login_logs" # type: ignore
    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)  # 关联用户
    user: User = Relationship(back_populates="login_logs", link_model="User")
    login_time: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.utcnow
    )  # 登录时间
    custom_ip: typing.Optional[ipaddress.IPv4Address]  # 登录用户IP
