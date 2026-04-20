# Code Execution Lab - Web Development Project

A full-stack web application for executing Python, C, and C++ code with real-time output, syntax highlighting, and AST (Abstract Syntax Tree) visualization.

## Features

- 🚀 **Multi-language Support**: Execute Python, C, and C++ code
- 💻 **Monaco Editor**: Syntax highlighting and code editing
- ⚡ **Real-time Execution**: Instant code execution with performance metrics
- 🌳 **AST Visualization**: Interactive Abstract Syntax Tree viewer for Python
- 🎨 **Modern UI**: Built with TailwindCSS and shadcn/ui components
- 📊 **Execution History**: Track your code execution history
- ⏱️ **Performance Metrics**: Execution time tracking

## Tech Stack

### Backend
- **Django 4.2** - Python web framework
- **Django REST Framework** - RESTful API
- **SQLite** - Database
- **Python subprocess** - Code execution

### Frontend
- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **TailwindCSS** - Styling
- **shadcn/ui** - UI components
- **Monaco Editor** - Code editor
- **Axios** - HTTP client

## Project Structure

```
WPL/
├── backend/                 # Django backend
│   ├── config/             # Django settings
│   ├── executor/           # Code execution app
│   │   ├── models.py       # Database models
│   │   ├── views.py        # API endpoints
│   │   ├── serializers.py  # DRF serializers
│   │   ├── utils.py        # Code execution logic
│   │   └── urls.py         # URL routing
│   ├── manage.py
│   └── requirements.txt
│
└── frontend/               # Next.js frontend
    ├── app/               # App router
    │   ├── page.tsx       # Home page
    │   ├── layout.tsx     # Root layout
    │   └── globals.css    # Global styles
    ├── components/        # React components
    │   ├── ui/           # shadcn/ui components
    │   ├── CodeEditor.tsx
    │   └── ASTViewer.tsx
    ├── lib/              # Utilities
    │   ├── api.ts        # API client
    │   └── utils.ts      # Helper functions
    └── package.json
```

## Prerequisites

- **Python 3.8+** (with pip)
- **Node.js 18+** (with npm)
- **GCC/G++** compiler (for C/C++ execution)

### Installing GCC/G++ on macOS
```bash
xcode-select --install
# Or install via Homebrew
brew install gcc
```

### Installing GCC/G++ on Linux
```bash
sudo apt-get update
sudo apt-get install build-essential
```

## Setup Instructions

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional, for admin access)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

The backend will be available at `http://localhost:8000`

### 2. Frontend Setup

```bash
# Open a new terminal
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

### Execute Code
**POST** `/api/execute/`
```json
{
  "language": "python|c|cpp",
  "code": "print('Hello World')",
  "input_data": "optional input"
}
```

**Response:**
```json
{
  "id": 1,
  "output": "Hello World\n",
  "error": "",
  "execution_time": 0.023,
  "created_at": "2026-04-04T12:00:00Z"
}
```

### Generate AST (Python only)
**POST** `/api/ast/`
```json
{
  "code": "def hello(): print('world')"
}
```

**Response:**
```json
{
  "success": true,
  "ast": { /* AST structure */ }
}
```

### Execution History
**GET** `/api/history/`

Returns the last 20 code executions.

### Health Check
**GET** `/api/health/`

Check if the API is running.

## Usage

1. **Select Language**: Choose Python, C, or C++ from the language selector
2. **Write Code**: Use the Monaco editor to write your code
3. **Add Input**: Provide stdin input in the input textarea (if needed)
4. **Execute**: Click "Run Code" to execute
5. **View Results**: See output, errors, and execution time
6. **AST Viewer**: For Python code, click "AST" to visualize the syntax tree

## Example Code

### Python
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial(number)}")
```

### C
```c
#include <stdio.h>

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    printf("Factorial of %d is %d\n", number, factorial(number));
    return 0;
}
```

### C++
```cpp
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
}
```

## Security Considerations

⚠️ **Important**: This application executes arbitrary code. Current security measures:

- **Timeout**: 5-second execution limit
- **Temporary Files**: Code runs in temporary files that are deleted after execution
- **Local Only**: Designed for local/lab use only

**For Production**:
- Use Docker containers with resource limits
- Implement code sandboxing
- Add user authentication
- Rate limiting
- Input validation and sanitization

## Development

### Backend Development

```bash
# Run tests
python manage.py test

# Create migrations
python manage.py makemigrations

# Access admin panel
# http://localhost:8000/admin
```

### Frontend Development

```bash
# Type checking
npm run type-check

# Linting
npm run lint

# Build for production
npm run build
```

## Troubleshooting

### GCC/G++ not found
Install build tools for your operating system (see Prerequisites).

### Port already in use
- Backend: Change port with `python manage.py runserver 8001`
- Frontend: Change port with `npm run dev -- -p 3001`

### CORS errors
Ensure Django CORS settings in `backend/config/settings.py` include your frontend URL.

### Module not found errors
- Backend: Activate virtual environment and reinstall dependencies
- Frontend: Delete `node_modules` and run `npm install` again

## License

MIT License - Feel free to use this project for educational purposes.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- Built for Web Programming Lab coursework
- Uses Monaco Editor (VS Code's editor)
- UI components from shadcn/ui
- Code execution inspired by online IDEs

---

**Note**: This is a educational project. Do not deploy to production without implementing proper security measures.
