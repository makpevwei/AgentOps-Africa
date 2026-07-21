export interface ChatRequest {
  message: string;
}

export interface CompanyAnalysis {
  company_name: string;
  executive_summary: string;
  strengths: string[];
  weaknesses: string[];
  opportunities: string[];
  risks: string[];
}

export interface ChatResponse {
  response: CompanyAnalysis;
}