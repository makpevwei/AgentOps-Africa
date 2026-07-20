interface OpportunityPageProps {
    params: Promise<{
        id: string;
    }>;
}

export default async function OpportunityPage({
    params,
}: OpportunityPageProps) {
    const { id } = await params;

    return (
        <div className="space-y-6">

            <h1 className="text-3xl font-bold">
                Opportunity Workspace
            </h1>

            <p className="text-muted-foreground">
                Opportunity ID
            </p>

            <pre className="rounded-lg border p-4">
                {id}
            </pre>

        </div>
    );
}