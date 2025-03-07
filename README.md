
# MLOps Assignment 1

A simple Flask web application created as part of MLOps course assignment.

## Description

This is a basic Flask application that demonstrates routing and web server functionality. It includes:
- A root endpoint that returns "Hello, MLOps!"
- A custom endpoint `/abd` that returns a personal greeting

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mlops_assignment1.git
cd mlops_assignment1
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask
```

## Usage

To run the application:
```bash
python app.py
```

The server will start on `http://localhost:5000` with the following endpoints:
- `/` - Main greeting
- `/abd` - Personal greeting

## Development

The application runs in debug mode, allowing for automatic reloading when code changes are made.

