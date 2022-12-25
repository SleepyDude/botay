from fastapi import FastAPI, Depends
from mangum import Mangum
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
handler = Mangum(app)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.get('/items/')
async def read_items(token: str = Depends(oauth2_scheme)):
    return {'token': token}

# form_data depends on OAuth2PasswordRequestForm
# if it fails then it not return data to the form_data
# else - all will be right
@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}


# /
@app.get('/')
async def home():
    return {"Message": "Botay or die"}


'''
USER section
'''
# POST /user/register
# POST /user/login
# POST /user/logout
# GET /user/me
# 

# /list-tasks
@app.get('/list-tasks')
async def list_tasks():
    return {'tasks': []}

# /task-by-index/{index}
# /get-uncompleted-task
# /add-task
# /get-task?id=...

