from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def default_route():
    return {
        "message": "Welcome to the simple QR system backend",
        "version": "beta-v1",
        "developer": "Justin",
        "license": "MIT License",
    }


@app.get("/qr")
def get_qr_code(request: Request):
    return {
        "message": "This is the qr generation section"
    }


@app.post("/send-verification"):
def send_email_verification():
    return {
        "message": "This is the backend to start the email verification workflow."
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
