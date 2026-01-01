import random, time
from geo_db import LOCATIONS

ATTACKS = [
    "DDoS", "Port Scan", "Brute Force", "Malware",
    "Ransomware", "Phishing", "SQL Injection",
    "XSS", "Botnet", "Credential Stuffing"
]

SEVERITY = ["Low", "Medium", "High", "Critical"]
ORGS = ["AWS", "Google Cloud", "Azure", "PayPal", "ICICI", "HDFC"]

def generate_event():
    src = random.choice(LOCATIONS)
    tgt = random.choice(LOCATIONS)

    return {
        "time": time.strftime("%H:%M:%S"),
        "attack_type": random.choice(ATTACKS),
        "severity": random.choice(SEVERITY),
        "source": {"country": src[0], "lat": src[1], "lon": src[2]},
        "target": {"country": tgt[0], "lat": tgt[1], "lon": tgt[2]},
        "target_org": random.choice(ORGS)
    }