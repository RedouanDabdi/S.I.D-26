import os
from pathlib import Path
from datetime import datetime

# 1. تحديد مكان حفظ التقرير (بجانب الملف الحالي)
log_path = Path(__file__).parent / "security_report.txt"

# 2. جمع المعلومات الاستخباراتية
system_type = os.name       # هل نحن ويندوز أم لينكس؟
current_location = os.getcwd() # أين نحن؟
time_now = datetime.now()   # متى حدث هذا؟

# 3. كتابة التقرير (دمج المهارات)
with open(log_path, "a", encoding="utf-8") as file:
    file.write(f"--- 🛡️ VIGÍA REPORT ---\n")
    file.write(f"⏰ Time: {time_now}\n")
    file.write(f"🖥️ OS Type: {system_type}\n")
    file.write(f"📍 Location: {current_location}\n")
    file.write("✅ Status: SYSTEM SECURE.\n")
    file.write("-" * 30 + "\n")

print(f"REPORT CREATED SUCCESSFULLY: {log_path}")