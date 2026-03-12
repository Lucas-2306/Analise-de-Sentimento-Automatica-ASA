from fastapi import FastAPI
from backend.routes.analyze import router as analyze_router
from backend.routes.health import router as health_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Sentiment Analysis API",
    version="1.0"
)

app.include_router(analyze_router)
app.include_router(health_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "running"}