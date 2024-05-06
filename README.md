# R34 Video Downloader

The R34 Video Downloader is a Python application designed to automate the downloading of MP4 videos from the Rule34 platform. It ensures that no video is downloaded more than once by maintaining a record of downloaded videos in a SQLite database.

## Features

- **Video Downloading**: Automatically download MP4 videos from Rule34.
- **Duplicate Avoidance**: Check against a local SQLite database to ensure videos are not downloaded multiple times.
- **Simple and Robust**: Easy to set up and use with robust error handling.

## Prerequisites

Before you can run this script, make sure you have Python installed on your machine. The script has been tested with Python 3.8 and above. You will also need the `requests` library to handle HTTP requests and `sqlite3` which is included in the Python standard library.

## Installation

To get started with the R34 Video Downloader, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/r34-video-downloader.git
   cd r34-video-downloader
2. Execute the main:
   ```
   python3 main.py
