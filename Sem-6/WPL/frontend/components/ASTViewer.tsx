'use client';

import React, { useState } from 'react';
import { ChevronRight, ChevronDown } from 'lucide-react';

interface ASTViewerProps {
  data: any;
}

export default function ASTViewer({ data }: ASTViewerProps) {
  return (
    <div className="bg-muted p-4 rounded-md overflow-auto max-h-[600px]">
      <ASTNode node={data} level={0} />
    </div>
  );
}

interface ASTNodeProps {
  node: any;
  level: number;
}

function ASTNode({ node, level }: ASTNodeProps) {
  const [isExpanded, setIsExpanded] = useState(level < 2);

  if (node === null || node === undefined) {
    return <span className="text-muted-foreground italic">null</span>;
  }

  if (typeof node !== 'object') {
    return (
      <span className="text-green-600">
        {typeof node === 'string' ? `"${node}"` : String(node)}
      </span>
    );
  }

  if (Array.isArray(node)) {
    if (node.length === 0) {
      return <span className="text-muted-foreground">[]</span>;
    }

    return (
      <div className="ml-4">
        <span className="text-muted-foreground">[</span>
        {node.map((item, index) => (
          <div key={index} className="ml-4">
            <ASTNode node={item} level={level + 1} />
            {index < node.length - 1 && <span className="text-muted-foreground">,</span>}
          </div>
        ))}
        <span className="text-muted-foreground">]</span>
      </div>
    );
  }

  const entries = Object.entries(node);
  
  if (entries.length === 0) {
    return <span className="text-muted-foreground">{'{}'}</span>;
  }

  return (
    <div>
      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="flex items-center gap-1 hover:bg-accent px-1 rounded"
      >
        {isExpanded ? (
          <ChevronDown className="w-4 h-4" />
        ) : (
          <ChevronRight className="w-4 h-4" />
        )}
        <span className="font-medium text-blue-600">
          {node.type || 'Object'}
        </span>
        {node.lineno && (
          <span className="text-xs text-muted-foreground ml-2">
            Line {node.lineno}
          </span>
        )}
      </button>
      
      {isExpanded && (
        <div className="ml-6 border-l-2 border-muted-foreground/20 pl-2">
          {entries.map(([key, value]) => (
            <div key={key} className="my-1">
              <span className="text-purple-600 font-mono text-sm">{key}: </span>
              <ASTNode node={value} level={level + 1} />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
