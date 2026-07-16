from agentops.core.model_provider import ChatModelProvider
from agentops.core.logger import logger
from agentops.config.settings import settings


def main():

    logger.info("=" * 60)
    logger.info(settings.APP_NAME)
    logger.info("=" * 60)

    logger.info(f"Environment : {settings.ENVIRONMENT}")
    logger.info(f"Provider    : {settings.LLM_PROVIDER}")
    logger.info(f"Model       : {settings.DEFAULT_MODEL}")

    model = ChatModelProvider.create()

    logger.info("")
    logger.info("Model initialized successfully.")
    logger.info(model)


if __name__ == "__main__":
    main()