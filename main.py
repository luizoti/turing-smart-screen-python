from fastapi import FastAPI

from src.sensors.sensors_librehardwaremonitor import Cpu

app = FastAPI()


@app.get("/")
async def root():
    return {"cpu": {"temp": Cpu().temperature()}}
