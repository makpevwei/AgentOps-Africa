"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Sparkles } from "lucide-react";

export function AssistantPrompt() {
    return (
        <section className="rounded-2xl border bg-card p-8 shadow-sm">
            <div className="mb-6 flex items-center gap-3">
                <div className="rounded-full bg-primary/10 p-2">
                    <Sparkles className="h-6 w-6 text-primary" />
                </div>

                <div>
                    <h2 className="text-2xl font-bold">
                        Good Evening 👋
                    </h2>

                    <p className="text-muted-foreground">
                        What would you like your Executive Assistant to help you with today?
                    </p>
                </div>
            </div>

            <div className="flex gap-3">
                <Input
                    placeholder="Research MTN Nigeria and prepare a proposal..."
                    className="h-12"
                />

                <Button size="lg">
                    Ask AI
                </Button>
            </div>
        </section>
    );
}