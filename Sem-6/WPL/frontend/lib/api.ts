import axios from "axios";

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export interface ExecuteCodeRequest {
  language: "python" | "c" | "cpp" | "java";
  code: string;
  input_data?: string;
}

export interface ExecuteCodeResponse {
  id: number;
  output: string;
  error: string;
  execution_time: number;
  created_at: string;
}

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

export interface ASTResponse {
  success: boolean;
  ast?: any;
  error?: string;
}

export const executeCode = async (
  data: ExecuteCodeRequest,
): Promise<ExecuteCodeResponse> => {
  const response = await api.post("/execute/", data);
  return response.data;
};

export const generateAST = async (
  code: string,
  language: string,
): Promise<ASTResponse> => {
  const response = await api.post("/ast/", { code, language });
  return response.data;
};

export const getExecutionHistory = async (): Promise<
  ExecutionHistoryItem[]
> => {
  const response = await api.get("/history/");
  return response.data;
};

export const healthCheck = async () => {
  const response = await api.get("/health/");
  return response.data;
};

export default api;
