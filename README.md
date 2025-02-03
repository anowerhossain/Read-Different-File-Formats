# Read-Different-File-Formats
Handling different file formats is crucial because data comes from various sources and needs to be processed efficiently.

## Reading from an XML File 📂
Here's how you can read an XML file, extract data, and convert it into a Pandas DataFrame. 🚀

Sample XML File 📜 (`employees.xml`)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<company>
    <employee>
        <id>1</id>
        <name>John Doe</name>
        <position>Software Engineer</position>
        <department>IT</department>
    </employee>
    <employee>
        <id>2</id>
        <name>Jane Smith</name>
        <position>Project Manager</position>
        <department>Operations</department>
    </employee>
</company>
```

### Load XML File into Python 📥
```python
import xml.etree.ElementTree as ET
import pandas as pd

# Load XML from a file
xml_file = "employees.xml"  # Replace with your XML file path
tree = ET.parse(xml_file)
root = tree.getroot()
```

### Extract Data from XML 🔍
```python
# Extract data
data = []
for employee in root.findall("employee"):
    emp_data = {
        "ID": employee.find("id").text,
        "Name": employee.find("name").text,
        "Position": employee.find("position").text,
        "Department": employee.find("department").text
    }
    data.append(emp_data)
```
### Convert to a DataFrame 📊
```python
# Convert to DataFrame
df = pd.DataFrame(data)
```

## Reading from an XML File 📂
Here's how you can read an XML file, extract data, and convert it into a Pandas DataFrame. 🚀

Sample JSON File 📜 (`products.json`)
```json
{
  "store": {
    "name": "Tech Gadget Store",
    "location": "New York",
    "products": [
      {
        "id": 101,
        "name": "Smartphone",
        "brand": "TechBrand",
        "category": "Electronics",
        "price": 699.99,
        "stock": {
          "available": 120,
          "warehouse": "NYC-1"
        },
        "specifications": {
          "screen_size": "6.5 inches",
          "battery_life": "24 hours",
          "processor": "Octa-core",
          "storage_options": ["64GB", "128GB", "256GB"],
          "colors": ["Black", "Blue", "Silver"]
        }
      },
      {
        "id": 102,
        "name": "Laptop",
        "brand": "UltraTech",
        "category": "Computers",
        "price": 1199.99,
        "stock": {
          "available": 45,
          "warehouse": "LA-2"
        },
        "specifications": {
          "screen_size": "15.6 inches",
          "battery_life": "10 hours",
          "processor": "Intel Core i7",
          "ram": "16GB",
          "storage": "512GB SSD",
          "colors": ["Gray", "Silver"]
        }
      },
      {
        "id": 103,
        "name": "Wireless Headphones",
        "brand": "SoundMax",
        "category": "Accessories",
        "price": 149.99,
        "stock": {
          "available": 200,
          "warehouse": "TX-3"
        },
        "specifications": {
          "battery_life": "30 hours",
          "noise_cancellation": true,
          "connectivity": "Bluetooth 5.0",
          "colors": ["Black", "White", "Red"]
        }
      }
    ]
  }
}
```

### Load JSON File into Python 📥
```python
import json
import pandas as pd

with open("products.json", "r") as file:  # Open the file in read mode
    data = json.load(file)  # Load JSON content
```

### Extract Data from JSON 🔍
```python
products = data["store"]["products"]  # Extract the 'products' list
```

### Convert to a DataFrame 📊
```python
df = pd.json_normalize(products, sep="_")  # Flatten nested data
```


