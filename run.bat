@echo off
start cmd /k "uvicorn app.main:app --reload"
start cmd /k "python app/scheduler.py"
