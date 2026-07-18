from agentops.clients.finnhub_client import FinnhubClient

client = FinnhubClient()

print(client.company_profile("AAPL"))
