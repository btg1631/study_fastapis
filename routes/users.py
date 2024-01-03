from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")


# 회원가입 /users/insert
@router.get("/inserts")
async def insert(request:Request):
    html = "<body> <h2>It's Home List</h2> </body>"
    return templates.TemplateResponse("users/inserts.html", {'request':request})
