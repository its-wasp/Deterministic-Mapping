import re
def remove_brackets(text):
    """Remove any content within brackets (square, round, or curly)."""
    return re.sub(r"\[.*?\]|\(.*?\)|\{.*?\}", "", text).strip()

def categorize_medicine(medicine_data):
    # Define the mapping of keywords to types
    type_mapping = {
        "Tablet": "TAB",
        "Capsule": "CAP",
        "Syrup": "SYP",
        "Powder": "POWDER",
        "Cream": "OINT",  
        "Injection": "INJ",
        "Suspension": "SUSP",
        "Eye Drop": "EYE DROP",
        "Jelly": "JELLY",
        "Drop": "DROP",
        "Gel": "GEL",
        "Nasal Spray": "NASAL SPRAY",
        "Bottle": "BOTTLE",
        "Strip": "STRIP",
        "Tube" : "TUBE",
        "Sachet": "SACHET",
        "Eye Ointment": "EYE OINTMENT",
    }
    # Initialize variables
    med_type = None
    quantity = None
    content = medicine_data.get("content", "")  # Get content
    pack_size_label = medicine_data.get("pack_size_label", "")  # Get pack size label
    name = medicine_data.get("name", "").upper()  # Get name and make uppercase

    # Remove brackets from content
    clean_content = remove_brackets(content)

    # Identify the type based on keywords in the name
    for keyword, med_type_name in type_mapping.items():
        if keyword in name:
            med_type = med_type_name
            name = name.replace(keyword, "").strip()  # Remove type keyword from name
            break

    # Extract the quantity (e.g., 15 mg) from content or pack_size_label
    quantity_match = re.search(r"\b\d+\s?(mg|ml|gm|kg)\b", pack_size_label + " " + content, re.IGNORECASE)
    if quantity_match:
        quantity = quantity_match.group(0).lower()

    # Extract type_name (e.g., "bottle")
    type_name_match = re.search(r"\bbottle|strip|vial|tube|sachet\b", pack_size_label, re.IGNORECASE)
    type_name = type_name_match.group(0).lower() if type_name_match else None

    # Remove numbers, units, and excess words from the name to keep only the core name
    name = re.sub(r"\b(\d+mg|\d+ml|\d+gm|\d+kg|tablet|capsule|syrup|powder|cream|injection|suspension|eye drop|jelly)\b", "", name, flags=re.IGNORECASE)
    name = re.sub(r"\s+", " ", name).strip()  # Remove extra spaces

    # Return the formatted dictionary
    return {
        "name": name.strip(),
        "type": med_type,
        "quantity": quantity,
        "content": clean_content.strip(),
        "type_name": type_name
    }
