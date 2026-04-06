import secrets
import string
from sqlalchemy.orm import Session
from .models import URL


def generate_key(db: Session, length: int = 6) -> str:
    while True:
        key = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
        existing_url = db.query(URL).filter(URL.short_url == key).first()
        if existing_url is None:
            return key

