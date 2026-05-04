# 🔍 Multithreaded Port Scanner (Python)

## 📌 Overview
This project is a Python-based multithreaded port scanner that identifies open TCP ports on a target system. It uses socket programming for network communication and threading to improve scanning performance.

---

## 🚀 Features
- Scan multiple ports (customizable range)
- Multithreaded execution for faster scanning
- Detect open ports and associated services
- Clean and formatted output
- Measures total scan time

---

## 🛠️ Technologies Used
- Python
- Socket Programming
- Threading

---

## ⚙️ How It Works
1. Takes a target (IP address or domain name) as input  
2. Resolves domain to IP address  
3. Scans a range of ports  
4. Uses multithreading to scan multiple ports simultaneously  
5. Displays open ports with service names  

---

## ▶️ How to Run

```bash
python port_scanner.py
```

📊 Example Output
[OPEN]   Port 21    Service: ftp
[OPEN]   Port 22    Service: ssh
[OPEN]   Port 80    Service: http

Scan Complete!
Open Ports: [21, 22, 80]
Time taken: 5.32 seconds

⚠️ Disclaimer

This tool is for educational purposes only. Do not use it to scan systems without proper authorization.

👩‍💻 Author
Diya
