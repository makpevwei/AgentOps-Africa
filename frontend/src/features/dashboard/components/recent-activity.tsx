export function RecentActivity() {
  const activities = [
    "Proposal generated for Mainstreet Microfinance Bank",
    "Company research completed for MTN Nigeria",
    "Opportunity created for GTI Microfinance Bank",
  ];

  return (
    <section className="rounded-xl border bg-card p-6">
      <h2 className="mb-4 text-lg font-semibold">
        Recent AI Activity
      </h2>

      <ul className="space-y-3">
        {activities.map((activity) => (
          <li
            key={activity}
            className="border-b pb-3 last:border-none"
          >
            {activity}
          </li>
        ))}
      </ul>
    </section>
  );
}