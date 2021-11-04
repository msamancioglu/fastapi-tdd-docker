# project/app/main.py


from fastapi import FastAPI, Depends

from config import get_settings, Settings


app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }

import uvicorn
import os
if __name__ == "__main__":
    run_base = f"{os.path.basename(__file__).split('.')[0]}:app"
    print(run_base)
    uvicorn.run(run_base, reload=True)
