from sqlalchemy.orm import Session
from models.mbtiModels import MBTI_Type, MBTI_Show
from sqlalchemy.orm import Session
from models.depressionModels import ShowUserDepression, UserDepression
from models.userModels import User
from fastapi import HTTPException, status
import requests



callback_url = "https://tstcontainer.purplecoast-7a34b4b4.eastasia.azurecontainerapps.io/"

def get_kawan_cocok(mbti):
    if (mbti == "ISTP" or mbti == "ISTJ" or mbti== "ISFJ" or mbti == "ISFP"):
        text = "Berdasarkan kesehatan mental Anda, disarankan untuk lebih banyak berinteraksi dengan orang yang memiliki tipe kepribadian INFJ, INFP, INTJ, INTP"
    elif (mbti == "INFJ" or mbti == "INFP" or mbti== "INTJ" or mbti == "INTP"):
        text = "Berdasarkan kesehatan mental Anda, disarankan untuk lebih banyak berinteraksi dengan orang yang memiliki tipe kepribadian ISTJ, ISTP, ISFJ, ISFP"
    elif (mbti == "ESTP" or mbti == "ESTJ" or mbti== "ESFP" or mbti == "ESFJ"):
        text = "Berdasarkan kesehatan mental Anda, disarankan untuk lebih banyak berinteraksi dengan orang yang memiliki tipe kepribadian ENFP, ENFJ, ENTP, ENTJ"
    elif (mbti == "ENFP" or mbti == "ENFJ" or mbti== "ENTJ" or mbti == "ENTP"):
        text = "Berdasarkan kesehatan mental Anda, disarankan untuk lebih banyak berinteraksi dengan orang yang memiliki tipe kepribadian ESFJ, ESTP, ESTJ, ESFP"
    return text

def get_depression_attach(request: UserDepression, db: Session, user: str):

    #mengambil user
    db_user = db.query(User).filter(User.email == user).first()
 
    res = requests.post(callback_url +"users/signin", data= {
        "username": request.username, 
        "password": request.password,})
    
    session = requests.Session()
    out = session.get(callback_url + "users/", 
        headers={"Authorization": "Bearer " + res.json().get("access_token")})
    
    for row in out.json():
        if row.get("email") == request.username:
            personality = row.get("personality")
            tipe_mbti= personality[0:4]
            
            userOut = ShowUserDepression(
                nama= row.get("nama"), 
                email= row.get("email"),
                diagnosis= row.get("diagnosis"),
                severity= row.get("severity"),
                tipe_mbti= personality[0:4],
                rekomendasi = str(get_kawan_cocok(tipe_mbti))
            )
            return userOut

def explain_type_mbti(db: Session):
    return db.query(MBTI_Type).all()
