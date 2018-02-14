import json
from flask import jsonify

class PlantJsonBuilder:
    
    def build(plant, recent_readings):
        plantJson = jsonify(plant=plant.serialize())
        recentReadingsJson = jsonify(recent_readings=[reading.serialize() for reading in recent_readings])
        plantDetailsJson = {'plant':plantJson, 'recentReadings': recentReadingsJson}
        return json.dumps(plantDetailsJson)