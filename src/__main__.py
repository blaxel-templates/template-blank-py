import uvicorn
import os

port = os.getenv("BL_SERVER_PORT", "80")
host = os.getenv("BL_SERVER_HOST", "0.0.0.0")

if __name__ == "__main__":
    uvicorn.run("src.main:app", host=host, port=int(port), reload=False)