export type OpportunityStatus =
    | "new"
    | "researching"
    | "proposal_drafted"
    | "quotation_ready"
    | "awaiting_approval"
    | "sent"
    | "negotiation"
    | "won"
    | "lost";

export type OpportunitySource =
    | "email"
    | "telegram"
    | "whatsapp"
    | "website"
    | "linkedin"
    | "manual"
    | "api";

export type OpportunityPriority =
    | "low"
    | "medium"
    | "high"
    | "urgent";

export interface Opportunity {
    id: string;
    organization_id: string;

    title: string;
    description: string;

    company_id: string | null;
    company_name: string;

    contact_name: string | null;
    email: string | null;
    phone: string | null;

    priority: OpportunityPriority;
    source: OpportunitySource;
    status: OpportunityStatus;

    assigned_agent: string | null;

    created_at: string;
    updated_at: string;
}