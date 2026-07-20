import axios from "axios";
import { env } from "@/config/env";

export const api = axios.create({
    baseURL: env.apiBaseUrl,
    timeout: 30000,
    headers: {
        "Content-Type": "application/json",
    },
});

// Attach JWT token to every request
api.interceptors.request.use((config) => {
    const token =
        typeof window !== "undefined"
            ? localStorage.getItem("access_token")
            : null;

    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
});

// Handle common API errors
api.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response?.status === 401) {
            // We'll implement token refresh later.
            console.warn("Unauthorized request");
        }

        return Promise.reject(error);
    }
);