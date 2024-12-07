import json 
from find_attributes import categorize_medicine
from single_example_compare import test_single_input

def remark(score):
    """Returns a remark based on the score."""
    
    if score >= 0.95:
        return "Exact Match"
    elif score >= 0.8:
        return "Highly Similar"
    elif score >= 0.7:
        return "Similar"
    else:
        return "No Match"
def mapping(unclean_file):
    """Maps the every unclean data to the master data and returns a new json file named 'mapped_data.json'."""
    
    with open(unclean_file, "r") as file:
        unclean_data = json.load(file)
        
    mapped_data = {}
    
    for key, value in list(unclean_data.items()):
        print(f"Mapping {key} .... ")
        best_match, score = test_single_input(value)
        remark_ = remark(score)
        mapped_data[key] = {
            "unclean_data": categorize_medicine(value, is_master=False),
            "master_data": best_match[1],
            "score": score,
            "remark": remark_,
        }
    with open("mapped_data.json", "w") as file:
        json.dump(mapped_data, file, indent=4)
    
if __name__ == "__main__":
        
    mapping("unclean_data.json")