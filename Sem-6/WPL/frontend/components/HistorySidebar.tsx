"use client";

import React, { useEffect, useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";
import { getExecutionHistory } from "@/lib/api";
import { History, Clock, CheckCircle, XCircle, Code2 } from "lucide-react";
import { Badge } from "@/components/ui/badge";

export interface ExecutionHistoryItem {
  id: number;
  language: string;
  code: string;
  input_data: string;
  output: string;
  error: string;
  execution_time: number;
  created_at: string;
}

interface HistorySidebarProps {
  onSelectExecution?: (execution: ExecutionHistoryItem) => void;
}

export default function HistorySidebar({
  onSelectExecution,
}: HistorySidebarProps) {
  const [history, setHistory] = useState<ExecutionHistoryItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedId, setSelectedId] = useState<number | null>(null);

  const fetchHistory = async () => {
    try {
      setLoading(true);
      const data = await getExecutionHistory();
      setHistory(data);
    } catch (error) {
      console.error("Failed to fetch history:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHistory();
    // Refresh every 10 seconds
    const interval = setInterval(fetchHistory, 10000);
    return () => clearInterval(interval);
  }, []);

  const handleSelect = (execution: ExecutionHistoryItem) => {
    setSelectedId(execution.id);
    onSelectExecution?.(execution);
  };

  const getLanguageBadgeColor = (language: string) => {
    const colors: Record<string, string> = {
      python: "bg-blue-500",
      c: "bg-gray-500",
      cpp: "bg-purple-500",
      java: "bg-orange-500",
    };
    return colors[language] || "bg-gray-500";
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    const now = new Date();
    const diff = now.getTime() - date.getTime();
    const minutes = Math.floor(diff / 60000);
    const hours = Math.floor(diff / 3600000);
    const days = Math.floor(diff / 86400000);

    if (minutes < 1) return "Just now";
    if (minutes < 60) return `${minutes}m ago`;
    if (hours < 24) return `${hours}h ago`;
    return `${days}d ago`;
  };

  return (
    <Card className='h-full'>
      <CardHeader className='pb-3'>
        <CardTitle className='text-base flex items-center gap-2'>
          <History className='w-4 h-4' />
          Execution History
        </CardTitle>
      </CardHeader>
      <CardContent className='p-0'>
        <ScrollArea className='h-[calc(100vh-12rem)]'>
          {loading ? (
            <div className='p-4 text-center text-sm text-muted-foreground'>
              Loading history...
            </div>
          ) : history.length === 0 ? (
            <div className='p-4 text-center text-sm text-muted-foreground'>
              <Code2 className='w-8 h-8 mx-auto mb-2 opacity-50' />
              <p>No executions yet</p>
            </div>
          ) : (
            <div className='space-y-2 p-3'>
              {history.map((execution) => (
                <div
                  key={execution.id}
                  onClick={() => handleSelect(execution)}
                  className={`p-3 rounded-lg border cursor-pointer transition-colors hover:bg-accent ${
                    selectedId === execution.id
                      ? "bg-accent border-primary"
                      : ""
                  }`}
                >
                  <div className='flex items-start justify-between mb-2'>
                    <Badge
                      className={`${getLanguageBadgeColor(execution.language)} text-white text-xs`}
                    >
                      {execution.language.toUpperCase()}
                    </Badge>
                    <span className='text-xs text-muted-foreground'>
                      {formatDate(execution.created_at)}
                    </span>
                  </div>

                  <div className='space-y-2'>
                    {/* Code Preview */}
                    <div className='text-xs font-mono bg-muted p-2 rounded overflow-hidden'>
                      <div className='truncate'>
                        {execution.code.split("\n")[0] || "Empty code"}
                      </div>
                      {execution.code.split("\n").length > 1 && (
                        <div className='text-muted-foreground mt-1'>
                          +{execution.code.split("\n").length - 1} more lines
                        </div>
                      )}
                    </div>

                    {/* Status */}
                    <div className='flex items-center justify-between text-xs'>
                      <div className='flex items-center gap-1'>
                        {execution.error ? (
                          <>
                            <XCircle className='w-3 h-3 text-destructive' />
                            <span className='text-destructive'>Error</span>
                          </>
                        ) : (
                          <>
                            <CheckCircle className='w-3 h-3 text-green-500' />
                            <span className='text-green-500'>Success</span>
                          </>
                        )}
                      </div>
                      <div className='flex items-center gap-1 text-muted-foreground'>
                        <Clock className='w-3 h-3' />
                        <span>{execution.execution_time.toFixed(3)}s</span>
                      </div>
                    </div>

                    {/* Input preview if exists */}
                    {execution.input_data && (
                      <div className='text-xs text-muted-foreground'>
                        Input: {execution.input_data.substring(0, 30)}
                        {execution.input_data.length > 30 ? "..." : ""}
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </ScrollArea>
      </CardContent>
    </Card>
  );
}
