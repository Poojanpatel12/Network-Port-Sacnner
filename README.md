# NetScan — Python Network Port Scanner

A real network port scanner built with Python (Flask + socket) and a web UI.

## Project Structure

```
port_scanner/
├── app.py               ← Python Flask backend (real TCP scanning)
├── requirements.txt     ← Python dependencies
├── templates/
│   └── index.html       ← Web UI (HTML/CSS/JS)
└── README.md
```

## How to Run

### Step 1 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Run the app
```bash
python app.py
```

### Step 3 — Open in browser
```
http://127.0.0.1:5000
```

## Features

- Real TCP port scanning using Python's `socket` module
- Multi-threaded scanning with `ThreadPoolExecutor`
- Live streaming results via Server-Sent Events (SSE)
- Service detection for 40+ common ports
- Filter results: All / Open / Closed / Filtered
- Export results as CSV or JSON
- Copy scan report to clipboard
- Quick presets: Common, Full, Web, MySQL, Dev Ports, etc.

## How It Works

1. User enters target host + port range in the browser
2. Browser sends a POST request to the Python Flask backend
3. Python uses `socket.connect_ex()` to attempt TCP connections
4. Results stream back live to the browser using Server-Sent Events
5. UI updates in real time showing port status and latency

## Technologies Used

| Layer    | Technology              |
|----------|------------------------|
| Backend  | Python 3, Flask        |
| Scanner  | Python `socket` module |
| Threading| `concurrent.futures`   |
| Frontend | HTML, CSS, JavaScript  |
| Streaming| Server-Sent Events     |

## Port Status

| Status   | Meaning                                      |
|----------|----------------------------------------------|
| OPEN     | Port accepted the TCP connection             |
| CLOSED   | Port is reachable but rejected the connection|
| FILTERED | No response within timeout (firewall/blocked)|

## Note

Only scan hosts you own or have permission to scan.
