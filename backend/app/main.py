from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from app.config.settings import settings
from app.config.logger import logger
from app.routes.health import router as health_router
from app.routes.chat import router as chat_router

# Log application startup
logger.info("Starting Agentic Multi-Modal AI Assistant...")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Agentic Multi-Modal AI Assistant Backend",
)

# -----------------------------
# CORS Configuration
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Register Routes
# -----------------------------
app.include_router(health_router, tags=["Health"])
print(">>> Loading health router")

app.include_router(chat_router, tags=["Chat"])
print(">>> Loading chat router")
print(app.routes)
print("\n========== REGISTERED ROUTES ==========")

for route in app.routes:
    if isinstance(route, APIRoute):
        print(route.path, route.methods)


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/", tags=["Root"])
async def root():
    logger.info("Root endpoint accessed")

    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "message": "Welcome to the Agentic Multi-Modal AI Assistant 🚀",
    }


# -----------------------------
# Startup Event
# -----------------------------
@app.on_event("startup")
async def startup_event():
    logger.info("Application startup completed successfully.")


# -----------------------------
# Shutdown Event
# -----------------------------
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown completed.")