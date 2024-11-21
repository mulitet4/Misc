@echo off
cd /d D:\Programming\UpEase\API
git pull
.venv\Scripts\activate
uvicorn main:app --reload