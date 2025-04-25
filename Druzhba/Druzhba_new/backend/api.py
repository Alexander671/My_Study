from functools import wraps
import urllib
import urllib.parse

from fastapi import FastAPI, HTTPException, Header
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from starlette.middleware.cors import CORSMiddleware
from starlette.templating import Jinja2Templates
from starlette.requests import Request

from db.models import  User
from config import Config
from utils import check_webapp_signature, decode_base64_str

config = Config()
app = FastAPI()

templates = Jinja2Templates(directory=config.templates_dir)

origins = ["*"]


static_dir = config.app_dir + '/backend/static'
app.mount('/static', StaticFiles(directory=static_dir), name='static')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def auth(func):
    @wraps(func)
    def wrapper(*args, **kvargs):
        if 'authorization' in kvargs:
            authorization = kvargs['authorization']
            decoded_str = decode_base64_str(authorization)
            init_data = urllib.parse.unquote(decoded_str)
            if config.token is None:
                raise HTTPException(status_code=501, detail="BotConfig is unavailable")
            ok = check_webapp_signature(config.token, init_data)
            if not ok:
                raise HTTPException(status_code=401, detail="Query ID is wrong or user is not Unauthorized")
        result = func(*args, **kvargs)
        return result
    return wrapper

######################################
# templates
######################################
@app.get('/UserRegistration')
async def get_user_registration_html(request: Request):
    headers = {
        'ngrok-skip-browser-warning': '100',
    }
    host = Config().base_url
    return templates.TemplateResponse('userRegistration.html',
                                      context={'request': request, 'host': host}, headers=headers)


# проверка ssl сертификата
@app.get("/.well-known/pki-validation/{file_path}")
async def download_file(file_path:str):
  return FileResponse(path=f'certificate/{file_path}', filename=file_path, media_type='multipart/form-data')


@app.post('/api/user/')
@auth
def create_new_user(user: User, authorization: str | None = Header(convert_underscores=True)):
    print(user, authorization)
    # """
    # Create new user
    # :param user:
    # :param authorization:
    # :return:
    # """
    # db_user, db_accounts = db.create_user(user)
    # assert db_user is not None
    # assert db_accounts is not None
# 
    # web_init = WebAppInitData.form_auth_header(authorization)
    # data = {
    #     'command': 'create_user',
    #     'user_id': db_user.id,
    #     'account_id': db_accounts[0].id
    # }
    # data_json = json.dumps(data)
    # r = send_answer_web_app_query(web_init.query_id, data_json)
    # assert 200 == r.status_code
    # return {'account_id': db_accounts[0].id}