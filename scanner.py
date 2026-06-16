import re

def scan_text(text):
    findings = []

    emails = re.findall(r'\S+@\S+', text)

    phones = re.findall(r'\d{10,}', text)

    if emails:
        findings.append(f"Emails Found: {len(emails)}")

    if phones:
        findings.append(f"Phone Numbers Found: {len(phones)}")

    return findings