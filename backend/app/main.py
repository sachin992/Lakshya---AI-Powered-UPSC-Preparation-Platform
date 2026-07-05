from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth, current_affairs, dashboard, mains, puzzle, test_generator, upsc_gpt
from app.core.config import settings
from app.db.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)

origins = [origin.strip() for origin in settings.allowed_origins.split(",") if origin.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=settings.api_prefix)
app.include_router(upsc_gpt.router, prefix=settings.api_prefix)
app.include_router(test_generator.router, prefix=settings.api_prefix)
app.include_router(mains.router, prefix=settings.api_prefix)
app.include_router(current_affairs.router, prefix=settings.api_prefix)
app.include_router(puzzle.router, prefix=settings.api_prefix)
app.include_router(dashboard.router, prefix=settings.api_prefix)


@app.get("/")
def root():
    return {"message": "Lakshya API is running"}
