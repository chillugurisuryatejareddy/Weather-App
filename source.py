from tkinter import *
from tkinter.ttk import *
import tkinter.font as font
import requests





def get_data():
    city=city_name.get()
    response=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3c6679635a8c3691db92d978ca07fc15")
    data=response.json()
    
    
    climate_value.config(text=str.capitalize(str(data["weather"][0]["main"])))
    temperature_value.config(text=str(int(data ["main"]["temp"]-273.15))+" °C")
    temperature_max_value.config(text=str(int(data ["main"]["temp_max"]-273.15))+" °C")
    temperature_min_value.config(text=str(int(data ["main"]["temp_min"]-273.15))+" °C")
    pressure_value.config(text=str(int(data ["main"]["pressure"]))+" Pa")
        
    





     






win = Tk()
win.title("Weather Application")
win.geometry("500x500")
win.config(bg="#828abf")





name_label=Label(win,text="Weather Report", foreground="white"
                 ,font=("italic","30","bold"),background="#828abf",anchor="center")


name_label.place(x=25,y=45,height=60,width=450)



list_names=[
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Kolkata",
    "Pune",
    "Ahmedabad",
    "Jaipur",
    "Lucknow",
    "Kanpur",
    "Nagpur",
    "Visakhapatnam",
    "Indore",
    "Thane",
    "Bhopal",
    "Patna",
    "Vadodara",
    "Ghaziabad",
    "Ludhiana",
    "Agra",
    "Nashik",
    "Faridabad",
    "Meerut",
    "Rajkot",
    "Varanasi",
    "Srinagar",
    "Aurangabad",
    "Dhanbad",
]#["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name=StringVar()

com=Combobox(win,text="city", values=list_names,
             font=("Time New Roman","8","bold"),foreground="#828abf",textvariable=city_name)
com.place(x=125,y=110,height=25,width=250)



climate=Label(win,text="Climate", foreground="white"
                 ,font=("Time New Roman","15","bold"),background="#828abf",anchor="center")
climate.place(x=60,y=190,width=240,height=30)

climate_value=Label(win,text="", foreground="white"
                 ,font=("Time New Roman","15","bold"),background="#828abf",anchor="w")
climate_value.place(x=310,y=190,width=180,height=30)







temperature=Label(win,text="Temerature", foreground="white"
                 ,font=("Time New Roman","15","bold"),background="#828abf",anchor="center")
temperature.place(x=60,y=220,width=240,height=30)

temperature_value=Label(win,text="", foreground="white"
                 ,font=("Time New Roman","15","bold"),background="#828abf",anchor="center")
temperature_value.place(x=310,y=220,width=100,height=30)





temperature_min=Label(win,text="Minimum Temperature", foreground="white"
                 ,font=("Time New Roman","15","bold"),background="#828abf",anchor="center")
temperature_min.place(x=60,y=250,width=240,height=30)

temperature_min_value=Label(win,text="", foreground="white"
                 ,font=("Time New Roman","15","bold"),background="#828abf",anchor="center")
temperature_min_value.place(x=310,y=250,width=100,height=30)




temperature_max=Label(win,text="Maximum Temperature", foreground="white"
                 ,font=("Time New Roman","15","bold"),background="#828abf",anchor="center")
temperature_max.place(x=60,y=280,width=240,height=30)

temperature_max_value=Label(win,text="", foreground="white"
                 ,font=("Time New Roman","15","bold"),background="#828abf",anchor="center")
temperature_max_value.place(x=310,y=280,width=100,height=30)




pressure=Label(win,text="pressure", foreground="white"
                 ,font=("Time New Roman","15","bold"),background="#828abf",anchor="center")
pressure.place(x=60,y=310,width=240,height=30)

pressure_value=Label(win,text="", foreground="white"
                 ,font=("Time New Roman","15","bold"),background="#828abf",anchor="center")
pressure_value.place(x=310,y=310,width=100,height=30)




buttonFont = font.Font(family='Times New Roman', size=16, weight='bold')

done_button=Button(win,text="Done",command=get_data)
done_button.place(x=200,y=150,width=100,height=30)







win.mainloop()
