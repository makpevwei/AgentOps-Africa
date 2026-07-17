from agentops.providers.model_provider import ChatModelProvider


def main():

    model = ChatModelProvider.create()

    response = model.invoke("Say hello in one sentence.")

    print(response.content)


if __name__ == "__main__":
    main()