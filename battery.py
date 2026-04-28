.import psutil
import time
import pyttsx3 # Ovozli gapirish uchun kutubxona

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

print("--- TIZIM NAZORATCHISI ISHGA TUSHDI ---")

last_status = None

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent
    power_plugged = battery.power_plugged
    
    # Holat o'zgarganda xabar berish
    if last_status != power_plugged:
        if power_plugged:
            speak("Zaryadlanish boshlandi. Hozirgi quvvat: " + str(percent) + " foiz")
        else:
            speak("Zaryadlagich sug'urildi. Ehtiyot bo'ling.")
        last_status = power_plugged

    # Quvvat juda kam qolganda ogohlantirish
    if percent <= 20 and not power_plugged:
        speak("Diqqat! Batareya quvvati 20 foizdan kam qoldi. Iltimos, quvvatlagichga ulang!")
        time.sleep(300) # 5 daqiqa dam oladi
        
    time.sleep(10) # Har 10 soniyada tekshiradi
