# CNAME Checker Tool

A Python CLI utility to check CNAME records for lists of subdomains with colorful output and professional ASCII art banner.

## Features

- Checks CNAME records for multiple subdomains
- Color-coded output for easy reading
- Professional ASCII art banner
- Handles large lists of subdomains
- Cross-platform (works on Windows, Linux, macOS)
- Comprehensive error handling

## Requirements

- Python 3.6+
- External dependencies listed in `requirements.txt`

## Installation

1. Clone the repository or download the script
2. Install required modules:

```bash
pip install -r requirements.txt
```

## Usage
```
python cname_checker.py
```
When prompted, enter the path to your subdomains file.

## Subdomains File Format
Create a text file with one subdomain per line:
```
sub1.example.com
sub2.example.com
test.site.org
```