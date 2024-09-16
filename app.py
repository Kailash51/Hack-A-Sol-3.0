from flask import Flask, render_template, request
import pandas as pd
import os  
app = Flask(__name__)


rural_areas = [
    'Manali', 'Solang', 'Naggar', 'Kasol', 'Tirthan Valley',
    'Dharamshala', 'Palampur', 'Bir', 'Kangra', 'Kullu'
]
hilly_areas = [
    'Rohtang Pass', 'Triund', 'Churdhar Peak', 'Parvati Valley', 'Hampta Pass',
    'Kheer Ganga', 'Great Himalayan National Park', 'Bhrigu Lake', 'Beas Kund', 'Malana'
]

@app.route('/')
def index():
    return render_template('index.html', rural_areas=rural_areas, hilly_areas=hilly_areas)

@app.route('/predict', methods=['POST'])
def predict():
    selected_rural_area = request.form.get('rural_area')
    selected_hilly_area = request.form.get('hilly_area')

    connectivity_possible = True 
    cost_plan = {'material': 50000, 'labour': 30000, 'maintenance': 20000}  
    
    return render_template('prediction.html', 
                            rural_area=selected_rural_area, 
                            hilly_area=selected_hilly_area,
                            connectivity_possible=connectivity_possible, 
                            cost_plan=cost_plan)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
