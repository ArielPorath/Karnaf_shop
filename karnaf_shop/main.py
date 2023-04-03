from fastapi import FastAPI

from karnaf_shop.api.router import api_router
from karnaf_shop.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Mount the API router on the karnaf_shop
app.include_router(api_router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:karnaf_shop",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
    )