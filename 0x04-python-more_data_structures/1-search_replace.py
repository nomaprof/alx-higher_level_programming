#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return ([change if change != search else replace for change in my_list])
