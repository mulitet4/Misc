"use client";

import CodeEditor from "@/components/CodeEditor";
import HistorySidebar from "@/components/HistorySidebar";
import { Code2 } from "lucide-react";
import { useState } from "react";
import type { ExecutionHistoryItem } from "@/lib/api";

export default function Home() {
  const [selectedExecution, setSelectedExecution] =
    useState<ExecutionHistoryItem | null>(null);

  return (
    <main className='flex h-screen overflow-hidden bg-gradient-to-b from-background to-muted/20'>
      {/* Sticky Sidebar - Full Height */}
      <aside className='w-80 h-screen border-r bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60'>
        <div className='p-4 border-b sticky top-0 bg-background/95 backdrop-blur z-10'>
          <div className='flex items-center gap-2 mb-2'>
            <Code2 className='w-6 h-6' />
            <h2 className='text-xl font-bold'>CodeBrew</h2>
          </div>
          <p className='text-xs text-muted-foreground'>
            Multi-language execution platform
          </p>
        </div>
        <HistorySidebar onSelectExecution={setSelectedExecution} />
      </aside>

      {/* Main Content Area */}
      <div className='flex-1 flex flex-col h-screen overflow-hidden'>
        {/* Header */}

        {/* Editor Area - Takes remaining height */}
        <div className='flex-1 overflow-hidden'>
          <CodeEditor selectedExecution={selectedExecution} />
        </div>
      </div>
    </main>
  );
}
