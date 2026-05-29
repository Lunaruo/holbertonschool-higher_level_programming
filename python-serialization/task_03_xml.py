#!/usr/bin/env python3
"""
Module for XML serialization and deserialization.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Output XML filename.
    """

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a dictionary.

    Args:
        filename (str): XML filename.

    Returns:
        dict: Deserialized dictionary.
    """

    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}

    for child in root:
        data[child.tag] = child.text

    return data
