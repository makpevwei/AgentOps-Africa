export function PipelineSummary() {
  return (
    <section className="rounded-xl border bg-card p-6">
      <h2 className="mb-6 text-lg font-semibold">
        Opportunity Pipeline
      </h2>

      <div className="space-y-5">
        <div>
          <div className="flex justify-between">
            <span>Qualified Leads</span>
            <strong>12</strong>
          </div>
        </div>

        <div>
          <div className="flex justify-between">
            <span>Proposals Sent</span>
            <strong>8</strong>
          </div>
        </div>

        <div>
          <div className="flex justify-between">
            <span>Won Opportunities</span>
            <strong>3</strong>
          </div>
        </div>
      </div>
    </section>
  );
}