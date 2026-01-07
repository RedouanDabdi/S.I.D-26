import os
import json
import time

# --- 1. Navegación del Sistema (Zero-Error Navigation) ---
# تحديد المسارات بدقة لضمان عدم حدوث أخطاء
current_script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(current_script_path)
project_root = os.path.dirname(script_directory)
vault_path = os.path.join(project_root, "02_Sovereign_Data_Vault")

# --- 2. Interfaz de Usuario (Español) ---
print("\n--- 🇪🇸 S.I.D-26 : CONTROL DE ACCESO v1.0 --- : ESCÁNER DE IDENTIDAD ---")
print("Estado: SISTEMA ACTIVO. INTEGRIDAD ASEGURADA.")

# طلب الإدخال بالإسبانية
target_id = input("👉 Introduzca ID (Enter ID): ").strip()

print(f"\n🔄 Buscando en la Bóveda de Datos (Searching Vault): [{target_id}]...")
time.sleep(1) # محاكاة المعالجة

file_name = f"{target_id}.json"
full_file_path = os.path.join(vault_path, file_name)

# --- 3. Verificación (Verification Logic) ---
if os.path.exists(full_file_path):
    # فتح الملف
    with open(full_file_path, "r", encoding="utf-8") as f:
        citizen_data = json.load(f)
    
    # رسالة القبول الرسمية
    print("\n✅ ACCESO CONCEDIDO (Access Granted)") 
    print("------------------------------------------------")
    print(f"👤 Nombre:    {citizen_data['full_name']}")
    print(f"🛡️ Cargo:     {citizen_data['role']}")
    print(f"🔑 Nivel:     {citizen_data['clearance_level']}")
    print(f"📅 Registro:  {citizen_data['registration_date']}")
    print("------------------------------------------------")
    print("👋 Bienvenido, Arquitecto.")

else:
    # رسالة الرفض الرسمية
    print("\n❌ ACCESO DENEGADO (Access Denied)")
    print(f"🚫 La identidad '{target_id}' no consta en el registro nacional.")
    print("🚨 Incidente de seguridad reportado al núcleo.")