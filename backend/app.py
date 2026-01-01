# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
import random
import time

from detection_engine import detect

app = Flask(__name__)
CORS(app)

# ---- SIMULATED GLOBAL LOCATIONS (REAL WORLD COORDINATES) ----
LOCATIONS = [
    {"country": "USA", "lat": 37.0902, "lng": -95.7129},
    {"country": "India", "lat": 20.5937, "lng": 78.9629},
    {"country": "China", "lat": 35.8617, "lng": 104.1954},
    {"country": "Germany", "lat": 51.1657, "lng": 10.4515},
    {"country": "Russia", "lat": 61.5240, "lng": 105.3188},
    {"country": "Brazil", "lat": -14.2350, "lng": -51.9253},
    {"country": "UK", "lat": 55.3781, "lng": -3.4360},
    {"country": "France", "lat": 46.2276, "lng": 2.2137},
    {"country": "Japan", "lat": 36.2048, "lng": 138.2529},
    {"country": "Australia", "lat": -25.2744, "lng": 133.7751},
]

# ---- ATTACK TYPES & SEVERITIES ----
ATTACK_TYPES = [
    "DDoS",
    "Port Scan",
    "Brute Force",
    "Malware",
    "Ransomware",
    "Phishing",
    "SQL Injection",
    "XSS",
    "Botnet",
    "Credential Stuffing"
]

SEVERITIES = ["Low", "Medium", "High", "Critical"]


# ---- AUTO ATTACK GENERATOR (NO MANUAL INPUT) ----
def generate_attack():
    src = random.choice(LOCATIONS)
    dst = random.choice(LOCATIONS)

    attack = {
        "timestamp": time.strftime("%H:%M:%S"),
        "attack_type": random.choice(ATTACK_TYPES),
        "severity": random.choice(SEVERITIES),
        "source_country": src["country"],
        "target_country": dst["country"],
        "source": {
            "lat": src["lat"],
            "lng": src["lng"]
        },
        "target": {
            "lat": dst["lat"],
            "lng": dst["lng"]
        }
    }

    return detect(attack)


# ---- ROOT ROUTE (FIXES 404 ERROR) ----
@app.route("/")
def home():
    return jsonify({
        "status": "KALI-SOC Global Cyber Threat Map Running",
        "api": "/api/live-attacks"
    })


# ---- LIVE ATTACK FEED API ----
@app.route("/api/live-attacks")
def live_attacks():
    attacks = [generate_attack() for _ in range(5)]
    return jsonify(attacks)


# ---- START SERVER ----
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)