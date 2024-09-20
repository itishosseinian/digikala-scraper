import httpx
import json

base_url = "https://api.digikala.com/v1/incredible-offers/products/?page="


response = httpx.get(base_url + "1", timeout=httpx.Timeout(30.0))
data = json.loads(response.text)

total_pages = data['data']['pager']['total_pages']

parsed_data = []

for page in range(1, total_pages):
    url = base_url + str(page)
    print(f"Working on {url}")
    response = httpx.get(url, timeout=httpx.Timeout(30.0))
    data = json.loads(response.text)
    products = data['data']['products']
    
    for pro in products:
        parsed_data.append({
            'id': pro['id'],
            'title': pro['title_fa'],
            'product_url': pro['url'],
            'images': pro['images'],
            'colors': pro['colors'],
            'org_price': str(pro['default_variant']['price']['rrp_price']) + ' toman' if pro['default_variant'] else 'None',
            'incredible_price': str(pro['default_variant']['price']['selling_price']) + ' toman' if pro['default_variant'] else 'None'
        })
    break
    
filename = 'digikala.json'

with open(filename, 'w', encoding='utf-8') as file:
    json.dump(parsed_data, file, ensure_ascii=False, indent=4)

print("Data has been saved to " + filename)
