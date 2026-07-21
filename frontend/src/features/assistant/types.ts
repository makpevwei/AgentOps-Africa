export interface ChatRequest {
  message: string;
}

export interface ChatResponse {
  response: unknown;
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
}