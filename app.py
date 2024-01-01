from fastapi import FastAPI
from routers import framework_router, module_router, doc_list_router
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

def main():
    app = FastAPI()

    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(framework_router.router)
    app.include_router(module_router.router)
    app.include_router(doc_list_router.router)

    return app

app = main()