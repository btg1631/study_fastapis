from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")

@router.get("/buttons")
async def buttons(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/buttons.html"
                                      , context={"request":request})

@router.get("/cards")
async def cards(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/cards.html"
                                      , context={"request":request})

@router.get("/colors")
async def colors(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/colors.html"
                                      , context={"request":request})

@router.get("/containers")
async def containers(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/containers.html"
                                      , context={"request":request})
