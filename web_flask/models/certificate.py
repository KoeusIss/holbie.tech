""" Certificate model """

from web_flask.models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean, Date, DateTime
from marshmallow import Schema, fields, ValidationError, pre_load
from datetime import datetime


class Certificate(BaseModel, Base):
    """
        name: (str) name of the certificate
        authority: (str) authority issued certificate
        issued_at: (date) issued date
        expire_at: (date) expiring date
        is_expire: (bool) is the certificate expire
        certificate_id: (str) the certificate id
        description: (str) the description
        student_id: (str) a reference to address's state

    """
    __tablename__ = "certificates"
    student_id = Column(
        String(60),
        ForeignKey("students.id"),
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
    authority = Column(
        String(128),
        nullable=False
    )
    issued_at = Column(
        DateTime,
        nullable=False,
    )
    expired_at = Column(
        DateTime,
        default=None
    )
    is_expire = Column(
        Boolean,
        default=False
    )
    certificate_id = Column(
        String(128)
    )
    description = Column(
        String(255)
    )

class CertificateSchema(Schema):
    """ Certificate Schema """
    id = fields.Str()
    name = fields.Str()
    authority = fields.Str()
    certificate_id = fields.Str()
    issued_at = fields.Str()
    expired_at = fields.Str()
    is_expire = fields.Boolean()
    description = fields.Str()
    student_id = fields.Str()
