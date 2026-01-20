import csv

# Chat widget data from research
chat_data = {
    # Gorgias users
    "Pipcorn": "Gorgias",
    "Glorious Gaming": "Gorgias",
    "Varley": "Gorgias",
    "Lifepro Fitness": "Gorgias",
    "Caswell Massey": "Gorgias",
    "Magnetic Me": "Gorgias",
    "Dandelion Chocolate": "Gorgias",
    "Askinosie Chocolate": "Gorgias",
    "Chomps": "Gorgias",
    "Ghia": "Gorgias",
    "Brightland": "Gorgias",
    "Heatonist": "Gorgias",
    "Verve Coffee": "Gorgias",
    "Jones Road": "Gorgias",
    "Truly Beauty": "Gorgias",
    "Glossier": "Gorgias",
    "Summer Fridays": "Gorgias",
    "Cocokind": "Gorgias",
    "Naturium": "Gorgias",
    "Brooklyn Candle Studio": "Gorgias",
    "Blueland": "Gorgias",
    "Girlfriend Collective": "Gorgias",
    "Away": "Gorgias",
    "Gorjana": "Gorgias",
    "Vital Proteins": "Gorgias",
    "Bala": "Gorgias",
    "Wild One": "Gorgias",
    "Hello Bello": "Gorgias",
    "Kotn": "Gorgias",
    "Depology": "Gorgias",
    "Outstanding Foods": "Gorgias",
    "Firebelly Tea": "Gorgias",
    "True Botanicals": "Gorgias",
    "Indie Lee": "Gorgias",
    "Voluspa": "Gorgias",
    "CARIUMA": "Gorgias",
    "Canopy": "Gorgias",
    "Kinfield": "Gorgias",
    "Finn + Emma": "Gorgias",
    "Public Goods": "Gorgias",
    "Hatch": "Gorgias",
    "Beyond Yoga": "Gorgias",

    # Gladly users
    "Merit": "Gladly",
    "Allbirds": "Gladly",
    "Nisolo": "Gladly",
    "The Farmer's Dog": "Gladly",
    "Pact": "Gladly",
    "Alo Yoga": "Gladly",
    "Native Shoes": "Gladly",
    "Splits59": "Gladly",

    # Kustomer users
    "Catbird NYC": "Kustomer",
    "Summersalt": "Kustomer",
    "Pura Vida": "Kustomer",
    "Cuts": "Kustomer",
    "Burrow": "Kustomer",
    "Prose": "Kustomer",
    "Smalls": "Kustomer",
    "Halfday Travel": "Kustomer",
    "Bespoke Post": "Kustomer",

    # Zendesk users
    "American Tall": "Zendesk",
    "Moscot": "Zendesk",
    "Nom Nom": "Zendesk",
    "Gaiam": "Zendesk",
    "Sunny Health": "Zendesk",

    # Salesforce users
    "Drunk Elephant": "Salesforce",
    "Olaplex": "Salesforce",
    "Tonal": "Salesforce",
    "Bonobos": "Salesforce",
    "Sweaty Betty": "Salesforce",

    # Other vendors
    "Bloomscape": "HubSpot",
    "Homesick": "Tidio",
    "Everlane": "DigitalGenius",
    "Cotopaxi": "Forethought",
    "Outdoor Voices": "Alia",
    "Freshly Picked": "Redo",
    "Rothy's": "Globo",
    "Thrive Market": "Ada",
    "Pepper Palace": "tawk.to",
    "Arctic Fox": "Re:amaze",
    "Three Ships Beauty": "Freshworks",
    "Pair Eyewear": "DigitalGenius",
    "BioLite": "Remark",
    "Peloton": "Drift",
    "Liforme": "Zipchat",
    "JadeYoga": "Chatbot.com",

    # No widget (explicitly checked)
    "Stellar Eats": "",
    "Fishwife": "",
    "Bittermilk": "",
    "Diaspora Co": "",
    "Ritual Chocolate": "",
    "Herbivore Botanicals": "",
    "P.F. Candle Co.": "",
    "The Sill": "",
    "Vuori": "",
    "Thursday Boots": "",
    "Harry's": "",
    "Beardbrand": "",
    "Primary": "",
    "Casper": "",
    "Rifle Paper Co.": "",
    "ColourPop": "",
    "Function of Beauty": "",
    "Tracksmith": "",
    "Kyte Baby": "",
    "Little Sleepies": "",
    "Set Active": "",
    "Hiya Health": "",
    "Cymbiotika": "",
    "Goli": "",
    "MaryRuth Organics": "",
    "Honest Company": "",
    "Miansai": "",
    "United Sodas": "",
    "Haus": "",
    "Pulp Pantry": "",
    "Fruition Chocolate": "",
    "Xocolatl": "",
    "indi chocolate": "",
    "Kate's Real Food": "",
    "Momofuku": "",
    "Gobble": "",
    "BelliWelli": "",
    "Muddy Bites": "",
    "Popsmith": "",
    "Graza": "",
    "SŚAINT": "",
    "Fièra Cosmetics": "",
    "Maelys": "",
    "Laura Geller": "",
    "Kylie Cosmetics": "",
    "NCLA Beauty": "",
    "Ouai": "",
    "Innersense": "",
    "Paddywax": "",
    "Harlem Candle Co.": "",
    "TOV Furniture": "",
    "Poketo": "",
    "Brooklinen": "",
    "Vivien Frank": "",
    "Rebel Nell": "",
    "Collina Strada": "",
    "KNOWN SUPPLY": "",
    "MATE the Label": "",
    "Tentree": "",
    "Brixton": "",
    "Unique Vintage": "",
    "Boll & Branch": "",
    "Polène": "",
    "Garrett Leight": "",
    "Thousand Fell": "",
    "Indosole": "",
    "Plant People": "",
    "Honest Paws": "",
    "Fi": "",
    "PetLab Co.": "",
    "Happiest Baby": "",
    "Grove Collaborative": "",
    "Dropps": "",
    "Branch Basics": "",
    "Tea Collection": "",
    "Maisonette": "",
    "Coterie": "",
    "Manduka": "",
    "Doe Lashes": "",
    "TRX": "",
    "Heath Ceramics": "",
    "Wolven": "",
    "Carbon38": "",
    "KontrolFreek": "",
    "Hanahana Beauty": "",
    "TomboyX": "",
    "Ten Little": "",
    "See Kai Run": "",
    "Plae": "",
    "Kindred Bravely": "",
    "Bowflex": "",
    "Monica + Andy": "",
    "Baby Mori": "",
    "Earth Mama": "",
    "Meow Meow Tweet": "",
    "Buff City Soap": "",
    "Kickee Pants": "",
    "Zutano": "",
    "Loulou Lollipop": "",
}

