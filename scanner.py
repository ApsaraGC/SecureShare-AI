import re

def scan_text(text):
    findings = []

    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

    phones = re.findall(
        r'\b\d{10,15}\b',
        text
    )

    passports = re.findall(
        r'\b[A-Z]{1,2}[0-9]{6,8}\b',
        text
    )

    credit_cards = re.findall(
        r'\b(?:\d[ -]*?){13,16}\b',
        text
    )

    if emails:
        findings.append(f"Email Addresses Found: {len(emails)}")

    if phones:
        findings.append(f"Phone Numbers Found: {len(phones)}")

    if passports:
        findings.append(f"Passport Numbers Found: {len(passports)}")

    if credit_cards:
        findings.append(f"Possible Card Numbers Found: {len(credit_cards)}")

    return findings