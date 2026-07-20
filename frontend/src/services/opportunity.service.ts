import { api } from "@/lib/api";
import type { Opportunity } from "@/types/opportunity";
import type { OpportunityFormData } from "@/features/opportunities/schemas/opportunity.schema";

export async function getOpportunities(): Promise<Opportunity[]> {
  const response = await api.get<Opportunity[]>("/opportunities/");
  return response.data;
}

export async function createOpportunity(
  data: OpportunityFormData,
): Promise<Opportunity> {
  const response = await api.post<Opportunity>(
    "/opportunities/",
    data,
  );

  return response.data;
}