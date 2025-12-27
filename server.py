import socket
import json

# Определяем функции, которые будут доступны удаленно [cite: 21, 24]
def add(a, b):
    return a + b

functions = {
    "add": add
}

def start_server():
    # Создаем TCP сокет [cite: 25, 96]
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000)) # Слушаем на порту 5000 [cite: 47]
    server.listen(5)
    print("RPC Server is running on port 5000...")

    while True:
        conn, addr = server.accept()
        try:
            data = conn.recv(1024).decode()
            if not data:
                continue

            # Декодируем JSON запрос [cite: 73]
            request = json.loads(data)
            req_id = request.get("request_id")
            method_name = request.get("method")
            params = request.get("params")

            print(f"[LOG] Request {req_id}: Executing {method_name}") # Логирование [cite: 99]

            # Выполняем функцию
            if method_name in functions:
                result = functions[method_name](**params)
                status = "OK"
            else:
                result = None
                status = "Method not found"

            # Формируем ответ [cite: 75-79]
            response = {
                "request_id": req_id,
                "result": result,
                "status": status
            }
            conn.send(json.dumps(response).encode())
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    start_server()