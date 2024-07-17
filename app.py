import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from PIL import ImageTk, Image
import phonenumbers 
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier,geocoder


number_Locatiion ='Nothing to display '
serviceProvider = 'Nothing to display '
API_key = "61c8d0810c8c41928ab66e2649740fb0"
def locate():
     
    checkNumber = phonenumbers.parse(str(get_entry_value()))
    number_Locatiion = geocoder.description_for_number(checkNumber, "en")
    
    serviceProvider = carrier.name_for_number(checkNumber, "en")
    from opencage.geocoder import OpenCageGeocode
    geocode = OpenCageGeocode(API_key)
    QUERY = str(number_Locatiion)
    results = geocode.geocode(QUERY)

    latitude = results[0]['geometry']['lat']
    longitude = results[0]['geometry']['lng']
    score_label = ttk.Label(frame,  text=f"Results for {str(get_entry_value())}: \n \nNumber Location: {number_Locatiion} \nService Provider: {serviceProvider} \ncoordinates: {latitude} {longitude}", anchor='center', padding=10)
    score_label.pack(pady=10)
    
def get_entry_value():
    return user_input.get()

root = tk.Tk()  # root
root.title("hacking App")
root.config(bg="Black")
root.geometry("500x500")
style = Style(theme="flatly")
# scroll 

scrollbar = ttk.Scrollbar(root, orient='vertical')
scrollbar.pack(side='right', fill='y')
# Create a custom dark theme style
style.configure("TButton", background="#333333", foreground="#FFFFFF", borderwidth=4,width=100)
style.configure("TLabel", background="#333333", foreground="#FFFFFF" ,font=(20))
style.configure("TFrame", background="#333333",width=50)

frame = ttk.Frame(root, padding=10, style="TFrame")
frame.pack(fill="both", expand=True)

label = ttk.Label(frame, text=f"Enter the number you want to locate:", style="TLabel", padding=40)
label.pack()

user_input = tk.Entry(frame, bg="black", fg="white", font=("Arial", 20), width=150)
user_input.pack(pady=10)
button = ttk.Button(frame, text="Locate", command= locate, style="TButton")
button.pack(pady=10)
# scrolling

get_entry_value()
root.mainloop()

























'''
number = str(input("Enter the nmber you wanna track(incluide the country code): \n"))
checkNumber = phonenumbers.parse(number)
numberLocatiion = geocoder.description_for_number(checkNumber, "en")
print(numberLocatiion)

API_key = "61c8d0810c8c41928ab66e2649740fb0"

from phonenumbers import carrier

serviceProvider = phonenumbers.parse(number)
print(carrier.name_for_number(serviceProvider, "en"))

time = timezone.time_zones_for_number(checkNumber)
print(time)
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(API_key)

QUERY = str(numberLocatiion)
results = geocoder.geocode(QUERY)

latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']
print(latitude,longitude)

# get the pointer in the map using co-oodinates

map_location = folium.Map(location= [latitude,longitude], zoom_start=9)
folium.Marker([latitude,longitude], popup= numberLocatiion).add_to(map_location)
map_location.save('myLocation.html')
'''