from database.db import get_db
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.userModels import UserSchema, ShowUser, Token, AnswerSchema, ChangePassword
from models.depressionModels import UserDepression, ShowUserDepression
from models.mbtiModels import MBTI_Type, MBTI_Show
from controllers import personalityControllers
from sqlalchemy.orm import Session
from typing import List
from auth.authenticate import authenticate
from pydantic import EmailStr

from controllers import userControllers

personality_router = APIRouter(
    tags=["Personality Information"],
)


@personality_router.get("/mbti-explanation", response_model=List[MBTI_Show])
def get_mbti_explanation(db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return personalityControllers.explain_type_mbti(db)


@personality_router.put("/mbti-test")
def analyze_mbti(request: AnswerSchema, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return userControllers.analyze_mbti(request, db, user)

@personality_router.put("/mbti-depression-analyze")
def get_mbti_on_depression_analysis(request: UserDepression, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return personalityControllers.get_depression_attach(request, db, user)