"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";

import {
    opportunitySchema,
    type OpportunityFormData,
} from "../schemas/opportunity.schema";

interface OpportunityFormProps {
    onSubmit: (data: OpportunityFormData) => Promise<void> | void;
    isSubmitting?: boolean;
}

export function OpportunityForm({
    onSubmit,
    isSubmitting = false,
}: OpportunityFormProps) {
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<OpportunityFormData>({
        resolver: zodResolver(opportunitySchema),
        defaultValues: {
            title: "",
            description: "",
            company_name: "",
            contact_name: "",
            email: "",
            phone: "",
            source: "manual",
        },
    });

    return (
        <form
            onSubmit={handleSubmit(onSubmit)}
            className="space-y-6"
        >
            {/* Customer Need */}

            <div>
                <label className="mb-2 block text-sm font-medium">
                    What does the customer need?
                </label>

                <Input
                    {...register("title")}
                    placeholder="e.g. School Management System"
                />

                {errors.title && (
                    <p className="mt-1 text-sm text-red-500">
                        {errors.title.message}
                    </p>
                )}
            </div>

            {/* Company */}

            <div>
                <label className="mb-2 block text-sm font-medium">
                    Company (Optional)
                </label>

                <Input
                    {...register("company_name")}
                    placeholder="Business name"
                />
            </div>

            {/* Contact */}

            <div className="grid gap-4 md:grid-cols-2">
                <div>
                    <label className="mb-2 block text-sm font-medium">
                        Contact Person
                    </label>

                    <Input
                        {...register("contact_name")}
                        placeholder="John Doe"
                    />
                </div>

                <div>
                    <label className="mb-2 block text-sm font-medium">
                        Phone / WhatsApp
                    </label>

                    <Input
                        {...register("phone")}
                        placeholder="+234..."
                    />
                </div>
            </div>

            {/* Email */}

            <div>
                <label className="mb-2 block text-sm font-medium">
                    Email
                </label>

                <Input
                    type="email"
                    {...register("email")}
                    placeholder="john@example.com"
                />

                {errors.email && (
                    <p className="mt-1 text-sm text-red-500">
                        {errors.email.message}
                    </p>
                )}
            </div>

            {/* Lead Source */}

            <div>
                <label className="mb-2 block text-sm font-medium">
                    How did this opportunity come in?
                </label>

                <select
                    {...register("source")}
                    className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                >
                    <option value="manual">Manual Entry</option>
                    <option value="website">Website</option>
                    <option value="whatsapp">WhatsApp</option>
                    <option value="telegram">Telegram</option>
                    <option value="email">Email</option>
                    <option value="linkedin">LinkedIn</option>
                    <option value="api">API</option>
                </select>
            </div>

            {/* Description */}

            <div>
                <label className="mb-2 block text-sm font-medium">
                    Opportunity Description
                </label>

                <Textarea
                    rows={6}
                    {...register("description")}
                    placeholder="Describe the customer's request in as much detail as possible..."
                />

                {errors.description && (
                    <p className="mt-1 text-sm text-red-500">
                        {errors.description.message}
                    </p>
                )}
            </div>

            {/* Buttons */}

            <div className="flex justify-end gap-3 pt-2">
                <Button
                    type="submit"
                    disabled={isSubmitting}
                >
                    {isSubmitting
                        ? "Creating..."
                        : "Create Opportunity"}
                </Button>
            </div>
        </form>
    );
}