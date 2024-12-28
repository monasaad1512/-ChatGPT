import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "1f5cd35f9d23492dc35a2ce53f9e542d"

def get_weather():
    location = location_entry.get()
    if not location:
        messagebox.showwarning("Error", "Please enter a location")
        return


    # OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "cod" in data:
 # استخراج المعلومات وعرضها
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            pressure = data["main"]["pressure"]
            precipitation = data.get("rain", {}).get("1h", 0)
            if precipitation is not None:
                precip_label.config(text=f"Precipitation: {precipitation}%")
            else:
                precip_label.config(text="Precipitation: No data available")

            temp_label.config(text=f"Temperature: {temperature}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_label.config(text=f"Wind Speed: {wind_speed} km/h")
            pressure_label.config(text=f"Pressure: {pressure} hPa")
            precip_label.config(text=f"Precipitation: {precipitation}%")
        else:
            messagebox.showerror("Error", f"City not found: {location}")
            return
    else:
        print(f"Error: Unable to fetch data, Status code: {response.status_code}")
        return None
        
        

   
# إنشاء النافذة
window = tk.Tk()
window.title("Weather_Forecast")
window.geometry("500x300")


tk.Label(window, text="Location:").grid(row=0, column=0, padx=20, pady=20, sticky="e")
location_entry = tk.Entry(window, width=30)
location_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

# Search button
search_button = tk.Button(window, text="Search", command=get_weather, width=15)
search_button.grid(row=0, column=3, padx=20, pady=20)

# Weather information labels
temp_label = tk.Label(window, text="Temperature: ")
temp_label.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="w")
humidity_label = tk.Label(window, text="Humidity: ")
humidity_label.grid(row=2, column=0, columnspan=4, padx=20, pady=10, sticky="w")
wind_label = tk.Label(window, text="Wind Speed: ")
wind_label.grid(row=3, column=0, columnspan=4, padx=20, pady=10, sticky="w")
pressure_label = tk.Label(window, text="Pressure: ")
pressure_label.grid(row=4, column=0, columnspan=4, padx=20, pady=10, sticky="w")
precip_label = tk.Label(window, text="Precipitation: ")
precip_label.grid(row=5, column=0, columnspan=4, padx=20, pady=10, sticky="w")


window.mainloop()
