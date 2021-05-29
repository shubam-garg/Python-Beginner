# for window users to activate virtual setupenv:(command):.\setupfile2\Scripts\activate.ps1
''' way to install pandas: pip install pandas
    way to create virtualenvironment: pip install virtualenv 
    next command to store setup in folder: virtualenv Folder_Name(Setupfile2)
    next command for activation: .\setupenv\Scripts\activate.ps1(if error occured) 
    pass next command: Set-ExecutionPolicy Unrestricted -Scope Process
    then again type: .\setupenv\Scripts\activate.ps1 
    to deactivate virtualenv setupenv: deactivate
    to check installed packages: pip freeze
    to save all installed packages along with version: pip freeze > FileName(version.txt)
    to install all packages to new setup: pip install -r .\version.txt(file name)'''
import flask
import pandas as pd
import pygame
