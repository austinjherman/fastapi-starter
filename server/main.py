from app import create_app
from app.user.routes import user_router


app = create_app()
app.include_router(user_router())
