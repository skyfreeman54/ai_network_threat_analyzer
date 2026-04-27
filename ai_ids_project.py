from openai import OpenAI
from pathlib import Path

print("AI IDS Analyzer Online")

client = OpenAI()

captures = Path("captures")
outputs = Path("outputs")

filename = input("Enter capture filename: ")
file_path = captures / filename

data = file_path.read_text(encoding="utf-8", errors="ignore")

prompt = f"""
Analyze this Wireshark packet capture text for suspicious network activity.

Look for:
- Nmap behavior
- port scanning
- repeated connection attempts
- ICMP probing
- unusual ports
- suspicious source and destination patterns

Return:
1. Executive Summary
2. Suspicious Indicators
3. Likely Attack Type
4. Risk Level
5. Evidence
6. Recommended Mitigation
7. Student-Friendly Explanation

Packet data:
{data[:10000]}
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

report = response.output_text

print("\n===== AI THREAT REPORT =====\n")
print(report)

output_file = outputs / "report.txt"
output_file.write_text(report, encoding="utf-8")

print("\nSaved to outputs/report.txt")