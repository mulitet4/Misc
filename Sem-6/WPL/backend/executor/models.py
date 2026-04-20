from django.db import models


class CodeExecution(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('c', 'C'),
        ('cpp', 'C++'),
        ('java', 'Java'),
    ]
    
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    code = models.TextField()
    input_data = models.TextField(blank=True, null=True)
    output = models.TextField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    execution_time = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.language} - {self.created_at}"
