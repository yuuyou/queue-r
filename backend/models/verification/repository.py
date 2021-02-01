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


def verify_user(db: Session, verification: VerificationModel):
    db_verification = db.query(VerificationSchema).filter(VerificationSchema.email  == verification.email).first()
    # If user found in database, check verification code
    if db_verification:
        if db_verification.temp_pass == verification.temp_pass:
            # Generate json key using secret
            json_key = vr.generate_json_string(verification.email)
            return json_key
    return "User not found"
