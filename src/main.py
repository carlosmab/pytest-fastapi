from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/contact")
async def contact():
    return {"message": "Contact page!"}


class User(BaseModel):
    username: str
    password: str


@app.post("/user", response_model=User)
async def create_user(user: User):
    return {"username": user.username, "password": user.password}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)