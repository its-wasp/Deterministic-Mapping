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
    """Cleans up text according to the clean_up_regexes dictionary."""
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
    content = clean_text(data.get(content_key, "").lower().strip()).replace("plus ", "").strip()
    
    content = re.sub(r"\b[a-z]\b|\.|\d+|%", "", content).replace("  ", "").strip() #removing single characters, digits, %, . and extra spaces
    
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
        "c_hsn_code": "30049029",
        "c_gst": "12.00",
        "c_stock_availability": "0",
        "j_molecules": [
            {
                "c_molecule_code": "MC0873",
                "c_molecule_name": "OFLOXACIN",
                "c_description": "Antibacterial, Antibiotic, Fluoroquinolone",
                "c_usage": "Oral tablet, ophthalmic solution",
                "c_note": "FDA labeled - Acute otitis media, Bacterial conjunctivitis, Chlamydial infection, Community acquired pneumonia, Corneal ulcer, Cystitis, Gonorrhea, Infection of skin, Pelvic inflammatory disease, Prostatitis, Urinary tract infection, Infection due to staphylococcus aureus, Nongonococcal urethritisNON-FDA labeled - Helicobacter pylori gastrointestinal tract infection, Leprosy, Tuberculosis, Typhoid fever, Upper respiratory tract infection, Infective cholangitis, Sepsis.",
                "c_side_effect": "Category C/ Risk in animals, risk cannot be ruled out in humans",
                "c_contra_indications": "hypersensitive to ofloxacin or other quinolones."
            },
            {
                "c_molecule_code": "MC0886",
                "c_molecule_name": "ORNIDAZOLE",
                "c_description": "Antiprotozoal, Antiparasitic, Nitro imidazole",
                "c_usage": "TabletInjectionOral Suspension",
                "c_note": "FDA Labeled -AmoebiasisAnaerobic bacterial infectionsChlamydia infectionGiardiasisSurgical site infectionsVaginal infectionsTrichomoniasis",
                "c_side_effect": "Category C/ Risk in animals, risk cannot be ruled out in humans",
                "c_contra_indications": "Hypersensitivity to ornidazole or other nitro imidazole derivatives"
            },
            {
                "c_molecule_code": "MC1179",
                "c_molecule_name": "TERBINAFINE",
                "c_description": "Antifungal, Allylamine",
                "c_usage": "TabletsOral granulesTopiccal solutionsCreams",
                "c_note": "FDA labeled Dermal mycosisOnychomycosis due to dermatophyteTinea capitisNON-FDA labeled Seborrheic dermatitis",
                "c_side_effect": "Category C/ Risk in animals, risk cannot be ruled out in humans",
                "c_contra_indications": "Chronic liver diseaseHistory of Allergic reaction to oral Terbinafine"
            },
            {
                "c_molecule_code": "MC0313",
                "c_molecule_name": "CLOBETASOL",
                "c_description": "Corticosteroid",
                "c_usage": "Topical creamLotionOintment",
                "c_note": "FDA Labeled :Disorder of skinPlaque psoriasisScalp psoriasisNon-FDA Labeled :Genital lichen sclerosisVesicular stomatitis",
                "c_side_effect": "Category B/ No evidence of risk in animals but limited human model studies",
                "c_contra_indications": "Hypersensitivity to clobetasolPrimary scalp infectionOpthalmic use"
            }
        ],
        "c_item_code": "368145",
        "c_item_name": "DERMIKEM OC CREAM",
        "c_pack_name": "15GM",
        "c_mfg_code": "M00178",
        "c_mfg_name": "ALKEM LABORATORIES (GENERIC/FUTURA)",
        "n_mrp": 92.0,
        "n_pack_size": 1,
        "j_item_thumbnail_images": [
            {}
        ],
        "c_contains": "CLOBETASOL+OFLOXACIN+ORNIDAZOLE+TERBINAFINE",
        "c_watchlist_status": "N",
        "c_shortbook_status": "N",
        "c_discount_status": "N",
        "c_pack_type_name": "TUBE",
        "j_item_images": [
            {}
        ],
        "category": "MEDICINE"
    }

    clean_input = {
        "name": "Dermikem OC Cream",
        "price": 84,
        "manufacturer_name": "Alkem Laboratories Ltd",
        "pack_size_label": "tube of 15 gm Cream",
        "content": "Terbinafine (1% w/w) + Clobetasol (0.05% w/w) + Ofloxacin (0.75% w/w) + Ornidazole (2% w/w)"
    }
    
    #checking the output attribute dictionaries
    
    print(f"Unclean Input: {categorize_medicine(unclean_input, is_master=False)}")
    print(f"Master Input: {categorize_medicine(clean_input)}")   