import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/random')
def get_random():
    randLegend = random.choice(legends)
    randGun1 = random.choice(guns)
    randGun2 = random.choice(guns)
    
    return jsonify({
        'legend': randLegend,
        'gun1': randGun1,
        'gun2': randGun2
    })

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's port if available
    app.run(host='0.0.0.0', port=port, debug=False)