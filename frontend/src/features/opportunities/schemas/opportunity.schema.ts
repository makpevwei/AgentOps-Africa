import { z } from "zod";

export const opportunitySchema = z.object({
    title: z
        .string()
        .min(3, "Title must be at least 3 characters."),

    description: z
        .string()
        .min(10, "Description must be at least 10 characters."),

    company_name: z.string().optional(),

    contact_name: z.string().optional(),

    email: z
        .string()
        .email("Invalid email address.")
        .optional()
        .or(z.literal("")),

    phone: z.string().optional(),

    source: z.enum([
        "manual",
        "website",
        "email",
        "telegram",
        "whatsapp",
        "linkedin",
        "api",
    ]),
});

export type OpportunityFormData = z.infer<typeof opportunitySchema>;