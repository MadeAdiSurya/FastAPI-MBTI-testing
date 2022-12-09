from sqlalchemy.orm import Session
from models.questionModels import QuestionSchema, Question, QuestionUpdate
from fastapi import HTTPException, status

def create_question(request: QuestionSchema, db: Session, user:str):
    if (user != "admin@gmail.com"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Fitur ini hanya dapat digunakan oleh admin."
        )

    pertanyaan = db.query(Question).filter(Question.pertanyaan == request.pertanyaan)

    if pertanyaan.first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Pertanyaan tersebut sudah ada."
        )

    pertanyaan_baru = Question(pertanyaan=request.pertanyaan, pilihan=request.pilihan)
    db.add(pertanyaan_baru)
    db.commit()
    # db.refresh(pertanyaan_baru)

    return {
        "Pesan": "Pertanyaan berhasil ditambahkan."
    }


def get_questions(db: Session):
    return db.query(Question).all()


def get_question(id: int, db: Session):
    pertanyaan = db.query(Question).filter(Question.id == id)

    if not pertanyaan.first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="pertanyaan dengan id tersebut tidak ditemukan."
        )

    return pertanyaan.first()


def update_question(id: int, request: QuestionUpdate, db: Session, user:str):
    if (user != "admin@gmail.com"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Fitur ini hanya dapat digunakan oleh admin."
        )

    pertanyaan = db.query(Question).filter(Question.id == id)

    if not pertanyaan.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="pertanyaan dengan id tersebut tidak ditemukan."
        )

    pertanyaan.update({'pertanyaan': request.pertanyaan})
    db.commit()

    return {
        "Pesan": "pertanyaan berhasil diperbarui."
    }


def delete_question(id: int, db: Session, user:str):
    if (user != "admin@gmail.com"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Fitur ini hanya dapat digunakan oleh admin."
        )

    pertanyaan = db.query(Question).filter(Question.id == id)

    if not pertanyaan.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="pertanyaan dengan id tersebut tidak ditemukan."
        )

    pertanyaan.delete(synchronize_session=False)
    db.commit()

    return {
        "Pesan": "pertanyaan berhasil dihapus."
    }
