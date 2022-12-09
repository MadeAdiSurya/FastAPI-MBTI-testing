from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models.userModels import User, UserSchema, AnswerSchema, ChangePassword
from fastapi import HTTPException, status
from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token, delete_access_token
from pydantic import EmailStr


def sign_up(request: UserSchema, db: Session):
    user = db.query(User).filter(User.email == request.email).first()

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email sudah digunakan."
        )

    if len(request.password) < 8:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Password setidaknya memiliki 8 karakter."
        )

    hashed_password = HashPassword().create_hash(request.password)
    new_user = User(email=request.email, nama=request.nama,
                    password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "Pesan": "Akun berhasil dibuat."
    }


def sign_in(request, db: Session):
    user = db.query(User).filter(User.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Akun dengan email tersebut tidak ditemukan."
        )

    if not HashPassword().verify_hash(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Gagal, silahkan periksa email/password Anda kembali!")

    access_token = create_access_token(user.email)

    return {"access_token": access_token, "token_type": "bearer"}


def get_all_user(db: Session):
    return db.query(User).all()


def get_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User dengan id tersebut tidak ditemukan."
        )

    return user

def analyze_mbti(request: AnswerSchema, db: Session, user: str):
    
    #mengambil user yang akan diupdate
    update_user = db.query(User).filter(User.email == user)

    #membuat variabel int untuk komponen penilaian
    E = 0
    I = 0
    S = 0
    N = 0
    T = 0
    F = 0
    J = 0
    P = 0

    #inisialisasi result
    result = ''

    #komponen soal
    #1- 5: J/P
    #6-10 : E/I
    #11-15 : N/S
    #16-20 : F/T

    #get jawaban user
    answer_box = [
        request.jawaban_1, request.jawaban_2, request.jawaban_3, request.jawaban_4, 
        request.jawaban_5, request.jawaban_6, request.jawaban_7, request.jawaban_8, 
        request.jawaban_9, request.jawaban_10, request.jawaban_11, request.jawaban_12, 
        request.jawaban_13, request.jawaban_14, request.jawaban_15, request.jawaban_16, 
        request.jawaban_17, request.jawaban_18, request.jawaban_19, request.jawaban_20, 
    ]

    #mengambil jawaban J/P
    i = 0
    while i != 4:
        if answer_box[i] == 1:
            J+=1
        elif answer_box[i] == 2:
            P+=1
        i+=1
    #mengambil jawaban E/I
    while i != 9:
        if answer_box[i] == 1:
            E+=1
        elif answer_box[i] == 2:
            I+=1
        i+=1
    #mengambil jawaban N/S
    while i != 14:
        if answer_box[i] == 1:
            N+=1
        elif answer_box[i] == 2:
            S+=1
        i+=1
    #mengambil jawaban F/T
    while i != 19:
        if answer_box[i] == 1:
            F+=1
        elif answer_box[i] == 2:
            T+=1
        i+=1
    #melakukan penyusunan MBTI
    #ada 16 kemungkinan kombinasi

    if E > I:
        result += 'E'
    else:
        result += 'I'

    if S > N:
        result += 'S'
    else:
        result += 'N'

    if T > F:
        result += 'T'
    else:
        result += 'F'

    if J > P:
        result += 'J'
    else:
        result += 'P'

    #get percentage dari setiap komponen
    E_p = round((E / (E + I)) * 100, 2)
    I_p = round((I / (E + I)) * 100, 2)
    S_p = round((S / (S + N)) * 100, 2)
    N_p = round((N / (S + N)) * 100, 2)
    T_p = round((T / (T + F)) * 100, 2)
    F_p = round((F / (T + F)) * 100, 2)
    J_p = round((J / (J + P)) * 100, 2)
    P_p = round((P / (J + P)) * 100, 2)
    
    #deskripsi dari mbti
    text = 'Anda memiliki kepribadian dengan tipe ' + result + ' dengan kecenderungan Extraverted : ' + str(E_p) + '% Introverted : ' + str(I_p) + '% Sensing : ' + str(S_p) + '% Intuitive : ' + str(N_p) + '% Thinking :'  + str(T_p) + '%' + ' Feeling : '+ str(F_p) + '% Judging : ' + str(J_p) + '% Perceiving : ' + str(P_p)

    #melakukan update pada database
    update_user.update({'MBTI': result})
    update_user.update({'Deskripsi': text})
    
    db.commit()

    return {
        "MBTI": result, 
        "Deskripsi" : text
    }


def change_password(request: ChangePassword, db: Session, user:str):

    #mengambil user yang passwordnya akan diubah
    update_user = db.query(User).filter(User.email == user)
                     
    if (request.password_baru == request.konfirmasi_password_baru):
        if len(request.password_baru) < 8:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Password setidaknya memiliki 8 karakter."
            )

        hashed_password = HashPassword().create_hash(request.password_baru)

        update_user.update({'password': hashed_password})
        
        db.commit()
        # db.refresh(update_user)
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Password baru dan konfirmasi password baru tidak sama."
        )

    return {
        "Password berhasil diubah"
    }


def delete_user(db: Session, user:str):
    curr_user = db.query(User).filter(User.email == user)

    deactivate_access_token = delete_access_token(user)

    curr_user.delete(synchronize_session=False)
    db.commit()
    

    return {"Akun anda berhasil dihapus, sesi anda akan berakhir"}
