from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import weather
from models.weatherData import WeatherData

import os

app = FastAPI()

# Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data instance
weather_data = WeatherData(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/weather.csv"))

# Include routers
app.include_router(weather.router, prefix="/weather", tags=["data", "weather"])
app.include_router(weather.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
