import scraper
import file_manager
import sys

print("Starting price tracking")

API_URL = "https://www.a1.bg/mgw-web/eshop/products/grid?PriceTypeFilter=2&DeviceType=Smartphone&PresetCollectionId=1&CurrentPage=1&perPage=100"

products = scraper.get_product_details(API_URL)
if not products:
    print("Error while fetching")
    sys.exit()
    
print(f"Successfully fetched {len(products)} products from A1")

history = file_manager.load_history()

alerts_triggered = 0

for prod in products:
    name = prod["name"]
    link = prod["link"]
    price = prod["price"]
    
    analysis = file_manager.update_and_check_product(history, name, link, price)
    
    if analysis:
        if analysis["drop_price"]:
            old_price = analysis["old_price"]
            diff = old_price - price
            percentage = (diff / old_price) * 100
            print(f"\n Price drop detected")
            print(f"  Device: {name}")
            print(f"  Old Price: {old_price} EURO | New Price: {price} EURO (-{percentage:.2f}%)")
            print(f"  Buy: {link}")
            alerts_triggered += 1
            
            
file_manager.save_history(history)
print(f"\n Update session finished. Active Alerts Triggered: {alerts_triggered}")