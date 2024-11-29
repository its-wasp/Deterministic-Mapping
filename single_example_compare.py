import json
from fuzzywuzzy import fuzz
from find_unclean_attributes import categorize_medicine as categorize_medicine_unclean
import random
from find_master_attributes import categorize_medicine as categorize_medicine_master
weights = {
    "name": 0.4, 
    "type": 0.2,      
    "quantity": 0.05,  
    "content": 0.3,  
    "type_name": 0.05  
}
def compare_dicts(dict1, dict2, weights):
    total_score = 0.0
    for key, weight in weights.items():
        value1 = dict1.get(key, "")
        value2 = dict2.get(key, "")
        if not value1 or not value2:
            similarity = 1
        else:
            similarity = fuzz.ratio(str(value1).lower(), str(value2).lower()) / 100
        weighted_score = similarity * weight
        total_score += weighted_score
        # print(f"Key: {key}, Value1: '{value1}', Value2: '{value2}', Similarity: {similarity:.2f}, Weighted Score: {weighted_score:.2f}")
    return total_score

def find_best_match(d2, json_file):
    best_match = None
    best_score = 0.0

    with open(json_file, "r") as file:
        data = json.load(file)
        # print(f"Total records in JSON: {len(data)}")

    for key, value in data.items():
        
        d1 = categorize_medicine_master(value)
        if not d1["name"]:
            continue
        # Compare the dictionaries
        final_score = compare_dicts(d1, d2, weights)
        if final_score > best_score:
            best_score = final_score
            best_match = value
    print(best_match)
    print(best_score)




dict1 = {
    "c_barcode": ".",
    "j_alternatives": [],
    "c_hsn_code": "30049099",
    "c_gst": "12.00",
    "c_stock_availability": "0",
    "j_molecules": [
        {
            "c_molecule_code": "MC0290",
            "c_molecule_name": "CLINIDIPINE",
            "c_description": "Calcium channel blocker, Antihypertensive agent",
            "c_usage": "Tablet",
            "c_note": "HypertensionStrokeAnginaHeart attack",
            "c_side_effect": "Category C/ Risk in animals, risk cannot be ruled out in humans",
            "c_contra_indications": "Hypersensitivity to Clinidipine Low blood pressure due to cardiogenic shock"
        }
    ],
    "c_item_code": "191877",
    "c_item_name": "CILACAR 10MG TAB",
    "c_pack_name": "10`S",
    "c_mfg_code": "M01216",
    "c_mfg_name": "J. B. CHEMICALS & PHARMACEUTICALS LTD.",
    "n_mrp": 193.65,
    "n_pack_size": 10,
    "j_item_thumbnail_images": [
        {
            "c_thumbnail_image": "NaN"
        }
    ],
    "c_contains": "CILNIDIPINE",
    "c_watchlist_status": "N",
    "c_shortbook_status": "N",
    "c_discount_status": "N",
    "c_pack_type_name": "STRIPS",
    "j_item_images": [
        {
            "c_item_image": "NaN"
        }
    ],
    "category": "MEDICINE"
}
d2 = categorize_medicine_unclean(dict1)
print(d2)
find_best_match(d2, "clean_data.json")