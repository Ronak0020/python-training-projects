from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import requests

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg="#3A7FF6")


canvas = Canvas(
    window,
    bg="#3A7FF6",
    height=519,
    width=862,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    430.99,
    0.0,
    861.99,
    519.0,
    fill="#FCFCFC",
    tag="rectangleSomething",
    outline="",
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(630.0, 230.0, image=entry_image_1, tag="entrybg")
entry_1 = Entry(bd=0, fg="#000716", highlightthickness=0, background="#b7bbb9", font="Roboto")
entry_1.place(x=450.0, y=210.0, width=348.0, height=44.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: weatherAnalyze(),
    relief="flat",
)
button_1.place(x=556.99, y=303.0, width=180.0, height=55.0)

canvas.create_text(
    58.99,
    46.0,
    anchor="nw",
    text="Weather Report",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1),
)

canvas.create_text(
    500.99,
    74.0,
    anchor="nw",
    text="Enter city name",
    fill="#505485",
    font=("Roboto Bold", 24 * -1),
)

canvas.create_rectangle(58.99, 74.0, 365.99, 79.0, fill="#FCFCFC", outline="")

canvas.create_text(
    50,
    154.0,
    anchor="nw",
    text="Enter City name",
    fill="#FCFCFC",
    font=("Tajawal Regular", 24 * -1),
)

canvas.create_text(
    50,
    302.0,
    anchor="nw",
    width=300,
    text="Get the weather data",
    fill="#FCFCFC",
    font=("Tajawal Regular", 24 * -1),
)

canvas.create_text(
    50,
    234.0,
    anchor="nw",
    text="Powered by OpenWeather",
    fill="#FFFFFF",
    font=("Tajawal Regular", 24 * -1),
)

entry_widget = Entry(window, background="#F1F5FF", width=50)

window.resizable(False, False)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: resetButtons(),
    relief="flat",
)


def weatherAnalyze():
    canvas.itemconfig(tagOrId="rectanglePath", state="hidden")
    button_1.place_forget()
    canvas.itemconfig(tagOrId="textInput", state="hidden")
    text = entry_1.get()
    print(text)
    details = getWeather(text)
    weatherType = details["weather"][0]["main"]
    temp = details["main"]["temp"]
    feelstemp = details["main"]["feels_like"]
    humidity = details["main"]["humidity"]
    cityname = details["name"]
    
    canvas.create_text(
        450.0,
        130.0,
        anchor="nw",
        width=400,
        text=f"Location: {cityname}\nWeather: {weatherType}\nCurrent Temperation | Feels Like: {temp} ° C | {feelstemp} ° C\nHumidity: {humidity}",
        fill="#848484",
        tags="weather_details",
        font=("Tajawal Regular", 24 * -1),
    )
    button_1.place_forget()
    button_3.place(x=556.99, y=303.0, width=180.0, height=55.0)
    canvas.delete("entrybg")
    canvas.itemconfig(tagOrId="textInput", state="hidden")
    entry_1.place_forget()


def resetButtons():
    button_3.place_forget()
    canvas.delete("weather_details")
    button_1.place(x=556.99, y=303.0, width=180.0, height=55.0)
    entry_1.place(x=500.0, y=200.0, width=348.0, height=44.0)


def getWeather(city):
    apiKey = "edde23ce5194305478a320f7ed254f3a"
    City = city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={City}&APPID={apiKey}&units=metric"
    weather = requests.get(url, headers={"Accept": "application/json"})
    print(weather)
    if weather.status_code == 404:
        return "Invalid City"
    else:
        wdata = weather.json()
        return wdata


window.mainloop()
