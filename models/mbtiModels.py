from sqlalchemy import Column, Integer, String
from database.db import Base
from pydantic import BaseModel

class MBTI_Type(Base):
    __tablename__ = 'information'

    id = Column(Integer, primary_key = True, index = True)
    Jenis_MBTI = Column(String)
    Kepribadian = Column(String)
    print(Jenis_MBTI)

    class Config:
        schema_extra ={
            "Contoh" :{
                'Jenis_MBTI' : "ISTJ (Introverted, Sensing, Thinking, Judging)",
                'Kepribadian' : "Orang dengan tipe kepribadian ISTJ biasanya cenderung pendiam dan serius, namun sangat gigih, bertanggung jawab, dan dapat diandalkan. Pribadi ISTJ umumnya juga selalu menginginkan ketertiban dan keteraturan dalam setiap aspek hidupnya."
            }
        }

class MBTI_Show(BaseModel):
    id : int
    Jenis_MBTI : str
    Kepribadian : str

    class Config:
        orm_mode = True
        schema_extra ={
            "Contoh" :{
                "Jenis_MBTI" : "ISTJ (Introverted, Sensing, Thinking, Judging)",
                "Kepribadian" : "Orang dengan tipe kepribadian ISTJ biasanya cenderung pendiam dan serius, namun sangat gigih, bertanggung jawab, dan dapat diandalkan. Pribadi ISTJ umumnya juga selalu menginginkan ketertiban dan keteraturan dalam setiap aspek hidupnya."
            }
        }