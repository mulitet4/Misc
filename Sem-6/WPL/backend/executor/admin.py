from django.contrib import admin
from .models import CodeExecution


@admin.register(CodeExecution)
class CodeExecutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'language', 'created_at', 'execution_time']
    list_filter = ['language', 'created_at']
    search_fields = ['code', 'output', 'error']
    readonly_fields = ['created_at']
