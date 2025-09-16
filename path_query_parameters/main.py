from fastapi import FastAPI

app = FastAPI()

##Paths
@app.get("/users/{user_id}")
def road_user(user_id: int):
    return {"user": user_id}

##Query
@app.get("/users/")
def road_user1(user_id : int, name : str=None):
    return{"user_id": user_id, "name" : name}

#Path and Query
@app.get("/users/{user_id}/details")
def read_user_details(user_id:int, include_email:bool=False):
    if include_email:
        return {"user_id":user_id, "include email": "email included"}
    else:
        return {"user_id":user_id, "include email": "email not included"}