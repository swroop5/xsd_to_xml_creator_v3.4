from lxml import etree

# Register the xsi namespace
etree.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")

# Create the root element
root = etree.Element("{http://www.EDV-COMPAS.com/2005/icom}formularbs", formularname="eip_nachricht",
                     xmlns="http://www.EDV-COMPAS.com/2005/icom")

# Set the xsi:schemaLocation attribute
root.set("{http://www.w3.org/2001/XMLSchema-instance}schemaLocation", "http://www.EDV-COMPAS.com/2005/icom formularbeschreibung.xsd")

# Create the prolog element
prolog = etree.SubElement(root, "prolog")
XMLDecl = etree.SubElement(prolog, "XMLDecl")
xsdHeaderAttribute = etree.SubElement(prolog, "xsdHeaderAttribute")
schemaLocationZuerst = etree.SubElement(prolog, "schemaLocationZuerst")
schemaLocation = etree.SubElement(schemaLocationZuerst, "schemaLocation",
                                  xsdNameSpace="http://www.xjustiz.de",
                                  xsdDocumentTypeNs="xjustiz_0500_straf_3_2.xsd")

# Create the satz element
satz = etree.SubElement(root, "satz", xmlRootTag="tns:nachricht.gds.uebermittlungSchriftgutobjekte.0005005",
                        xmlKonstanteRootAttribute="xmlns:tns='http://www.xjustiz.de' "
                                                 "xmlns:xoev-code='http://xoev.de/schemata/code/1_0' "
                                                 "xmlns:xoev-lc='http://xoev.de/latinchars/1_1/datatypes' "
                                                 "xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'")

# Create the zeile element
zeile = etree.SubElement(satz, "zeile")

# Create the konstante elements
konstante_values = [
    ("j", " ", "leeresFeld"),
    ("j", "1", "konstEins"),
    ("j", "2", "konstZwei"),
    ("j", "204", "ereignis"),
    ("j", "007", "sachgebiet"),
    ("j", "false", "konstFalse"),
    ("j", "002", "konstAliasidentitaet"),
    ("j", "017", "konstPrivatanschrift"),
    ("j", "b4d09847-0dfb-44ce-a688-03c80b4610a6", "nachrichtenId"),
    ("j", "Platzhalter", "Platzhalter"),
    ("j", "Sonstiger Empfänger", "Empf")
]

for konstante_value in konstante_values:
    konstante = etree.SubElement(zeile, "konstante", hilfsfeld=konstante_value[0],
                                vorbelegungsmethode=konstante_value[1])
    konstante.text = konstante_value[2]

# Create the XML tree
tree = etree.ElementTree(root)

# Write the XML to a file
tree.write("output.xml", pretty_print=True, xml_declaration=True, encoding="UTF-8")
