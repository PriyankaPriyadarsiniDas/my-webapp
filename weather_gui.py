# weather_gui.py
import requests
from tkinter import *
from tkinter import messagebox

API_KEY ="5d57453117fda95e31a34c3a38a71c8f"

def fetch_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showinfo("Input needed", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
    except Exception as e:
        messagebox.showerror("Network error", str(e))
        return

    if data.get("cod") != 200:
        messagebox.showerror("Error", data.get("message", "City not found"))
        return

    city_text = f"{data['name']}, {data['sys']['country']}"
    temp_text = f"Temperature: {data['main']['temp']} °C"
    humidity_text = f"Humidity: {data['main']['humidity']}%"
    cond_text = f"Condition: {data['weather'][0]['description'].capitalize()}"

    result_var.set(f"{city_text}\n{temp_text}\n{humidity_text}\n{cond_text}")

# GUI
root = Tk()
root.title("Weather App")
root.geometry("360x220")
root.resizable(False, False)

frame = Frame(root, padx=12, pady=12)
frame.pack(expand=True, fill=BOTH)

Label(frame, text="Enter City:", font=("Arial", 12)).pack(anchor="w")
city_entry = Entry(frame, font=("Arial", 12))
city_entry.pack(fill=X, pady=6)

btn = Button(frame, text="Check Weather", command=fetch_weather, font=("Arial", 11))
btn.pack(pady=6)

result_var = StringVar()
result_label = Label(frame, textvariable=result_var, font=("Arial", 11), justify=LEFT)
result_label.pack(anchor="w", pady=6)

root.mainloop()
