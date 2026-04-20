"use client";

import React, { useState } from "react";
import Editor from "@monaco-editor/react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import {
  ResizablePanelGroup,
  ResizablePanel,
  ResizableHandle,
} from "@/components/ui/resizable";
import {
  executeCode,
  generateAST,
  ExecuteCodeRequest,
  ExecutionHistoryItem,
} from "@/lib/api";
import { Play, Code2, AlertCircle, Clock, FileCode } from "lucide-react";
import ASTViewer from "./ASTViewer";
import { useEffect } from "react";

const LANGUAGE_OPTIONS = [
  { value: "python", label: "Python", monaco: "python" },
  { value: "c", label: "C", monaco: "c" },
  { value: "cpp", label: "C++", monaco: "cpp" },
  { value: "java", label: "Java", monaco: "java" },
] as const;

const DEFAULT_CODE = {
  python: `# Python Code Example
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial(number)}")`,
  c: `// C Code Example
#include <stdio.h>

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    printf("Factorial of %d is %d\\n", number, factorial(number));
    return 0;
}`,
  cpp: `// C++ Code Example
#include <iostream>
using namespace std;

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;
    cout << "Factorial of " << number << " is " << factorial(number) << endl;
    return 0;
}`,
  java: `// Java Code Example
import java.util.Scanner;

public class Factorial {
    public static int factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        System.out.println("Factorial of " + number + " is " + factorial(number));
        scanner.close();
    }
}`,
};

interface CodeEditorProps {
  selectedExecution?: ExecutionHistoryItem | null;
}

