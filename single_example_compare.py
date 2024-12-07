from find_attributes import categorize_medicine
from comparison import find_best_match
import json
import random

def test_single_input(unclean_input):
    """finds the best match present in the master for a single unclean input"""

    d2 = categorize_medicine(unclean_input, is_master=False)
    best_m = find_best_match(d2, "clean_data.json")
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
    
    # unclean_input = {
    #     "c_barcode": ".",
    #     "j_alternatives": [],
    #     "c_hsn_code": "30049061",
    #     "c_gst": "12.00",
    #     "c_stock_availability": "0",
    #     "j_molecules": [
    #         {
    #             "c_molecule_code": "MC0910",
    #             "c_molecule_name": "PARACETAMOL",
    #             "c_description": "Analgesic, Antipyretic",
    #             "c_usage": "Oral Tablet -  Chewable, Disentegrate,  Intravenous solution, Suspension, Rectal suppository",
    #             "c_note": "FDA labeled - Fever, mild to moderate pain, pain in combination with opioidsNON-FDA labeled - Migraine",
    #             "c_side_effect": "Category C/ Risk in animals, risk cannot be ruled out in humans",
    #             "c_contra_indications": "acute and severe hepatic diseases, severe hepatic impairment, hypersensitivity to acetaminophen"
    #         }
    #     ],
    #     "c_item_code": "192032",
    #     "c_item_name": "DOLO DROPS 15ML",
    #     "c_pack_name": "15ML",
    #     "c_mfg_code": "M01566",
    #     "c_mfg_name": "MICRO LABS (GTF 1)",
    #     "n_mrp": 30.07,
    #     "n_pack_size": 1,
    #     "j_item_thumbnail_images": [
    #         {
    #             "c_thumbnail_image": "https://lcitemimages.blob.core.windows.net/item-images/20211109/dolo_drops_15ml_0_29111.jpg"
    #         }
    #     ],
    #     "c_contains": "PARACETAMOL",
    #     "c_watchlist_status": "N",
    #     "c_shortbook_status": "N",
    #     "c_discount_status": "N",
    #     "c_pack_type_name": "DROPS",
    #     "j_item_images": [
    #         {
    #             "c_item_image": "https://lcitemimages.blob.core.windows.net/item-images/20211109/dolo_drops_15ml_0_29111.jpg"
    #         }
    #     ],
    #     "category": "MEDICINE"
    # }
    
    # best_match, score = test_single_input(unclean_input)
    # print(f"Unclean Input: {categorize_medicine(unclean_input, is_master=False)}")
    # print(f"Best Match: {best_match[0]} : {categorize_medicine(best_match[1])}")
    # print(f"Score: {score}")
    # print("\n")
    
    #tesing one random input
    
    test_one_random_input()