from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, HTMLResponse
import random

app = FastAPI()

system_codes = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Global variable to store last damaged system
last_damaged_system = {"name": None}


@app.get("/status")
def get_status():
    damaged_system = random.choice(list(system_codes.keys()))
    last_damaged_system["name"] = damaged_system
    return {"damaged_system": damaged_system}


@app.get("/repair-bay")
def repair_bay():
    damaged_system = last_damaged_system.get("name") or "unknown"
    code = system_codes.get(damaged_system, "UNKNOWN")
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{code}</div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/teapot")
def teapot():
    return Response(content="I'm a teapot", status_code=418, media_type="text/plain")
