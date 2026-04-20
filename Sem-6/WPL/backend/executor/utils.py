import subprocess
import tempfile
import os
import time
import ast
import json
from pathlib import Path


class CodeExecutor:
    """Execute code in different languages with timeout and safety measures."""
    
    TIMEOUT = 5  # seconds
    
    @staticmethod
    def execute_python(code, input_data=""):
        """Execute Python code and return output, error, and execution time."""
        start_time = time.time()
        
        try:
            # Create a temporary file for the code
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                temp_file = f.name
            
            # Create a temporary file for input
            input_file = None
            if input_data:
                with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
                    f.write(input_data)
                    input_file = f.name
            
            # Execute the code
            try:
                if input_file:
                    with open(input_file, 'r') as stdin:
                        result = subprocess.run(
                            ['python3', temp_file],
                            stdin=stdin,
                            capture_output=True,
                            text=True,
                            timeout=CodeExecutor.TIMEOUT
                        )
                else:
                    result = subprocess.run(
                        ['python3', temp_file],
                        capture_output=True,
                        text=True,
                        timeout=CodeExecutor.TIMEOUT
                    )
                
                execution_time = time.time() - start_time
                
                return {
                    'output': result.stdout,
                    'error': result.stderr,
                    'execution_time': execution_time
                }
            
            except subprocess.TimeoutExpired:
                return {
                    'output': '',
                    'error': f'Execution timed out after {CodeExecutor.TIMEOUT} seconds',
                    'execution_time': CodeExecutor.TIMEOUT
                }
            
            finally:
                # Clean up temp files
                os.unlink(temp_file)
                if input_file:
                    os.unlink(input_file)
        
        except Exception as e:
            return {
                'output': '',
                'error': str(e),
                'execution_time': time.time() - start_time
            }
    
    @staticmethod
    def execute_c(code, input_data=""):
        """Compile and execute C code."""
        start_time = time.time()
        
        try:
            # Create temporary files
            with tempfile.NamedTemporaryFile(mode='w', suffix='.c', delete=False) as f:
                f.write(code)
                source_file = f.name
            
            executable = source_file.replace('.c', '.out')
            
            # Compile
            compile_result = subprocess.run(
                ['gcc', source_file, '-o', executable],
                capture_output=True,
                text=True,
                timeout=CodeExecutor.TIMEOUT
            )
            
            if compile_result.returncode != 0:
                os.unlink(source_file)
                return {
                    'output': '',
                    'error': f'Compilation Error:\n{compile_result.stderr}',
                    'execution_time': time.time() - start_time
                }
            
            # Execute
            try:
                input_file = None
                if input_data:
                    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
                        f.write(input_data)
                        input_file = f.name
                
                if input_file:
                    with open(input_file, 'r') as stdin:
                        result = subprocess.run(
                            [executable],
                            stdin=stdin,
                            capture_output=True,
                            text=True,
                            timeout=CodeExecutor.TIMEOUT
                        )
                else:
                    result = subprocess.run(
                        [executable],
                        capture_output=True,
                        text=True,
                        timeout=CodeExecutor.TIMEOUT
                    )
                
                execution_time = time.time() - start_time
                
                return {
                    'output': result.stdout,
                    'error': result.stderr,
                    'execution_time': execution_time
                }
            
            except subprocess.TimeoutExpired:
                return {
                    'output': '',
                    'error': f'Execution timed out after {CodeExecutor.TIMEOUT} seconds',
                    'execution_time': CodeExecutor.TIMEOUT
                }
            
            finally:
                # Clean up
                os.unlink(source_file)
                if os.path.exists(executable):
                    os.unlink(executable)
                if input_file:
                    os.unlink(input_file)
        
        except Exception as e:
            return {
                'output': '',
                'error': str(e),
                'execution_time': time.time() - start_time
            }
    
    @staticmethod
    def execute_cpp(code, input_data=""):
        """Compile and execute C++ code."""
        start_time = time.time()
        
        try:
            # Create temporary files
            with tempfile.NamedTemporaryFile(mode='w', suffix='.cpp', delete=False) as f:
                f.write(code)
                source_file = f.name
            
            executable = source_file.replace('.cpp', '.out')
            
            # Compile
            compile_result = subprocess.run(
                ['g++', source_file, '-o', executable],
                capture_output=True,
                text=True,
                timeout=CodeExecutor.TIMEOUT
            )
            
            if compile_result.returncode != 0:
                os.unlink(source_file)
                return {
                    'output': '',
                    'error': f'Compilation Error:\n{compile_result.stderr}',
                    'execution_time': time.time() - start_time
                }
            
            # Execute
            try:
                input_file = None
                if input_data:
                    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
                        f.write(input_data)
                        input_file = f.name
                
                if input_file:
                    with open(input_file, 'r') as stdin:
                        result = subprocess.run(
                            [executable],
                            stdin=stdin,
                            capture_output=True,
                            text=True,
                            timeout=CodeExecutor.TIMEOUT
                        )
                else:
                    result = subprocess.run(
                        [executable],
                        capture_output=True,
                        text=True,
                        timeout=CodeExecutor.TIMEOUT
                    )
                
                execution_time = time.time() - start_time
                
                return {
                    'output': result.stdout,
                    'error': result.stderr,
                    'execution_time': execution_time
                }
            
            except subprocess.TimeoutExpired:
                return {
                    'output': '',
                    'error': f'Execution timed out after {CodeExecutor.TIMEOUT} seconds',
                    'execution_time': CodeExecutor.TIMEOUT
                }
            
            finally:
                # Clean up
                os.unlink(source_file)
                if os.path.exists(executable):
                    os.unlink(executable)
                if input_file:
                    os.unlink(input_file)
        
        except Exception as e:
            return {
                'output': '',
                'error': str(e),
                'execution_time': time.time() - start_time
            }
    
    @staticmethod
    def execute_java(code, input_data=""):
        """Compile and execute Java code."""
        start_time = time.time()
        
        try:
            # Extract class name from code
            import re
            class_match = re.search(r'public\s+class\s+(\w+)', code)
            if not class_match:
                return {
                    'output': '',
                    'error': 'Error: No public class found in code',
                    'execution_time': time.time() - start_time
                }
            
            class_name = class_match.group(1)
            
            # Create temporary directory for Java files
            temp_dir = tempfile.mkdtemp()
            source_file = os.path.join(temp_dir, f'{class_name}.java')
            
            with open(source_file, 'w') as f:
                f.write(code)
            
            # Compile
            compile_result = subprocess.run(
                ['javac', source_file],
                capture_output=True,
                text=True,
                timeout=CodeExecutor.TIMEOUT,
                cwd=temp_dir
            )
            
            if compile_result.returncode != 0:
                import shutil
                shutil.rmtree(temp_dir)
                return {
                    'output': '',
                    'error': f'Compilation Error:\n{compile_result.stderr}',
                    'execution_time': time.time() - start_time
                }
            
            # Execute
            try:
                input_file = None
                if input_data:
                    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
                        f.write(input_data)
                        input_file = f.name
                
                if input_file:
                    with open(input_file, 'r') as stdin:
                        result = subprocess.run(
                            ['java', class_name],
                            stdin=stdin,
                            capture_output=True,
                            text=True,
                            timeout=CodeExecutor.TIMEOUT,
                            cwd=temp_dir
                        )
                else:
                    result = subprocess.run(
                        ['java', class_name],
                        capture_output=True,
                        text=True,
                        timeout=CodeExecutor.TIMEOUT,
                        cwd=temp_dir
                    )
                
                execution_time = time.time() - start_time
                
                return {
                    'output': result.stdout,
                    'error': result.stderr,
                    'execution_time': execution_time
                }
            
            except subprocess.TimeoutExpired:
                return {
                    'output': '',
                    'error': f'Execution timed out after {CodeExecutor.TIMEOUT} seconds',
                    'execution_time': CodeExecutor.TIMEOUT
                }
            
            finally:
                # Clean up
                import shutil
                shutil.rmtree(temp_dir)
                if input_file:
                    os.unlink(input_file)
        
        except Exception as e:
            return {
                'output': '',
                'error': str(e),
                'execution_time': time.time() - start_time
            }


