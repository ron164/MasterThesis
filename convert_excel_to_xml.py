"""
import pandas as pd
from lxml import etree as et
from lxml.etree import QName

raw_data = pd.read_excel("A:\Thesis\Requirements\Sample_Requirements.xlsx")

root = et.Element('requirements')

for row in raw_data.iterrows():
    root_tags = et.SubElement(root, 'requirement')
    colummn_heading_1 = et.SubElement(root_tags, 'Requirement_ID')
    colummn_heading_2 = et.SubElement(root_tags, 'Content')
    colummn_heading_3 = et.SubElement(root_tags, 'Qualification_Method')
    colummn_heading_4 = et.SubElement(root_tags, 'Artifact_Type')
    colummn_heading_5 = et.SubElement(root_tags, 'System_Requirement_State')
    colummn_heading_6 = et.SubElement(root_tags, 'Assignee')
    colummn_heading_7 = et.SubElement(root_tags, 'Review_Comment')
    colummn_heading_8 = et.SubElement(root_tags, 'Primary_Discipline')
    colummn_heading_9 = et.SubElement(root_tags, 'Requirement_Type')
    colummn_heading_10 = et.SubElement(root_tags, 'System_Elements')
    colummn_heading_11 = et.SubElement(root_tags, 'ASIL_Rating')
    colummn_heading_12 = et.SubElement(root_tags, 'Cybersecurity')
    colummn_heading_13 = et.SubElement(root_tags, 'Key_Requirement')
    colummn_heading_14 = et.SubElement(root_tags, 'Legal_Certification_Requirement')
    colummn_heading_15 = et.SubElement(root_tags, 'Variant')
    colummn_heading_16 = et.SubElement(root_tags, 'Verification_Criteria')
    colummn_heading_17 = et.SubElement(root_tags, 'Verification_Method')
    colummn_heading_18 = et.SubElement(root_tags, 'Verification_Owner')

    colummn_heading_1.text = str(row[1]['Requirement_ID'])
    colummn_heading_2.text = str(row[1]['Content'])
    colummn_heading_3.text = str(row[1]['Qualification_Method'])
    colummn_heading_4.text = str(row[1]['Artifact_Type'])
    colummn_heading_5.text = str(row[1]['System_Requirement_State'])
    colummn_heading_6.text = str(row[1]['Assignee'])
    colummn_heading_7.text = str(row[1]['Review_Comment'])
    colummn_heading_8.text = str(row[1]['Primary_Discipline'])
    colummn_heading_9.text = str(row[1]['Requirement_Type'])
    colummn_heading_10.text = str(row[1]['System_Elements'])
    colummn_heading_11.text = str(row[1]['ASIL_Rating'])
    colummn_heading_12.text = str(row[1]['Cybersecurity'])
    colummn_heading_13.text = str(row[1]['Key_Requirement'])
    colummn_heading_14.text = str(row[1]['Legal_Certification_Requirement'])
    colummn_heading_15.text = str(row[1]['Variant'])
    colummn_heading_16.text = str(row[1]['Verification_Criteria'])
    colummn_heading_17.text = str(row[1]['Verification_Method'])
    colummn_heading_18.text = str(row[1]['Verification_Owner'])

tree = et.ElementTree(root)
et.indent(tree, space="\t", level=0)
tree.write('demo_req.xml', encoding="utf-8")
"""
import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np

def convert_excel_to_xml(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file)

    # Fill NaN values with empty strings to avoid serialization errors
    df = df.replace({np.nan: ''})

    # Function to convert all values to strings
    def convert_to_string(value):
        if isinstance(value, bool):
            return str(value).lower()  # Convert boolean to 'true' or 'false'
        return str(value)

    # Create the root element for the XML file
    requirements = ET.Element('requirements')

    # Iterate over each row in the DataFrame and create an XML element for each requirement
    for _, row in df.iterrows():
        requirement = ET.SubElement(requirements, 'requirement', id=str(row['Requirement_ID']))
        ET.SubElement(requirement, 'Content').text = convert_to_string(row['Content'])
        ET.SubElement(requirement, 'Header').text = convert_to_string(row['Header'])
        ET.SubElement(requirement, 'Qualification_Method').text = convert_to_string(row['Qualification_Method'])
        ET.SubElement(requirement, 'Artifact_Type').text = convert_to_string(row['Artifact_Type'])
        ET.SubElement(requirement, 'System_Requirement_State').text = convert_to_string(row['System_Requirement_State'])
        ET.SubElement(requirement, 'Assignee').text = convert_to_string(row['Assignee'])
        ET.SubElement(requirement, 'Review_Comment').text = convert_to_string(row['Review_Comment'])
        ET.SubElement(requirement, 'Primary_Discipline').text = convert_to_string(row['Primary_Discipline'])
        ET.SubElement(requirement, 'Requirement_Type').text = convert_to_string(row['Requirement_Type'])
        ET.SubElement(requirement, 'System_Elements').text = convert_to_string(row['System_Elements'])
        ET.SubElement(requirement, 'ASIL_Rating').text = convert_to_string(row['ASIL_Rating'])
        ET.SubElement(requirement, 'Cybersecurity').text = convert_to_string(row['Cybersecurity'])
        ET.SubElement(requirement, 'Key_Requirement').text = convert_to_string(row['Key_Requirement'])
        ET.SubElement(requirement, 'Legal_Certification_Requirement').text = convert_to_string(row['Legal_Certification_Requirement'])
        ET.SubElement(requirement, 'Variant').text = convert_to_string(row['Variant'])
        # ET.SubElement(requirement, 'Verification_Criteria').text = convert_to_string(row['Verification_Criteria'])
        ET.SubElement(requirement, 'Verification_Method').text = convert_to_string(row['Verification_Method'])
        ET.SubElement(requirement, 'Verification_Owner').text = convert_to_string(row['Verification_Owner'])

    # Write the XML to a file
    tree = ET.ElementTree(requirements)
    with open(output_file, 'wb') as f:
        tree.write(f, xml_declaration=True, encoding='UTF-8')

    """

    # Write the XML to a file
    tree = ET.ElementTree(requirements)
    tree.write(output_file, xml_declaration=True, encoding='UTF-8')
    
    """

if __name__ == "__main__":
    input_file = "A:\Thesis\Requirements\ECall_Connectivity_Requirements.xlsx"
    output_file = 'ECall_Connectivity_Requirements.xlsx.xml'
    convert_excel_to_xml(input_file, output_file)
    print(f"Converted {input_file} to {output_file}")
