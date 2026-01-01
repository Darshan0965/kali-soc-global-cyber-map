# backend/detection_engine.py

# Kali Linux tool mapping (conceptual IDS signatures)
KALI_TOOLS = {
    "DDoS": ["hping3", "slowloris", "goldeneye"],
    "Port Scan": ["nmap", "masscan"],
    "Brute Force": ["hydra", "medusa", "patator"],
    "Malware": ["msfvenom", "veil"],
    "Ransomware": ["metasploit", "msfconsole"],
    "Phishing": ["setoolkit"],
    "SQL Injection": ["sqlmap"],
    "XSS": ["xsser", "beef"],
    "Botnet": ["dnsrecon", "maltego"],
    "Credential Stuffing": ["hydra", "patator"]
}

# Threat score model (SOC-style)
THREAT_SCORE = {
    "Low": 20,
    "Medium": 45,
    "High": 75,
    "Critical": 95
}

def detect(event):
    """
    Detect attack using IDS-style logic inspired by Kali Linux tools.
    Adds:
    - detected_by (tools)
    - threat_score
    - risk_level
    """

    attack_type = event.get("attack_type", "Unknown")
    severity = event.get("severity", "Low")

    # Kali tools used for detection
    event["detected_by"] = KALI_TOOLS.get(
        attack_type,
        ["generic-ids"]
    )

    # Threat scoring
    event["threat_score"] = THREAT_SCORE.get(severity, 10)

    # Risk level (SOC terminology)
    if event["threat_score"] >= 90:
        event["risk_level"] = "Extreme"
    elif event["threat_score"] >= 70:
        event["risk_level"] = "High"
    elif event["threat_score"] >= 40:
        event["risk_level"] = "Medium"
    else:
        event["risk_level"] = "Low"

    return event