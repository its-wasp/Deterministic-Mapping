import json
import argparse
from find_attributes import categorize_medicine
from single_example_compare import test_single_input
def remark(score):
    """Returns a remark based on the score."""
    if score >= 0.90:
        return "Exact Match"
    elif score >= 0.8:
        return "Highly Similar"
    elif score >= 0.7:
        return "Similar"
    else:
        return "No Match"

def mapping(unclean_file, clean_file):
    """Maps every unclean data to the master data from clean file and returns a new json file named 'mapped_data.json'."""
    with open(unclean_file, "r") as file:
        unclean_data = json.load(file)
    
    mapped_data = {}

    for key, value in list(unclean_data.items()):
        print(f"Mapping {key} .... ")
        best_match, score = test_single_input(value, clean_file)  
        remark_ = remark(score)
        mapped_data[key] = {
            "unclean_data": categorize_medicine(value, is_master=False),
            "master_data": best_match[1], 
            "score": score,
            "remark": remark_
        }

    with open("mapped_data.json", "w") as file:
        json.dump(mapped_data, file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Map unclean data to master data and generate a mapped JSON file.")
    parser.add_argument("unclean_file", help="The file name of the unclean data JSON to process")
    parser.add_argument("clean_file", help="The file name of the clean data JSON to be used as a reference")
    args = parser.parse_args()

    mapping(args.unclean_file, args.clean_file)