"use client";

import { NewOpportunityDialog } from "@/features/opportunities/components/new-opportunity-dialog";
import { OpportunityCard } from "@/features/opportunities/components/opportunity-card";
import { useOpportunities } from "@/features/opportunities/hooks/use-opportunities";
import type { Opportunity } from "@/types/opportunity";

export default function OpportunitiesPage() {
    const { data = [], isLoading, error } = useOpportunities();

    if (isLoading) {
        return (
            <div className="p-8">
                Loading opportunities...
            </div>
        );
    }

    if (error) {
        return (
            <div className="p-8 text-red-500">
                Unable to load opportunities.
            </div>
        );
    }

    return (
        <div className="space-y-8">
            {/* Page Header */}
            <div className="flex items-center justify-between">
                <div>
                    <h1 className="text-3xl font-bold">
                        Opportunities
                    </h1>

                    <p className="text-muted-foreground">
                        Manage your sales opportunities with AI Employees.
                    </p>
                </div>

                <NewOpportunityDialog />
            </div>

            {/* Empty State */}
            {data.length === 0 ? (
                <div className="rounded-xl border p-10 text-center">
                    <h3 className="text-lg font-semibold">
                        No opportunities yet
                    </h3>

                    <p className="mt-2 text-muted-foreground">
                        Click "New Opportunity" to create your first opportunity.
                    </p>
                </div>
            ) : (
                /* Opportunity Cards */
                <div className="grid gap-4">
                    {data.map((opportunity: Opportunity) => (
                        <OpportunityCard
                            key={opportunity.id}
                            opportunity={opportunity}
                        />
                    ))}
                </div>
            )}
        </div>
    );
}