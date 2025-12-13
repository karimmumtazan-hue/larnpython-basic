import requests
import json
from datetime import datetime, timedelta
from tabulate import tabulate
from colorama import init, Fore, Style
import time
import sys

# Initialize colorama for Windows
init(autoreset=True)

def get_prayer_times(city, country="Indonesia", method=20, days_ahead=0):
    url = f"https://api.aladhan.com/v1/timingsByCity"
    params = {"city": city, "country": country, "method": method}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        date = datetime.now() + timedelta(days=days_ahead)
        timings = data['data']['timings']
        hijri_date = data['data']['date']['hijri']['date']
        
        prayer_times = {
            "Shubuh": timings["Fajr"],
            "Dzuhur": timings["Dhuhr"], 
            "Ashar": timings["Asr"],
            "Maghrib": timings["Maghrib"],
            "Isya": timings["Isha"]
        }
        
        return {
            "date": date.strftime("%Y-%m-%d"),
            "hijri": hijri_date,
            "times": prayer_times
        }
    return None

def time_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def minutes_between_times(time1, time2):
    """Hitung selisih menit antara 2 waktu (handle midnight crossing)"""
    m1 = time_to_minutes(time1)
    m2 = time_to_minutes(time2)
    return (m2 - m1) % (24 * 60)

def get_next_prayer(now_minutes, prayer_data):
    """Cari sholat berikutnya + countdown menit"""
    next_prayer = None
    min_diff = float('inf')
    
    for prayer, time_str in prayer_data["times"].items():
        prayer_minutes = time_to_minutes(time_str)
        diff = (prayer_minutes - now_minutes) % (24 * 60)
        
        if diff < min_diff and diff > 0:
            min_diff = diff
            next_prayer = prayer
    
    return next_prayer, min_diff

def get_color_status(now_minutes, prayer_time):
    """Color coding: hijau(sudah), kuning(segera), merah(berikutnya)"""
    prayer_minutes = time_to_minutes(prayer_time)
    diff = (prayer_minutes - now_minutes) % (24 * 60)
    
    if diff > 60:  # >1 jam lagi
        return Fore.RED  # Berikutnya
    elif diff > 15:  # 15-60 menit
        return Fore.YELLOW  # Segera
    elif diff > 0:   # <15 menit
        return Fore.CYAN   # Sangat dekat
    else:            # Sudah lewat
        return Fore.GREEN

def display_single_city(prayer_data, now_minutes):
    if not prayer_data:
        print(f"{Fore.RED}❌ Kota tidak ditemukan")
        return
    
    table_data = []
    durations = []
    prev_time = None
    
    for i, (prayer, time_str) in enumerate(prayer_data["times"].items()):
        color = get_color_status(now_minutes, time_str)
        duration = minutes_between_times(prev_time, time_str) if prev_time else "-"
        durations.append(duration)
        prev_time = time_str
        
        table_data.append([color + prayer + Style.RESET_ALL, 
                          time_str, 
                          f"{duration//60}:{duration%60:02d}" if duration != "-" else "-"])
    
    next_prayer, countdown = get_next_prayer(now_minutes, prayer_data)
    status = f"{Fore.CYAN}⏰ {next_prayer}: {countdown//60}:{countdown%60:02d} lagi{Style.RESET_ALL}"
    
    print(f"\n🕌 {Fore.WHITE}Jadwal Sholat {prayer_data['date']} (Hijriah: {prayer_data['hijri']})")
    print(tabulate(table_data, headers=["Sholat", "Waktu", "Durasi"], tablefmt="grid"))
    print(status)

def display_multiple_cities(cities, now_minutes):
    """Tabel multiple kota berdampingan"""
    all_data = []
    
    for city in cities:
        data = get_prayer_times(city.strip())
        if data:
            row = [city.title()]
            for prayer in ["Shubuh", "Dzuhur", "Ashar", "Maghrib", "Isya"]:
                time_str = data["times"][prayer]
                color = get_color_status(now_minutes, time_str)
                row.append(color + time_str + Style.RESET_ALL)
            all_data.append(row)
    
    if all_data:
        print(tabulate(all_data, headers=["Kota", "Shubuh", "Dzuhur", "Ashar", "Maghrib", "Isya"], tablefmt="grid"))

def prayer_reminder_loop(prayer_data):
    """Reminder loop - update setiap menit"""
    print("\n🔄 Reminder aktif (Ctrl+C untuk stop)")
    try:
        while True:
            now = datetime.now()
            now_minutes = now.hour * 60 + now.minute
            
            print(f"\r{now.strftime('%H:%M')} ", end="")
            display_single_city(prayer_data, now_minutes)
            time.sleep(60)  # Update setiap menit
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Reminder dihentikan")

def main():
    print(f"{Fore.CYAN}=== JADWAL SHOLAT SMART ==={Style.RESET_ALL}")
    print("1. Satu kota")
    print("2. Multiple kota")
    print("3. Real-time sholat")
    
    choice = input("Pilih (1/2/3): ").strip()
    now = datetime.now()
    now_minutes = now.hour * 60 + now.minute
    
    if choice == "2":
        cities = input("Kota (pisah koma): ").strip()
        display_multiple_cities(cities.split(","), now_minutes)
    elif choice == "3":
        city = input("Kota: ").strip().title()
        prayer_data = get_prayer_times(city)
        prayer_reminder_loop(prayer_data)
    else:  # Single city
        city = input("Kota: ").strip().title()
        prayer_data = get_prayer_times(city)
        display_single_city(prayer_data, now_minutes)

if __name__ == "__main__":
    main()
