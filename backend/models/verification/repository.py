from sqlalchemy.orm import Session
from .model import Verification as VerificationModel
from .schema import Verification as VerificationSchema
from controllers import verification as vr

def create_verification_request(db: Session, email: str):
    db_verification = db.query(VerificationSchema).filter(VerificationSchema.email == email).first()
    random_string = vr.generate_random_string()
    if db_verification:
        db_verification.temp_pass = random_string
        db.commit()
        return "Modified verification"
    data = VerificationModel(email=email, temp_pass=random_string)
    db.add(VerificationSchema(**data.dict()))
    db.commit()
    return "New user"
