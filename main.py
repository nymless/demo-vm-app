from fastapi import FastAPI
from pydantic import BaseModel
from src.model.image_to_text import load_model


class Item(BaseModel):
    url: str


app = FastAPI()
image_to_text = load_model()


@app.get("/")
def root():
    return {'message': 'Hi there!'}


@app.post("/predict/")
async def predict(item: Item):
    return await image_to_text(item.url)
