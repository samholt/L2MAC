#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python could not be found, please install Python 3."
    exit
fi

# Install required Python packages
pip install -r requirements.txt

# Run the Blackjack game
python3 blackjack.py

