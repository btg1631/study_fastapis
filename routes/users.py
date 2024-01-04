from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")

# 회원가입 form /users/form -> users/inserts.html
@router.get("/form")
async def insert(request:Request):
    return templates.TemplateResponse("users/inserts.html", {'request':request})


# 회원가입 /users/insert -> users/login.html
@router.get("/insert")
async def insert(request:Request):
    pass
    return templates.TemplateResponse("users/logins.html", {'request':request})
