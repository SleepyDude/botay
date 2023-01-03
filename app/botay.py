from fastapi import FastAPI, Body
from mangum import Mangum
from app.models.link_mod import PutLinkRequest
from uuid import uuid4
import os
import boto3

app = FastAPI()
handler = Mangum(app)


@app.get('/')
async def home():
    return {"Message": "Botay or die, hello API!"}

@app.post('/add_link')
def add_link(put_link_request: PutLinkRequest):
    item = {
        'user_id': put_link_request.user_id,
        'title': put_link_request.title,
        'url': put_link_request.url,
        'link_id': f'link_{uuid4().hex}'
    }

    table = _get_table()
    table.put_item(Item=item)
    return {'link': item}

def _get_table():
    table_name = os.environ.get('LINKS_TABLE_NAME')
    return boto3.resource('dynamodb').Table(table_name)