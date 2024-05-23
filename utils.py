import os
import xml.etree.ElementTree as ET
from kivy.storage.jsonstore import JsonStore

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
    return len(root[4])

def available_collections():
    slcs = os.listdir(f'collections')
    slcs = [x.split('.')[0] for x in slcs]
    return slcs

def add_completed(collection,level):
    store = JsonStore('output/completed.json')
    if collection in store.keys():
        completed = store.get(collection)['completed']
        if level not in completed:
            completed.append(level)
        store.put(collection,completed = completed)
    else:
        store.put(collection,completed = [level])

def is_completed(collection,level):
    store = JsonStore('output/completed.json')
    if collection in store.keys():
        completed = store.get(collection)['completed']
        if level in completed:
            return (1, 1, 0, 1)
        else:
            return (0.5, 0.5, 0.5, 1)
    else:
        return (0.5, 0.5, 0.5, 1)
    
def count_completed(collection):
    store = JsonStore('output/completed.json')
    if collection in store.keys():
        completed = len(store.get(collection)['completed'])
    else:
        completed = 0
    total = count_levels(collection)
    return completed,total