import requests
import xml.etree.ElementTree as ET

URL = "https://www.simbrief.com/api/xml.fetcher.php?username=tynian78"

response = requests.get(URL)
with open("simbrief.xml", "wb") as file:
    file.write(response.content)

tree = ET.parse("simbrief.xml")
root = tree.getroot()

# one specific item attribute
# print("Item #2 attribute:")
# print(root[0][1].attrib)

# all item attributes
# print("\nAll attributes:")
for i, elem in enumerate(root):
    for subelem in elem:
        print(f"{i}/{subelem.attrib}: {subelem.text}")

# one specific item's data
print("\nItem #2 data:")
print(root[0].text)
