from fastapi import FastAPI
from database.db import engine
import uvicorn
from models import userModels, questionModels
from routes.userRoutes import user_router
from routes.questionRoutes import question_router
from routes.personalityRoutes import personality_router


app = FastAPI()
app.debug  = True

userModels.Base.metadata.create_all(engine)
questionModels.Base.metadata.create_all(engine)

app.include_router(user_router, prefix="/users")
app.include_router(question_router, prefix="/questions")
app.include_router(personality_router, prefix="/personality")

@app.get('/')
def index():
    return {
        "MBTI TEST FOR YOU!~"
        "MBTI adalah test kepribadian yang akan menunjukkan kecenderungan kepribadian Anda dan behavior dari kehidupan sehari-hari Anda"
        "Dalam project ini, test MBTI disederhanakan menjadi 20 soal saja dari yang seharusnya ada >70 soal"
    }


