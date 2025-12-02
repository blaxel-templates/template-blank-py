# Blaxel Agent Template (Python)

<p align="center">
  <img src="https://blaxel.ai/logo.png" alt="Blaxel" width="200"/>
</p>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-ready-green.svg)](https://fastapi.tiangolo.com/)

</div>

A minimal Python template for a Blaxel-hosted agent. It includes a small FastAPI server, optional telemetry, and ready-to-use commands for local development and deployment on Blaxel.

## 📑 Table of Contents

- [Blaxel Agent Template (Python)](#blaxel-agent-template-python)
  - [📑 Table of Contents](#-table-of-contents)
  - [✨ Features](#-features)
  - [🚀 Quick Start](#-quick-start)
  - [📋 Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
  - [🔧 Usage](#-usage)
    - [Running the Server Locally](#running-the-server-locally)
    - [Testing your agent](#testing-your-agent)
    - [Deploying to Blaxel](#deploying-to-blaxel)
  - [📁 Project Structure](#-project-structure)
  - [❓ Troubleshooting](#-troubleshooting)
    - [Common Issues](#common-issues)
  - [👥 Contributing](#-contributing)
  - [🆘 Support](#-support)
  - [📄 License](#-license)

## ✨ Features

- Minimal FastAPI server (Hello World)
- Python-first setup
- Optional Blaxel telemetry via OpenTelemetry FastAPI instrumentation
- Hot reload for local development
- One-command deploy to Blaxel

## 🚀 Quick Start

For those who want to get up and running quickly:

```bash
# Clone the repository
git clone https://github.com/blaxel-templates/template-blank-py.git

# Navigate to the project directory
cd template-blank-py

# Install dependencies
uv sync

# Start the server (hot reload)
bl serve --hotreload
```

## 📋 Prerequisites

- **Python:** 3.10 or later
- **UV:** UV package manager
- **Blaxel Platform Setup:** Complete Blaxel setup by following the Quickstart
  - **Blaxel CLI:** Ensure you have the Blaxel CLI installed. If not, install it globally:
    ```bash
    curl -fsSL https://raw.githubusercontent.com/blaxel-ai/toolkit/main/install.sh | BINDIR=/usr/local/bin sudo -E sh
    ```
  - **Blaxel login:** Login to Blaxel platform
    ```bash
    bl login YOUR-WORKSPACE
    ```

## 💻 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/blaxel-templates/template-blank-py.git
cd template-blank-py
uv sync
```

## 🔧 Usage

### Running the Server Locally

Start the development server with hot reloading:

```bash
bl serve --hotreload
```

The server listens on the host and port provided by Blaxel, already implemented in `src/__main__.py`:

```ts
port = os.getenv("PORT", "80")
host = os.getenv("HOST", "0.0.0.0")
```

### Testing your agent

You can test your agent with curl:

```bash
curl -X POST http://127.0.0.1:1338/ \
  -H "content-type: application/json" \
  -d '{"inputs":"hello"}'
```

### Deploying to Blaxel

When you are ready to deploy your application:

```bash
bl deploy
```

This will package your code using your configuration and deploy it as a serverless endpoint on Blaxel. See the Quickstart for details: https://docs.blaxel.ai/Agents/Quickstart-agent

## 📁 Project Structure

- **src/main.py** - Application entry point and HTTP route(s)
- **src/__main__.py** - Uvicorn startup script (prod/dev)
- **src/middleware.py** - Correlation IDs and request logging
- **src/error.py** - Error handlers
- **pyproject.toml** - Python project config and dependencies
- **uv.lock** - UV lockfile
- **blaxel.toml** - Blaxel deployment configuration

## ❓ Troubleshooting

### Common Issues

1. **Blaxel Platform Issues**:
   - Ensure you're logged in to your workspace: `bl login MY-WORKSPACE`
   - Verify deployment: `bl deploy` outputs an endpoint URL in the console

2. **Python / UV Issues**:
   - Make sure you have Python 3.10+
   - Ensure `uv` is installed and on PATH (`uv --version`)

3. **Application Errors**:
   - Check Uvicorn/FastAPI startup logs
   - Verify imports in `src/main.py`

4. **Local Serve Issues**:
   - If port 1338 is taken, change the dev entrypoint port in `blaxel.toml`
   - Check console logs for FastAPI/Uvicorn errors

## 👥 Contributing

Contributions are welcome! Here's how you can contribute:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes:
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Submit** a Pull Request

Please make sure to follow the Python code style of the project (ruff is configured).

## 🆘 Support

If you need help with this template:

- [Submit an issue](https://github.com/blaxel-templates/template-blank-py/issues) for bug reports or feature requests
- Visit the [Blaxel Documentation](https://docs.blaxel.ai) for platform guidance
- Join our [Discord Community](https://discord.gg/G3NqzUPcHP) for real-time assistance

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
