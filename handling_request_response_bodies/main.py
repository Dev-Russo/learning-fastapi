from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

## Modelo Base para requisões body
class User(BaseModel):
    name: str
    age: int
    
    #Verificação de dados no Body
    @field_validator("name")
    def name_must_not_be_empty(cls,v):
        if not v:
            return ValueError("Name must not be empty")
        return v
    
## Request by Body
@app.post("/users/")
async def create_user(user: User):
    u = {"name": user.name, "age": user.age}
    return u 