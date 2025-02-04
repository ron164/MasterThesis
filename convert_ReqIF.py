import xml.etree.ElementTree as ET

def convert_to_reqif(input_file, output_file):
    # Parse the input XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Create the root element for the ReqIF file
    reqif = ET.Element('REQ-IF')

    # Create sub-elements for the ReqIF structure
    core_content = ET.SubElement(reqif, 'CORE-CONTENT')
    requirements = ET.SubElement(core_content, 'SPEC-OBJECTS')

    # Function to convert all values to strings
    def convert_to_string(value):
        if isinstance(value, bool):
            return str(value).lower()  # Convert boolean to 'true' or 'false'
        if value is None:
            return ''  # Convert None to empty string
        return str(value)

    # Iterate over each requirement in the input XML and create an XML element for each in ReqIF
    for req in root.findall('.//requirement'):
        req_id = req.get('id')
        if req_id is None:
            continue  # Skip this requirement if 'id' attribute is missing

        spec_object = ET.SubElement(requirements, 'SPEC-OBJECT', ID=convert_to_string(req_id))
        for child in req:
            ET.SubElement(spec_object, child.tag.upper()).text = convert_to_string(child.text)

    # Write the ReqIF XML to a file
    reqif_tree = ET.ElementTree(reqif)
    with open(output_file, 'wb') as f:
        reqif_tree.write(f, xml_declaration=True, encoding='UTF-8')

if __name__ == "__main__":
    input_file = 'ECall_Connectivity_Requirements.xlsx.xml'
    output_file = 'ECall_Connectivity_Requirements.xlsx.reqif'
    convert_to_reqif(input_file, output_file)
    print(f"Converted {input_file} to {output_file}")
