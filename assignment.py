from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

class User(BaseModel):
    Firstname:str
    Lastname:str
    Age:int
    Email:str
    Height:int

app = FastAPI()

responses = []

origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

async def logger_middleware(request:Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Duration: {duration}")
    responses.append(response)
    return response

app.middleware("http")(logger_middleware)

@app.post("/users",status_code=200)
def create_users(user:User):
    print(responses)
    return user
