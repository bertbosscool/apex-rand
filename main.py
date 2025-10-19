import random

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

RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
BOLD = '\033[1m'
RESET = '\033[0m'

print(f"{CYAN}{BOLD}")
print("╔═══════════════════════════════════════════╗")
print("║                                           ║")
print("║      🎮  APEX LEGENDS RANDOMIZER  🎮      ║")
print("║                                           ║")
print("╚═══════════════════════════════════════════╝")
print(RESET)
print()
print(f"{MAGENTA}┌───────────────────────────────────────────┐{RESET}")
print(f"{MAGENTA}│{RESET}  {BOLD}LEGEND:{RESET}  {RED}{BOLD}{randLegend:^30}{RESET}  {MAGENTA}│{RESET}")
print(f"{MAGENTA}├───────────────────────────────────────────┤{RESET}")
print(f"{MAGENTA}│{RESET}  {BOLD}GUN 1:{RESET}   {YELLOW}{randGun1:^30}{RESET}  {MAGENTA}│{RESET}")
print(f"{MAGENTA}│{RESET}  {BOLD}GUN 2:{RESET}   {YELLOW}{randGun2:^30}{RESET}  {MAGENTA}│{RESET}")
print(f"{MAGENTA}└───────────────────────────────────────────┘{RESET}")
print()
print(f"{CYAN}✨ Good luck, Legend! Drop hot and get that W! ✨{RESET}")