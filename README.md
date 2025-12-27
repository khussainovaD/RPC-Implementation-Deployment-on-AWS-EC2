# RPC Implementation on AWS EC2 (Lab 1)

## Description
This project implements a simple Remote Procedure Call (RPC) system using Python TCP sockets and JSON serialization. It features timeout handling and a retry mechanism.

## How to Run
1. **Server:** - Launch an EC2 instance and open port 5000 in Security Groups.
   - Run: `python3 server.py`
2. **Client:** - Launch another EC2 instance.
   - Update `SERVER_IP` in `client.py` with your server's Public IP.
   - Run: `python3 client.py`

## Failure Handling
- **Mechanism:** Timeout (2.0s) and Retries (3 attempts).
- **Semantics:** At-least-once.
- **Test:** Use `sudo ufw deny 5000` on the server to observe client retries.
