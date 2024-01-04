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
    return templates.TemplateResponse("users/inserts.html", context={'request':request})

# 로그인 /users/insert -> users/login.html
@router.post("/insert")
async def login(request:Request):
    datas = await request.form()
    print(dict(datas))
    return templates.TemplateResponse("users/logins.html", context={'request':request})

# 회원 리스트 /users/list -> users/lists.html
@router.post("/list")
async def list_post(request:Request):
    datas = await request.form()
    print(dict(datas))
    return templates.TemplateResponse("users/lists.html", context={'request':request})

@router.get("/list")
async def list_get(request:Request):
    return templates.TemplateResponse("users/lists.html", context={'request':request})

# 회원 상세정보 /users/read -> users/reads.html
# Path parameters : /users/read/id or /users/read/unique_name
@router.get("/read/{object_id}")
async def read(request:Request, object_id:str):
    return templates.TemplateResponse("users/reads.html", context={'request':request})


# 지정 안해도 됨
# async def insert(request, object_id):
