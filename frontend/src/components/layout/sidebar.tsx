"use client";

import Link from "next/link";
import { navigation } from "./navigation";

export function Sidebar() {
  return (
    <aside className="w-64 border-r bg-background">
      <div className="p-6">
        <h1 className="text-xl font-bold">
          AgentOps Enterprise
        </h1>
      </div>

      <nav className="px-3">
        {navigation.map((item) => (
          <Link
            key={item.name}
            href={item.href}
            className="flex items-center gap-3 rounded-lg px-3 py-2 hover:bg-muted"
          >
            <item.icon className="h-5 w-5" />
            {item.name}
          </Link>
        ))}
      </nav>
    </aside>
  );
}