export default function CodeEditor({ selectedExecution }: CodeEditorProps) {
  const [language, setLanguage] = useState<"python" | "c" | "cpp" | "java">(
    "python",
  );
  const [code, setCode] = useState(DEFAULT_CODE.python);
  const [input, setInput] = useState("5");
  const [output, setOutput] = useState("");
  const [error, setError] = useState("");
  const [executionTime, setExecutionTime] = useState<number | null>(null);
  const [loading, setLoading] = useState(false);
  const [astData, setAstData] = useState<any>(null);
  const [astError, setAstError] = useState("");

  // Load execution from history when selected
  useEffect(() => {
    if (selectedExecution) {
      setLanguage(
        selectedExecution.language as "python" | "c" | "cpp" | "java",
      );
      setCode(selectedExecution.code);
      setInput(selectedExecution.input_data || "");
      setOutput(selectedExecution.output || "");
      setError(selectedExecution.error || "");
      setExecutionTime(selectedExecution.execution_time);
      setAstData(null);
      setAstError("");
    }
  }, [selectedExecution]);

  const handleLanguageChange = (newLang: "python" | "c" | "cpp" | "java") => {
    setLanguage(newLang);
    setCode(DEFAULT_CODE[newLang]);
    setOutput("");
    setError("");
    setExecutionTime(null);
    setAstData(null);
    setAstError("");
  };

  const handleExecute = async () => {
    setLoading(true);
    setOutput("");
    setError("");
    setExecutionTime(null);

    try {
      const request: ExecuteCodeRequest = {
        language,
        code,
        input_data: input,
      };

      const response = await executeCode(request);

      setOutput(response.output);
      setError(response.error);
      setExecutionTime(response.execution_time);
    } catch (err: any) {
      setError(
        err.response?.data?.error || err.message || "Failed to execute code",
      );
    } finally {
      setLoading(false);
    }
  };

  const handleGenerateAST = async () => {
    setLoading(true);
    setAstData(null);
    setAstError("");

    try {
      const response = await generateAST(code, language);

      if (response.success) {
        setAstData(response.ast);
      } else {
        setAstError(response.error || "Failed to generate AST");
      }
    } catch (err: any) {
      setAstError(
        err.response?.data?.error || err.message || "Failed to generate AST",
      );
    } finally {
      setLoading(false);
    }
  };

  const currentLanguageConfig = LANGUAGE_OPTIONS.find(
    (l) => l.value === language,
  );

  return (
    <ResizablePanelGroup className='h-full'>
      {/* Left Panel - Code Editor */}
      <ResizablePanel defaultSize={50} minSize={30}>
        <div className='h-full flex flex-col'>
          <Card className='h-full flex flex-col border-0 rounded-none'>
            <CardHeader className='flex-shrink-0'>
              <CardTitle className='flex items-center gap-2'>
                <Code2 className='w-5 h-5' />
                Code Editor
              </CardTitle>
              <CardDescription>Write your code and execute it</CardDescription>
            </CardHeader>
            <CardContent className='flex-1 flex flex-col space-y-4 overflow-hidden'>
              {/* Language Selector */}
              <div className='flex gap-2 flex-shrink-0'>
                {LANGUAGE_OPTIONS.map((lang) => (
                  <Button
                    key={lang.value}
                    variant={language === lang.value ? "default" : "outline"}
                    onClick={() => handleLanguageChange(lang.value)}
                    size='sm'
                  >
                    {lang.label}
                  </Button>
                ))}
              </div>

              {/* Code Editor */}
              <div className='border rounded-md overflow-hidden flex-1'>
                <Editor
                  height='100%'
                  language={currentLanguageConfig?.monaco}
                  value={code}
                  onChange={(value) => setCode(value || "")}
                  theme='vs-dark'
                  options={{
                    minimap: { enabled: false },
                    fontSize: 14,
                    lineNumbers: "on",
                    scrollBeyondLastLine: false,
                    automaticLayout: true,
                  }}
                />
              </div>

              {/* Input */}
              <div className='flex-shrink-0'>
                <label className='text-sm font-medium mb-2 block'>
                  Input (stdin)
                </label>
                <Textarea
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  placeholder='Enter input for your program'
                  className='font-mono'
                  rows={3}
                />
              </div>

              {/* Action Buttons */}
              <div className='flex gap-2 flex-shrink-0'>
                <Button
                  onClick={handleExecute}
                  disabled={loading}
                  className='flex-1'
                >
                  <Play className='w-4 h-4 mr-2' />
                  {loading ? "Executing..." : "Run Code"}
                </Button>

                <Button
                  onClick={handleGenerateAST}
                  disabled={loading}
                  variant='outline'
                >
                  <FileCode className='w-4 h-4 mr-2' />
                  AST
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </ResizablePanel>

      <ResizableHandle withHandle />

      {/* Right Panel - Output & AST */}
      <ResizablePanel defaultSize={50} minSize={30}>
        <div className='h-full flex flex-col'>
          <Card className='h-full flex flex-col border-0 rounded-none'>
            <CardHeader className='flex-shrink-0'>
              <CardTitle>Results</CardTitle>
            </CardHeader>
            <CardContent className='flex-1 overflow-hidden'>
              <Tabs
                defaultValue='output'
                className='w-full h-full flex flex-col'
              >
                <TabsList className='grid w-full grid-cols-2 flex-shrink-0'>
                  <TabsTrigger value='output'>Output</TabsTrigger>
                  <TabsTrigger value='ast'>AST Viewer</TabsTrigger>
                </TabsList>

                <TabsContent
                  value='output'
                  className='space-y-4 flex-1 overflow-y-auto'
                >
                  {/* Execution Time */}
                  {executionTime !== null && (
                    <div className='flex items-center gap-2 text-sm text-muted-foreground'>
                      <Clock className='w-4 h-4' />
                      <span>Execution time: {executionTime.toFixed(3)}s</span>
                    </div>
                  )}

                  {/* Standard Output */}
                  {output && (
                    <div>
                      <label className='text-sm font-medium mb-2 block'>
                        Output
                      </label>
                      <pre className='bg-muted p-4 rounded-md overflow-x-auto text-sm'>
                        {output}
                      </pre>
                    </div>
                  )}

                  {/* Errors */}
                  {error && (
                    <div>
                      <label className='text-sm font-medium mb-2 text-destructive flex items-center gap-2'>
                        <AlertCircle className='w-4 h-4' />
                        Error
                      </label>
                      <pre className='bg-destructive/10 text-destructive p-4 rounded-md overflow-x-auto text-sm'>
                        {error}
                      </pre>
                    </div>
                  )}

                  {/* Empty State */}
                  {!output && !error && executionTime === null && (
                    <div className='text-center py-12 text-muted-foreground'>
                      <Code2 className='w-12 h-12 mx-auto mb-4 opacity-50' />
                      <p>Run your code to see the output</p>
                    </div>
                  )}
                </TabsContent>

                <TabsContent value='ast' className='flex-1 overflow-y-auto'>
                  {astData ? (
                    <ASTViewer data={astData} />
                  ) : astError ? (
                    <div className='bg-destructive/10 text-destructive p-4 rounded-md'>
                      <div className='flex items-center gap-2 font-medium mb-2'>
                        <AlertCircle className='w-4 h-4' />
                        AST Error
                      </div>
                      <pre className='text-sm'>{astError}</pre>
                    </div>
                  ) : (
                    <div className='text-center py-12 text-muted-foreground'>
                      <FileCode className='w-12 h-12 mx-auto mb-4 opacity-50' />
                      <p>Generate AST to visualize your code structure</p>
                    </div>
                  )}
                </TabsContent>
              </Tabs>
            </CardContent>
          </Card>
        </div>
      </ResizablePanel>
    </ResizablePanelGroup>
  );
}
