# --- EXTRACT (Extração) ---
users = [
    {"id": 1, "name": "Abner", "account": "1001", "news": []},
    {"id": 2, "name": "Beatriz", "account": "2002", "news": []},
    {"id": 3, "name": "Carlos", "account": "3003", "news": []}
]

# --- TRANSFORM (Transformação) ---
def generate_ai_news(user):
    return f"Olá {user['name']}, vimos que sua conta {user['account']} está ativa. Que tal investir hoje?"

for user in users:
    message = generate_ai_news(user)
    user['news'].append({"icon": "🚀", "description": message})

# --- LOAD (Carregamento) ---
print("Pipeline ETL Finalizado:")
for user in users:
    print(user)
