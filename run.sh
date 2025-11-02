#!/bin/bash

# Exit immediately if any command fails
set -e

# Activate conda environment
if [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
    source /opt/anaconda3/etc/profile.d/conda.sh
    conda activate courtroom_ai
else
    echo "Conda not found. Please activate your environment manually."
    exit 1
fi

echo "✅ Environment activated."

# Install required packages
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt || {
    echo "⚠️ Failed to install from requirements.txt. Installing individually."
    python -m pip install spacy nltk pandas numpy matplotlib tqdm datasets
}

# Download NLP models
echo "📥 Downloading spaCy and NLTK data..."
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt wordnet brown averaged_perceptron_tagger omw-1.4

# Run the script (use relative path)
echo "🚀 Launching VerdictIQ NLP engine..."
python notebook/verdict_iq.py