# Read the existing CSV
with open('/Users/stellagarber/hoop-bdr/leads_1000_shopify_brands.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

# Add new columns if they don't exist
if 'chat_widget' not in fieldnames:
    fieldnames.append('chat_widget')
if 'chat_vendor' not in fieldnames:
    fieldnames.append('chat_vendor')

# Update rows with chat widget data
for row in rows:
    brand_name = row['brand_name']
    if brand_name in chat_data:
        vendor = chat_data[brand_name]
        row['chat_widget'] = 'Yes' if vendor else 'No'
        row['chat_vendor'] = vendor
    else:
        # Not yet researched - leave empty
        row['chat_widget'] = ''
        row['chat_vendor'] = ''

# Write the updated CSV
with open('/Users/stellagarber/hoop-bdr/leads_1000_shopify_brands.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Count statistics
total = len(rows)
researched = sum(1 for r in rows if r['chat_widget'])
with_widget = sum(1 for r in rows if r['chat_widget'] == 'Yes')
without_widget = sum(1 for r in rows if r['chat_widget'] == 'No')

print(f"Total brands: {total}")
print(f"Brands researched: {researched}")
print(f"With chat widget: {with_widget}")
print(f"Without chat widget: {without_widget}")
print(f"Not yet researched: {total - researched}")

# Print vendor breakdown
vendors = {}
for r in rows:
    if r.get('chat_vendor'):
        vendor = r['chat_vendor']
        vendors[vendor] = vendors.get(vendor, 0) + 1

print("\nVendor breakdown:")
for vendor, count in sorted(vendors.items(), key=lambda x: -x[1]):
    print(f"  {vendor}: {count}")
