import xml.etree.ElementTree as ET
def level_finder(collection,level):
    tree = ET.parse(f'collections/{collection}.slc')
    root = tree.getroot()
    elem = root[4][level]
    width,height = int(elem.attrib['Width']), int(elem.attrib['Height'])
    level = []
    for child in elem:
        level.append(child.text)
    return width,height,level

