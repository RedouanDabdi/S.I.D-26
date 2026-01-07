import os
import time
from datetime import datetime

# --- 1. Navegación y Rutas (Navigation) ---
current_script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(current_script_path)
project_root = os.path.dirname(script_directory)

constitution_path = os.path.join(project_root, "00_Constitution_&_Protocols", "Sovereign_Constitution.txt")
log_folder = os.path.join(project_root, "99_Immutable_Logs")
log_file = os.path.join(log_folder, "system_access.log")

# --- 2. Sistema de Registro (Logging) ---
def record_event(event_type, message):
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # نبقي السجلات بالإنجليزية لأنها تقنية، لكن الواجهة إسبانية
    log_entry = f"[{timestamp}] [{event_type}] {message}\n"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

# ... (الكود السابق الخاص بالمسارات واللوغ يبقى كما هو)

# --- 3. Interfaz de Arranque ---
system_name = "S.I.D-26 v1.0" # الاسم المختصر والإصدار
full_system_name = "Sistema de Integridad Digital" # الاسم الكامل للواجهة

print(f"\n--- 🇪🇸 INICIANDO {system_name} : {full_system_name} ---")
print(f"📍 Ubicación del Núcleo: {script_directory}")
print(f"📜 Verificando Protocolos: {constitution_path}")
print("⏳ Cargando módulos del sistema...")
time.sleep(1)

if os.path.exists(constitution_path):
    print("\n✅ INTEGRIDAD VERIFICADA (Integrity Verified).")
    print(f"🔒 Operador: Arquitecto {architect}")
    print("🟢 SISTEMA OPERATIVO Y LISTO.")
    
    # التوثيق في السجل
    record_event("BOOT_SUCCESS", f"System Booted. Version: {system_name}.")
else:
# ... (الباقي كما هو)
    print("\n❌ ERROR CRÍTICO: ¡Falta el archivo de la Constitución!")
    print("🛑 SISTEMA DETENIDO.")
    record_event("BOOT_FAILURE", "Constitution file missing during boot sequence.")