import socket
import json
import uuid
import time

SERVER_IP = "54.167.34.209" 
PORT = 5000

def call_rpc(method, params):
    # Создаем уникальный ID запроса [cite: 61, 68]
    request_id = str(uuid.uuid4())
    
    # Структура сообщения [cite: 65-70]
    payload = {
        "request_id": request_id,
        "method": method,
        "params": params
    }

    # Попытки ретраев (макс 3) [cite: 31, 84]
    for attempt in range(1, 4):
        try:
            print(f"Attempt {attempt}: Sending request {request_id}...")
            
            # Создаем сокет и ставим таймаут 2 секунды [cite: 82]
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2.0) 
            
            sock.connect((SERVER_IP, PORT))
            sock.sendall(json.dumps(payload).encode())
            
            # Получаем ответ [cite: 81]
            data = sock.recv(1024).decode()
            response = json.loads(data)
            return response
            
        except (socket.timeout, ConnectionRefusedError):
            print(f"Attempt {attempt} failed (timeout or server down).")
            time.sleep(1) # Ждем перед повтором
        finally:
            sock.close()

    return {"status": "Error", "message": "Failed after 3 retries"} # [cite: 85]

if __name__ == "__main__":
    # Тестовый вызов функции add(5, 7)
    result = call_rpc("add", {"a": 5, "b": 7})
    print("\nFINAL RESULT:", result)