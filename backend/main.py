from fastapi import FastAPI, Request, Cookie, Body
from typing import Optional
import models.queue.schema 
import models.store.schema 
import models.user.schema
import models.verification.schema

import models.user.repository as user_repo
import models.verification.repository as vr_repo

from models.user.model import User as user_model
from models.verification.model import Verification as vr_model

from controllers import verification as vr_controller
import db

app = FastAPI()


# Start-up and tear-down script
@app.on_event("startup")
def startup_script():
    db.Base.metadata.create_all()


@app.on_event("shutdown")
def shutdown_script():
    db.SessionLocal.close_all()


@app.get("/")
def default_route():
    return {
        "message": "Welcome to the simple QR system backend",
        "version": "beta-v1.0.0",
        "developer": "Justin",
        "license": "MIT License",
    }


@app.get("/qr")
def get_qr_code(request: Request):
    return {"message": "This is the qr generation section"}


@app.post("/verification-request")
def send_verification_request(email: str = Body(..., embed=True)):
    status = vr_repo.create_verification_request(db=db.SessionLocal(), email=email)
    return {"status": status}

@app.post("/verification-approval")
def verification_approval(vr: vr_model):
    jwt_token = vr_controller.verify_user(db=db.SessionLocal(), verification=vr)
    return {"jwt_token": jwt_token}


@app.post("/decode-jwt")
def decode_jwt(jwt_token: Optional[str] = Cookie(None)):
    status = vr_controller.decode_jwt(token=jwt_token)
    return {"response": status}


@app.post("/create-user")
def create_user(user: user_model, jwt_token: str = Cookie(...)):
    status = vr_controller.decode_jwt(token=jwt_token)
    if "Invalid" in status:
        return "INVALID INPUT"
    user = user_repo.create_user(db=db.SessionLocal(), user=user)
    return user

@app.post("/queue")
def add_to_queue():
    pass

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
