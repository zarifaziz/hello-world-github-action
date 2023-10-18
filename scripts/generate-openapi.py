import json
from fastapi.openapi.utils import get_openapi
from src.main import app


with open('openapi.json', 'w', encoding='utf-8') as f:
    json.dump(get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    ), f)
