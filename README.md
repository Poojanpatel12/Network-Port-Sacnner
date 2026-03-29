# Network-Port-Sacnner
A real-time network port scanner built with Python (Flask + Socket) and a modern web UI.

### 🔍 Network Port Scanner

A real-time network port scanner built with **Python** and **Flask** that scans commonly used TCP ports on any target host and displays live results through a modern web-based interface.

---

## 👨‍💻 Developed By
**Poojan Patel**

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Core programming language |
| Flask | Web framework (backend) |
| Socket | Real TCP port scanning |
| ThreadPoolExecutor | Multi-threaded concurrent scanning |
| HTML / CSS / JavaScript | Frontend UI |
| Server-Sent Events (SSE) | Live streaming results to browser |

---

## ✨ Features

- ✅ Scans 13 well-known ports automatically
- ✅ Real-time live results streamed to browser
- ✅ Detects port status — Open / Closed / Filtered
- ✅ Shows service name and latency for each port
- ✅ Export results as CSV or JSON
- ✅ Copy scan report to clipboard
- ✅ Clean cyberpunk-themed terminal UI

---

## 🔎 Ports Scanned

| Port | Service |
|------|---------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3306 | MySQL |
| 3389 | RDP |
| 5900 | VNC |
| 8080 | HTTP-Alt |

---

## 🚀 How to Run

### Step 1 — Clone the repository
```bash
git clone https://github.com/Poojanpatel12/Network-Port-Sacnner.git
cd Network-Port-Sacnner
```

### Step 2 — Install dependencies
```bash
pip3 install flask
```

### Step 3 — Run the app
```bash
python3 app.py
```

### Step 4 — Open in browser
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure
```
Network-Port-Scanner/
├── app.py                  ← Python Flask backend (real TCP scanning)
├── requirements.txt        ← Python dependencies
├── templates/
│   └── index.html          ← Web UI (HTML/CSS/JS)
└── README.md               ← Project documentation
```

---

## 📌 How It Works

1. User enters a **target host/IP** in the browser
2. Browser sends request to the **Python Flask backend**
3. Python uses **socket.connect_ex()** to attempt TCP connections
4. Results **stream back live** to the browser using Server-Sent Events
5. UI updates in real time showing **port status and latency**

---

## ⚠️ Disclaimer

> This tool is made for **educational purposes only**.  
> Only scan hosts you **own or have permission** to scan.  
> Unauthorized port scanning may be illegal in your region.

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
