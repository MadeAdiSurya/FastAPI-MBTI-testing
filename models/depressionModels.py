from pydantic import BaseModel, EmailStr

class ShowUserDepression(BaseModel):
    email: str
    nama : str
    diagnosis : str
    severity : str
    tipe_mbti : str
    rekomendasi : str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "email@gmail.com",
                "nama": "Agus",
                "diagnosis": "Normal",
                "severity": "Mild",
                "tipe_mbti" : "INTP",
                "rekomendasi" : "Berdasarkan kesehatan mental Anda, disarankan untuk lebih banyak berinteraksi dengan orang yang memiliki tipe kepribadian ISTJ, ISTP, ISFJ, ISFP"
            }
        }


class UserDepression(BaseModel):
    username: EmailStr
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "adi@gmail.com",
                "password": "passwordadi",
            }
        }
