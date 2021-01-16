# User CRUD
import sqlalchemy
from sqlalchemy.orm import Session
from .schema import User as UserRepo
from .model import User as UserModel


def get_user_by_id(db: Session, user_id: str):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def create_user(db: Session, user: UserModel):
    # use schema when adding stuff not the model, model is purely for validation sake
    db_user = UserRepo(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: UserModel):
    db_user = (
        db.query(UserModel)
        .filter(UserModel.id == user.id)
        .first()
        .update(**user.dict())
    )
    db.commit()
    db.refresh(db_user)
    return db_user