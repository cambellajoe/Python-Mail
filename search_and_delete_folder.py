# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:53:32 2019

@author: JKMUTUA

This script allows a user to find a folder by providing root directory and folder name
Then it deletes all the occurences of the folder with its contents
"""

import os
import shutil

"""For python 3.*"""
folder_name = input("Pass the month or folder name: ")
root_folder = input("Path the root folder where the folder resides: ")

"""For python 2.*"""
#folder_name = raw_input("Pass the month or folder name: ")
#root_folder = raw_input("Path the root folder where the folder resides: ")


for root, dirs, files in os.walk(root_folder):
    #print(root)
    if root.endswith(folder_name):
       shutil.rmtree(root)
       print (root)