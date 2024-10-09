#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------
# KodivertidoTeamTvCine - XBMC Add-on by Mendelux
# Version 1.0.0 (01.05.2022)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)
import os 
import sys                           
import re                                                                            
import xbmc                       
import xbmcgui                 
import xbmcaddon
import xbmcplugin
import plugintools               
import base64                      
import requests
import six
import xbmcvfs
import json as jsonmod
import xbmcvfs
import xbmcgui
import xbmcplugin
import urllib
from urllib import parse
#import urllib.request as ur
import time

myaddon =xbmcaddon .Addon ()


if six.PY2:
    translatePath = xbmc.translatePath
    LOG = xbmc.LOGNOTICE
elif six.PY3:
    translatePath = xbmcvfs.translatePath
    LOG = xbmc.LOGINFO

view_mode_id = 50
xbmc.executebuiltin('Container.SetViewMode(%d)' % view_mode_id) 


def run():
    
    plugintools.log("---> #### ####  Kodivertido.run ### ### <---")
    params = plugintools.get_params()
    action = params.get("action")
    if action and action in globals():
        globals()[action](params)
    else:
        main_list(params)

    plugintools.close_item_list()

#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------


#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------

def main_list(params):
       
    plugintools.add_item(action = "" , title = "", folder = False )

    plugintools.add_item(action = "" , title = "", folder = False )

    plugintools.add_item(action = "" , title = "[B][COLOR yellow]Vuelve el Armagedon....[/B][/COLOR]")
   

run()

