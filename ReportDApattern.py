import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

df = pd.read_csv(filedialog.askopenfilename())
profitList = df ['total_profit'].tolist()
monthList = df ['month_number'].tolist()
facecream = df['facecream'].tolist()
facewash = df['facewash'].tolist()
toothpaste = df['toothpaste'].tolist()
bathingsoap = df['bathingsoap'].tolist()
shampoo = df['shampoo'].tolist()
paper = df['paper'].tolist()
#Problem 1
plt.xticks(monthList)
plt.plot(monthList,profitList)
plt.xlabel('Month Number')
plt.ylabel('Total profit ($)')
plt.title('Profit of December')
plt.grid(True)
plt.show()
#Problem 2
plt.xticks(monthList)
plt.plot(monthList,facecream,label="Facecream")
plt.plot(monthList,facewash,label="Facewash")
plt.plot(monthList,toothpaste ,label="Toothpaste")
plt.plot(monthList,bathingsoap,label="Bathingsoap")
plt.plot(monthList,shampoo,label="Shampoo")
plt.plot(monthList,paper,label="Paper")
plt.title('Sales quantity')
plt.xlabel("Month")
plt.ylabel("Amout of products")
plt.grid(True)
plt.legend()
plt.show()
#Problem 3
X_axis = np.arange(len(monthList))
plt.xticks(X_axis,monthList)
plt.bar(X_axis-0.2,facecream,0.4,label="Facecream")
plt.bar(X_axis+0.2,facewash,0.4,label="Facewash")
plt.title('The sales volume difference between facecream and facewash')
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.show()
#Problem 4
S_facecream = df ['facecream'].sum()
S_facewash= df ['facewash'].sum()
S_toothpaste = df ['toothpaste'].sum()
S_bathingsoap = df ['bathingsoap'].sum()
S_shampoo = df ['shampoo'].sum()
S_paper = df ['paper'].sum()
Weight = np.array([S_facecream,S_facewash,S_toothpaste,S_bathingsoap,S_shampoo,S_paper])
mylabels = ['facecream','facewash','toothpaste','bathingsoap','shampoo','paper']
plt.pie(Weight,labels=mylabels,autopct='%1.1f%%')
plt.title('Ratio of each product')
plt.show()
#Problem 5
plt.subplot(1,2,1)
plt.xticks(monthList)
plt.plot(monthList,toothpaste)
plt.xlabel("Month")
plt.ylabel("Amount")
plt.grid(True)
plt.title("Toothpaste")
plt.subplot(1,2,2)
plt.xticks(monthList)
plt.plot(monthList,shampoo)
plt.title("Shampoo")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.grid(True)
plt.show()
#Problem 6
data = {
    "month_number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "facecream": [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    "facewash": [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    "toothpaste": [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    "bathingsoap": [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400],
    "shampoo": [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800],
    "paper": [1652, 2765, 1357, 1345, 1740, 1632, 2567, 2456, 1456, 2678, 2246, 3445]
}

plt.stackplot(data["month_number"], data["facecream"], data["facewash"], data["toothpaste"], data["bathingsoap"], data["shampoo"], data["paper"], labels=['Facecream', 'Facewash', 'Toothpaste', 'Bathingsoap', 'Shampoo', 'Paper'])
plt.xlabel('Month')
plt.ylabel('Quantity')
plt.title('Stack Plot of all Items')
plt.legend()
plt.show()