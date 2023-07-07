from fastapi import FastAPI

from app.core import settings, events
from app.api.routes.private import router as private_router
from app.api.routes.public import router as public_router

def get_application() -> FastAPI:
	application = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION,
    )
	
	application.add_event_handler("startup", events.create_start_app_handler(application))
    application.add_event_handler("shutdown", events.create_stop_app_handler(application))
	
	application.include_router(public_router, prefix='/public')
    application.include_router(private_router, prefix='/private')
	
	return application
	
app = get_application()