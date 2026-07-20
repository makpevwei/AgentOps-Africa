import {
  Bot,
  Briefcase,
  Building2,
  FileSpreadsheet,
  FileText,
  LayoutDashboard,
  Search,
  Settings,
} from "lucide-react";

export const navigation = [
  {
    name: "Dashboard",
    href: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    name: "AI Employees",
    href: "/employees",
    icon: Bot,
  },
  {
    name: "Opportunities",
    href: "/opportunities",
    icon: Briefcase,
  },
  {
    name: "Companies",
    href: "/companies",
    icon: Building2,
  },
  {
    name: "Research",
    href: "/research",
    icon: Search,
  },
  {
    name: "Proposals",
    href: "/proposals",
    icon: FileText,
  },
  {
    name: "Quotations",
    href: "/quotations",
    icon: FileSpreadsheet,
  },
  {
    name: "Settings",
    href: "/settings",
    icon: Settings,
  },
];