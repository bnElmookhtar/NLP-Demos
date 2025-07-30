from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from models.summarizer import summarize

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize", response_class=HTMLResponse)
async def get_summary(request: Request, text: str = Form(...)):
   
    summary = summarize(text)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "summary": summary,
        "input_text": text
    })
