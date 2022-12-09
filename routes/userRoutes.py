from database.db import get_db
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.userModels import UserSchema, ShowUser, Token, AnswerSchema, ChangePassword
from sqlalchemy.orm import Session
from typing import List
from auth.authenticate import authenticate
from pydantic import EmailStr

from controllers import userControllers

user_router = APIRouter(
    tags=["User"],
)


@user_router.post("/signup")
def sign_user_up(request: UserSchema, db: Session = Depends(get_db)) -> dict:
    return userControllers.sign_up(request, db)


@user_router.post("/signin", response_model=Token)
def sign_user_in(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> dict:
    return userControllers.sign_in(request, db)

@user_router.patch("/changepassword")
def change_password(request: ChangePassword, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return userControllers.change_password(request, db, user)

@user_router.get("/", response_model=List[ShowUser])
def get_user_list(db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return userControllers.get_all_user(db)


@user_router.get("/{id}", response_model=ShowUser)
def get_a_user(id: int, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return userControllers.get_user(id, db)

@user_router.delete("/delete")
def delete_my_account(db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return userControllers.delete_user(db, user)
