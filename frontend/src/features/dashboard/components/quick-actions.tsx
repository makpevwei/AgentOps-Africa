import {
  Building2,
  FileText,
  FileSpreadsheet,
  FileSearch,
} from "lucide-react";

const actions = [
  {
    title: "Research Company",
    description: "Gather company intelligence with AI",
    icon: Building2,
  },
  {
    title: "Generate Proposal",
    description: "Create a professional proposal",
    icon: FileText,
  },
  {
    title: "Create Quote",
    description: "Generate a client quotation",
    icon: FileSpreadsheet,
  },
  {
    title: "Analyze Document",
    description: "Extract insights from documents",
    icon: FileSearch,
  },
];

export function QuickActions() {
  return (
    <section>
      <h2 className="mb-4 text-xl font-semibold">
        Quick Actions
      </h2>

      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        {actions.map((action) => {
          const Icon = action.icon;

          return (
            <button
              key={action.title}
              className="rounded-xl border bg-card p-5 text-left transition hover:border-primary hover:shadow-md"
            >
              <Icon className="mb-3 h-8 w-8 text-primary" />

              <h3 className="font-semibold">
                {action.title}
              </h3>

              <p className="mt-2 text-sm text-muted-foreground">
                {action.description}
              </p>
            </button>
          );
        })}
      </div>
    </section>
  );
}