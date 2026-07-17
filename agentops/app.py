from agentops.config.settings import settings
from agentops.core.logger import logger
from agentops.core.model_provider import ChatModelProvider


def main():

    logger.info("=" * 60)
    logger.info(settings.APP_NAME)
    logger.info("=" * 60)

    logger.info("Environment: %s", settings.ENVIRONMENT)
    logger.info("Provider: %s", settings.LLM_PROVIDER)
    logger.info("Model: %s", settings.DEFAULT_MODEL)

    model = ChatModelProvider.create()

    logger.info("")
    logger.info("Model initialized successfully.")
    logger.info("Initialized model: %s", model)


if __name__ == "__main__":
    main()
