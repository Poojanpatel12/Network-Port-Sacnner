from flask import Flask, render_template, request, jsonify, Response
import socket
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

app = Flask(__name__)

# ── Service Database ──────────────────────────────────────────────────────────
SERVICE_DB = {
    20: ("FTP-Data", "FTP Data Transfer"),
    21: ("FTP", "File Transfer Protocol"),
    22: ("SSH", "Secure Shell"),
    23: ("Telnet", "Unencrypted Remote Login"),
    25: ("SMTP", "Simple Mail Transfer"),
    53: ("DNS", "Domain Name System"),
    80: ("HTTP", "Hypertext Transfer Protocol"),
    110: ("POP3", "Post Office Protocol v3"),
    123: ("NTP", "Network Time Protocol"),
    135: ("MSRPC", "Microsoft RPC"),
    139: ("NetBIOS", "NetBIOS Session Service"),
    143: ("IMAP", "Internet Message Access"),
    161: ("SNMP", "Simple Network Management"),
    389: ("LDAP", "Lightweight Directory Access"),
    443: ("HTTPS", "HTTP over TLS/SSL"),
    445: ("SMB", "Server Message Block"),
    465: ("SMTPS", "SMTP over SSL"),
    587: ("SMTP", "SMTP Mail Submission"),
    993: ("IMAPS", "IMAP over SSL"),
    995: ("POP3S", "POP3 over SSL"),
    1433: ("MSSQL", "Microsoft SQL Server"),
    1521: ("Oracle", "Oracle DB Listener"),
    1723: ("PPTP", "Point-to-Point Tunneling"),
    2049: ("NFS", "Network File System"),
    3000: ("Dev", "Node.js / React Dev Server"),
    3306: ("MySQL", "MySQL Database"),
    3389: ("RDP", "Remote Desktop Protocol"),
    4200: ("Angular", "Angular Dev Server"),
    5000: ("Flask", "Python Flask Dev Server"),
    5432: ("PostgreSQL", "PostgreSQL Database"),
    5672: ("AMQP", "RabbitMQ Messaging"),
    5900: ("VNC", "Virtual Network Computing"),
    6379: ("Redis", "Redis In-Memory DB"),
    8000: ("HTTP-Alt", "Alternative HTTP"),
    8080: ("HTTP-Proxy", "HTTP Proxy / Tomcat"),
    8443: ("HTTPS-Alt", "Alternative HTTPS"),
    8888: ("Jupyter", "Jupyter Notebook"),
    9000: ("SonarQube", "SonarQube / PHP-FPM"),
    9090: ("Prometheus", "Prometheus Monitoring"),
    9200: ("Elasticsearch", "Elasticsearch REST API"),
    27017: ("MongoDB", "MongoDB Database"),
}


# ── Port Scanner Core ─────────────────────────────────────────────────────────
def scan_port(host, port, timeout):
    """Try TCP connect to a port and return its status."""
    start = time.time()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout / 1000.0)
        result = sock.connect_ex((host, port))
        latency = int((time.time() - start) * 1000)
        sock.close()
        status = "open" if result == 0 else "closed"
    except socket.timeout:
        latency = timeout
        status = "filtered"
    except Exception:
        latency = 0
        status = "closed"

    service = SERVICE_DB.get(port)
    return {
        "port": port,
        "status": status,
        "latency": latency,
        "service": service[0] if service else None,
        "description": service[1] if service else "Unknown service",
    }


# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    """Stream scan results using Server-Sent Events."""
    data = request.get_json()
    host = data.get("host", "").strip()
    port_start = int(data.get("portStart", 1))
    port_end = int(data.get("portEnd", 1024))
    timeout = int(data.get("timeout", 500))
    concurrency = int(data.get("concurrency", 50))

    try:
        resolved_ip = socket.gethostbyname(host)
    except socket.gaierror:
        return jsonify({"error": f"Cannot resolve host: {host}"}), 400

    ALLOWED_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 5900, 8080]
    ports = ALLOWED_PORTS
    results = []

    def generate():
        yield f"data: {json.dumps({'type': 'start', 'host': host, 'ip': resolved_ip, 'total': len(ports)})}\n\n"

        with ThreadPoolExecutor(max_workers=min(concurrency, 200)) as executor:
            futures = {executor.submit(scan_port, resolved_ip, p, timeout): p for p in ports}
            done = 0
            for future in as_completed(futures):
                res = future.result()
                done += 1
                res["done"] = done
                res["total"] = len(ports)
                results.append(res)
                yield f"data: {json.dumps({'type': 'result', **res})}\n\n"

        open_c = sum(1 for r in results if r["status"] == "open")
        closed_c = sum(1 for r in results if r["status"] == "closed")
        filtered_c = sum(1 for r in results if r["status"] == "filtered")
        yield f"data: {json.dumps({'type': 'done', 'total': len(ports), 'open': open_c, 'closed': closed_c, 'filtered': filtered_c})}\n\n"

    return Response(
        generate(),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


if __name__ == "__main__":
    print("\n" + "=" * 52)
    print("   NetScan - Python Network Port Scanner")
    print("   Visit: http://127.0.0.1:5000")
    print("=" * 52 + "\n")
    app.run(debug=True, threaded=True)
