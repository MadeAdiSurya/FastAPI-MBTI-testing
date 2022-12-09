from sqlalchemy import Column, Integer, String
from database.db import Base
from pydantic import BaseModel, EmailStr, conint
from typing import Optional


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    nama = Column(String)
    password = Column(String)
    MBTI = Column(String, default="")
    Deskripsi = Column(String, default="")


    class Config:
        schema_extra = {
            "Contoh": {
                "email": "contoh@gmail.com",
                "nama" : "Bambang",
                "password": "Pamungkas",
            }
        }


class UserSchema(BaseModel):
    email: EmailStr
    nama: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "Contoh": {
                "email": "contoh@gmail.com",
                "nama" : "Bambang",
                "password": "Pamungkas",
            }
        }


class ShowUser(BaseModel):
    email: EmailStr
    nama: str
    MBTI: str
    Deskripsi : str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "contoh@gmail.com",
                "nama": "Bambang",
                "MBTI": "INTP",
                "Deskripsi ": "Anda memiliki kepribadian dengan tipe INTP dengan kecenderungan Extraverted : 40.0% Introverted : 60.0% Sensing : 40.0% Intuitive : 60.0% Thinking :60.0% Feeling : 40.0% Judging : 50.0% Perceiving : 50.0"
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

class AnswerSchema(BaseModel):
    jawaban_1: conint(gt=0, lt=3)
    jawaban_2: conint(gt=0, lt=3)
    jawaban_3: conint(gt=0, lt=3)
    jawaban_4: conint(gt=0, lt=3)
    jawaban_5: conint(gt=0, lt=3)
    jawaban_6: conint(gt=0, lt=3)
    jawaban_7: conint(gt=0, lt=3)
    jawaban_8: conint(gt=0, lt=3)
    jawaban_9: conint(gt=0, lt=3)
    jawaban_10: conint(gt=0, lt=3)
    jawaban_11: conint(gt=0, lt=3)
    jawaban_12: conint(gt=0, lt=3)
    jawaban_13: conint(gt=0, lt=3)
    jawaban_14: conint(gt=0, lt=3)
    jawaban_15: conint(gt=0, lt=3)
    jawaban_16: conint(gt=0, lt=3)
    jawaban_17: conint(gt=0, lt=3)
    jawaban_18: conint(gt=0, lt=3)
    jawaban_19: conint(gt=0, lt=3)
    jawaban_20: conint(gt=0, lt=3)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "jawaban_1": 1,
                "jawaban_2": 1,
                "jawaban_3": 2,
                "jawaban_4": 2,
                "jawaban_5": 2,
                "jawaban_6": 1,
                "jawaban_7": 2,
                "jawaban_8": 1,
                "jawaban_9": 2,
                "jawaban_10": 1,
                "jawaban_11": 2,
                "jawaban_12": 1,
                "jawaban_13": 2,
                "jawaban_14": 1,
                "jawaban_15": 2,
                "jawaban_16": 1,
                "jawaban_17": 2,
                "jawaban_18": 1,
                "jawaban_19": 2,
                "jawaban_20": 2
            }
        }

class ChangePassword(BaseModel):
    password_baru : str
    konfirmasi_password_baru : str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "password_baru": "inipasswordbaru",
                "konfirmasi_password_baru": "inipasswordbaru",
            }
        }
