
# DJ Song Tracker (Satire App)

## Overview

This is a satire, one-feature app that I created to track how many times I play specific songs while DJing. The app provides three buttons to track the number of plays for:
- "The Dougie"
- "No Hands"
- "FE!N"

It saves the play counts in a local file on my computer, so the data persists between sessions. The app is primarily used for humor and as a personal learning exercise.

## Purpose

The main goals behind creating this app are:
- **Port Forwarding**: I used this project to learn and practice how to set up port forwarding, allowing me to access services hosted on my computer from outside my local network.
- **Front-End Refresh**: This project was also a way to refresh my skills on basic front-end tools, such as:
  - **HTML**
  - **CSS**
  - **Bootstrap** for responsive and clean UI design.

## Features
- Three buttons to increment the play count of each song.
- Play counts are saved in a file, ensuring data persists even if the app is restarted.
- Simple, responsive design using Bootstrap.
- Hosted locally on my computer, with access enabled through port forwarding for remote usage.

## How to Run the App
1. Clone the repository.
2. Create a virtual environment and install Flask.
   ```
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate   # For Windows
   pip install flask
   ```
3. Run the app.
   ```
   python app.py
   ```
4. Access the app in your browser at `http://127.0.0.1:5000/`.

## Notes
This app is purely for fun and educational purposes! I built it to better understand how to host services on my computer and experiment with basic web development tools.
