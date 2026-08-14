Web Security Scanner

A lightweight Python-based web scanner for basic website reconnaissance and security checks.

Features
Website connectivity check
Response time measurement
HTTP status code detection
Security header detection
robots.txt and sitemap.xml checks
Common directory detection
CMS detection for popular platforms
Basic request error handling
Requirements
Python 3.x
requests
Installation

Clone the repository:

git clone https://github.com/0xtutela/WebScanner.git
cd WebScanner

Install the required dependency:

pip install -r requirements.txt
Usage

Run the main program:

python run.py

Enter the website URL when prompted.

The scanner will perform the available checks and display the results in the terminal.

Project Structure
.
├── run.py
├── connect.py
├── headers.py
├── directories_scan.py
├── CMS_detector.py
├── requirements.txt
└── README.md
Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Only scan websites and systems that you own or have explicit permission to test.
