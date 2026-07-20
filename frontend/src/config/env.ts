const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export const env = {
  apiBaseUrl: API_BASE_URL,
} as const;