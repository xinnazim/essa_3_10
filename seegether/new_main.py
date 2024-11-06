from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import new_crud

app = FastAPI(title='seegether')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/sportsdate/select") # 쿼리 매개변수 활용 예시
def get_sports_gamedate(sports_type: str,date, place: str, team: str):
    return new_crud.read_sports_gamedate(sports_type, date, place, team)

@app.get("/baseball_groupdata") # 쿼리 매개변수 활용 예시
def get_baseball_groupdata(date, cheer_team:str):
    return new_crud.get_group_list_by_sports(date, cheer_team)

