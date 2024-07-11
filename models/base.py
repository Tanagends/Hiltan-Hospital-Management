"""All Base Models"""
from datetime import datetime


class Base:
    """Base for all classes"""
    id = db.Column(db.String(200), primary_key=True)
    date_created = db.Column(db.DateTime(), default=datetime.now())
    date_modified = db.Columnvf
