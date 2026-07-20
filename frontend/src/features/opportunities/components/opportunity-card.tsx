"use client";

import Link from "next/link";

import type { Opportunity } from "@/types/opportunity";

interface OpportunityCardProps {
    opportunity: Opportunity;
}

export function OpportunityCard({
    opportunity,
}: OpportunityCardProps) {
    return (
        <Link
            href={`/opportunities/${opportunity.id}`}
            className="block"
        >
            <div className="rounded-xl border bg-card p-5 shadow-sm transition-all hover:border-primary hover:shadow-md hover:-translate-y-0.5">

                <div className="flex items-start justify-between">

                    <div>

                        <h3 className="text-lg font-semibold">
                            {opportunity.title}
                        </h3>

                        <p className="mt-1 text-muted-foreground">
                            {opportunity.company_name || "👤 Individual Lead"}
                        </p>

                    </div>

                    <span className="rounded-full bg-slate-100 px-3 py-1 text-xs capitalize">
                        {opportunity.status.replace("_", " ")}
                    </span>

                </div>

                <p className="mt-4 text-sm text-muted-foreground line-clamp-2">
                    {opportunity.description}
                </p>

            </div>
        </Link>
    );
}