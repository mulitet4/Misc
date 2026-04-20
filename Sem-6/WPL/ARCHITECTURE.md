# CodeBrew - Multi-Language Code Execution Lab

> A powerful web-based code execution platform supporting Python, C, C++, and Java with real-time output and AST visualization

## System Overview

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Browser   │ ◄─────► │   Next.js    │ ◄─────► │   Django    │
│   (User)    │  HTTP   │   Frontend   │   API   │   Backend   │
└─────────────┘         └──────────────┘         └─────────────┘
                              │                         │
                              │                         │
                        ┌─────▼──────┐           ┌─────▼──────┐
                        │  Monaco    │           │  Code      │
                        │  Editor    │           │  Executor  │
                        └────────────┘           └─────────────┘
                                                        │
                                                        │
                                                  ┌─────▼──────┐
                                                  │ Python/    │
                                                  │ GCC/G++    │
                                                  │ Subprocess │
                                                  └────────────┘
```

## Backend Architecture (Django)

### Components

1. **API Layer** (`executor/views.py`)
   - REST API endpoints
   - Request validation
   - Response formatting

2. **Execution Engine** (`executor/utils.py`)
   - `CodeExecutor`: Handles Python, C, C++, Java execution
   - `ASTGenerator`: Generates AST for all supported languages
     - Python: Built-in `ast` module
     - C: `tree-sitter-c` parser
     - C++: `tree-sitter-cpp` parser
     - Java: `javalang` library
   - Timeout management
   - Temporary file handling

3. **Data Layer** (`executor/models.py`)
   - `CodeExecution` model
   - Execution history storage
   - Audit trail

### API Endpoints

| Endpoint        | Method | Purpose               |
| --------------- | ------ | --------------------- |
| `/api/execute/` | POST   | Execute code          |
| `/api/ast/`     | POST   | Generate AST          |
| `/api/history/` | GET    | Get execution history |
| `/api/health/`  | GET    | Health check          |

### Code Execution Flow

```
Request → Validation → Language Detection → Create Temp File
                                                    │
                                                    ▼
Response ◄── Format Results ◄── Capture Output ◄── Execute
```

## Frontend Architecture (Next.js)

### Components Structure

```
app/
├── layout.tsx          # Root layout
├── page.tsx           # Main page
└── globals.css        # Global styles

components/
├── CodeEditor.tsx     # Main editor component
├── ASTViewer.tsx      # AST visualization
└── ui/               # shadcn/ui components
    ├── button.tsx
    ├── card.tsx
    ├── tabs.tsx
    └── textarea.tsx

lib/
├── api.ts            # API client
└── utils.ts          # Utilities
```

### State Management

```typescript
// CodeEditor Component State
- language: Current programming language
- code: Code in editor
- input: stdin input
- output: Execution output
- error: Error messages
- executionTime: Performance metric
- astData: AST structure
- loading: UI state
```

### Data Flow

```
User Input → Monaco Editor → State Update → API Call
                                               │
                                               ▼
Display Results ◄── State Update ◄── API Response
```

## Technology Stack Details

### Backend Stack

- **Django 4.2**: Web framework
- **Django REST Framework**: API framework
- **SQLite**: Database (can be swapped for PostgreSQL)
- **Python subprocess**: Code execution
- **CORS Headers**: Cross-origin support
- **tree-sitter**: C/C++ AST parsing
- **javalang**: Java AST parsing
- **pycparser**: Alternative C parsing (legacy)

### Frontend Stack

- **Next.js 14**: React framework with App Router
- **TypeScript**: Type safety
- **TailwindCSS**: Utility-first CSS
- **shadcn/ui**: Component library
- **Monaco Editor**: VS Code's editor
- **Axios**: HTTP client
- **Lucide React**: Icons

## Security Features

1. **Timeout Protection**: 5-second execution limit
2. **Temporary Files**: Automatic cleanup
3. **Isolated Execution**: Each execution in separate process
4. **CORS**: Restricted to localhost
5. **Input Validation**: Request validation with DRF

## Performance Considerations

1. **Editor**: Monaco lazy loading
2. **API**: RESTful endpoints
3. **Database**: Indexed queries
4. **Execution**: Process pooling possible
5. **Frontend**: Next.js automatic optimization

## Extensibility

### Adding New Languages

1. Add language to `LANGUAGE_CHOICES` in models.py
2. Implement executor method in `CodeExecutor` class (utils.py)
3. Implement AST generator method in `ASTGenerator` class (utils.py)
4. Add language to `ExecuteCodeSerializer` choices
5. Update language options in frontend (`CodeEditor.tsx`)
6. Add default code example to `DEFAULT_CODE`
7. Update Monaco language support and serializers

### Adding Features

- **Code Formatting**: Add prettier/black integration
- **Code Linting**: Integrate pylint/eslint
- **Collaboration**: Add WebSocket support
- **File Upload**: Support multi-file projects
- **Themes**: Add dark/light mode toggle

## Database Schema

```sql
CodeExecution
├── id (PK)
├── language (VARCHAR)  -- 'python', 'c', 'cpp', 'java'
├── code (TEXT)
├── input_data (TEXT)
├── output (TEXT)
├── error (TEXT)
├── execution_time (FLOAT)
└── created_at (TIMESTAMP)
```

## Language Support

### Supported Languages

| Language | Compiler/Interpreter | AST Parser      | Features                            |
| -------- | -------------------- | --------------- | ----------------------------------- |
| Python   | python3              | Built-in `ast`  | Full support, native AST            |
| C        | gcc                  | tree-sitter-c   | Syntax tree with position info      |
| C++      | g++                  | tree-sitter-cpp | Syntax tree with position info      |
| Java     | javac + java         | javalang        | Full Java parser with semantic info |

### Execution Process

#### Python

1. Write code to temporary `.py` file
2. Execute with `python3`
3. Capture stdout/stderr
4. Parse AST using built-in `ast.parse()`

#### C

1. Write code to temporary `.c` file
2. Compile with `gcc -o executable`
3. Execute binary
4. Parse AST using `tree-sitter-c`

#### C++

1. Write code to temporary `.cpp` file
2. Compile with `g++ -o executable`
3. Execute binary
4. Parse AST using `tree-sitter-cpp`

#### Java

1. Extract public class name from code
2. Create temporary directory
3. Write code to `ClassName.java`
4. Compile with `javac`
5. Execute with `java ClassName`
6. Parse AST using `javalang.parse()`
7. Clean up temporary directory

## Deployment Considerations

### Backend

- Use Gunicorn/uWSGI
- PostgreSQL for production
- Docker containerization
- Environment variables
- Nginx reverse proxy

### Frontend

- Vercel/Netlify deployment
- Environment variables
- CDN for static assets
- SSR/SSG optimization

### Security

- Sandbox code execution (Docker/VM)
- Rate limiting
- User authentication
- Code size limits
- Resource constraints

---

For implementation details, see the source code and README.md
