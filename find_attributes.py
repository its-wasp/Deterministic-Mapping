import re
from data_normalization_dictionaries import clean_up_regexes, substitution

def get_substitution_regex(substitute):
    condition_regexes = {
        'anything': r".*",
        'digits': r"\s?\d+\s?",
        'words': r"\w+",
        'not first': r"(?<!^)",
        'beginning': r"^",
        'ending':  r"$",
    }

    regex = r"|".join(substitute['words'])
    regex = "(?:" + regex + ")"

    if substitute.get("preConditions", None):
        pre_conditions = substitute["preConditions"]
        for condition in pre_conditions:
            regex = condition_regexes[condition] + regex

    if substitute.get("postConditions", None):
        post_conditions = substitute["postConditions"]
        for condition in post_conditions:
            regex = regex + condition_regexes[condition]

    regex = r"\b(?<!\.)" + regex + r"(?!\.)\b"
    return regex

def clean_text(text):
    
    for _, (pattern, replacement) in clean_up_regexes.items():
        
        text = re.sub(pattern, replacement, text)
    return text  

def normalize_sku_name(name): 
    """Normalizes the SKU name."""
    
    item_name = name
    item_name = clean_text(item_name) #cleaning text before substitution
    for substitute_key in substitution:
        substitute = substitution[substitute_key]
        regex = get_substitution_regex(substitute)
        replacer = substitute["replacer"]
        item_name = re.sub(regex, replacer, item_name, re.IGNORECASE)  
    return item_name

def extract_quantity_from_pack_size(pack_size_label):
    """Extracts the quantity from the pack size label."""
    
    match = re.search(r"\d+\s*(mg|ml|gm|kg|\d*\s?[a-zA-Z]+|\d+)", pack_size_label, re.IGNORECASE)
    if match:
        return match.group(0).strip()
    return "Unknown"


def categorize_medicine(data, is_master=True):
    """Categorizes the medicine data into a dictionary."""
    
    name_key = "name" if is_master else "c_item_name"
    pack_size_key = "pack_size_label" if is_master else "c_pack_name"
    manufacturer_key = "manufacturer_name" if is_master else "c_mfg_name"
    content_key = "content" if is_master else "c_contains"
    
    name = normalize_sku_name(data.get(name_key, "").lower().strip())
    pack_size_label = data.get(pack_size_key, "").lower().strip()
    pack_size_quantity = extract_quantity_from_pack_size(pack_size_label)
    manufacturer = clean_text(data.get(manufacturer_key, "").lower().strip())
    
    if(is_master):
        content = clean_text(data.get(content_key, "").lower().strip()).replace("plus ", "").strip()
    else:
        content = clean_text(data.get(content_key, "").lower().strip())
    
    return {
        "name": name.strip(),
        "content": content.strip(),
        "manufacturer": manufacturer.strip(),
        "pack_size_quantity": pack_size_quantity.split(' ')[0] if len(pack_size_quantity.split()) > 1 and pack_size_quantity.split()[1] not in ['ml', 'mg', 'gm', 'kg'] else pack_size_quantity,
    }

if __name__ == "__main__":
    
    #example unclean_input and clean_input
    unclean_input = {
        "c_barcode": ".",
        "j_alternatives": [],
        "c_hsn_code": "30049099",
        "c_gst": "12.00",
        "c_stock_availability": "0",
        "j_molecules": [
            {
                "c_molecule_code": "MC0254",
                "c_molecule_name": "CELECOXIB",
                "c_description": "NSAIDs",
                "c_usage": "Oral capsulesOral solution",
                "c_note": "FDA -LabeledAnkylosing spondylitis, Management of signs and symptomsJuvenile rheumatoid arthritisMigraine, Acute; with or without auraOsteoarthritisPain, acutePrimary dysmenorrheaRheumatoid arthritisNON-FDA LabeledColorectal adenoma, Sporadic, High-risk patients; prophylaxisCoronary stent stenosis, Adjunct; Prophylaxis Gout, acutePostoperative pain, acute",
                "c_side_effect": "Category C/ Risk in animals, risk cannot be ruled out in humans",
                "c_contra_indications": "Hypersensitivity to the drugs which are hypersensitivity to to celecoxib or any components of the drug productHistory of asthma, Urticaria, or other allergic-type reactions after taking aspirin or other NSAIDs; severe, sometimes fatal, anaphylactic reactions to NSAIDs have been reported In the setting of CABG surgery In patients who have demonstrated allergic-type reactions to sulfoamides"
            }
        ],
        "c_item_code": "037065",
        "c_item_name": "CELCOX 100MG CAP",
        "c_pack_name": "10`S",
        "c_mfg_code": "M01376",
        "c_mfg_name": "LUPIN LIMITED (ENDEAVOUR)",
        "n_mrp": 172.9,
        "n_pack_size": 10,
        "j_item_thumbnail_images": [
            {
                "c_thumbnail_image": "NaN"
            }
        ],
        "c_contains": "CELECOXIB",
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

    clean_input = {
        "name": "Pozone-S 1500 Injection",
        "price": 230,
        "manufacturer_name": "Positif Life sciences",
        "pack_size_label": "vial of 1 Injection",
        "content": "Cefoperazone (1000mg) + Sulbactam (500mg)"
    }
    
    #checking the output attribute dictionaries
    
    print(f"Unclean Input: {categorize_medicine(unclean_input, is_master=False)}")
    print(f"Master Input: {categorize_medicine(clean_input)}")   