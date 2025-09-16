from fastapi import FastAPI

app = FastAPI()

list = []

@app.get("/items")
def get_all():
    return list

@app.get("/items/{item_id}")
def get_by_id(item_id: int):
    return list[item_id]

@app.post("/items/")
def create_item(name: str, price: float):
    list.append([name, price])
    return {"message": f"Item {name} com preço {price} adicionado com sucesso"}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    list[item_id][0] = name
    list[item_id][1] = price
    return {"message": f"Item {item_id} Alterado com Sucesso"}

@app.delete("/items/{item_id}")
def delete_iem(item_id: int):
    list.pop(item_id)
    return {"message" : "Item deletado com sucesso"}