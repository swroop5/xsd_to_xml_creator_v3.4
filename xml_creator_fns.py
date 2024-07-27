JA = 'j'
NEIN = 'n'
listVersionID = 'listVersionID'
code = 'code'
xjustizVersion = 'xjustizVersion='
Quote = '"'


def startTagBlock():
    return '<block '

def startTagZeile():
    return '<zeile '

def startTagF():
    return '<f '

def closeAngBracket():
    return '>'

def closeTagBlock():
    return '</block>'

def closeTagZeile():
    return '</zeile>'

def closeTagF():
    return '</f>'

def attrName():
    return 'name='

def attrXML():
    return 'xml='

def attrMuss():
    return 'muss='

def attrxmlKonstanteAttribute():
    return 'xmlKonstanteAttribute='

def attrvorbelegungsmethode():
    return 'vorbelegungsmethode='

def attrkonvertierungsmethode():
    return 'konvertierungsmethode='

def attrL():
    return 'l='

def attrhilfsfeld():
    return 'hilfsfeld='

def addNamespaceBeforeAttr():
    return '"tns:'

from lxml import etree

root = etree.Element("root")


child1 = etree.SubElement(root, "child1")
child1.text = "Hello"

child2 = etree.SubElement(root, "child2")
child2.text = "World"

tree = etree.ElementTree(root)
tree.write("output.xml", pretty_print=True)
