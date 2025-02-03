import xml.etree.ElementTree as ET
import pandas as pd

# Load XML from a file
xml_file = "employees.xml"  # Replace with your XML file path
tree = ET.parse(xml_file)
root = tree.getroot()

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

# Convert to DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df)
