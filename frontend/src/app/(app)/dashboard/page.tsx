import { AssistantChat } from "@/features/assistant/components/assistant-chat";

import {
  PipelineSummary,
  QuickActions,
  RecentActivity,
} from "@/features/dashboard";

export default function DashboardPage() {
  return (
    <div className="space-y-8">
      <AssistantChat />

      <QuickActions />

      <div className="grid gap-6 lg:grid-cols-2">
        <RecentActivity />
        <PipelineSummary />
      </div>
    </div>
  );
}