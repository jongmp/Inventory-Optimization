'''
IMPORT STATEMENT
- Tkinter for GUI
'''
# For GUI Modules
import tkinter as tk
from PIL import Image, ImageTk 
from scipy.stats import norm
import math

# Define function to calculate ideal inventory
def ideal_inv_calc():
    
    # Generate the inputs
    avg_daily_demand = float(avg_demand.get())
    lead_time = float(avg_lt.get())
    
    demand_var = str(demand_menu.get())
    lt_var = str(lt_menu.get())
    ss_var = str(safety_menu.get())
    
    # Defining Variability Variables into Strings for Demand Variability
    # High > oD of 0.5, Medium > oD of 0.3, Low > oD of 0.1
    if demand_var == "High":
        variability_level = 0.5
    elif demand_var == "Medium":
        variability_level = 0.3
    else:
        variability_level = 0.1
    
    # Defining Variability Variables into String for Lead Time Variability
    if lt_var == "High":
        olt = 5.0
    elif lt_var == "Medium":
        olt = 3.0
    else:
        olt = 1.0
    
    # Defining Customer Service Level with the Safety Stock Level
    # Safety Stock Level - High > CSL 0.9, Medium > 0.75, Low > 0.6, None > 0.5
    if ss_var == "High":
        csl = 0.9
    elif ss_var == "Medium":
        csl = 0.75
    elif ss_var == "Low":
        csl = 0.6
    else:
        csl = 0.5

    # Safety Stock - norm inv(CSL) * sqrt(( lt * oDT ^2) + D^2 * oLT ^2)
    safety_stock = norm.ppf(csl) * math.sqrt((lead_time * variability_level**2) + avg_daily_demand**2 * olt**2)

    # Reorder Point - Demand over Lead Time
    reorder_point = avg_daily_demand * lead_time + safety_stock

    # Round Up Reorder point to a round number
    reorder_point = int(round(reorder_point, 0))
    
    # Inserting Sentiment Score Into Text Box
    text_box.delete('1.0',tk.END)
    text_box.insert(tk.END, reorder_point)


    
'''
Setting Up Tkinter Object for GUI
'''
# Setting Up Tkinter Object
root = tk.Tk()
root.title("Inventory Optimization App")

# Setting Up the Canvas
canvas = tk.Canvas(root, width = 1494, height = 840)
canvas.grid(columnspan=20, rowspan = 20)

# Importing Image
background = Image.open('background.png')
background = ImageTk.PhotoImage(background)
background_label = tk.Label(image = background)
background_label.image = background
background_label.grid(column = 10, row = 10)

# Creating Input Field for Average Daily Demand
avg_demand = tk.Entry(root, font=('Raleway 14'))
canvas.create_window(225, 300, height = 40, width = 200, window = avg_demand)

#Set the Menu initially
demand_menu = tk.StringVar()
demand_menu.set("Select Variability Level")

#Create a dropdown Menu
demand_var = tk.OptionMenu(root, demand_menu,"High", "Medium","Low")

# Creating Input Field for Variability of Demand
canvas.create_window(225, 560, height = 40, width = 200, window = demand_var)

# Creating Input Field for Average Lead Time
avg_lt = tk.Entry(root, font=('Raleway 14'))
canvas.create_window(759, 300, height = 40, width = 200, window = avg_lt)

#Set the Menu initially
lt_menu = tk.StringVar()
lt_menu.set("Select Variability Level")

#Create a dropdown Menu
lt_var = tk.OptionMenu(root, lt_menu,"High", "Medium","Low")

# Creating Input Field for Variability of Demand
canvas.create_window(759, 560, height = 40, width = 200, window = lt_var)

#Set the Menu initially
safety_menu = tk.StringVar()
safety_menu.set("Select Safety Stock Level")

#Create a dropdown Menu
ss_var = tk.OptionMenu(root, safety_menu,"High", "Medium","Low","None")

# Creating Input Field for Variability of Demand
canvas.create_window(1250, 300, height = 40, width = 200, window = ss_var)

# Creating Button to Generate Sentiment Analysis and Webscraping
btn = tk.Button(root, text = "Generate", font = ("Raleway 18"), command = ideal_inv_calc)
btn.place(x = 1175 , y = 490, in_=root)

# Creating Text Object for Sentiment Score
text_box = tk.Text(root, height = 3, width = 20, font=('Raleway 18'))
text_box.place(x = 800, y = 660, in_=root)

root.mainloop()


