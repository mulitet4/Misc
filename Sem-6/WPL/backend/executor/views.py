from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CodeExecution
from .serializers import CodeExecutionSerializer, ExecuteCodeSerializer
from .utils import CodeExecutor, ASTGenerator


@api_view(['POST'])
def execute_code(request):
    """Execute code in specified language and return results."""
    serializer = ExecuteCodeSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    language = serializer.validated_data['language']
    code = serializer.validated_data['code']
    input_data = serializer.validated_data.get('input_data', '')
    
    # Execute code based on language
    if language == 'python':
        result = CodeExecutor.execute_python(code, input_data)
    elif language == 'c':
        result = CodeExecutor.execute_c(code, input_data)
    elif language == 'cpp':
        result = CodeExecutor.execute_cpp(code, input_data)
    elif language == 'java':
        result = CodeExecutor.execute_java(code, input_data)
    else:
        return Response(
            {'error': 'Unsupported language'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Save execution to database
    execution = CodeExecution.objects.create(
        language=language,
        code=code,
        input_data=input_data,
        output=result['output'],
        error=result['error'],
        execution_time=result['execution_time']
    )
    
    return Response({
        'id': execution.id,
        'output': result['output'],
        'error': result['error'],
        'execution_time': result['execution_time'],
        'created_at': execution.created_at
    })


@api_view(['POST'])
def generate_ast(request):
    """Generate AST for code in any supported language."""
    code = request.data.get('code', '')
    language = request.data.get('language', 'python')
    
    if not code:
        return Response(
            {'error': 'No code provided'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Generate AST based on language
    if language == 'python':
        result = ASTGenerator.generate_ast(code)
    elif language == 'c':
        result = ASTGenerator.generate_c_ast(code)
    elif language == 'cpp':
        result = ASTGenerator.generate_cpp_ast(code)
    elif language == 'java':
        result = ASTGenerator.generate_java_ast(code)
    else:
        return Response(
            {'error': 'Unsupported language'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    return Response(result)


@api_view(['GET'])
def execution_history(request):
    """Get execution history."""
    executions = CodeExecution.objects.all()[:20]  # Last 20 executions
    serializer = CodeExecutionSerializer(executions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def health_check(request):
    """Health check endpoint."""
    return Response({'status': 'ok', 'message': 'Code Execution API is running'})
