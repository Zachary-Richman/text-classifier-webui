#!/bin/bash

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed."
    exit 1
else
    echo "Python3 is installed."
fi

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "ERROR: Git is not installed."
    exit 1
else
    echo "Git is installed."
fi

# Clone the repository if it doesn't exist
REPO_URL="https://www.github.com/Zachary-Richman/text-classifier-webui"
REPO_DIR="text-classifier-webui"

if [ -d "$REPO_DIR" ]; then
    echo "Repository '$REPO_DIR' already exists. Skipping clone."
else
    git clone "$REPO_URL"
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to clone the repository."
        exit 1
    fi
    echo "Repository cloned successfully."
fi

# Navigate to the repository
cd "$REPO_DIR" || { echo "ERROR: Failed to enter the directory '$REPO_DIR'."; exit 1; }

# Create and activate the virtual environment
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "Virtual environment created."
fi

source ./.venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to activate the virtual environment."
    exit 1
fi
echo "Virtual environment activated."

# Install dependencies
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies."
    exit 1
fi

# List installed packages
pip list

echo "Setup completed successfully."

