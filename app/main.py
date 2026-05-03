"""
FastAPI application for Lung Cancer Detection using LIDC-IDRI dataset
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

# Import routes
from app.routes import web_routes

# Initialize FastAPI app
app = FastAPI(
    title="Lung Cancer Detection System",
    description="AI-powered lung cancer detection using LIDC-IDRI dataset",
    version="1.0.0"
)

# Mount static files (CSS, JS, images)
static_path = Path(__file__).parent / "static"
if not static_path.exists():
    # If static doesn't exist in root, try app/static
    static_path = Path(__file__).parent / "app" / "static"
static_path.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

# Include routes
app.include_router(web_routes.router)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "app": "Lung Cancer Detection System"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
