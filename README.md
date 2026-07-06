# Phishing-URL-checker-
A beginner-friendly cybersecurity project that analyzes URLs and flags common phishing indicators using rule-based detection.

##Overview 

This project is a Python-based phishing URL checker built as a portfolio project for learning practical IT security concepts. It evaluates a user-provided URL, assigns a risk score, and explains why a link may be suspicious instead of returning only a simple yes/no result.

The goal is to build an explainable security tool that demonstrates secure thinking, basic threat detection, input validation, and clean project documentation.

## Features

- Analyze user-submitted URLs for common phishing patterns.
- Detect suspicious indicators such as raw IP addresses, excessive URL length, many subdomains, special characters, and risky keywords.
- Assign a simple risk score and verdict such as `Safe`, `Suspicious`, or `Likely Phishing`.
- Return human-readable reasons for the verdict.
- Provide a simple interface through the command line or a small web UI.
- Keep the logic modular so additional rules or APIs can be added later.

## Example Checks

The checker can include rules such as:

- URL uses an IP address instead of a domain.
- URL contains the `@` symbol.
- URL is unusually long.
- URL contains many subdomains.
- URL uses suspicious words such as `login`, `verify`, `secure`, `update`, or `account`.
- URL comes from a known shortening service.
- URL uses punycode or unusual character patterns.

## Project Structure

```text
phishing-url-checker/
├── app.py
├── analyzer.py
├── rules.py
├── tests/
├── requirements.txt
└── README.md
