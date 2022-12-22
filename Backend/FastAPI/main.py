### Hola Mundo ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"
from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers - Clase en vídeo (08/12/2022): https://www.twitch.tv/videos/1673759045
app.include_router(products.router)
app.include_router(users.router)

# Recursos estáticos - Clase en vídeo (14/12/2022): https://www.twitch.tv/videos/1679022882
app.mount("/static", StaticFiles(directory="static"), name="static")


# Url local: http://127.0.0.1:8000


@app.get("/")
async def root():
    return "Hola FastAPI!"

# Url local: http://127.0.0.1:8000/url


@app.get("/url")
async def url():
    return {"url": "https://alioncadev.com/python"}

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc