from flask import Flask, request, jsonify
from db_helpers import run_query
import sys

app = Flask(__name__)

@app.get('/api/animals')
def animals_get():
    # TODO: db SELECT
    animal_list = []
    return jsonify(animal_list), 200
@app.post('/api/animals')
def animals_post():
    data = request.json
    animal_name = data.get('animalName')
    image_url = data.get('imageURL')
    if not animal_name:
        return jsonify("Missing required argument 'animalName'"), 422
    if not image_url:
        return jsonify("Missing required argument 'imageURL'"), 422
    # TODO: Error checking the actual values for the arguments
    # TODO: DB write
    





if (len(sys.argv) > 1):
    mode = sys.argv[1]
else:
    print("No mode argument: testing | production")
    exit()    
    
if mode == "testing":
    from flask_cors import CORS
    CORS(app)    # Only want CORS on testing servers
    app.run(debug=True)
elif mode == "production":
    import bjoern
    bjoern.run(app, "0.0.0", 5000)
    print('Running in development mode!')
else:
    print("Invalid mode.  Must be testing or production")