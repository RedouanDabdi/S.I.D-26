import os
import json
import random
from datetime import datetime

# --- Configuración ---
system_name = "S.I.D-26 (Registro Civil)"
# تصحيح المسار ليكون ذكياً مثل باقي الملفات
current_script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(current_script_path)
project_root = os.path.dirname(script_directory)
vault_path = os.path.join(project_root, "02_Sovereign_Data_Vault")

def generate_id():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_code = "".join(random.choice(chars) for _ in range(4))
    return f"ESP-2026-{random_code}"

# --- Interfaz en Español ---
print(f"\n--- 🇪🇸 {system_name} : EMISIÓN DE CREDENCIALES ---")
# طلب الاسم بالإسبانية
name = input("👉 Introduzca Nombre Oficial (Official Name): ")
role = "Strategic Architect" # الرتب التقنية تبقى بالإنجليزية لسهولة المعالجة

citizen_data = {
    "sovereign_id": generate_id(),
    "full_name": name,
    "role": role,
    "clearance_level": "LEVEL 5 (ROOT)",
    "registration_date": datetime.now().strftime("%Y-%m-%d"),
    "status": "ACTIVE"
}

# --- Guardado (Saving) ---
if not os.path.exists(vault_path):
    os.makedirs(vault_path)

file_name = f"{citizen_data['sovereign_id']}.json"
full_file_path = os.path.join(vault_path, file_name)

with open(full_file_path, "w", encoding="utf-8") as f:
    json.dump(citizen_data, f, indent=4)

print("\n✅ REGISTRO COMPLETADO CON ÉXITO")
print(f"💳 ID Generado: {citizen_data['sovereign_id']}")
print(f"📂 Datos guardados en la Bóveda: {file_name}")