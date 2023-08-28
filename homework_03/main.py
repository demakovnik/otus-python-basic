from fastapi import FastAPI
from views import router as ping_router
import uvicorn

app = FastAPI()
app.include_router(ping_router, prefix="/ping")

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)