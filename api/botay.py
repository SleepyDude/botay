from fastapi import FastAPI, Depends
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

# /
@app.get('/')
async def home():
    return {"Message": "Botay or die, hello API!"}
