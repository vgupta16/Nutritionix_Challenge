from flask import Flask, send_file, request
from nutritionix import Nutritionix
import json
app = Flask(__name__)

# Retrieve keys from https://developer.nutritionix.com/signup
nix = Nutritionix(app_id="", api_key="")

@app.route('/')
def index():
    return send_file("templates/index.html")

@app.route('/search', methods=['POST'])
def search():
	parsed_request = json.loads(request.data)
	search_query = parsed_request['data']
	json_return = []
	try:
		#query the top five hits from the api
		search_result = nix.search(search_query, results='0:5').json()
		for item in search_result['hits']:
			item_dict = {}
			item_dict['brand'] = item['fields']['brand_name']
			item_id = item['_id']
			item_info = nix.item(id=item_id).json()
			parsed = parse_result(item_info)
			item_dict.update(parsed)
			json_return.append(item_dict)

		return json.dumps(json_return)
	
	except:
		return json.dumps([])

# Helper function to exctract out certain nutritional information
def parse_result(result):
	nutrition_info = {}
	nutrition_info['serving_size'] = result['nf_serving_size_qty']
	nutrition_info['serving_unit'] = result['nf_serving_size_unit']
	nutrition_info['carbs'] = result['nf_total_carbohydrate']
	nutrition_info['calories'] = result['nf_calories']
	nutrition_info['protein'] = result['nf_protein']
	nutrition_info['fat'] = result['nf_total_fat']

	return nutrition_info
 

if __name__ == '__main__':
    app.run(debug=False)
