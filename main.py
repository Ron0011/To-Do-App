from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

import models, schemas, crud
from database import engine, get_db

# Ensure DB tables exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Static + Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})


@app.post("/add")
def add_task(title: str = Form(...), db: Session = Depends(get_db)):
    title = title.strip()
    if not title:
        return RedirectResponse("/", status_code=303)
    crud.create_task(db, schemas.TaskCreate(title=title))
    return RedirectResponse("/", status_code=303)


@app.get("/delete/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_task(db, task_id)
    if not ok:
        # Not fatal for the UI; just redirect back
        return RedirectResponse("/", status_code=303)
    return RedirectResponse("/", status_code=303)


@app.get("/toggle/{task_id}")
def toggle_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.update_task_status(db, task_id)
    # If not found, don’t crash the page — just redirect back
    return RedirectResponse("/", status_code=303)
