from rest_framework import serializers
from .models import CodeExecution


class CodeExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeExecution
        fields = ['id', 'language', 'code', 'input_data', 'output', 'error', 'execution_time', 'created_at']
        read_only_fields = ['id', 'output', 'error', 'execution_time', 'created_at']


class ExecuteCodeSerializer(serializers.Serializer):
    language = serializers.ChoiceField(choices=['python', 'c', 'cpp', 'java'])
    code = serializers.CharField()
    input_data = serializers.CharField(required=False, allow_blank=True)
