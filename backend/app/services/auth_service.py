from datetime import datetime, timedelta
import re

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import User


pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def validate_phone(phone: str | None) -> bool:
    if not phone:
        return True
    return re.match(r"^[6-9]\d{9}$", phone.replace(" ", "")) is not None


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def create_access_token(subject: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode = {"sub": subject, "exp": expire}
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)


def register_user(db: Session, payload) -> User:
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise ValueError("Email already registered")
    if not validate_phone(payload.phone):
        raise ValueError("Invalid phone number")

    user = User(
        full_name=payload.full_name,
        email=payload.email,
        phone=payload.phone,
        password_hash=hash_password(payload.password),
        bpsc_attempt=payload.bpsc_attempt,
        commitment_4hrs=payload.commitment_4hrs,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    user.last_login = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user
