import xml.etree.ElementTree as lib
tree = ET.parse("sample.xml")
print(tree)
root = tree.getRoot();
for elem in root:
   for subelem in elem:
      print(subelem.text)
for elem in root:
	for subelem in elem:
 			print(elem.text)
            print(subelem.text)
            print(elem.tag)
            print(subelem.tag) 
