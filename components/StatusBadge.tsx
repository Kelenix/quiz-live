import { cn, statusColor, statusLabel } from "@/lib/utils";
import type { QuizStatus } from "@/types";

export function StatusBadge({
  status,
  className,
}: {
  status: QuizStatus;
  className?: string;
}) {
  return (
    <span className={cn("chip", statusColor(status), className)}>
      <span className="h-1.5 w-1.5 rounded-full bg-current" />
      {statusLabel(status)}
    </span>
  );
}
