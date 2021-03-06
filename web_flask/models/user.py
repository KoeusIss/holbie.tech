""" User model """
from web_flask.models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields, ValidationError, pre_load
from hashlib import md5


class User(BaseModel, Base):
    """
        email: (str) user email
        password: (str) user password
        password_confirmation: (str) user password confirmation
        role: (str) user role for authorization

    """
    __tablename__ = "users"
    email = Column(
        String(128),
        nullable=False,
        unique=True
    )
    password = Column(
        String(128),
        nullable=False
    )
    role = Column(
        String(128),
        default="student"
    )
    active = Column(
        Boolean(),
        default=False
    )
    otp = Column(
        String(16)
    )
    otp_expired_at = Column(
        DateTime()
    )
    student = relationship(
        "Student",
        uselist=False,
        back_populates="user",
        cascade="all, delete"
    )
    recruiter = relationship(
        "Recruiter",
        uselist=False,
        back_populates="user",
        cascade="all, delete"
    )

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)


class UserSchema(Schema):
    """ User Schema """
    id = fields.Str()
    email = fields.Str()
    role = fields.Str()