class ASTGenerator:
    """Generate Abstract Syntax Tree for Python code."""
    
    @staticmethod
    def generate_ast(code):
        """Parse Python code and return AST as JSON."""
        try:
            tree = ast.parse(code)
            return {
                'success': True,
                'ast': ASTGenerator._ast_to_dict(tree)
            }
        except SyntaxError as e:
            return {
                'success': False,
                'error': f'Syntax Error at line {e.lineno}: {e.msg}'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    @staticmethod
    def _ast_to_dict(node):
        """Convert AST node to dictionary representation."""
        if isinstance(node, ast.AST):
            result = {
                'type': node.__class__.__name__,
                'fields': {}
            }
            
            for field, value in ast.iter_fields(node):
                if isinstance(value, list):
                    result['fields'][field] = [ASTGenerator._ast_to_dict(item) for item in value]
                else:
                    result['fields'][field] = ASTGenerator._ast_to_dict(value)
            
            # Add position info if available
            if hasattr(node, 'lineno'):
                result['lineno'] = node.lineno
            if hasattr(node, 'col_offset'):
                result['col_offset'] = node.col_offset
            
            return result
        else:
            return node
    
    @staticmethod
    def generate_c_ast(code):
        """Generate AST for C code using tree-sitter."""
        try:
            from tree_sitter import Language, Parser
            import tree_sitter_c
            
            # Create parser for C
            C_LANGUAGE = Language(tree_sitter_c.language())
            parser = Parser(C_LANGUAGE)
            
            # Parse the code
            tree = parser.parse(bytes(code, 'utf8'))
            root_node = tree.root_node
            
            # Convert to dictionary
            ast_dict = ASTGenerator._tree_sitter_to_dict(root_node, code)
            
            return {
                'success': True,
                'ast': ast_dict
            }
            
        except ImportError as e:
            return {
                'success': False,
                'error': f'tree-sitter-c not installed. Run: pip install tree-sitter tree-sitter-c'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    @staticmethod
    def generate_cpp_ast(code):
        """Generate AST for C++ code using tree-sitter."""
        try:
            from tree_sitter import Language, Parser
            import tree_sitter_cpp
            
            # Create parser for C++
            CPP_LANGUAGE = Language(tree_sitter_cpp.language())
            parser = Parser(CPP_LANGUAGE)
            
            # Parse the code
            tree = parser.parse(bytes(code, 'utf8'))
            root_node = tree.root_node
            
            # Convert to dictionary
            ast_dict = ASTGenerator._tree_sitter_to_dict(root_node, code)
            
            return {
                'success': True,
                'ast': ast_dict
            }
            
        except ImportError as e:
            return {
                'success': False,
                'error': f'tree-sitter-cpp not installed. Run: pip install tree-sitter tree-sitter-cpp'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    @staticmethod
    def _tree_sitter_to_dict(node, source_code):
        """Convert tree-sitter node to dictionary."""
        result = {
            'type': node.type,
            'start_point': {'row': node.start_point[0], 'column': node.start_point[1]},
            'end_point': {'row': node.end_point[0], 'column': node.end_point[1]},
        }
        
        # Add text for leaf nodes
        if node.child_count == 0:
            result['text'] = source_code[node.start_byte:node.end_byte]
        
        # Add children
        if node.child_count > 0:
            result['children'] = []
            for child in node.children:
                result['children'].append(ASTGenerator._tree_sitter_to_dict(child, source_code))
        
        # Add named children for easier navigation
        if node.named_child_count > 0:
            result['named_children_count'] = node.named_child_count
        
        return result
    
    @staticmethod
    def generate_java_ast(code):
        """Generate AST for Java code using javalang."""
        try:
            import javalang
            
            # Parse the Java code
            tree = javalang.parse.parse(code)
            
            # Convert to dictionary
            ast_dict = ASTGenerator._javalang_to_dict(tree)
            
            return {
                'success': True,
                'ast': ast_dict
            }
            
        except ImportError:
            return {
                'success': False,
                'error': 'javalang not installed. Run: pip install javalang'
            }
        except javalang.parser.JavaSyntaxError as e:
            return {
                'success': False,
                'error': f'Java syntax error: {str(e)}'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    @staticmethod
    def _javalang_to_dict(node):
        """Convert javalang AST node to dictionary."""
        if node is None:
            return None
        
        # Handle different types
        if isinstance(node, str):
            return node
        elif isinstance(node, (int, float, bool)):
            return node
        elif isinstance(node, list):
            return [ASTGenerator._javalang_to_dict(item) for item in node]
        elif isinstance(node, set):
            return list(node)
        
        # Handle javalang nodes
        if hasattr(node, 'attrs'):
            result = {
                'type': node.__class__.__name__
            }
            
            # Add position info if available
            if hasattr(node, 'position') and node.position:
                result['line'] = node.position.line
                result['column'] = node.position.column
            
            # Add all attributes
            for attr in node.attrs:
                value = getattr(node, attr, None)
                if value is not None:
                    result[attr] = ASTGenerator._javalang_to_dict(value)
            
            return result
        
        return str(node)
