#!/usr/bin/env python3

import subprocess
import sys
import os

print("📦 Setting up your environment...")

# Create virtual environment
print("✅ Creating virtual environment...")
subprocess.run([sys.executable, "-m", "venv", "venv"])

# Activate venv and install Flask and SpaCy
print("⬇️  Installing Flask and SpaCy...")
venv_pip = os.path.join("venv", "bin", "pip")
subprocess.run([venv_pip, "install", "--no-cache-dir", "flask", "spacy"])

# Download SpaCy model
print("📥 Downloading SpaCy language model...")
venv_python = os.path.join("venv", "bin", "python")
subprocess.run([venv_python, "-m", "spacy", "download", "en_core_web_sm"])

# Launch the app
print("🚀 Launching app...")
subprocess.run([venv_python, "app/app.py"])
