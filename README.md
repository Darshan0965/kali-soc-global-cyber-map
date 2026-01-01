# 🌍 KALI-SOC Global Cyber Threat Map

A **real-time SOC-style Global Cyber Threat Visualization platform** built using **Kali Linux, Python (Flask), and Web Technologies**.  
This project simulates and visualizes **live cyber attack detections** on an **interactive real-world map**, similar to enterprise SOC dashboards.

---

## 🚀 Project Overview

**KALI-SOC Global Cyber Threat Map** is designed to demonstrate how a **Security Operations Center (SOC)** monitors global cyber threats in real time.

The system:
- Automatically generates cyber attack events
- Maps attacks across **real-world geographic locations**
- Displays threat severity, threat score, tools detected, and attack types
- Shows a **live attack feed** in table format
- Runs fully on **Kali Linux** environment

⚠️ **Note:**  
This project is for **educational, ethical, and demonstration purposes only**.  
No real attacks are performed.

---

## 🧠 Key Features

✅ Real-world interactive world map  
✅ Automatic cyber attack simulation (no manual input)  
✅ 80+ simulated detections  
✅ Live attack feed (SOC-style table)  
✅ Threat severity & threat score calculation  
✅ Kali Linux tools mapping (Hydra, Nmap, SQLmap, etc.)  
✅ Backend API using Flask  
✅ Clean frontend dashboard  
✅ GitHub & Hackathon ready structure  

---

## 🗺️ Visual Output

### 🌐 Global Cyber Threat Map
![Global Map](screenshots/map.png)

---

## 🧱 Project Architecture
Frontend (HTML/CSS/JS) │ ▼ Flask REST API (app.py) │ ▼ Detection Engine (detection.py) │ ▼ Attack Simulation & Threat Scoring
kali-soc-global-cyber-map/ │ ├── backend/ │   ├── app.py │   ├── detection.py │   ├── attack_engine.py │   ├── traffic_simulator.py │   ├── requirements.txt │   └── pycache/ │ ├── frontend/ │   ├── index.html │   ├── css/ │   │   └── style.css │   ├── js/ │   │   └── map.js │ ├── screenshots/ │   └── map.png │ ├── .gitignore ├── README.md
---

## ⚙️ Technologies Used

### 🔹 Backend
- Python 3
- Flask
- Flask-CORS
- Kali Linux Environment

### 🔹 Frontend
- HTML5
- CSS3
- JavaScript
- Leaflet.js (Map rendering)

### 🔹 Security Context
- Kali Linux SOC tools (simulated)
- Threat scoring logic
- Attack classification

---

## 🛠️ Kali Linux Tools Simulated

| Tool Name | Attack Type |
|---------|------------|
| Nmap | Port Scanning |
| Hydra | Brute Force |
| SQLmap | SQL Injection |
| Nikto | Web Vulnerability Scan |
| Metasploit | Exploitation |
| Slowloris | DoS Attack |
| Setoolkit | Phishing |
| Hping3 | DDoS Simulation |

---

## 📊 Threat Severity Levels

| Level | Description |
|-----|------------|
| Low | Recon / Scan |
| Medium | Exploitation Attempt |
| High | Active Attack |
| Critical | Coordinated Attack |

Threat Score is calculated dynamically based on:
- Attack type
- Frequency
- Source & target distance
- Tool used

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Darshan0965/kali-soc-global-cyber-map.git
cd kali-soc-global-cyber-map
