from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router
from criar_tabelas import create_tables

app = FastAPI(title='API using FastAPI and SQL Alchemy')
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get('/')
async def root():
    return {'message': "IT'S WORK!!"}


if __name__ == '__main__':
    import uvicorn
    create_tables()
    uvicorn.run(
        'main:app', host='0.0.0.0', port=9000, log_level='info', reload=True
    )
