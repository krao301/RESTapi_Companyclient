def client_serializer(client) -> dict:
    return {
        "id": str(client["_id"]),
        "name": client["name"],
        "address": client["address"],
        "phoneno": client["phoneno"],
        
    }

def clients_serializer(clients) -> list:
    return [client_serializer(client) for client in clients]