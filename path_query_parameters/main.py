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
    
"""
Path determina o caminho da URL enquanto o Query da algumas opções que não são obrigatórias
por exemplo quero saper quantas vendas teve um comissário especifico
/comissarios/{comissario_id}/vendas (Path) mas quero saber referente a um
mês especifico 
/comissarios/{comissario_id}/vendas/?mês=setembro

Buscaria todas as vendas de setembro sem obrigatoriedade de puxar por mes 
cria um consulta a menos se pararmos para pensar
"""