import { useState } from "react";
import { sendMessage } from "../api/assistant.api";
import { ChatResponse } from "../types";

export function useAssistant() {
    const [loading, setLoading] = useState(false);
    const [response, setResponse] =
        useState<ChatResponse | null>(null);

    async function ask(message: string) {
        setLoading(true);

        try {
            const result = await sendMessage(message);
            setResponse(result);
            return result;
        } finally {
            setLoading(false);
        }
    }

    return {
        loading,
        response,
        ask,
    };
}