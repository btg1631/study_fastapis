from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory = "templates/")

@router.get("/buttons", response_class=HTMLResponse)
async def buttons(request:Request):
    pass
    return templates.TemplateResponse(name="gadgets/buttons.html"
                                      , context={"request":request})

# GET
@router.get("/cards")
# request = Request(query)
async def cards(request:Request):
    # request.query_params
    # QueryParams('name=youngji&email=waity0912%40gmail.com')
    ## dict(request.query_params)
    ## {'name': 'youngji', 'email': 'waity0912@gmail.com'}
    return templates.TemplateResponse(name="gadgets/cards.html"
                                      , context={"request":request})
# POST
@router.post("/cards")
async def cards_post(request:Request):
    # request.query_params
    # QueryParams('')
    # await request.form()
    # FormData([('name', 'youngji'), ('email', 'waity0912@gmail.com')])
    ## dict(await request.form())
    ## {'name': 'youngji', 'email': 'waity0912@gmail.com'}
    # form_datas = await request.form()
    # dict(form_datas)
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
