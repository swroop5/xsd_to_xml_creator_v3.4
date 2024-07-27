from lxml import etree

# Path to the XSD schema file
xsd_file = "xjustiz_0000_grunddatensatz_3_4.xsd"


# Load the XSD schema file
tree = etree.parse(xsd_file)

root = tree.getroot()

print(root.tag + ' ' + str(root.attrib))

# for child in root:
#     print(child.tag, child.attrib)

for neighbor in root.iter('element'):
    print(neighbor.attrib)