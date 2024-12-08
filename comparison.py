from weights import WEIGHTS
from fuzzywuzzy import fuzz
import json 
from find_attributes import categorize_medicine

def compare_dicts(dict1, dict2, WEIGHTS):
    """Compares two dictionaries and returns a similarity score."""
    
    total_score = 0.0
    for key, weight in WEIGHTS.items():
        value1 = dict1.get(key, "")
        value2 = dict2.get(key, "")
        if not value1 or not value2:
            # Penalising the missing values
            continue
        
        if key == "name":
            if value1.split()[0].lower().strip() != value2.split()[0].lower().strip():
                weight = weight * 0.8 # penality for different brand names
        
        similarity = fuzz.ratio(str(value1).lower().strip(), str(value2).lower().strip()) / 100
        weighted_score = similarity * weight
        total_score += weighted_score
        
    return total_score
def find_best_match(d2, json_file):
    """Finds the best match for one unclean_dictionary in the json file(master)."""
    best_match = None
    best_score = 0.0
    with open(json_file, "r") as file:
        data = json.load(file)
        

    for key, value in data.items():
        
        d1 = categorize_medicine(value)
        if not d1["name"]:
            continue
        # Compare the dictionaries
        final_score = compare_dicts(d1, d2, WEIGHTS)
        if final_score > best_score:
            best_score = final_score
            best_match = key, value
    return best_match, best_score
