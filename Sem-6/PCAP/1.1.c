#include <stdio.h>
#include <cuda_runtime.h>

__global__ void vecadd(int* a, int* b, int* c, int N){
  int i = threadIdx.x;
  if (i < N) c[i] = a[i] + b[i];
}

int main(){
  int N = 1024;
  int threads = 256;
  int blocks = (N + threads - 1) / threads; // Ceiling operation
  
  size_t size = sizeof(float) * N;
  float *h_a = (float*) malloc(size);
  float *h_b = (float*) malloc(size);
  float *h_c = (float*) malloc(size);

  for(int i = 0; i < N; i++){
    scanf("%d", &h_a[i]);
    h_b[i] = h_a[i];
  }

  int *d_a, *d_b, *d_c;
  cudaMalloc(&d_a, size);
  cudaMalloc(&d_b, size);
  cudaMalloc(&d_c, size);

  cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
  cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);
  
  vecadd<<<1, N>>>(d_a, d_b, d_c,N);

  cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost);
  // print sresult
}

__global__ void sineKernel(float* in, float* out, int N){
  int i = blockIdx.x * blockDim.x + threadIdx.x;
  if(i < N) out[i] = sinf(in[i]);
}

// int threads = 256
// int N = 2000
// int blocks = (N + threads - 1) / threads
// sineKernel<<<blocks, threads>>>(in, out, N)


__global__ void convolution1D(float* N, float* M, float* P, int width, int m_width){
  int i = blockIdx.x * blockDim.x + threadIdx.x;
  if(i < width){
    float sum = 0;
    int half = m_width / 2;
    for(int j = 0; j < mask_width; j++){
      int index = (i - half) + j;
      if(index >= 0 && index < width){
        sum += N[index] + M[j];
      }
    }
    P[i] = sum;
  }
}

__global__ void selectionSort(int* in, int* out, int n){
  int i = threadIdx.x + blockIdx.x + blockDim.x;
  if(i < N){
    int count = 0;
    int val = in[i];
    for(int j = 0; j < N; j++){
      int other = input[j];
      if(other < val || (other == val && j < i)) count++;
      out[count] = val;
    }
  }
}

__global__ void countOccurrences(char* str, char* word, int str_len, int word_len, int* count){
  int i = blockIdx.x * blockDim.x +  threadIdx.x;
  if(i <= str_len - word_len){
    for(int j = 0; j < word_len; j++){
      if (str[i + j] != word[j]) return;
    }
    atomicAdd(count)
  }
}


// int* d_count
// scanf("%[^\n]%*c", str)
// cudaMalloc(*d_count, sizeof(int))


__global__ void produceString(char* S, char* RS, int N){
  int i = blockIdx.x * blockDim.x + threadIdx.x;
  int total_len = (N*(N+1))/2; //formula for Sum(N^2)
  if(i < total_len){
    int current_row_start = 0;
    int char_in_row = N;
    for(int level = 0; level < N; level++){
      if(i < (current_row_start + char_in_row)){
        int col = i - current_row_start;
        RS[i] = S[col];
        return;
      }
      current_row_start += char_in_row;
      char_in_row--;
    }
  }
}

// Output
// In: Aaryan
// Out: AaryanAaryaAaryAarAaA


// every row by 1 thread
__global__ void matAddA(float* A, float* B, float* C, int N){
  int i = threadIdx.x;
  if (i < N){
    for(int j = 0; j < N; j++){
      int idx = i * N + j;
      c[idx] = a[idx] + b[idx];
    }
  }
}

// every col by 1 thread
__global__ void matAddB(float* A, float* B, float* C, int N){
  int i = threadIdx.x;
  if(i < N){
    for(int j = 0; j < N; j++){
      int idx = j * N + i;
      c[idx] = a[idx] + b[idx];
    }
  }
}

// every element by 1 thread, 2D block
__global__ void matAddC(float* A, float* B, float* C, int N){
  int i = threadIdx.x;
  int j = threadIdx.y;
  if(i < N && j < N){
    idx = i * N + j;
    c[idx] = a[idx] + b[idx];
  }
}


// mul every row by 1 thread
__global__ void matAddA(float* A, float* B, float* C, int N, int H, int M){
  int i = threadIdx.x;
  if(i < N){
    for(int j = 0; j < M; j++){
      sum = 0;
      idx = i * M + j;
      for(int k = 0; k < H; k++){
        sum += A[i * H + k] * B[k * M + j]
      }
      C[idx] = sum;
    }
  }
}

// mul every col by 1 thread
__global__ void matAddB(float* A, float* B, float* C, int N, int H, int M){
int j = threadIdx.x;
  if(j < M){
    for(int i = 0; i < N; j++){
      sum = 0;
      idx = i * M + j;
      for(int k = 0; k < H; k++){
        sum += A[i * H + k] * B[k * M + j]
      }
      C[idx] = sum;
    }
  }
}

// mul every element by 1 thread
__global__ void matAddC(float* A, float* B, float* C, int N, int H, int M){
  int i = threadIdx.x;
  int j = threadIdx.y;
  if(i < N && j < M){
    sum = 0;
    for(int k = 0; k < H; k++){
      sum += A[i * H + k] * B[k * M + j];
    }
    C[i * M + j] = sum;
  }
}


__global__ void csrspmv(int n_rows, float* values,)