import random
import tkinter as tk
from tkinter import messagebox
legends = [
    "Alter","Ash","Ballistic","Bangalore","Bloodhound","Catalyst","Caustic","Conduit",
    "Crypto","Fuse","Gibraltar","Horizon","Lifeline","Loba","Mad Maggie","Mirage",
    "Newcastle","Octane","Pathfinder","Rampart","Revenant","Seer","Sparrow","Valkyrie",
    "Vantage","Wattson","Wraith"
]

guns = [
    "Havoc","Flatline","Hemlok","R-301","Nemesis","Alternator","Prowler","R-99","Volt","CAR",
    "Devotion","L-STAR","Spitfire","Rampage","G7 Scout","Triple Take","30-30","Bocek",
    "Charge Rifle","Longbow","Kraber","Sentinel","EVA-8","Mastiff","Mozambique","Peacekeeper",
    "RE-45","P2020","Wingman"
]

randLegend = legends[random.randrange(0,len(legends))]
randGun1 = guns[random.randrange(0,len(guns))]
randGun2 = guns[random.randrange(0,len(guns))]


root = tk.Tk()
root.withdraw()

message = f"Legend: {randLegend}\nGun 1: {randGun1}\nGun 2: {randGun2}"
messagebox.showinfo("Your Random Loadout", message)