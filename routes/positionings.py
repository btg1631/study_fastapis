from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")

@router.get("/forms")
async def forms(request:Request):
    pass
    return templates.TemplateResponse(name="positionings/forms.html"
                                      , context={"request":request})

@router.get("/grids")
async def grids(request:Request):
    pass
    return templates.TemplateResponse(name="positionings/grids.html"
                                      , context={"request":request})

@router.get("/standards")
async def standards(request:Request):
    pass
    return templates.TemplateResponse(name="positionings/standards.html"
                                      , context={"request":request})

@router.get("/tables")
async def tables(request:Request):
    pass
    return templates.TemplateResponse(name="positionings/tables.html"
                                      , context={"request":request})
