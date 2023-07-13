#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thursday July 13 15:13:37 2023

@author: Etinosa Noma-Osaghae
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Savnge object to a file

    Arguments:
        my_obj (obj): The object to convert in json format
        filename (str): Name of the output file

    Return:
        A file with a text in jason format
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(json.dumps(my_obj))
