import re

def remove_brackets(text):
    # This function removes any content within square brackets [], round brackets (), or curly brackets {}
    return re.sub(r"\[.*?\]|\(.*?\)|\{.*?\}", "", text)

def categorize_medicine(medicine_data):
    # Define the mapping of keywords to types
    type_mapping = {
        "TAB": "Tablet",
        "CAP": "Capsule",
        "SYP": "Syrup",
        "POWDER": "Powder",
        "CREAM": "Cream",
        "INJ": "Injection",
        "SUSP": "Suspension",
        "EYE DROPS": "Eye Drop",
        "EYE DROP": "Eye Drop",
        "OINT": "Cream",
        "JELLY": "Jelly",
        "DROP": "Drop",
        "GEL": "Gel",
        "NASAL SPRAY": "Nasal Spray",
        "BOTTLE": "Bottle",
        "STRIP": "Strip",
        "TUBE": "Tube",
        "SACHET": "Sachet",
        "EYE OINTMENT": "Eye Ointment"
        
    }
    # Initialize variables
    med_type = None
    quantity = None
    content = medicine_data.get("c_contains", "")  # Get content (c_contains)
    type_name = medicine_data.get("c_pack_type_name", "")  # Get type_name (c_pack_type_name)

    # Remove brackets from the content (c_contains)
    clean_content = remove_brackets(content)

    # Identify the type based on keywords in c_item_name
    for keyword, med_type_name in type_mapping.items():
        if keyword in medicine_data["c_item_name"].upper():  # Case-insensitive comparison
            med_type = med_type_name
            break

    # Extract the quantity (last part containing a number and unit)
    quantity_parts = medicine_data["c_item_name"].split()
    for part in quantity_parts:
        if any(unit in part.upper() for unit in ["ML", "MG", "GM", "KG"]):
            quantity = part
            break

    # Extract the name (remaining part after removing type and quantity)
    name = medicine_data["c_item_name"]
    if med_type:
        name = name.upper().replace(med_type, "").strip()
    if quantity:
        name = name.replace(quantity, "").strip()

    # Clean name
    name = name.strip()

    # Return the dictionary with all required fields, including cleaned content
    return {
        "name": name,
        "type": med_type,
        "quantity": quantity,
        "content": clean_content,  # Add cleaned content (c_contains)
        "type_name": type_name  # Add type_name (c_pack_type_name)
    }
