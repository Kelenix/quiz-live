import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { QuizForm } from "@/components/QuizForm";

export default function NewQuizPage() {
  return (
    <div className="space-y-6">
      <Link href="/admin" className="inline-flex items-center gap-2 text-sm text-zinc-400 hover:text-zinc-200">
        <ArrowLeft className="h-4 w-4" /> Retour aux quiz
      </Link>
      <div>
        <h1 className="text-2xl font-bold">Nouveau quiz</h1>
        <p className="text-sm text-zinc-400">
          Configure ton quiz et ajoute des questions. Un code de connexion sera généré automatiquement.
        </p>
      </div>
      <QuizForm />
    </div>
  );
}
