from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from attrdict import AttrDict
import string
import random

from config.base import DB_URL

Base = declarative_base()

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

engine = create_engine(DB_URL)

def random_string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

staticValues = AttrDict({
    "restricted_endpoint" : True,
    "user_id": 1,
    "user_obj": {}
})

