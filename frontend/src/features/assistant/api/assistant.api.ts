import { ChatResponse } from "../types";

const API_URL =
    process.env.NEXT_PUBLIC_API_URL ??
    "http://localhost:8000/api/v1";

export async function sendMessage(
    message: string
): Promise<ChatResponse> {
    const response = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            message,
        }),
    });

    if (!response.ok) {
        throw new Error("Unable to reach AgentOps API.");
    }

    return response.json();
}