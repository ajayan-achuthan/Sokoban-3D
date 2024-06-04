import os
import xml.etree.ElementTree as ET
from kivy.storage.jsonstore import JsonStore

store = JsonStore('output/completed.json')

def level_finder(collection,level):
    tree = ET.parse(f'collections/{collection}.slc')
    root = tree.getroot()
    elem = root[4][level]
    width,height = int(elem.attrib['Width']), int(elem.attrib['Height'])
    level = []
    for child in elem:
        level.append(child.text)
    return width,height,level

def count_levels(collection):
    tree = ET.parse(f'collections/{collection}.slc')
    root = tree.getroot()
    for child in root:
        if child.tag =='LevelCollection':
            levels = child
            break
    return len(levels)

def available_collections():
    slcs = os.listdir(f'collections')
    slcs = [x.split('.')[0] for x in slcs]
    return slcs

def add_completed(collection,level):
    if collection in store.keys():
        completed = store.get(collection)['completed']
        if level not in completed:
            completed.append(level)
        store.put(collection,completed = completed)
    else:
        store.put(collection,completed = [level])

def is_completed(collection,level):
    if collection in store.keys():
        completed = store.get(collection)['completed']
        if level in completed:
            return True
        else:
            return False
    else:
        return False
    
def count_completed(collection):
    
    if collection in store.keys():
        completed = len(store.get(collection)['completed'])
    else:
        completed = 0
    total = count_levels(collection)
    return completed,total