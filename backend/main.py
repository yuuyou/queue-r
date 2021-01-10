from fastapi import FastAPI, Request

app = FastAPI()


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
    return {
        "message": "This is the qr generation section"
    }


@app.post("/verification-request")
def send_verification_request():
    return {
        "message": "This is the backend to generate the verification request."
    }

@app.post("/verification-approval")
def verification_approval:
    return {
        "message": "This is the backend to approve the verification request."
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
