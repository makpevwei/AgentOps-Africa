"use client";

import { useState } from "react";

import { Button } from "@/components/ui/button";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "@/components/ui/dialog";

import { OpportunityForm } from "./opportunity-form";
import { useCreateOpportunity } from "../hooks/use-create-opportunity";
import type { OpportunityFormData } from "../schemas/opportunity.schema";

export function NewOpportunityDialog() {
    const [open, setOpen] = useState(false);

    const mutation = useCreateOpportunity();

    async function handleSubmit(
        data: OpportunityFormData,
    ) {
        try {
            await mutation.mutateAsync(data);

            setOpen(false);
        } catch (error) {
            console.error("Failed to create opportunity:", error);
        }
    }

    return (
        <Dialog
            open={open}
            onOpenChange={setOpen}
        >
            <DialogTrigger asChild>
                <Button>
                    + New Opportunity
                </Button>
            </DialogTrigger>

            <DialogContent className="max-w-2xl">
                <DialogHeader>
                    <DialogTitle>
                        New Opportunity
                    </DialogTitle>

                    <DialogDescription>
                        Capture a new sales opportunity.
                    </DialogDescription>
                </DialogHeader>

                <OpportunityForm
                    onSubmit={handleSubmit}
                    isSubmitting={mutation.isPending}
                />
            </DialogContent>
        </Dialog>
    );
}