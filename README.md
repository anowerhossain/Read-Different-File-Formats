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



