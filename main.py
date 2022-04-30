import uvicorn
from src.core.config import config

if __name__ == "__main__":
    uvicorn.run(
        app="src:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True if config.ENV != "production" else False
    )
