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

area_costs = {
    'Manali': {'material': 75, 'labour': 45, 'maintenance': 30},
    'Solang': {'material': 82, 'labour': 48, 'maintenance': 35},
    'Naggar': {'material': 65, 'labour': 38, 'maintenance': 28},
    'Kasol': {'material': 70, 'labour': 42, 'maintenance': 32},
    'Tirthan Valley': {'material': 85, 'labour': 50, 'maintenance': 38},
    'Dharamshala': {'material': 68, 'labour': 40, 'maintenance': 30},
    'Palampur': {'material': 62, 'labour': 36, 'maintenance': 26},
    'Bir': {'material': 58, 'labour': 34, 'maintenance': 25},
    'Kangra': {'material': 60, 'labour': 35, 'maintenance': 27},
    'Kullu': {'material': 72, 'labour': 43, 'maintenance': 33},
    'Rohtang Pass': {'material': 95, 'labour': 58, 'maintenance': 45},
    'Triund': {'material': 78, 'labour': 46, 'maintenance': 35},
    'Churdhar Peak': {'material': 88, 'labour': 52, 'maintenance': 40},
    'Parvati Valley': {'material': 80, 'labour': 48, 'maintenance': 36},
    'Hampta Pass': {'material': 92, 'labour': 55, 'maintenance': 42},
    'Kheer Ganga': {'material': 85, 'labour': 50, 'maintenance': 38},
    'Great Himalayan National Park': {'material': 90, 'labour': 54, 'maintenance': 41},
    'Bhrigu Lake': {'material': 83, 'labour': 49, 'maintenance': 37},
    'Beas Kund': {'material': 76, 'labour': 45, 'maintenance': 34},
    'Malana': {'material': 87, 'labour': 51, 'maintenance': 39}
}

@app.route('/')
def index():
    return render_template('index.html', rural_areas=rural_areas, hilly_areas=hilly_areas)

@app.route('/predict', methods=['POST'])
def predict():
    selected_rural_area = request.form.get('rural_area')
    selected_hilly_area = request.form.get('hilly_area')
    
    # Define the non-feasible areas (last 4 from each list)
    non_feasible_rural = ['Dharamshala', 'Palampur', 'Bir', 'Kangra']
    non_feasible_hilly = ['Great Himalayan National Park', 'Bhrigu Lake', 'Beas Kund', 'Malana']
    
    # Check if selected areas are in non-feasible lists
    if selected_rural_area in non_feasible_rural or selected_hilly_area in non_feasible_hilly:
        # Return zero costs for non-feasible areas
        cost_plan = {
            'material': 0,
            'labour': 0,
            'maintenance': 0,
            'total': 0
        }
        connectivity_possible = False
    else:
        # Get costs based on selected areas
        rural_costs = area_costs[selected_rural_area]
        hilly_costs = area_costs[selected_hilly_area]
        
        # Calculate average costs between the two areas
        cost_plan = {
            'material': (rural_costs['material'] + hilly_costs['material']) // 2,
            'labour': (rural_costs['labour'] + hilly_costs['labour']) // 2,
            'maintenance': (rural_costs['maintenance'] + hilly_costs['maintenance']) // 2
        }
        
        # Calculate total cost
        cost_plan['total'] = cost_plan['material'] + cost_plan['labour'] + cost_plan['maintenance']
        connectivity_possible = True
    
    return render_template('prediction.html',
                         rural_area=selected_rural_area,
                         hilly_area=selected_hilly_area,
                         connectivity_possible=connectivity_possible,
                         cost_plan=cost_plan)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
