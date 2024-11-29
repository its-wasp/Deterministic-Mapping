import json
from fuzzywuzzy import fuzz
from find_unclean_attributes import categorize_medicine as categorize_medicine_unclean
from find_master_attributes import categorize_medicine as categorize_medicine_master
import random

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
    return total_score

def find_best_match(d2, json_file):
    # best_match = None
    best_score = 0.0
    with open(json_file, "r") as file:
        data = json.load(file)
    for key, value in data.items():
        d1 = categorize_medicine_master(value)
        if not d1["name"]:
            continue
        # Compare the dictionaries
        final_score = compare_dicts(d1, d2, weights)
        if final_score > best_score:
            best_score = final_score
            best_match = value

    # print("\nBest Match:")
    # print(best_match)
    # print(f"\nFinal Similarity Score: {best_score:.2f}")
    return best_score

def find_bests(lis,idx):
    subset = lis[idx:idx+20]
    total_score = 0
    for item in subset:
        d2 = categorize_medicine_unclean(item[1])
        # print(d2)
        total_score += find_best_match(d2, "clean_data.json")
    return total_score / len(subset)
def test(json_file, n):
    with open(json_file, "r") as file:
        data = json.load(file)
        lis = list(data.items())
        avglis = []  # Store averages separately
        for i in range(n):
            idx = random.randint(0,1000)
            avg_score = find_bests(lis,idx)  # Calculate average score
            avglis.append(avg_score)  # Store in avglis
    return avglis  # Return the list of averages

# Run the test
avglis = test("unclean_data.json", 5)
print(avglis)
ans = sum([x for x in avglis]) / len(avglis)
print(ans)