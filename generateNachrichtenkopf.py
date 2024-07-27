from lxml import etree

# Create the root element
root = etree.Element("block", name="tns:nachrichtenkopf", xml="j", muss="j",
                     xmlKonstanteAttribute="xjustizVersion='3.3.1'")

# Create the first zeile element
zeile1 = etree.SubElement(root, "zeile", muss="n")

f1 = etree.SubElement(zeile1, "f", name="tns:aktenzeichen.absender")
f1.text = "VF$vfid"

f2 = etree.SubElement(zeile1, "f", name="tns:aktenzeichen.empfaenger")
f2.text = "VF$herkaz"

f3 = etree.SubElement(zeile1, "f", name="tns:erstellungszeitpunkt", l="19",
                      vorbelegungsmethode="getTagesdatumMitUhrzeit",
                      konvertierungsmethode="konvDatum dd.MM.yyyy\\ HH:mm:ss yyyy-MM-dd'T'HH:mm:ss")
f3.text = "erstellungszeitpunkt"

f4 = etree.SubElement(zeile1, "f", l="18", hilfsfeld="j")
f4.text = "VF$vfid"

# Create the block element inside nachrichtenkopf
block1 = etree.SubElement(root, "block", name="tns:auswahl_absender", xml="j")

zeile2 = etree.SubElement(block1, "zeile", index="tns:absender.gericht", xml="j", muss="j",
                          xmlKonstanteAttribute="listVersionID='3.5'|XJustizTyp3GerichteVersion")

f5 = etree.SubElement(zeile2, "f", name="code")
f5.text = "BK$bhkennz"

f6 = etree.SubElement(zeile2, "f", l="18", hilfsfeld="j")
f6.text = "VF$vfid"

zeile3 = etree.SubElement(block1, "zeile")
f7 = etree.SubElement(zeile3, "f", name="tns:absender.sonstige")
f7.text = "absender.sonstige"

# Create the block element inside nachrichtenkopf
block2 = etree.SubElement(root, "block", name="tns:auswahl_empfaenger", xml="j")

zeile4 = etree.SubElement(block2, "zeile", index="tns:empfaenger.gericht", xml="j",
                          xmlKonstanteAttribute="listVersionID=&quot;3.5&quot;")

f8 = etree.SubElement(zeile4, "f", name="code")
f8.text = "code"

zeile5 = etree.SubElement(block2, "zeile", muss="j")

f9 = etree.SubElement(zeile5, "f", name="tns:empfaenger.sonstige", vorbelegungsmethode="getFeldAbPosition Empf 1")
f9.text = "Empfaenger"

f10 = etree.SubElement(zeile5, "f", l="18", hilfsfeld="j")
f10.text = "VF$vfid"

# Create the zeile element inside nachrichtenkopf
zeile6 = etree.SubElement(root, "zeile", muss="n")

f11 = etree.SubElement(zeile6, "f", l="6", hilfsfeld="j")
f11.text = "BK$bhkennz"

f12 = etree.SubElement(zeile6, "f", name="tns:eigeneNachrichtenID",
                       vorbelegungsmethode="getFeldAbPosition nachrichtenId 1")
f12.text = "Nachrichtreferenz"

# Create the zeile element inside nachrichtenkopf
zeile7 = etree.SubElement(root, "zeile", index="tns:nachrichtenuebergreifenderProzess", xml="j", muss="n")

f13 = etree.SubElement(zeile7, "f", name="tns:prozessID")
f13.text = "prozessID"

f14 = etree.SubElement(zeile7, "f", name="tns:nachrichtenNummer")
f14.text = "nachrichtenNummer"

f15 = etree.SubElement(zeile7, "f", name="tns:nachrichtenAnzahl")
f15.text = "nachrichtenAnzahl"

# Create the zeile element inside nachrichtenkopf
zeile8 = etree.SubElement(root, "zeile", index="tns:ereignis", xml="j", muss="j",
                          xmlKonstanteAttribute="listVersionID='1.7'|XJustizTyp3EreignisVersion")

f16 = etree.SubElement(zeile8, "f", name="code", vorbelegungsmethode="getFeldAbPosition ereignis 1")
f16.text = "Ereignis"

f17 = etree.SubElement(zeile8, "f", l="18", hilfsfeld="j")
f17.text = "VF$vfid"

# Create the zeile element inside nachrichtenkopf
zeile9 = etree.SubElement(root, "zeile", index="tns:herstellerinformation", muss="n", xml="j")

f18 = etree.SubElement(zeile9, "f", name="tns:nameDesProdukts")
f18.text = "nameDesProdukts"

f19 = etree.SubElement(zeile9, "f", name="tns:herstellerDesProdukts")
f19.text = "herstellerDesProdukts"

f20 = etree.SubElement(zeile9, "f", name="tns:version")
f20.text = "version"

# Create the zeile element inside nachrichtenkopf
zeile10 = etree.SubElement(root, "zeile", index="tns:sendungsprioritaet", xml="j", muss="n",
                           xmlKonstanteAttribute="listVersionID=&quot;1.1&quot;")

f21 = etree.SubElement(zeile10, "f", name="code")
f21.text = "sendungsprioritaet"

f22 = etree.SubElement(zeile10, "f", l="18", hilfsfeld="j")
f22.text = "VF$vfid"

# Create the block element inside nachrichtenkopf
block3 = etree.SubElement(root, "block", name="tns:vertraulichkeit", xml="j")

zeile11 = etree.SubElement(block3, "zeile", index="tns:vertraulichkeitsstufe", xml="j", muss="j",
                           xmlKonstanteAttribute="listVersionID=&quot;1.1&quot;")

f23 = etree.SubElement(zeile11, "f", name="code")
f23.text = "vertraulichkeitsstufe"

zeile12 = etree.SubElement(block3, "zeile", muss="n")
f24 = etree.SubElement(zeile12, "f", name="tns:vertraulichkeitsgrund")
f24.text = "vertraulichkeitsgrund"

# Create the XML tree from the root element
tree = etree.ElementTree(root)

# Write the XML tree to a file
tree.write("output.xml", pretty_print=True, encoding="UTF-8")
