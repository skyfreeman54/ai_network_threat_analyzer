# AI-Powered Intrusion Detection and Threat Analysis System

## Overview
This project is a cybersecurity prototype that combines Wireshark packet captures, Python automation, and the OpenAI API to analyze network traffic for suspicious behavior. Instead of manually reviewing packet logs, the system reads exported capture files and generates an automated threat assessment report.

The goal of the project was to demonstrate how AI can assist traditional intrusion detection workflows by accelerating analysis and highlighting potential threats.

---

## Features

- Imports Wireshark packet capture exports (`.txt`)
- Uses Python to process capture data
- Sends network evidence to OpenAI for analysis
- Detects suspicious behavior such as:
  - Port scanning / reconnaissance
  - Unusual UDP traffic
  - Repeated connection attempts
  - Potential attack indicators
- Generates structured security reports including:
  - Threat summary
  - Risk level
  - Evidence observed
  - Recommended mitigation steps

---

## Tech Stack

- Python
- Wireshark
- OpenAI API
- PowerShell / VS Code

---

## How It Works

1. Capture network traffic using Wireshark  
2. Export packet data as plain text  
3. Run the Python script  
4. Enter capture filename  
5. Receive an AI-generated threat report

---

## Example Use Case

An Nmap scan was performed against a target device. Wireshark captured the traffic, and the system analyzed the exported packet data to identify reconnaissance behavior consistent with automated scanning.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
