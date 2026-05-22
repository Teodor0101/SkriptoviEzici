import requests

def get_product_details(url):
    print(f"Svurzvane s url:{url}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    response = requests.get(url, headers = headers)
   
    if response.status_code != 200:
        raise Exception(f"response didnt return status code 200, but status code {response.status_code}")
    
    data = response.json()

    products = []

    for item in data["Items"]:
        name = item["Name"]
        price = float(item["Specific"]["PriceMap"][0]["Price"][0]["Amount"])
        products.append({"name":name, "price":price})
    return products

print(get_product_details("https://www.a1.bg/mgw-web/eshop/products/grid?PriceTypeFilter=2&DeviceType=Smartphone&PresetCollectionId=1&CurrentPage=1&perPage=100"))
