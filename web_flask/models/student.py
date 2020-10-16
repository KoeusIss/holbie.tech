""" Student model """
from web_flask.models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields, ValidationError, pre_load
from web_flask.models.address import AddressSchema
from web_flask.models.certificate import CertificateSchema
from web_flask.models.education import EducationSchema


class Student(BaseModel, Base):
    """
        first_name: (str) student first name
        last_name: (str) student last name
        middle_name: (str) middle name
        id_number: (list) identity number
        passport_number: (str) passport number
        marital_status: (str) marital status
        address: (str) reference to student's address
        certificates: (str) student's certificates

    """
    __tablename__ = "students"
    first_name = Column(
        String(128),
        nullable=False
    )
    last_name = Column(
        String(128),
        nullable=False
    )
    middle_name = Column(
        String(128)
    )
    id_number = Column(
        String(128),
        nullable=False
    )
    passport_number = Column(
        String(128),
        default=None
    )
    marital_status = Column(
        String(60),
        default=""
    )
    address = relationship(
        "Address",
        uselist=False,
        back_populates="student",
        cascade="all, delete"
    )
    certificates = relationship(
        "Certificate",
        backref="student",
        cascade="all, delete"
    )
    educations = relationship(
        "Education",
        backref="student",
        cascade="all, delete"
    )
    experiences = relationship(
        "Experience",
        backref="student",
        cascade="all, delete"
    )
    projects = relationship(
        "Project",
        backref="student",
        cascade="all, delete"
    )
    social = relationship(
        "Social",
        uselist=False,
        back_populates="student",
        cascade="all, delete"
    )
       
 
class StudentSchema(Schema):
    """ Student Schema """
    id = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    middle_name = fields.Str()
    id_number = fields.Str()
    passport_number = fields.Str()
    marital_status = fields.Str()