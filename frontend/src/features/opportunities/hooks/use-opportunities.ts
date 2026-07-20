import { useQuery } from "@tanstack/react-query";
import { getOpportunities } from "@/services/opportunity.service";
import type { Opportunity } from "@/types/opportunity";

export function useOpportunities() {
    return useQuery<Opportunity[], Error>({
        queryKey: ["opportunities"],
        queryFn: getOpportunities,
    });
}