import string
import random
from jose import JWTError, jwt
from pydantic import BaseModel
from models.verification import repository as VerificationRepo


SECRET_KEY = "2ef2c0408ebdeab145cacaef77250f338fe46be1f056656d4479dc4e47e31750"
ALGO = "HS256"


def generate_random_string(size=6, chars=string.ascii_uppercase + string.digits):
    result = ''.join(random.choice(chars) for _ in range(size))
    return result

def generate_json_string(email: string):
    encoded_jwt = jwt.encode({"email": email}, SECRET_KEY, algorithm=ALGO)
    return encoded_jwt

def decode_jwt(token: str):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=ALGO)
        email = data.get('email', None)
        return email
    except:
        return "Invalid JWT"


def verify_user(db: Session, verification: VerificationModel):
    db_verification = db.query(VerificationSchema).filter(VerificationSchema.email  == verification.email).first()
    # If user found in database, check verification code
    if db_verification:
        if db_verification.temp_pass == verification.temp_pass:
            # Generate json key using secret
            json_key = vr.generate_json_string(verification.email)
            return json_key
    return "User not found"
