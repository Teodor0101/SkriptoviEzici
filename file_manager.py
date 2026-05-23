import json
import os
from datetime import datetime

DATA_FILE = "price_history.json"

def load_history():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_history(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def update_and_check_product(history, name, url, price):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_entry = {
        "timestamp": timestamp,
        "price": price,
    }
    
    analysis = None
    
    if name in history:
        product_data = history[name]
        previous_history = product_data["history"]
        
        if previous_history:
            last_entry = previous_history[-1]
            old_price = last_entry["price"]
            
            drop_price = price < old_price
            
            analysis = {
                "old_price": old_price,
                "drop_price": drop_price,
            }

        product_data["history"].append(new_entry)
        product_data["url"] = url
    else:

        history[name] = {
            "url": url,
            "history": [new_entry]
        }
        
    return analysis
