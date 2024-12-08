from find_attributes import categorize_medicine
from comparison import find_best_match
import json
import random

def test_single_input(unclean_input, clean_file):
    """finds the best match present in the master for a single unclean input"""

    d2 = categorize_medicine(unclean_input, is_master=False)
    best_m = find_best_match(d2, clean_file)
    return best_m[0], best_m[1]


def test_one_random_input():
    with open("unclean_data.json", "r") as file:
        data = json.load(file)

    key, value = random.choice(list(data.items()))
    best_match, score = test_single_input(value)
    print(f"Unclean Input: {key} : {categorize_medicine(value, is_master=False)}")
    print(f"Best Match: {best_match[0]} : {categorize_medicine(best_match[1])}")
    print(f"Score: {score}")
    print("\n")
    
if __name__ == "__main__":
    
    #testing one input 
    
    unclean_input = {
        "c_barcode": ".",
        "j_alternatives": [],
        "c_hsn_code": "3004",
        "c_gst": "12.00",
        "c_stock_availability": "0",
        "j_molecules": [
            {
                "c_molecule_code": "MC0771",
                "c_molecule_name": "MENTHOL",
                "c_description": "Antitussive oropharyngeal",
                "c_usage": "Lozenges",
                "c_note": "FDA labeled pharyngitis                       Cough",
                "c_side_effect": "Category C/ Risk in animals, risk cannot be ruled out in humans",
                "c_contra_indications": "Hypersensitivity to menthol"
            },
            {
                "c_molecule_code": "MC0786",
                "c_molecule_name": "METHYL SALICYLATE",
                "c_description": "Analgesic ",
                "c_usage": "Topical creams Lotions ",
                "c_note": "Analgesia for minor muscle and joint pains",
                "c_side_effect": "Category C/ Risk in animals, risk cannot be ruled out in humans",
                "c_contra_indications": "Hypersentivity to methyl salicylate "
            },
            {
                "c_molecule_code": "MC0391",
                "c_molecule_name": "DICLOFENAC DIMETHYLAMINE",
                "c_description": "Phenylacetic acid derivative, Non Steroidal Anti Inflammatory Drug (NSAID)",
                "c_usage": "Tablet, capsule, Intravenous (IV),  Opthalmic solution            Topical : Gel, Patch",
                "c_note": "Muscle and joint pain due to sprains",
                "c_side_effect": "Category C/ Risk in animals, risk cannot be ruled out in humans",
                "c_contra_indications": "Pregnancy (3rd trimester), Asthmatic attacksRhinitisUrticaria"
            },
            {
                "c_molecule_code": "MC0719",
                "c_molecule_name": "LINSEED OIL",
                "c_description": "Cardiovascular herbal, dermatology herbal, gastrointestinal herbal",
                "c_usage": "Oils, seed",
                "c_note": "Bowel obstructionDry eyeConstipation",
                "c_side_effect": "Category X/ Contraindicated in pregnancy",
                "c_contra_indications": "EndometriosisBleeding disordersUterine fibroids"
            }
        ],
        "c_item_code": "545884",
        "c_item_name": "NERVSHINE GEL",
        "c_pack_name": "30GM",
        "c_mfg_code": "M00130",
        "c_mfg_name": "AKUMENTIS HEALTHCARE (DELIGHTS)",
        "n_mrp": 192.0,
        "n_pack_size": 1,
        "j_item_thumbnail_images": [
            {}
        ],
        "c_contains": "DICLOFENAC+LINSEED OIL+MENTHOL+METHYL SALICYLATE",
        "c_watchlist_status": "N",
        "c_shortbook_status": "N",
        "c_discount_status": "N",
        "c_pack_type_name": "BOTTLE",
        "j_item_images": [
            {}
        ],
        "category": "MEDICINE"
    }
    
    best_match, score = test_single_input(unclean_input, "clean_data.json")
    print(f"Unclean Input: {categorize_medicine(unclean_input, is_master=False)}")
    print("\n")
    print(f"Best Match: {best_match[0]} : {categorize_medicine(best_match[1])}")
    print(f"Score: {score}")
    print("\n")
    
    #tesing one random input
    
    # test_one_random_input()