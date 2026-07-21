"""
Global Exception Handlers

Registers application-wide exception handlers.
"""

from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from agentops.core.exceptions import (
    AgentOpsException,
    NotFoundException,
)
from agentops.core.logger import logger
from agentops.core.responses import ErrorResponse


def register_exception_handlers(app: FastAPI) -> None:
    """Register application-wide exception handlers."""

    @app.exception_handler(NotFoundException)
    async def not_found_handler(
        _: Request,
        exc: NotFoundException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=404,
            content=ErrorResponse(
                message=str(exc),
            ).model_dump(),
        )

    @app.exception_handler(AgentOpsException)
    async def application_exception_handler(
        _: Request,
        exc: AgentOpsException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content=ErrorResponse(
                message=str(exc),
            ).model_dump(),
        )

    @app.exception_handler(Exception)
    async def unexpected_exception_handler(
        _: Request,
        exc: Exception,
    ) -> JSONResponse:
        logger.exception(
            "Unhandled exception",
            exc_info=exc,
        )

        return JSONResponse(
            status_code=500,
            content=ErrorResponse(
                message="An unexpected error occurred.",
            ).model_dump(),
        )
