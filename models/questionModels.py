from sqlalchemy import Column, Integer, String
from database.db import Base
from pydantic import BaseModel

class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key = True, index = True)
    pertanyaan = Column(String)
    pilihan = Column(String)

    class Config:
        schema_extra ={
            "Contoh" :{
                "pertanyaan" : "Apakah orang baru dapat Anda ceritakan dengan hal yang menjadi ketertarikan Anda?",
                "pilihan" : "1) Tentu bisa, 2) Hanya jika orang tersebut sudah cukup dekat"
            }
        }


class QuestionSchema(BaseModel):
    pertanyaan: str
    pilihan : str

    class Config:
        orm_mode = True
        schema_extra ={
            "Contoh" :{
                "pertanyaan" : "Apakah orang baru dapat Anda ceritakan dengan hal yang menjadi ketertarikan Anda?",
                "pilihan" : "1) Tentu bisa, 2) Hanya jika orang tersebut sudah cukup dekat"
            }
        }

class QuestionShow(BaseModel):
    id: int
    pertanyaan: str
    pilihan: str

    class Config:
        orm_mode = True
        schema_extra = {
            "Contoh" :{
                "pertanyaan" : "Apakah orang baru dapat Anda ceritakan dengan hal yang menjadi ketertarikan Anda?",
                "pilihan" : "1) Tentu bisa, 2) Hanya jika orang tersebut sudah cukup dekat"
            }
        }

class QuestionUpdate(BaseModel):
    pertanyaan: str

    class Config:
        orm_mode = True
        schema_extra = {
            "Contoh" :{
                "pertanyaan" : "Apakah orang baru dapat Anda ceritakan dengan hal yang menjadi ketertarikan Anda?"
            }
        }
        