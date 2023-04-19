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
import base64
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
   plugintools.log("---> KodivertidoTeamTvCine.run <---")  
   #    
                                                                         
    # Get params                                          
   params = plugintools.get_params()                     
    
   if params.get("action") is None:                      
      main_list(params)                                          
   else:                                                                     
      action = params.get("action")
      exec (action+"(params)")
    
   plugintools.close_item_list()
 


#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------


#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------

def main_list(params):
   
    
   # 

   plugintools.add_item(action = "" , title = "[COLOR lime][B]#######[COLOR aqua]##################[COLOR lime]####[/B][/COLOR]", thumbnail ="https://i.imgur.com/yMUqrM3.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

   plugintools.add_item(action = "" , title = "[COLOR lime][B]##         [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]Tv[COLOR blue]C[COLOR yellow]i[COLOR aqua]n[COLOR yellow]e         [COLOR lime]##[/B][/COLOR]",  thumbnail ="https://i.imgur.com/yMUqrM3.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg", folder = False )

   plugintools.add_item(action = "" , title = "[COLOR lime][B]#######[COLOR aqua]##################[COLOR lime]####[/B][/COLOR]", thumbnail ="https://i.imgur.com/yMUqrM3.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

   plugintools.add_item(action = "" , title = "", thumbnail ="https://i.imgur.com/yMUqrM3.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg", folder = False )

   plugintools.add_item(action = "openUrl" , title = "[COLOR white][B] Únete a Telegram [COLOR lime]<https://t.me/+EdhJPA_QlCkzYTlk>[/B][/COLOR]" , thumbnail = "https://i.imgur.com/x16izoN.jpg" , url = "https://t.me/kodivertidoteam" , fanart = "https://i.imgur.com/cE1QfPa.jpg" , folder = True,isPlayable=False )

   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    
   plugintools.add_item(action = "vaboo" , title = "[COLOR lime][B]> [COLOR yellow]Tv[COLOR gold]Va[COLOR yellow]voo[COLOR lime] <[/B][/COLOR]" , thumbnail = "https://i.imgur.com/NHUuQ7F.jpg"  , url = "", fanart = "https://i.imgur.com/4fiWW6i.jpg" , plot = "",  folder = True,isPlayable = False  )
   
   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
   
   plugintools.add_item(action = "agendas_deportivas" , title = "[COLOR lime][B]> [COLOR lime]AGE[COLOR gold]NDAS[COLOR yellow] DEPORTIVAS[COLOR lime] <[/B][/COLOR]" , thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png"  , url = "", fanart = "https://i.imgur.com/DVTt1Fv.jpg" , plot = "",  folder = True,isPlayable = False  )
   
   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)   
            
   plugintools.add_item(action = "canalesacestream" , title = "[COLOR lime][B]>[COLOR orange] SALA ACESTREAM[COLOR lime] <[COLOR orange] <<[COLOR lightpink]Necesario Acestream[COLOR orange]>>[/B][/COLOR]", thumbnail ="https://i.postimg.cc/5010m2BJ/Photo-1667495091544.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )

   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

   plugintools.add_item(action = "moviola" , title = "[COLOR lime][B]>[COLOR white] LA[COLOR gold]MOVI[COLOR orange]OLA[COLOR white] REPETICIONES[COLOR gold] DEPORTIVAS[COLOR lime] <[/B][/COLOR]" , thumbnail = "http://perillas.mendelux.es/thumb.png"  , url = "", fanart = "http://perillas.mendelux.es/moviola.jpg" , plot = "",  folder = True,isPlayable = False  )
   
   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

   plugintools.add_item(action = "cine" , title = "[COLOR lime][B]>[COLOR gold] CINE [COLOR yellow]ESTRENOS[COLOR lime] <[/B][/COLOR]" , thumbnail = "https://i.imgur.com/iPMtAVo.jpg"  , fanart = "https://i.imgur.com/cE1QfPa.jpg" , plot = "",  folder = True,isPlayable = False  )
   
   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
   
   plugintools.add_item(action = "alegres" , title = "[COLOR lime][B]>[COLOR orange] TV ADULTOS[COLOR lime] <[/B][/COLOR]", thumbnail ="https://i.imgur.com/HCiV6ND.jpg", fanart = "https://i.imgur.com/kgSbSPb.jpg", folder = True )
      
    
#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################       
#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################
#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################


def iptv(params):
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png", fanart = "https://i.imgur.com/r3lavFX.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]El[COLOR blue] Jar[COLOR yellow]di[COLOR aqua]n                               [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png", fanart = "https://i.imgur.com/r3lavFX.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png", fanart = "https://i.imgur.com/r3lavFX.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    #plugintools.add_item(action = "iptv1" , title = "[COLOR lime][B]->LISTA 1<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/kVXxRxi.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg", folder = True )

    plugintools.add_item(action = "iptv_v" , title = "[COLOR lime][B]->[COLOR orange]ENTRA AL [COLOR yellow]JARDIN[COLOR lime]<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png", fanart = "https://i.imgur.com/r3lavFX.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    #plugintools.add_item(action="stalker", title = "[B][COLOR lime][B]->[COLOR orange]Stalker[COLOR lime]<-[/COLOR][/B]", url= '', fanart = 'https://i.imgur.com/r3lavFX.jpg' , thumbnail = 'https://i.imgur.com/cQLMaCA.jpg', folder=True, isPlayable=False)
 
    #plugintools.add_item(action = "iptv3" , title = "[COLOR lime][B]->LISTA 3<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/OqADwwu.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg", folder = True )

    #plugintools.add_item(action = "iptv4" , title = "[COLOR lime][B]->LISTA 4<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/niIFp0G.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg", folder = True )
  
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
   
    plugintools.add_item(action = "alegres" , title = "[COLOR lime][B]->[COLOR orange]TV ADULTOS[COLOR lime]<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/HCiV6ND.jpg", fanart = "https://i.imgur.com/kgSbSPb.jpg", folder = True )
   
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
   
    plugintools.add_item(action = "canalesacestream" , title = "[COLOR lime][B]->[COLOR orange]SALA ACESTREAM[COLOR lime]<-[COLOR orange] <<[COLOR lightpink]Necesario Acestream[COLOR orange]>>[/B][/COLOR]", thumbnail ="https://i.postimg.cc/5010m2BJ/Photo-1667495091544.png", fanart = "https://imgur.com/a/TgybFf6.jpeg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
   
    plugintools.add_item(action = "main_list" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.imgur.com/xdn0NDc.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
   
def iptv1(params):
    
    url3 = 'http://91.208.115.170:25461/get.php?username=simon&password=Mo9nuj5f1qHJMmp0N&type=m3u_plus'
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url3, headers=header)
    url = read_url.strip()

    grupos = re.findall(r'(?s).*?group-title="([^"]+)', url, re.DOTALL)
    
    almacen_grupos = []
    
    for grupo in grupos:
        if grupo not in almacen_grupos:
            almacen_grupos.append(grupo)

    for t in range(len(almacen_grupos)):
        plugintools.add_item(action="iptv1_res", title = "[B][UPPERCASE][COLOR yellow]" + almacen_grupos[t] + "[/COLOR][/UPPERCASE][/B]", url=url, extra = almacen_grupos[t],
                             fanart = 'https://i.imgur.com/xdn0NDc.jpg' , thumbnail = 'https://i.imgur.com/Jp7jf0Y.jpg', folder=True, isPlayable=False) 

def iptv1_res(params):
    
    url3 = 'http://91.208.115.170:25461/get.php?username=simon&password=Mo9nuj5f1qHJMmp0N&type=m3u_plus'
    seleccion = (params.get("extra")).strip()
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url3, headers=header)
    url = read_url.strip()    
    
    matches = re.findall(r'(?s).*?name="(.*?)".*?logo="(.*?)".*?title="(.*?)".*?\n.*?(ht.*?://.*?/.*?/.*?/[A-Za-z0-9_]+)', url, re.DOTALL)
   
    for title, thumb,grup, url in matches:
        if grup.strip() in seleccion:
            plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = thumb , folder = False , isPlayable = True )

def iptv2(params):
    url = "http://perillas.mendelux.es/launo.txt"
    llamada = requests.get(url)
    datos = llamada.text
    
    matches = re.findall(r'(?s).*?name="(.*?)".*?logo="(.*?)".*?title="(.*?)".*?\n.*?(ht.*?://.*?/.*?/.*?/[A-Za-z0-9_]+)', datos, re.DOTALL )
    for title, thumb, grup, url in matches:
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = thumb , folder = False , isPlayable = True )
  
def iptv4(params):
    
    
    #url3 = "http://goodtv.nicenam.xyz/get.php?username=vi08220&password=2281657605&type=m3u_plus"
    
    #(?s).*?name="(.*?)".*?logo="(.*?)".*?title="(.*?)".*?\n.*?(ht.*?://.*?/.*?/.*?/[A-Za-z0-9_]+)
    url = "http://perillas.mendelux.es/vio.txt"
    llamada = requests.get(url)
    datos = llamada.text
    grupos = re.findall(r'(?s).*?group-title="([^"]+)', datos, re.DOTALL)
    
    almacen_grupos = []
    
    for grupo in grupos:
        if grupo not in almacen_grupos:
            almacen_grupos.append(grupo)
    for t in range(len(almacen_grupos)):
        plugintools.add_item(action="iptv4_res", title = "[B][UPPERCASE][COLOR yellow]" + almacen_grupos[t] + "[/COLOR][/UPPERCASE][/B]", url=url, extra = almacen_grupos[t],
                             fanart = 'https://i.imgur.com/xdn0NDc.jpg' , thumbnail = 'https://i.imgur.com/GgGFDmd.jpg', folder=True, isPlayable=False) 
        
def iptv4_res(params):
    
    seleccion = (params.get("extra")).strip()
    url = "http://perillas.mendelux.es/vio.txt"
    llamada = requests.get(url)
    datos = llamada.text
    
    matches = re.findall(r'(?s).*?name="(.*?)".*?logo="(.*?)".*?title="(.*?)".*?\n.*?(ht.*?://.*?/.*?/.*?/[A-Za-z0-9_]+)', datos, re.DOTALL )
    for title, thumb,grup, url in matches:
        if grup.strip() in seleccion:
            plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = thumb , folder = False , isPlayable = True )

def vaboo(params):
    	
    import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys, xbmcvfs, glob
    import shutil
    import urllib
    import re
    import uservar
    import fnmatch
    try:    from sqlite3 import dbapi2 as database
    except: from pysqlite2 import dbapi2 as database
    from datetime import date, datetime, timedelta
    import wizard as wiz
    ADDON_ID         = uservar.ADDON_ID
    ADDONTITLE       = uservar.ADDONTITLE
    ADDON            = wiz.addonId(ADDON_ID)
    VERSION          = wiz.addonInfo(ADDON_ID,'version')
    ADDONPATH        = wiz.addonInfo(ADDON_ID, 'path')
    DIALOG           = xbmcgui.Dialog()
    DP               = xbmcgui.DialogProgress()
    HOME             = xbmcvfs.translatePath('special://home/')
    LOG              = xbmcvfs.translatePath('special://logpath/')
    PROFILE          = xbmcvfs.translatePath('special://profile/')
    TEMPDIR          = xbmcvfs.translatePath('special://temp')
    ADDONS           = os.path.join(HOME,      'addons')
    USERDATA         = os.path.join(HOME,      'userdata')
    PLUGIN           = os.path.join(ADDONS,    ADDON_ID)
    PACKAGES         = os.path.join(ADDONS,    'packages')
    ADDOND           = os.path.join(USERDATA,  'addon_data')
    ADDONDATA        = os.path.join(USERDATA,  'addon_data', ADDON_ID)
    ADVANCED         = os.path.join(USERDATA,  'advancedsettings.xml')
    SOURCES          = os.path.join(USERDATA,  'sources.xml')
    FAVOURITES       = os.path.join(USERDATA,  'favourites.xml')
    PROFILES         = os.path.join(USERDATA,  'profiles.xml')
    GUISETTINGS      = os.path.join(USERDATA,  'guisettings.xml')
    THUMBS           = os.path.join(USERDATA,  'Thumbnails')
    DATABASE         = os.path.join(USERDATA,  'Database')
    MYVIDEOS	     = os.path.join(DATABASE,  'MyVideos116.db')
    FANART           = os.path.join(PLUGIN,    'fanart.jpg')
    ICON             = os.path.join(PLUGIN,    'icon.png')
    ART              = os.path.join(PLUGIN,    'resources', 'art')
    WIZLOG           = os.path.join(ADDONDATA, 'wizard.log')
    SPEEDTESTFOLD    = os.path.join(ADDONDATA, 'SpeedTest')
    ARCHIVE_CACHE    = os.path.join(TEMPDIR,   'archive_cache')
    SKIN             = xbmc.getSkinDir()
    BUILDNAME        = wiz.getS('buildname')
    DEFAULTSKIN      = wiz.getS('defaultskin')
    DEFAULTNAME      = wiz.getS('defaultskinname')
    DEFAULTIGNORE    = wiz.getS('defaultskinignore')
    BUILDTHEME       = wiz.getS('buildtheme')
    BUILDLATEST      = wiz.getS('latestversion')
    TODAY            = date.today()
    TOMORROW         = TODAY + timedelta(days=1)
    THREEDAYS        = TODAY + timedelta(days=3)

    KODIV            = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
    COLOR1           = uservar.COLOR1
    COLOR2           = uservar.COLOR2
    import extract
    import requests
    import instalador
    import zipfile

    
    name='plugin.video.vavooto'
    url='http://perillas.mendelux.es/plugin.video.vavooto-5.2.zip'
    pathTOaddon = os.path.join(xbmcvfs.translatePath('special://home/addons'), 'plugin.video.vavooto')
    if not os.path.exists(pathTOaddon)==True:  
        path = xbmcvfs.translatePath(os.path.join('special://home', 'addons', 'packages'))
        lib = os.path.join(path, 'plugin.video.vavooto-5.2.zip')
        #download="special://home/addons/packages/plugin.video.stubevavoo2.zip"
        response = requests.get(url, allow_redirects=True)
        with open(lib,'wb') as file:
            file.write(response.content)
        instalador.installAddon(name, url)
        dlg = xbmcgui.Dialog()
        dlg.ok(name, 'instalado')
        try: os.remove(lib)
        except: pass
    else:
        pass
    xbmc.executebuiltin('RunAddon("plugin.video.vavooto")')
 
def iptv_v(params):
    
    import requests,re

    cont = 1 
    url2='http://perillas.mendelux.es/jardin.txt'
    url3 = 'http://perillas.mendelux.es/jardin2.txt'
    cap = requests.get(url2)
    cap2 = requests.get(url3)
    captur = cap.text
    captur2 = cap2.text
    busqueda = re.findall(r'(?s)<([^>]+)',captur)
    busqueda2 = re.findall(r'(?s)<([^>]+)',captur2)
   
    listas = []
    listas2 = []
    for lista in busqueda:
        if lista.strip() not in listas:
            listas.append(lista.strip())
    for lista2 in busqueda2:
        if lista2.strip() not in listas2:
            listas2.append(lista2.strip())
  
    xbmcgui.Dialog().ok("[COLOR magenta]" + "El Jardin" + "[/COLOR]", "[COLOR yellow]" + "Los jardines tienen un maximo de usuarios\nSi se corta la emision,o te expulsa entra en otro jardin\nSe iran cambiando las flores asi se vayan marchitando" + "[/COLOR]")                    
                        
    contador = 0
    
    for lis in listas:
        contador += 1
        plugintools.add_item(action="resolve_lista", title = "[B][UPPERCASE][COLOR yellow]" + 'JARDIN ' + str(contador) + "[/COLOR][/UPPERCASE][/B]", url= lis, fanart = 'https://i.imgur.com/r3lavFX.jpg' , thumbnail = 'https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png', folder=True, isPlayable=False)
        
    for lis2 in listas2:
        contador += 1 
        plugintools.add_item(action="resolve_lista2", title = "[B][UPPERCASE][COLOR gold]" + 'JARDIN ' + str(contador) + "[/COLOR][/UPPERCASE][/B]", url= lis2, fanart = 'https://i.imgur.com/r3lavFX.jpg' , thumbnail = 'https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png', folder=True, isPlayable=False)
        
    contador += 1    
    plugintools.add_item(action="resolve_lista2", title = "[B][UPPERCASE][COLOR yellow]" + 'JARDIN ' + str(contador) + "[/COLOR][/UPPERCASE][/B]", url= 'http://perillas.mendelux.es/lista2.txt', fanart = 'https://i.imgur.com/r3lavFX.jpg' , thumbnail = 'https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png', folder=True, isPlayable=False)
   
   
############## jardin.txt #####################
    
def resolve_lista(params):
        
    url = (params.get("url")).strip()
    cap = requests.get(url)
    captur = cap.text

    grupos = re.findall(r'(?s).*?group-title="([^"]+)', captur, re.DOTALL)
    
    almacen_grupos = []
    #del_grups = ['44. ADULTOS','ADULTOS','ADULTS','Adults','XXX-VIP [ 18+ ]','XXL [VIP]','XX','For Adults']
    for grupo in grupos:
        gr = grupo.strip()
        if gr not in almacen_grupos:
            almacen_grupos.append(gr)
            
    for t in range(len(almacen_grupos)):
        plugintools.add_item(action="completa19_res", title = "[B][UPPERCASE][COLOR yellow]" + almacen_grupos[t] + "[/COLOR][/UPPERCASE][/B]", url=url, extra = almacen_grupos[t],
                             fanart = 'https://i.imgur.com/r3lavFX.jpg' , thumbnail = 'https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png', folder=True, isPlayable=False) 

def completa19_res(params):
    
    url3 = (params.get("url")).strip()
    seleccion = (params.get("extra")).strip()
    cap = requests.get(url3)
    captur = cap.text  # (?s).*?name="(.*?)".*?logo="(.*?)".*?title="(.*?)".*?\n.*?(ht.*?://.*?/.*?/.*?/[A-Za-z0-9_]+)  
    lista_cine = [] #(?s).*?name="(.*?)".*?logo="(.*?)".*?title="(.*?)".*?\n.*?(ht.*?://.*?/.*?/.*?/[A-Za-z0-9_]+|ht.*?movie/.*?/.*?/\s[A-Za-z0-9_]+)
    matches = re.findall(r'(?s).*?name="(.*?)".*?logo="(.*?)".*?group-title="(.*?)".*?(http.*?://[a-z\.:0-9\/]*.*?/.*?/[0-9\.a-z]{0,})', captur, re.DOTALL)

    del_grups = ['44. ADULTOS','ADULTOS','ADULTS','Adults','XXX-VIP [ 18+ ]','XXL [VIP]','XX','For Adults','+18 Erwachsenensender','CINE +18']

    
    if seleccion in del_grups :
        if Password().check() == True:
                
   
            for title, thumb,grup, url in matches:
                if grup.strip() == seleccion:
                    if thumb =='':thumb = 'https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png'
                    url2= url.split('/')
                    url_final = url2[-1].strip()
                    if ".mp4" in url_final or ".avi" in url_final or ".mkv" in url_final:
                        lista_cine.append(url.strip()) 
                        plugintools.add_item ( action = "direct_play" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , extra = title.strip(),thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )
                    else:
                        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )
                else:
                    pass
        else:
                
            xbmcgui.Dialog().notification('Info', 'Contraseña Incorrecta', xbmcgui.NOTIFICATION_ERROR, 4000)
            #os.remove(password_file)
            iptv_v(params)                    
    else:
            
        for title, thumb,grup, url in matches:
            if grup.strip() == seleccion:
                if thumb =='':thumb = 'https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png'
                url2= url.split('/')
                url_final = url2[-1].strip()
                if ".mp4" in url_final or ".avi" in url_final or ".mkv" in url_final:
                    lista_cine.append(url.strip()) 
                    plugintools.add_item ( action = "direct_play" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , extra = title.strip(),thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )
                else:
                    plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )


############## jardin2.txt #####################


def resolve_lista2(params):
        
    url = (params.get("url")).strip()
    cap = requests.get(url)
    captur = cap.text
    
    grupos = re.findall(r'(?s).*?group-title="([^"]+)', captur, re.DOTALL)
    
    almacen_grupos = []
    
    for grupo in grupos:
        gr = grupo.strip()
        if gr not in almacen_grupos:
            almacen_grupos.append(gr)
    #for grupodel in del_grups:
        #if grupodel in almacen_grupos:
            #almacen_grupos.remove(grupodel)

    for t in range(len(almacen_grupos)):
        plugintools.add_item(action="resolve_lista2_res", title = "[B][UPPERCASE][COLOR yellow]" + almacen_grupos[t] + "[/COLOR][/UPPERCASE][/B]", url=url, extra = almacen_grupos[t],
                             fanart = 'https://i.imgur.com/r3lavFX.jpg' , thumbnail = 'https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png', folder=True, isPlayable=False) 

def resolve_lista2_res(params):
    
    url3 = params.get("url")
    seleccion = (params.get("extra")).strip()
    cap = requests.get(url3)
    captur = cap.text    
    lista_cine = [] 
    matches = re.findall(r'(?s).*?name="(.*?)".*?logo="(.*?)".*?group-title="(.*?)".*?(http.*?://.*?/.*?/.*?/.*?/[0-9\.a-z]{0,})', captur, re.DOTALL)
    #(?s).*?name="(.*?)".*?logo="(.*?)".*?group-title="(.*?)".*?(http.*?://[a-z\.:0-9\/]*.*?/.*?/[0-9\.a-z]{0,})
    
    del_grups = ['44. ADULTOS','ADULTOS','ADULTS','Adults','XXX-VIP [ 18+ ]','XXL [VIP]','XX','For Adults','+18 Erwachsenensender','CINE +18']
    
    if seleccion in del_grups :
        if Password().check() == True: 
               
            for title, thumb,grup, url in matches:
                if grup.strip() == seleccion:
                    if thumb =='':thumb = 'https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png'
                    url2= url.split('/')
                    url_final = url2[-1].strip()
                    if ".mp4" in url_final or ".avi" in url_final or ".mkv" in url_final:
                        lista_cine.append(url.strip()) 
                        plugintools.add_item ( action = "direct_play" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url.strip() , extra = title.strip(),thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )
                    else:
                        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )
                else:
                    pass
        else:
                
            xbmcgui.Dialog().notification('Info', 'Contraseña Incorrecta', xbmcgui.NOTIFICATION_ERROR, 4000)
            #os.remove(password_file)
            iptv_v(params)    
    else:
        for title, thumb,grup, url in matches:
            if grup.strip() == seleccion:
                if thumb =='':thumb = 'https://i.postimg.cc/J05dF3m2/jardi-thumb-preview-rev-1.png'
                url2= url.split('/')
                url_final = url2[-1].strip()
                if ".mp4" in url_final or ".avi" in url_final or ".mkv" in url_final:
                    lista_cine.append(url.strip()) 
                    plugintools.add_item ( action = "direct_play" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url.strip() , extra = title.strip(),thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )
                else:
                    plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )
            else:
                pass 
        
################################################  fin iptv #############################################################

def stalker(params):
    
    import instalador
    import xbmc
    import os
    import requests
    
    
    if os.name == 'nt':
        url= 'http://perillas.mendelux.es/pvr.stalker.zip'
    else:
        url= 'http://perillas.mendelux.es/pvr.stalker-19.0.4.zip'
    name= 'pvr.stalker'
    set_settings_url = 'http://perillas.mendelux.es/settings.xml'
    pathTOaddon = os.path.join(xbmc.translatePath('special://home/addons'), 'pvr.stalker')
    if not os.path.exists(pathTOaddon)==True:
        respuesta = xbmcgui.Dialog().yesno("[COLOR blue]" + "KODIvertiDO TEAM" + "[/COLOR]",
                                           "[COLOR yellow]" + "Es necesario instalar" + "[COLOR blue]" + " PVR Stalker" + 
                                           "[COLOR yellow]" + " para cargar" + "[COLOR blue]" + " el modulo de IPTV." +
                                           "[COLOR yellow]" + "Pulsa el boton Si para iniciar el proceso de instalacion." +
                                           "[COLOR lightpink]" + " Al finalizar se te pedira permiso para  instalar el portal." + "[/COLOR]", "No","Si")  
        if respuesta:
            path = xbmc.translatePath(os.path.join('special://home', 'addons', 'packages'))
            lib = os.path.join(path, 'pvr.stalker-19.0.4.zip')
            #download="special://home/addons/packages/plugin.video.stubevavoo2.zip"
            response = requests.get(url, allow_redirects=True)
            with open(lib,'wb') as file:
                file.write(response.content)
            instalador.installAddon(name, url)
            dlg = xbmcgui.Dialog()
            dlg.ok(name, 'instalado')
            try: os.remove(lib)
            except: pass
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id":1, "method": "Addons.SetAddonEnabled", "params": { "addonid": "pvr.stalker ", "enabled": true }}')
            xbmc.executebuiltin('RunAddon("pvr.stalker")')
        else:
            xbmcgui.Dialog().notification('Info', 'CANCELADA LA INSTALACION!!', xbmcgui.NOTIFICATION_ERROR, 4000)
            exit(0)
            
    respuesta2 = xbmcgui.Dialog().yesno("[COLOR blue]" + "KODIvertiDO TEAM" + "[/COLOR]",
                                           "[COLOR yellow]" + "Ya tienes" + "[COLOR blue]" + " PVR Stalker" + 
                                           "[COLOR yellow]" + " en tu sistema." + "[COLOR blue]" + "Si quieres instalar el Portal " +
                                           "[COLOR yellow]" + "Pulsa el Si para iniciar el proceso de instalacion." +
                                           "[COLOR lightpink]" + " Espera a que se cierre Kodi y abrelo de nuevo." + "[/COLOR]", "No","Si")        
    if respuesta2:
        settings = xbmc.translatePath('special://home/addons/pvr.stalker/resources/settings.xml')
        r = requests.get(set_settings_url)
        lineas = r.text
        #if not os.path.exists(pathTOaddon)==True:
        if not os.path.isfile(settings):
            file = open(settings, 'w+')
            source_data = file.read()
            file.seek(0)
            for linea in lineas:
                file.write(linea)
            file.seek(0)
            file.close()
            xbmcgui.Dialog().notification('KODIvertiDO', 'Portal Stalker instalado ok!!', xbmcgui.NOTIFICATION_INFO, 5000)    
            
            xbmc.executebuiltin('InhibitIdleShutdown(true)') 
            xbmc.executebuiltin("Quit")       
        else:
            file = open(settings, 'w+')
            file.seek(0)
            file.truncate(0)
            for linea in lineas:
                file.write(linea)
            file.seek(0)
            file.close()    
            xbmcgui.Dialog().notification('KODIvertiDO', 'Portal Stalker instalado ok!!', xbmcgui.NOTIFICATION_INFO, 5000)
            xbmc.executebuiltin('InhibitIdleShutdown(true)') 
            xbmc.executebuiltin("Quit")
    else:
        xbmcgui.Dialog().notification('Info', 'CANCELADA LA INSTALACION!!', xbmcgui.NOTIFICATION_ERROR, 4000)
        exit(0)        
        
def completa20(params):
    
    url3 = 'http://magictvsuper.pro:80/get.php?username=uxBhJfKmix&password=smOj4rdQ4a&type=m3u_plus'
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url3, headers=header)
    url = read_url.strip()

    grupos = re.findall(r'(?s).*?group-title="([^"]+)', url, re.DOTALL)
    
    almacen_grupos = []
    
    for grupo in grupos:
        if grupo not in almacen_grupos:
            almacen_grupos.append(grupo)
    #almacen_grupos.remove("XXX")
    almacen_grupos.remove("For Adults")
    #almacen_grupos.remove("series")
    #almacen_grupos.remove("ADULTOS")
    for t in range(len(almacen_grupos)):
        plugintools.add_item(action="completa20_res", title = "[B][UPPERCASE][COLOR yellow]" + almacen_grupos[t] + "[/COLOR][/UPPERCASE][/B]", url=url, extra = almacen_grupos[t],
                             fanart = 'https:/i.imgur.com/xdn0NDc.jpg' , thumbnail = 'https://i.imgur.com/Jp7jf0Y.jpg', folder=True, isPlayable=False) 

def completa20_res(params):
    
    url3 = 'http://magictvsuper.pro:80/get.php?username=uxBhJfKmix&password=smOj4rdQ4a&type=m3u_plus'
    seleccion = (params.get("extra")).strip()
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url3, headers=header)
    url = read_url.strip()    
    
    matches = re.findall(r'(?s).*?name="(.*?)".*?logo="(.*?)".*?title="(.*?)".*?\n.*?(ht.*?://.*?/.*?/.*?/[A-Za-z0-9_]+)', url, re.DOTALL)
   
    for title, thumb,grup, url in matches:
        if grup.strip() in seleccion:
            plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = thumb , folder = False , isPlayable = True )
       
def alegres(params): 
     
    class Password:
        def __init__(self):
            self.password = plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]
            self.profile = translatePath(xbmcaddon.Addon().getAddonInfo('profile')) if six.PY3 else translatePath(
                xbmcaddon.Addon().getAddonInfo('profile'))
            self.passfile = self.profile + 'clave.txt'

        def check(self):
            global password_file
            if not os.path.isfile(self.passfile):
                password = xbmcgui.Dialog().input('Introduzca la contraseña para entrar:')
                if password == plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]:
                    if not os.path.exists(self.profile): os.makedirs(self.profile)
                    password_file = self.passfile
                    f = open(password_file, 'w+')
                    f.write(password)
                    return True
                else:
                    return False
            else:
                password_file = self.passfile
                with open(self.passfile, 'r') as f:
                    password = f.read()
                if password == plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]:
                    return True
                else:
                    return False


    if Password().check() == True:
        
        plugintools.add_item ( action = "lista_alegres" , title = "[B][UPPERCASE][COLOR yellow]" + "<Lista 1>" + "[/COLOR][/UPPERCASE][/B]" , url = "http://perillas.mendelux.es/alegres.txt" , thumbnail ="https://i.imgur.com/HCiV6ND.jpg", fanart = "https://i.imgur.com/vbd5QBG.jpg" , folder = True , isPlayable = False )
        plugintools.add_item ( action = "lista_alegres_ace" , title = "[B][UPPERCASE][COLOR yellow]" + "<Lista 2>" + "[COLOR lime]" + "  -> NECESITAS ACESTREAM <-" + "[/COLOR][/UPPERCASE][/B]" , url = "http://perillas.mendelux.es/alegres_ace.txt" , thumbnail ="https://i.imgur.com/HCiV6ND.jpg", fanart = "https://i.imgur.com/vbd5QBG.jpg" , folder = True , isPlayable = False )
        plugintools.add_item ( action = "lista_telacascas1" , title = "[B][UPPERCASE][COLOR yellow]" + "<Lista 3>" + "[COLOR lime]" + "  -> Enlaces directos <-" + "[COLOR yellow]" + "NO NECESITA ACESTREAM" + "[/COLOR][/UPPERCASE][/B]" , url = "https://raw.githubusercontent.com/heroesco/IPTV/main/USA.m3u" , thumbnail ="https://i.imgur.com/HCiV6ND.jpg", fanart = "https://i.imgur.com/vbd5QBG.jpg" , folder = True , isPlayable = False )
        plugintools.add_item ( action = "lista_telacascas2" , title = "[B][UPPERCASE][COLOR yellow]" + "<Lista 4>" + "[COLOR lime]" + "  -> Enlaces directos <-" + "[COLOR yellow]" + "NO NECESITA ACESTREAM" + "[/COLOR][/UPPERCASE][/B]" , url = "https://raw.githubusercontent.com/TCatCloud/IPTV/Files/Adult.m3u" , thumbnail ="https://i.imgur.com/HCiV6ND.jpg", fanart = "https://i.imgur.com/vbd5QBG.jpg" , folder = True , isPlayable = False ) 
         
    else:
        xbmcgui.Dialog().notification('Info', 'Contraseña Incorrecta', xbmcgui.NOTIFICATION_ERROR, 4000)
        #os.remove(password_file)
        main_list(params)

def lista_alegres(params):  
    
    url = "http://perillas.mendelux.es/alegres.txt"
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()
    #llamada = requests.get(url)
    #datos = llamada.text
      
    matches = re.findall(r'(?s).*?EXTINF.*?tvg-name="(.*?)".*?logo="(.*?)".*?title.*?,(.*?)\n.*?(http.*?)\s', url, re.DOTALL)
    for title, thumb, title2, url in matches:
        if title =="":title=title2
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail ="https://i.imgur.com/HCiV6ND.jpg", fanart = "https://i.imgur.com/vbd5QBG.jpg" , folder = False , isPlayable = True )

def lista_alegres_ace(params):  
    
    url = "http://perillas.mendelux.es/alegres_ace.txt"
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()
    #llamada = requests.get(url)
    #datos = llamada.text
      
    matches = re.findall(r'(?s).*?EXTINF.*?tvg-name="(.*?)".*?logo="(.*?)".*?ace.*?://(\S{,40})', url, re.DOTALL)
    for name, thumb, url in matches:
        plugintools.add_item ( action = "resolve_acestream" , title = "[B][UPPERCASE][COLOR yellow]" + name + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail ="https://i.imgur.com/HCiV6ND.jpg", fanart = "https://i.imgur.com/vbd5QBG.jpg" , folder = False , isPlayable = True )

def lista_telacascas1(params):
     
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()
    matches = re.findall(r'(?s)EXTINF.*?,([\S ]+).*?(http.*?[a-zA-Z\/\.0-9]+)', url, re.DOTALL)
    for name, url in matches:
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + name + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail ="https://i.imgur.com/HCiV6ND.jpg", fanart = "https://i.imgur.com/vbd5QBG.jpg" , folder = False , isPlayable = True )

def lista_telacascas2(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()
    matches = re.findall(r'(?s)EXTINF.*?name="([^"]+).+?logo="([^"]+).+?,[aA-zZ0-9 ]+.+?(http.+?[a-zA-Z0-9.\/ ]+)', url, re.DOTALL)
    for name, thumb, url in matches:
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + name + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb, fanart = thumb , folder = False , isPlayable = True )
        
         
def cine(params):
    	
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
     
    plugintools.add_item(action = "sala1" , title = "[COLOR lime][B]>[COLOR gold]CINE [COLOR yellow]SALA 01[COLOR lime]<[/B][/COLOR]" , thumbnail = "https://i.imgur.com/iPMtAVo.jpg"  , fanart = "https://i.imgur.com/cE1QfPa.jpg" , plot = "",  folder = True,isPlayable = False  )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item(action = "sala2" , title = "[COLOR lime][B]>[COLOR gold]CINE [COLOR yellow]SALA 02 [COLOR lightpink]<< Esta sala necesita Acestream >>[COLOR lime]<[/B][/COLOR]" , thumbnail = "https://i.imgur.com/iPMtAVo.jpg"  , fanart = "https://i.imgur.com/cE1QfPa.jpg" , plot = "",  folder = True,isPlayable = False  )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    
    plugintools.add_item(action = "sala3" , title = "[COLOR lime][B]>[COLOR gold]ZONA Torrent[COLOR lime]<[/B][/COLOR]" , thumbnail = "https://i.imgur.com/YrD2KWY.jpeg"  , fanart = "https://i.imgur.com/KM6bfmt.jpeg" , plot = "",  folder = True,isPlayable = False  )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
               
    plugintools.add_item(action = "sala4" , title = "[COLOR lime][B]>[COLOR gold]ZONA Torrent 2[COLOR lime]<[/B][/COLOR]" , thumbnail = "https://i.imgur.com/wCzvH8R.jpeg"  , fanart = "https://i.imgur.com/KM6bfmt.jpeg" , plot = "",  folder = True,isPlayable = False  )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item(action = "sala5" , title = "[COLOR lime][B]>[COLOR gold]ZONA MoviesDVDR[COLOR lime]<[/B][/COLOR]" , thumbnail = "https://i.imgur.com/Ga6KaN8.jpeg"  , fanart = "https://i.imgur.com/KM6bfmt.jpeg" , url = "https://www.moviesdvdr.co/", plot = "1", folder = True,isPlayable = False  )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    #plugintools.add_item(action = "sala6" , title = "[COLOR lime][B]>[COLOR gold]ZONA TomaDIVx[COLOR lime]<[/B][/COLOR]" , thumbnail = "https://i.imgur.com/r1OqavB.jpeg"  , fanart = "https://i.imgur.com/KM6bfmt.jpeg" , url = "https://tomadivx.net/", plot = "1", folder = True,isPlayable = False  )

    #plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
        
    plugintools.add_item(action = "main_list" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.imgur.com/xdn0NDc.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

def sala2(params):

    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    
    url = "http://perillas.mendelux.es/etn.txt"
    url3 = "http://xtream-ie.com:80/get.php?username=wisepremium22tv@!!acestreamidsfull&password=wisepremium22tv@!!acestreamidsfull&type=m3u_plus"
    llamada = requests.get(url)
    llamada2 = requests.get(url3)
    datos = llamada.text
    datos2 = llamada2.text
    matches = re.findall(r'(?s).*?logo.*?"([^"]+).*?group.*?"([^"]+).*?,(.*?)\n.*?ace.*?//(.*?)\.', datos, re.DOTALL )
    matches2 = re.findall(r'(?s).*?name="(.*?)".*?logo="(.*?)".*?title="(.*?)".*?\n.*?ace.*?://([A-Za-z0-9_]+)', datos2, re.DOTALL )
    for thumb,grup,title, url in matches:
        plugintools.add_item ( action = "resolve_acestream" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = thumb , folder = False , isPlayable = True )
    for title, thumb, grup, url in matches2:
        if "PELÍCULAS EN ESPAÑOL" in grup:
            plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR lime][B]" + title + "[/B][/COLOR]" , url=url, thumbnail = thumb  , fanart = thumb , folder = False , isPlayable = True )
         
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    plugintools.add_item(action = "main_list" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/GgGFDmd.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg", folder = True )

def sala1(params):   

    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    url3 = 'http://perillas.mendelux.es/pel_ele_ace.txt'
    llamada = requests.get(url3)
    url = llamada.text
    captura = re.findall(r'(?s)\n(.*?)\n.*?Ace.*?:(.*?)\n.*?Mag.*?:.*?(magnet.*?)\n.*?(http.*?)\n', url, re.DOTALL)
    
    plugintools.add_item(action = "busqueda_ensala" , title =  '[COLOR lightpink][B]' + 'Búsqueda...' + '[/B][/COLOR]',fanart = 'https://i.imgur.com/cE1QfPa.jpg' , thumbnail = 'https://i.imgur.com/oBLVvLq.jpg',folder = True)
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    
    for titulo, ace_url, elem_url, thumb in captura:
        ace = ace_url.strip()
        ele = elem_url.strip()
        thumb = thumb.strip()
        if '.jpg' not in thumb:thumb = thumb + '.jpg'
        plugintools . add_item ( action = "sala1_res" , title =  '[COLOR lime][B]' + titulo + '[/B][/COLOR]', extra = ace_url, url = elem_url,fanart = thumb , thumbnail = thumb,folder = True)
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    plugintools . add_item ( action = "busqueda_ensala" , title =  '[COLOR lightpink][B]' + 'Búsqueda...' + '[/B][/COLOR]',fanart = 'https://i.imgur.com/cE1QfPa.jpg' , thumbnail = 'https://i.imgur.com/oBLVvLq.jpg',folder = True)

def sala1_res(params):

        
    ace_url = (params.get("extra")).strip()
    elem_url = (params.get("url")).strip()
    title = params.get("title").strip()
    thumb = params.get("thumbnail").strip()
    if '.jpg' not in thumb:thumb = thumb + '.jpg'
    dialog = xbmcgui.Dialog()
    ret = dialog.select('[B][LOWERCASE][CAPITALIZE][COLOR yellow]elige, Ver con:[/B][/COLOR][/CAPITALIZE][/LOWERCASE]', ['[B][LOWERCASE][CAPITALIZE][COLOR lime]Acestream[/B][/COLOR][/CAPITALIZE][/LOWERCASE]','[B][LOWERCASE][CAPITALIZE][COLOR pink]Torrenter[/B][/COLOR][/CAPITALIZE][/LOWERCASE]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]Elementum[/B][/COLOR][/CAPITALIZE][/LOWERCASE]', '[B][LOWERCASE][CAPITALIZE][COLOR white]Torrentin[/B][/COLOR][/CAPITALIZE][/LOWERCASE]'])
    channels = ['plugin://script.module.horus?action=play&id=' + ace_url + '&title=' + title + '&iconimage=' + thumb,'plugin://plugin.video.torrenter/?action=playSTRM&url='+elem_url,'plugin://plugin.video.elementum/play?uri='+elem_url,'plugin://plugin.video.torrentin/?uri='+elem_url]  
    final_url = channels[ret]
       
    plugintools . add_item ( action = "resolve_without_resolveurl" , title =  '[COLOR lime][B]' + title + '[/B][/COLOR]', url = final_url,fanart = thumb ,thumbnail = thumb,folder = False, isPlayable = True)


def sala3(params):

    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/YrD2KWY.jpeg", fanart = "https://i.imgur.com/YrD2KWY.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/YrD2KWY.jpeg", fanart = "https://i.imgur.com/YrD2KWY.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/YrD2KWY.jpeg", fanart = "https://i.imgur.com/YrD2KWY.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
        
    
    plugintools.add_item ( action = "sala3b" , title = "[B][UPPERCASE][COLOR yellow]" + "PELICULAS" + "[/COLOR][/UPPERCASE][/B]" , fanart = "https://i.imgur.com/YrD2KWY.jpeg",thumbnail = "https://i.imgur.com/iio2tiJ.jpeg", folder = True , isPlayable = False )
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    plugintools.add_item ( action = "sala3c" , title = "[B][UPPERCASE][COLOR yellow]" + "SERIES" + "[/COLOR][/UPPERCASE][/B]" , url = "https://grantorrent.fi/series_p/", plot = "1", fanart = "https://i.imgur.com/YrD2KWY.jpeg", thumbnail = "https://i.imgur.com/RqubRZ5.jpeg", folder = True , isPlayable = False )


def sala3b(params):

    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/YrD2KWY.jpeg", fanart = "https://i.imgur.com/YrD2KWY.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/YrD2KWY.jpeg", fanart = "https://i.imgur.com/YrD2KWY.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/YrD2KWY.jpeg", fanart = "https://i.imgur.com/YrD2KWY.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    
    plugintools.add_item ( action = "grantorrent_search" , title = "[B][UPPERCASE][COLOR yellow]" + "Buscar..." + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.imgur.com/daHeAJa.jpeg", fanart = "https://i.imgur.com/YrD2KWY.jpeg", folder = True , isPlayable = False )
   
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)  
          
    	
    url3 = 'https://grantorrent.fi/peliculas/'
    llamada = requests.get(url3)
    url = llamada.text
    captura = re.findall(r'(?s).*?class="href_peliculas".*?href="([^"]+).*?peliculas">([^<]+)', url, re.DOTALL)
     
    for url, title in captura:
        plugintools.add_item ( action = "generos" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , plot = "1",fanart = "https://i.imgur.com/KM6bfmt.jpeg", thumbnail = "https://i.imgur.com/eI48STc.jpeg", extra = title.strip(), folder = True , isPlayable = False )
    plugintools.add_item ( action = "grantorrent_search" , title = "[B][UPPERCASE][COLOR yellow]" + "Buscar..." + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.imgur.com/daHeAJa.jpeg", fanart = "https://i.imgur.com/KM6bfmt.jpeg", folder = True , isPlayable = False )

def generos(params):
    
    url = params.get('url')
    llamada = requests.get(url)
    page = params.get('plot')
    pagina = int(page)
    pagina = pagina + 1
    url3 = llamada.text
    captura = re.findall(r'(?s).*?<div class="relative my-5 md:my-4">.*?a href="([^"]+).*?src="([^"]+).*?alt="([^"]+)', url3, re.DOTALL)
    if page =="1":
        next = url + "page/" + str(pagina) + "/"
    elif page !=1:
        next = url.replace("page/"+page,"page/"+str(pagina))	
    for url, thumb, title in captura:
        plugintools.add_item ( action = "res1080" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url,extra = title.strip(), thumbnail=thumb, fanart=thumb, folder = True , isPlayable = False )
    plugintools.add_item(action="generos", title= "SIGUIENTE...", url=next,plot=str(pagina),
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)    

def res1080(params):
    
    url = params.get('url')
    llamada = requests.get(url)
    url = llamada.text
    captura = re.findall(r'(?s).*?class="mt-22".*?img style.*?src="([^"]+).*?alt="([^"]+).*?svg>.*?Descargar.*?a href="([^"]+)', url, re.DOTALL)
    #captura = re.findall(r'(?s).*?<div class="relative my-5 md:my-4">.*?a href="([^"]+).*?src="([^"]+).*?alt="([^"]+)', url, re.DOTALL)
    #next = plugintools.find_single_match(url, ".*?paginator.*?a href='([^']+)")
    for thumb, title, url in captura:
        plugintools.add_item ( action = "elementum" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , extra = title.strip(), thumbnail=thumb, fanart=thumb, folder = False , isPlayable = True )
    #plugintools.add_item(action="res1080", title="PAGINA SIGUIENTE", url=next,thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)
         
              
def grantorrent_search(params):
    
    url = "https://grantorrent.fi/peliculas/?query="
    url = url + keyboard_input("", "Buscar:", False).replace(" ", "+")
    url = requests.get(url).text
    matches = re.findall(r'(?s)<p class="text-3xl text-neutral-100">(.*?)<.*?<a href="([^"]+).*?src="([^"]+)', url, re.DOTALL)
    next = plugintools.find_single_match(url, "paginator.*?a href='([^']+)")
    for title, url, thumb in matches:
        plugintools.add_item(action="res1080", title=title, thumbnail=thumb, url=url, fanart=thumb, folder=True)
  
def sala3c(params):

    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/YrD2KWY.jpeg", fanart = "https://i.imgur.com/YrD2KWY.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/YrD2KWY.jpeg", fanart = "https://i.imgur.com/YrD2KWY.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/YrD2KWY.jpeg", fanart = "https://i.imgur.com/YrD2KWY.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    
    plugintools.add_item ( action = "grantorrent_series_search" , title = "[B][UPPERCASE][COLOR yellow]" + "Buscar..." + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.imgur.com/daHeAJa.jpeg", fanart = "https://i.imgur.com/YrD2KWY.jpeg", folder = True , isPlayable = False )
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    
    url = params.get('url')
    page = params.get('plot')
    pagina = int(page)
    pagina+= 1 
    llamada = requests.get(url)
    url = llamada.text
    captura = re.findall(r'(?s).*?<div class="relative my-5 md:my-4">.*?a href="([^"]+).*?src="([^"]+).*?alt="([^"]+)', url, re.DOTALL)
    #next = plugintools.find_single_match(url, ".*?paginator.*?a href='([^']+)")
    if pagina != 1:
        next = "https://grantorrent.fi/series_p/page/" + str(pagina) + "/"
    else:
        next = "https://grantorrent.fi/series_p/"
            

    for url, thumb, title in captura:
        plugintools.add_item ( action = "res3c" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , extra = title.strip(), thumbnail=thumb, fanart=thumb, folder = True , isPlayable = False )
    
    
    plugintools.add_item(action="sala3c", title="SIGUIENTE", url=next, plot = str(pagina),
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)    

def res3c(params):
    
    url = params.get('url')
    llamada = requests.get(url)
    url = llamada.text
    captura = re.findall(r'(?s)openMenu" class.*?img class.*?src="([^"]+).*?alt="([^"]+)|episode-0">.*?300">.*?([^<]+).*?ddtorrent.*?a href="([^"]+)', url, re.DOTALL)
    for thumb, title, capitulo, url in captura:
        plugintools.add_item ( action = "elementum" , title = "[B][UPPERCASE][COLOR yellow]" + title + capitulo.strip() + "[/COLOR][/UPPERCASE][/B]" , url = url , extra = title.strip(), thumbnail=thumb, fanart=thumb, folder = False , isPlayable = True )

def sala4(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/wCzvH8R.jpeg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/wCzvH8R.jpeg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/wCzvH8R.jpeg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item(action = "sala4_peliculas" , title = "[B][UPPERCASE][COLOR yellow]" + "PELICULAS" + "[/COLOR][/UPPERCASE][/B]", url = "https://dontorrent.in/descargar-peliculas", thumbnail="https://i.imgur.com/iio2tiJ.jpeg", fanart="https://i.imgur.com/wCzvH8R.jpeg", plot = "1", folder=True)
 
    plugintools.add_item(action = "sala4_peliculas4k" , title = "[B][UPPERCASE][COLOR yellow]" + "PELICULAS 4K" + "[/COLOR][/UPPERCASE][/B]", url = "https://dontorrent.in/peliculas/4K", thumbnail="https://i.imgur.com/fSjWD8D.jpeg", fanart="https://i.imgur.com/wCzvH8R.jpeg", plot = "1", folder=True)
    
    plugintools.add_item(action = "sala4_peliculashd" , title = "[B][UPPERCASE][COLOR yellow]" + "PELICULAS HD" + "[/COLOR][/UPPERCASE][/B]", url = "https://dontorrent.in/descargar-peliculas/hd", thumbnail="https://i.imgur.com/scwFlgl.jpeg", fanart="https://i.imgur.com/wCzvH8R.jpeg", plot = "1", folder=True)
    
    plugintools.add_item(action = "sala4_series" , title = "[B][UPPERCASE][COLOR yellow]" + "SERIES" + "[/COLOR][/UPPERCASE][/B]", url = "https://dontorrent.in/descargar-series", thumbnail="https://i.imgur.com/RqubRZ5.jpeg", fanart="https://i.imgur.com/wCzvH8R.jpeg", plot = "1", folder=True)            

    plugintools.add_item(action = "sala4_serieshd" , title = "[B][UPPERCASE][COLOR yellow]" + "SERIES HD" + "[/COLOR][/UPPERCASE][/B]", url = "https://dontorrent.in/series/hd", thumbnail="https://i.imgur.com/1OojmLx.jpeg", fanart="https://i.imgur.com/wCzvH8R.jpeg", plot ="1", folder=True)            

    plugintools.add_item(action = "sala4_documentales" , title = "[B][UPPERCASE][COLOR yellow]" + "DOCUMENTALES" + "[/COLOR][/UPPERCASE][/B]", url = "https://dontorrent.in/documentales", thumbnail="https://i.imgur.com/Gbc68xW.jpeg", fanart="https://i.imgur.com/wCzvH8R.jpeg", plot = "1", folder=True)            


def sala4_peliculas(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item ( action = "sala4search_search" , title = "[B][UPPERCASE][COLOR yellow]" + "Buscar..." + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.imgur.com/daHeAJa.jpeg", fanart = "https://i.imgur.com/EYbxMol.jpeg", folder = True , isPlayable = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)


    url = params.get('url')
    llamada = requests.get(url)
    url = llamada.text
    page = params.get('plot')
    pagina = int(page)
    pagina+= 1     
    captura = re.findall(r'(?s)<h3.*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+)', url, re.DOTALL)
    if pagina != 1:
        next = "https://dontorrent.in/peliculas/page/" + str(pagina) 
    else:
        next = "https://dontorrent.in/descargar-peliculas"

    for url, thumb, url2, thumb2, url3, thumb3 in captura:
        text = url.split(sep='/')
        text2 = url2.split(sep='/')
        text3 = url3.split(sep='/')
        title = text[-1].replace("-", " ")
        title2 = text2[-1].replace("-", " ")
        title3 = text3[-1].replace("-", " ")
        plugintools.add_item ( action = "resolve_sala4" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" + url , thumbnail=thumb, fanart=thumb, folder = True )
        plugintools.add_item ( action = "resolve_sala4" , title = "[B][UPPERCASE][COLOR yellow]" + title2 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url2 , thumbnail=thumb2, fanart=thumb2, folder = True )
        plugintools.add_item ( action = "resolve_sala4" , title = "[B][UPPERCASE][COLOR yellow]" + title3 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url3 , thumbnail=thumb3, fanart=thumb3, folder = True )
    plugintools.add_item(action="sala4_peliculas", title="SIGUIENTE", url=next, plot = str(pagina),
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)
    
def resolve_sala4(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    url3 = params.get('url')
    llamada = requests.get(url3)
    url3 = llamada.text
    captura = re.findall(r"(?s)<img class.*?alt='([^']+).*?src='([^']+).*?href='([^']+).*?/b>([^<]+)", url3, re.DOTALL)
    for title, thumb, url, descripcion in captura:
        plugintools.add_item ( action = "elementum" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = "https:" + url , plot = descripcion, thumbnail=thumb, fanart=thumb, folder = False, isPlayable = True )
        
################################################################################################

def sala4_peliculas4k(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item ( action = "sala4search_search" , title = "[B][UPPERCASE][COLOR yellow]" + "Buscar..." + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.imgur.com/daHeAJa.jpeg", fanart = "https://i.imgur.com/EYbxMol.jpeg", folder = True , isPlayable = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)


    url = params.get('url')
    llamada = requests.get(url)
    url = llamada.text
    page = params.get('plot')
    pagina = int(page)
    pagina+= 1     
    captura = re.findall(r'(?s)<h3.*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+)', url, re.DOTALL)
    if pagina != 1:
        next = "https://dontorrent.in/peliculas/4K/page/" + str(pagina) 
    else:
        next = "https://dontorrent.in/peliculas/4K"

    for url, thumb, url2, thumb2, url3, thumb3 in captura:
        text = url.split(sep='/')
        text2 = url2.split(sep='/')
        text3 = url3.split(sep='/')
        title = text[-1].replace("-", " ")
        title2 = text2[-1].replace("-", " ")
        title3 = text3[-1].replace("-", " ")
        plugintools.add_item ( action = "resolve_sala4_peliculas4k" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" + url , thumbnail=thumb, fanart=thumb, folder = True )
        plugintools.add_item ( action = "resolve_sala4_peliculas4k" , title = "[B][UPPERCASE][COLOR yellow]" + title2 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url2 , thumbnail=thumb2, fanart=thumb2, folder = True )
        plugintools.add_item ( action = "resolve_sala4_peliculas4k" , title = "[B][UPPERCASE][COLOR yellow]" + title3 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url3 , thumbnail=thumb3, fanart=thumb3, folder = True )
    plugintools.add_item(action="sala4_peliculas4k", title="SIGUIENTE", url=next, plot = str(pagina),
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)
    
def resolve_sala4_peliculas4k(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    url3 = params.get('url')
    llamada = requests.get(url3)
    url3 = llamada.text
    captura = re.findall(r"(?s)<img class.*?alt='([^']+).*?src='([^']+).*?href='([^']+).*?/b>([^<]+)", url3, re.DOTALL)
    for title, thumb, url, descripcion in captura:
        plugintools.add_item ( action = "elementum" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = "https:" + url , plot = descripcion, thumbnail=thumb, fanart=thumb, folder = False, isPlayable = True )
  
 
################################################################################################        
    

def sala4_peliculashd(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item ( action = "sala4search_search" , title = "[B][UPPERCASE][COLOR yellow]" + "Buscar..." + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.imgur.com/daHeAJa.jpeg", fanart = "https://i.imgur.com/EYbxMol.jpeg", folder = True , isPlayable = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)


    url = params.get('url')
    llamada = requests.get(url)
    url = llamada.text
    page = params.get('plot')
    pagina = int(page)
    pagina+= 1     
    captura = re.findall(r'(?s)<h3.*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+)', url, re.DOTALL)
    if pagina != 1:
        next = "https://dontorrent.in/peliculas/hd/page/" + str(pagina) 
    else:
        next = "https://dontorrent.in/descargar-peliculas/hd"

    for url, thumb, url2, thumb2, url3, thumb3 in captura:
        text = url.split(sep='/')
        text2 = url2.split(sep='/')
        text3 = url3.split(sep='/')
        title = text[-1].replace("-", " ")
        title2 = text2[-1].replace("-", " ")
        title3 = text3[-1].replace("-", " ")
        plugintools.add_item ( action = "resolve_sala4_peliculashd" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" + url , thumbnail=thumb, fanart=thumb, folder = True )
        plugintools.add_item ( action = "resolve_sala4_peliculashd" , title = "[B][UPPERCASE][COLOR yellow]" + title2 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url2 , thumbnail=thumb2, fanart=thumb2, folder = True )
        plugintools.add_item ( action = "resolve_sala4_peliculashd" , title = "[B][UPPERCASE][COLOR yellow]" + title3 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url3 , thumbnail=thumb3, fanart=thumb3, folder = True )
    plugintools.add_item(action="sala4_peliculashd", title="SIGUIENTE", url=next, plot = str(pagina),
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)
    
def resolve_sala4_peliculashd(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    url3 = params.get('url')
    llamada = requests.get(url3)
    url3 = llamada.text
    captura = re.findall(r"(?s)<img class.*?alt='([^']+).*?src='([^']+).*?href='([^']+).*?/b>([^<]+)", url3, re.DOTALL)
    for title, thumb, url, descripcion in captura:
        plugintools.add_item ( action = "elementum" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = "https:" + url , plot = descripcion, thumbnail=thumb, fanart=thumb, folder = False, isPlayable = True )
  
 
################################################################################################        


def sala4_series(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item ( action = "sala4_series_search" , title = "[B][UPPERCASE][COLOR yellow]" + "Buscar..." + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.imgur.com/daHeAJa.jpeg", fanart = "https://i.imgur.com/EYbxMol.jpeg", folder = True , isPlayable = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)


    url = params.get('url')
    llamada = requests.get(url)
    url = llamada.text
    page = params.get('plot')
    pagina = int(page)
    pagina+= 1     
    captura = re.findall(r'(?s)<h3.*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+)', url, re.DOTALL)
    if pagina != 1:
        next = "https://dontorrent.in/series/page/" + str(pagina) 
    else:
        next = "https://dontorrent.in/descargar-series"

    for url, thumb, url2, thumb2, url3, thumb3 in captura:
        text = url.split(sep='/')
        text2 = url2.split(sep='/')
        text3 = url3.split(sep='/')
        title = text[-1].replace("-", " ")
        title2 = text2[-1].replace("-", " ")
        title3 = text3[-1].replace("-", " ")
        plugintools.add_item ( action = "resolve_sala4_series" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" + url , thumbnail=thumb, fanart=thumb, folder = True )
        plugintools.add_item ( action = "resolve_sala4_series" , title = "[B][UPPERCASE][COLOR yellow]" + title2 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url2 , thumbnail=thumb2, fanart=thumb2, folder = True )
        plugintools.add_item ( action = "resolve_sala4_series" , title = "[B][UPPERCASE][COLOR yellow]" + title3 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url3 , thumbnail=thumb3, fanart=thumb3, folder = True )
    plugintools.add_item(action="sala4_series", title="SIGUIENTE", url=next, plot = str(pagina),
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)
    
def resolve_sala4_series(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    url3 = params.get('url')
    llamada = requests.get(url3)
    url3 = llamada.text
    cont = 0
    captura = re.findall(r"(?s).*?p-4.*?alt='([^']+).*?src='([^']+).*?my-3.*?/b>([^<]+)|middle.*?href='([^']+)", url3, re.DOTALL)
    for title, thumb, descripcion, url in captura:
        plugintools.add_item ( action = "elementum" , title = "[B][UPPERCASE][COLOR yellow]" + title + str(cont) + "[/COLOR][/UPPERCASE][/B]" , url = "https:" + url , plot = descripcion, thumbnail=thumb, fanart=thumb, folder = False, isPlayable = True )
        cont+= 1
 
################################################################################################        


def sala4_serieshd(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item ( action = "sala4search_search" , title = "[B][UPPERCASE][COLOR yellow]" + "Buscar..." + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.imgur.com/daHeAJa.jpeg", fanart = "https://i.imgur.com/EYbxMol.jpeg", folder = True , isPlayable = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)


    url = params.get('url')
    llamada = requests.get(url)
    url = llamada.text
    page = params.get('plot')
    pagina = int(page)
    pagina+= 1     
    captura = re.findall(r'(?s)<h3.*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+)', url, re.DOTALL)
    if pagina != 1:
        next = "https://dontorrent.in/series/hd/page/" + str(pagina) 
    else:
        next = "https://dontorrent.in/series/hd"

    for url, thumb, url2, thumb2, url3, thumb3 in captura:
        text = url.split(sep='/')
        text2 = url2.split(sep='/')
        text3 = url3.split(sep='/')
        title = text[-1].replace("-", " ")
        title2 = text2[-1].replace("-", " ")
        title3 = text3[-1].replace("-", " ")
        plugintools.add_item ( action = "resolve_sala4_serieshd" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" + url , thumbnail=thumb, fanart=thumb, folder = True )
        plugintools.add_item ( action = "resolve_sala4_serieshd" , title = "[B][UPPERCASE][COLOR yellow]" + title2 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url2 , thumbnail=thumb2, fanart=thumb2, folder = True )
        plugintools.add_item ( action = "resolve_sala4_serieshd" , title = "[B][UPPERCASE][COLOR yellow]" + title3 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url3 , thumbnail=thumb3, fanart=thumb3, folder = True )
    plugintools.add_item(action="sala4_serieshd", title="SIGUIENTE", url=next, plot = str(pagina),
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)
    
def resolve_sala4_serieshd(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    url3 = params.get('url')
    llamada = requests.get(url3)
    url3 = llamada.text
    cont = 0
    captura = re.findall(r"(?s).*?p-4.*?alt='([^']+).*?src='([^']+).*?my-3.*?/b>([^<]+)|middle.*?href='([^']+)", url3, re.DOTALL)
    for title, thumb, descripcion, url in captura:
        plugintools.add_item ( action = "elementum" , title = "[B][UPPERCASE][COLOR yellow]" + title + str(cont) + "[/COLOR][/UPPERCASE][/B]" , url = "https:" + url , plot = descripcion, thumbnail=thumb, fanart=thumb, folder = False, isPlayable = True )
        cont+= 1
 
################################################################################################        


def sala4_documentales(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item ( action = "sala4search_search" , title = "[B][UPPERCASE][COLOR yellow]" + "Buscar..." + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.imgur.com/daHeAJa.jpeg", fanart = "https://i.imgur.com/EYbxMol.jpeg", folder = True , isPlayable = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)


    url = params.get('url')
    llamada = requests.get(url)
    url = llamada.text
    page = params.get('plot')
    pagina = int(page)
    pagina+= 1     
    captura = re.findall(r'(?s)<h3.*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+).*?a href="([^"]+).*?src="([^"]+)', url, re.DOTALL)
    if pagina != 1:
        next = "https://dontorrent.in/documentales/page/" + str(pagina) 
    else:
        next = "https://dontorrent.in/documentales"

    for url, thumb, url2, thumb2, url3, thumb3 in captura:
        text = url.split(sep='/')
        text2 = url2.split(sep='/')
        text3 = url3.split(sep='/')
        title = text[-1].replace("-", " ")
        title2 = text2[-1].replace("-", " ")
        title3 = text3[-1].replace("-", " ")
        plugintools.add_item ( action = "resolve_sala4_documentales" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" + url , thumbnail=thumb, fanart=thumb, folder = True )
        plugintools.add_item ( action = "resolve_sala4_documentales" , title = "[B][UPPERCASE][COLOR yellow]" + title2 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url2 , thumbnail=thumb2, fanart=thumb2, folder = True )
        plugintools.add_item ( action = "resolve_sala4_documentales" , title = "[B][UPPERCASE][COLOR yellow]" + title3 + "[/COLOR][/UPPERCASE][/B]" , url = "https://dontorrent.in" +url3 , thumbnail=thumb3, fanart=thumb3, folder = True )
    plugintools.add_item(action="sala4_documentales", title="SIGUIENTE", url=next, plot = str(pagina),
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)
    
def resolve_sala4_documentales(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    url3 = params.get('url')
    llamada = requests.get(url3)
    url3 = llamada.text
    cont = 0
    captura = re.findall(r"(?s).*?p-4.*?alt='([^']+).*?src='([^']+).*?my-3.*?/b>([^<]+)|middle.*?href='([^']+)", url3, re.DOTALL)
    for title, thumb, descripcion, url in captura:
        plugintools.add_item ( action = "elementum" , title = "[B][UPPERCASE][COLOR yellow]" + title + str(cont) + "[/COLOR][/UPPERCASE][/B]" , url = "https:" + url , plot = descripcion, thumbnail=thumb, fanart=thumb, folder = False, isPlayable = True )
        cont+= 1

 
################################################################################################ 

def sala5(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item ( action = "sala5search" , title = "[B][UPPERCASE][COLOR yellow]" + "Buscar..." + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.imgur.com/daHeAJa.jpeg", fanart = "https://i.imgur.com/EYbxMol.jpeg", folder = True , isPlayable = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    url3 = params.get('url')
    llamada = requests.get(url3)
    page = params.get('plot')
    pagina = int(page)
    pagina+= 1     
    url3 = llamada.text
    matches = re.findall(r'(?s)<div class="item hitem">.*?a href="([^"]+).*?src="([^"]+).*?titulo.*?<.*?>([^<]+)', url3, re.DOTALL)
    if pagina != 1:
        next = "https://www.moviesdvdr.co/page/" + str(pagina) + "/"
    else:
        next = "https://www.moviesdvdr.co/"
            
    for url, thumb, title in matches:
        plugintools.add_item(action="resolve_sala5", title="[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]", url= url, thumbnail = thumb, fanart = thumb, folder=True)            
    plugintools.add_item(action="sala5", title="SIGUIENTE", url=next, plot = str(pagina),
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)
def resolve_sala5(params):
    
    url3 = params.get('url')
    llamada = requests.get(url3)
    url3 = llamada.text
    captura = re.findall(r'(?s)titulo">Descargar (.*?) Torrent<.*?src="([^"]+).*?p>([^<]+).*?linkastro.*?href="([^"]+)', url3, re.DOTALL)
    for title, thumb, descripcion, url in captura:
        plugintools.add_item ( action = "elementum" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , plot = descripcion, thumbnail=thumb, fanart=thumb, folder = False, isPlayable = True )

def sala5search(params):
    
    url = "https://www.moviesdvdr.co/?s="
    url = url + keyboard_input("", "Buscar:", False).replace(" ", "+")
    url = requests.get(url).text
    matches = re.findall(r'(?s).*?meio.*?h2.*?>([^<]+).*?>([^<]+)|.*?item hitem.*?a href="([^"]+).*?src="([^"]+).*?titulo.*?span>([^<]+)', url, re.DOTALL)
    for title, title2, url, thumb, title3 in matches:
        plugintools.add_item(action="resolve_sala5", title= "[B][UPPERCASE][COLOR yellow]" + title + "[COLOR gold]" + title2 + "[COLOR fuchsia]" + title3 + "[/COLOR][/UPPERCASE][/B]", thumbnail=thumb, url=url, fanart=thumb, folder=True)    



def sala6(params):
    
    
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)



    url = params.get('url')
    llamada = requests.get(url)
    page = params.get('plot')
    pagina = int(page)
    pagina+= 1     
    url3 = llamada.text
    canales =[]
    urls = []
    matches = re.findall(r'(?s)<a href="(\/.*?)".*?>(.*?)<', url3, re.DOTALL)
    for url,title in matches:
        urls.append(url)
        canales.append(title)
    for t in range(6):
        plugintools.add_item(action="resolve_sala6", title= "[B][UPPERCASE][COLOR yellow]" + canales[t] + "[/COLOR][/UPPERCASE][/B]", url= "https://tomadivx.net/" + urls[t], extra = canales[t], plot = "1", fanart="https://i.imgur.com/cE1QfPa.jpg", thumbnail="https://i.imgur.com/dCmmOPO.jpeg",folder=True)


def resolve_sala6(params):
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/iPMtAVo.jpg", fanart = "https://i.imgur.com/wCzvH8R.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item ( action = "sala6search" , title = "[B][UPPERCASE][COLOR yellow]" + "Buscar..." + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.imgur.com/daHeAJa.jpeg", fanart = "https://i.imgur.com/EYbxMol.jpeg", folder = True , isPlayable = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)    
    
    url = params.get('url')
    llamada = requests.get(url)
    page = params.get('plot')
    seccion = params.get('extra')   
    pagina = int(page)
    pagina+= 1     
    url3 = llamada.text 
        
    matches = re.findall(r'(?s)<a href="(\/.*?)".*?>(.*?)<', url3, re.DOTALL)
    
    
    
    
        
def grantorrent_series_search(params):
    
    url = "https://grantorrent.fi/series_p/?query="
    url = url + keyboard_input("", "Buscar:", False).replace(" ", "+")
    url = requests.get(url).text
    matches = re.findall(r'(?s)<p class="text-3xl text-neutral-100">(.*?)<.*?<a href="([^"]+).*?src="([^"]+)', url, re.DOTALL)
    next = plugintools.find_single_match(url, "paginator.*?a href='([^']+)")
    for title, url, thumb in matches:
        plugintools.add_item(action="res3c", title=title, thumbnail=thumb, url=url, fanart=thumb, folder=True)

def sala4search_search(params):
      
    url = "https://dontorrent.in/buscar/"
    url = url + keyboard_input("", "Buscar:", False).replace(" ", "+")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0"])
    header.append(["Referer","https://dontorrent.in/buscar"])
    body, response_headers = plugintools.read_body_and_headers(url, headers=header)
    url = body.strip()    
    matches = re.findall(r"(?s).*?p-4.*?b>(.*?)<|a href='([^']+).*?>([^<]+)", url, re.DOTALL)
    
    for title, url, title2 in matches:
        plugintools.add_item(action="resolve_sala4", title="[B][UPPERCASE][COLOR lime]" + title + "[COLOR yellow]" + title2 + "[/COLOR][/UPPERCASE][/B]", url= "https://dontorrent.in" + url, folder=True)            

def sala4_series_search(params):
       
    url = "https://dontorrent.in/buscar/"
    url = url + keyboard_input("", "Buscar:", False).replace(" ", "+")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0"])
    header.append(["Referer","https://dontorrent.in/descargar-series"])
    body, response_headers = plugintools.read_body_and_headers(url, headers=header)
    url = body.strip()    
    matches = re.findall(r"(?s).*?p-4.*?b>(.*?)<|a href='([^']+).*?>([^<]+)", url, re.DOTALL)
    
    for title, url, title2 in matches:
        plugintools.add_item(action="resolve_sala4_series", title="[B][UPPERCASE][COLOR lime]" + title + "[COLOR yellow]" + title2 + "[/COLOR][/UPPERCASE][/B]", url= "https://dontorrent.in" + url, folder=True)            


def busqueda_ensala(params):

    import requests
    import re

    searc = keyboard_input(default_text="" , title="Introduce texto para la busqueda..." , hidden=False)
    elec = searc.strip()
    url = 'http://perillas.mendelux.es/pel_ele_ace.txt'

    page = requests.get(url)
    match = page.text
    look = re.findall(r'(?s)\n(.*?)\n.*?Ace.*?:(.*?)\n.*?Mag.*?:.*?(magnet.*?)\n.*?(http.*?)\n', match, re.DOTALL)
 
    for title,ace,elemen,thumb in look:
        if elec in title:
            plugintools . add_item ( action = "busqueda_res" , title =  '[COLOR lime][B]' + title + '[/B][/COLOR]', url = elemen,extra = ace, fanart = thumb ,thumbnail = thumb,folder = False, isPlayable = True)

def busqueda_res(params):
    
         
    ace_url = (params.get("extra")).strip()
    elem_url = (params.get("url")).strip()
    title = params.get("title").strip()
    thumb = params.get("thumbnail").strip()
    dialog = xbmcgui.Dialog()
    if '.jpg' not in thumb:thumb = thumb + '.jpg'
    ret = dialog.select('[B][LOWERCASE][CAPITALIZE][COLOR yellow]elige, Ver con:[/B][/COLOR][/CAPITALIZE][/LOWERCASE]', ['[B][LOWERCASE][CAPITALIZE][COLOR lime]Acestream[/B][/COLOR][/CAPITALIZE][/LOWERCASE]','[B][LOWERCASE][CAPITALIZE][COLOR pink]Torrenter[/B][/COLOR][/CAPITALIZE][/LOWERCASE]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]Elementum[/B][/COLOR][/CAPITALIZE][/LOWERCASE]', '[B][LOWERCASE][CAPITALIZE][COLOR white]Torrentin[/B][/COLOR][/CAPITALIZE][/LOWERCASE]'])
    channels = ['plugin://script.module.horus?action=play&id=' + ace_url + '&title=' + title + '&iconimage=' + thumb,'plugin://plugin.video.torrenter/?action=playSTRM&url='+elem_url,'plugin://plugin.video.elementum/play?uri='+elem_url,'plugin://plugin.video.torrentin/?uri='+elem_url]  
    final_url = channels[ret]
       
    plugintools.play_resolved_url ( final_url )

def canalesacestream(params):
       
   
    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                       [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR blue]Ace[COLOR yellow]stream       [COLOR lime]##[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
     
    plugintools.add_item(action = "ace1" , title = "[COLOR lime][B]>[COLOR magenta]LISTA ACESTREAM 1[COLOR lime]<[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )
    
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item(action = "ace2" , title = "[COLOR lime][B]>[COLOR magenta]LISTA ACESTREAM 2[COLOR lime]<[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )
    
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False) 
  
    plugintools.add_item(action = "ace3" , title = "[COLOR lime][B]>[COLOR magenta]LISTA ACESTREAM 3[COLOR lime]<[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )
    
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
     
    plugintools.add_item(action = "ace4" , title = "[COLOR lime][B]>[COLOR magenta]LISTA ACESTREAM 4 [COLOR lightpink] el Barco[COLOR lime]<[/B][/COLOR]" , thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png"  , url = "", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg" , plot = "",  folder = True,isPlayable = False  )
   
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item(action = "ace5" , title = "[COLOR lime][B]>[COLOR magenta]LISTA ACESTREAM 5 [COLOR lightpink] Mcfly [COLOR aqua]TV & DEPORTES[COLOR lime]<[/B][/COLOR]" , thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png"  , url = "", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg" , plot = "",  folder = True,isPlayable = False  )
   
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item(action = "ace6" , title = "[COLOR lime][B]>[COLOR magenta]LISTA ACESTREAM 6 [COLOR lightpink] SirRandomss [COLOR aqua]TV & DEPORTES[COLOR lime]<[/B][/COLOR]" , thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png"  , url = "", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg" , plot = "",  folder = True,isPlayable = False  )
   
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    plugintools.add_item(action = "ace7" , title = "[COLOR lime][B]>[COLOR magenta]LISTA ACESTREAM 7 [COLOR lightpink] Ramses [COLOR yellow]por Lucas_m_o_o_m [COLOR aqua]TV & DEPORTES[COLOR lime]<[/B][/COLOR]" , thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png"  , url = "", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg" , plot = "",  folder = True,isPlayable = False  )
   
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
            
    plugintools.add_item(action = "main_list" , title = "[COLOR cyan][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False) 


def ace1(params):
    
    
   
    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                       [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR blue]Ace[COLOR yellow]stream       [COLOR lime]##[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
            
    plugintools.add_item(action = "canalesacestream" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)    
        
    url = 'http://perillas.mendelux.es/url_ace.txt'
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    matches = re.findall(r'(?s)<([^>]+)', url, re.DOTALL )
    
        
    #url3 = "https://gratisfutbol3.pages.dev/"
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    matches = re.findall(r'(?s).*?<a href="acestream://(.*?)".*?>([^<]+)', url, re.DOTALL )   
    for url, title in matches:
        title.strip()
        plugintools.add_item(action = "resolve_acestream",title="[COLOR yellow][B]" + title + "[/COLOR][/B]",  url = url, thumbnail = "https://i.postimg.cc/W1gSD5Sy/Photo-1667495860094.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = False, isPlayable = True)

def ace2(params):
    
    
   
    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                       [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR blue]Ace[COLOR yellow]stream       [COLOR lime]##[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)    

    plugintools.add_item(action = "canalesacestream" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
        
    url = "https://raw.githubusercontent.com/davidmuma/log_dobleM/master/ace_6878.m3u"
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    fecha = plugintools.find_single_match(url,r'(?s)#EXTM3U.([a-zA-Z0-9/: ]{0,})')
    matches = re.findall(r'(?s)id.*?"([^"]+).*?logo="([^"]+).*?group.*?="([^"]+).*?id=(\S{,40})', url, re.DOTALL)
    
    plugintools.add_item ( action = "" , title = "[B][UPPERCASE][COLOR greenyellow]" + "--> " + "[COLOR cyan]" + fecha.strip() + "[COLOR greenyellow]" + " <--" + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.postimg.cc/W1gSD5Sy/Photo-1667495860094.png"  , fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg" , folder = False , isPlayable = True )
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    for title, thumb, grup, url in matches:
        if thumb == "":thumb="https://i.postimg.cc/W1gSD5Sy/Photo-1667495860094.png"
        plugintools.add_item ( action = "resolve_acestream" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url, thumbnail = thumb  , fanart = thumb , folder = False , isPlayable = True )

def ace3(params):
    
    
   
    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                       [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR blue]Ace[COLOR yellow]stream       [COLOR lime]##[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)    

    plugintools.add_item(action = "canalesacestream" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)    

    url = 'http://perillas.mendelux.es/ace_spanish.txt'
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()  
        
    grupos = re.findall(r'(?s).*?([a-zA-Z0-9:._ ]+)\s.*?ace.*?:\/\/(\S{,40})', url, re.DOTALL)
          
    for title,url in grupos:
        plugintools.add_item(action="resolve_acestream", title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]", url=url,
                             thumbnail ="https://i.postimg.cc/W1gSD5Sy/Photo-1667495860094.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder=False, isPlayable=True) 

def ace4(params):
    
    
   
    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                       [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR blue]Ace[COLOR yellow]stream       [COLOR lime]##[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)    

    plugintools.add_item(action = "canalesacestream" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
        
    url = 'http://perillas.mendelux.es/elbarco.txt'
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()  
        
    grupos = re.findall(r'(?s)href="acestream://([^"]+).*?>([^<]+)', url, re.DOTALL)
          
    for url,title in grupos:
        plugintools.add_item(action="resolve_acestream", title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]", url=url,
                             thumbnail ="https://i.postimg.cc/W1gSD5Sy/Photo-1667495860094.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder=False, isPlayable=True) 

def ace5(params):
    
    
   
    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                       [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR blue]Ace[COLOR yellow]stream       [COLOR lime]##[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)    

    plugintools.add_item(action = "canalesacestream" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
        
    url = 'https://raw.githubusercontent.com/KevinMcfly/AC-iptv/main/IPTV%20Acestream%20actu.m3u'
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url3 = read_url.strip ()  
        
    grupos = re.findall(r'(?s)#EXTINF.+?logo="(.*?)".+?group-title="(.*?)"', url3, re.DOTALL)
    del_grups = ["Adultos","Peliculas"]      
    almacen_grupos = []
    almacen_thumb = []
    #cont = 0
    for thumb,grupo in grupos:
        gr = grupo.strip()
        if gr not in almacen_grupos and gr not in del_grups:
            almacen_grupos.append(gr)
            almacen_thumb.append(thumb)
                      
    for t in range(len(almacen_grupos)):
        plugintools.add_item(action="resolve_ace5", title = "[B][UPPERCASE][COLOR yellow]" + almacen_grupos[t] + "[/COLOR][/UPPERCASE][/B]", url=url, extra = almacen_grupos[t],
                             fanart = 'https://i.postimg.cc/85Wvw3m4/acestream.jpg' , thumbnail = almacen_thumb[t], folder=True, isPlayable=False) 

def resolve_ace5(params):
    
    url3 = params.get("url")
    seleccion = (params.get("extra")).strip()
    cap = requests.get(url3)
    captur = cap.text    
    lista_cine = [] 
    matches = re.findall(r'(?s)EXTINF.+?logo="(.*?)".+?group.+?="(.*?)".*?,(.*?)\n([\S]+)', captur, re.DOTALL)
    #(?s).*?name="(.*?)".*?logo="(.*?)".*?group-title="(.*?)".*?(http.*?://[a-z\.:0-9\/]*.*?/.*?/[0-9\.a-z]{0,})
    
   
 
               
    for thumb, grup, title, url in matches:
        if grup.strip() == seleccion:
            if thumb =='':thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png"
            url2= url.split('acestream://')
            url_final = url2[-1].strip()
            if "http" in url or "https" in url:
                lista_cine.append(url.strip()) 
                plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url.strip() , extra = title.strip(),thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )
            else:
                plugintools.add_item ( action = "resolve_acestream" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url_final , thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )
        else:
            pass
   
                

def resolve_ace3(params):
    
    url = "https://raw.githubusercontent.com/SirRandoms/lista/main/ids"
    seleccion = (params.get("extra")).strip()
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()  
    matches = re.findall(r'(?s).*?logo="(.*?)".*?group.*?="(.*?)".*?,(.*?)\n([a-zA-Z0-9:/\._]+)', url, re.DOTALL)                    

    for thumb, grup, title, id in matches:
        if thumb == "":thumb = "https://i.postimg.cc/W1gSD5Sy/Photo-1667495860094.png"
        if grup.strip() == seleccion:
            title = title.strip()
            if id.startswith('acestream') is True:
                url_s = id.split('/')
                url = url_s[-1]
                if url == "":title= "[COLOR red]" + "Off" + "[/COLOR]" 
                plugintools.add_item ( action = "resolve_acestream" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url, thumbnail = thumb  , fanart = thumb , folder = False , isPlayable = True )
            else:
                plugintools.add_item ( action = "resolve_without_resolveurl" , title =  '[COLOR yellow][B]' + title + '[/B][/COLOR]', url = id,fanart = thumb ,thumbnail = thumb,folder = False, isPlayable = True)

def ace6(params):
    
    
   
    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                       [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR blue]Ace[COLOR yellow]stream       [COLOR lime]##[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)    

    plugintools.add_item(action = "canalesacestream" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
        
    url = 'https://raw.githubusercontent.com/SirRandomss/kebabs/main/mixto'
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url3 = read_url.strip ()  
        
    grupos = re.findall(r'(?s)EXTINF.*?logo="(.*?)".*?gr.*?=.*?"(.*?)"', url3, re.DOTALL)  
    almacen_grupos = []
    almacen_thumb = []
    #cont = 0
    for thumb,grupo in grupos:
        gr = grupo.strip()
        if thumb =="":thumb ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png"
        if gr not in almacen_grupos:
            almacen_grupos.append(gr)
            almacen_thumb.append(thumb)
    for t in range(len(almacen_grupos)):
        if almacen_thumb[t] =="":almacen_thumb[t] ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png"
        plugintools.add_item(action="resolve_ace6", title = "[B][UPPERCASE][COLOR yellow]" + almacen_grupos[t] + "[/COLOR][/UPPERCASE][/B]", url=url, extra = almacen_grupos[t],
                             fanart = 'https://i.postimg.cc/85Wvw3m4/acestream.jpg' , thumbnail = almacen_thumb[t], folder=True, isPlayable=False) 

def resolve_ace6(params):
    
    url3 = params.get("url")
    seleccion = (params.get("extra")).strip()
    cap = requests.get(url3)
    captur = cap.text    
     
    matches = re.findall(r'(?s)EXTINF.*?lo.*?=.*?"(.*?)".*?gr.*?=.*?"(.*?)".*?,.*? ([\S \+]+)\n(\S{,70})', captur, re.DOTALL)
        
    for thumb, grup, title, url in matches:
        url = url.strip()
        
        if thumb =="":thumb ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png"
        if grup.strip() in seleccion:
            if url == "":title = "OFF"           
            if "http" in url or "https" in url:
                plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url ,thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )
            else:
                url2= url.split('acestream://')
                url_final = url2[-1].strip()
                if url_final == "":title = "OFF"
                plugintools.add_item ( action = "resolve_acestream" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url_final , thumbnail = thumb , fanart = "https://i.imgur.com/r3lavFX.jpg" , folder = False , isPlayable = True )
        else:
            pass
  
def ace7(params):
    
    
   
    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                       [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR blue]Ace[COLOR yellow]stream       [COLOR lime]##[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://www.dl.dropboxusercontent.com/s/pj9u99894pmfwag/logo-acestream.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)    

    plugintools.add_item(action = "canalesacestream" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.postimg.cc/85Wvw3m4/acestream.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
        
    url = 'https://hackmd.io/@cicvNR77Qoem0wkzPOdC8w/SJVN6Yajo'
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url3 = read_url.strip ()  
        
    matches = re.findall(r'(?s)\ !.*?\].*?\((htt.*?)\).*?\|(.*?)\|.*?\(ac.*?\/\/(\S{,40})', url3, re.DOTALL)  

    for thumb,title, url in matches:
        plugintools.add_item(action="resolve_acestream", title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]", url=url,
                             fanart = 'https://i.postimg.cc/85Wvw3m4/acestream.jpg' , thumbnail = thumb, folder=False, isPlayable=True) 


        
def moviola(params):
    
    
    thumb = "http://perillas.mendelux.es/thumb.png"
    fanart = "http://perillas.mendelux.es/moviola.jpg"
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail = "https://i.imgur.com/jtD69rR.jpeg", fanart = "https://i.imgur.com/kNEQ8MR.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR white]LA [COLOR gold]MOVI[COLOR orange]OLA                   [COLOR lime]##[/B][/COLOR]", thumbnail = "https://i.imgur.com/jtD69rR.jpeg", fanart = "https://i.imgur.com/kNEQ8MR.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail = "https://i.imgur.com/jtD69rR.jpeg", fanart = "https://i.imgur.com/kNEQ8MR.jpeg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
          
    plugintools.add_item(action = "main_list" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.imgur.com/kNEQ8MR.jpeg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)    
    

    url = "https://pastebin.com/raw/mbxG3357"
    llamada = requests.get(url)
    datos = llamada.text
    
    matches = re.findall(r'(?s).*?eve.*?<([^>]+).*?url<([^>]+)', datos, re.DOTALL )
    for title, url in matches:
        final_url = 'plugin://plugin.video.elementum/play?uri='+url
        plugintools . add_item ( action = "resolve_without_resolveurl" , title =  '[COLOR lime][B]' + title + '[/B][/COLOR]', url = final_url,fanart = "https://i.imgur.com/kNEQ8MR.jpeg" ,thumbnail = "https://i.imgur.com/jtD69rR.jpeg",folder = False, isPlayable = True)


def agendas_deportivas(params):
    

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##            [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR white]AGE[COLOR gold]NDA[COLOR orange] DEPORTIVA           [COLOR lime]##[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
          
    plugintools.add_item(action = "main_list" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    
    plugintools.add_item ( action = "agenda" , title = "[B][UPPERCASE][COLOR yellow]" + "AGENDA GRUPO" + "[COLOR gold]" + " KODIverti" + "[COLOR yellow]" + "DO" + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png" , fanart = "https://i.imgur.com/DVTt1Fv.jpg" , folder = True , isPlayable = False )

    plugintools.add_item ( action = "agenda2" , title = "[B][UPPERCASE][COLOR yellow]" + "AGE" + "[COLOR gold]" + "NDA" + "[COLOR golg]" + " platin" + "[COLOR white]" + "Sport" + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://www.platinsport.com/wp-content/themes/sahifa/images/logo.png"  , url = "", fanart = "https://i.imgur.com/DVTt1Fv.jpg" , plot = "",  folder = True,isPlayable = False  )
   
    plugintools.add_item ( action = "agenda3" , title = "[B][UPPERCASE][COLOR yellow]" + "EVEN" + "[COLOR gold]" +"TOS" + "[COLOR springgreen]"+" DEL DIA " + "[COLOR golg]"+"TOTAL"+"[COLOR white]"+"Sports"+"[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1C7YMCKbB-UQmkzZpyNyb7rc8T5nlC5AUXYFHl9xLjpxM7UMgRFh_T0zb70m3ZkPhVmyfZK9LwbB5nm6oCdi7jiN9SWXZ_q5k7DaYNiAPkIPJF8xZz9SKR65Cyjge4gLjl8bPSjrgMuSpFJJVxRnUU8nhWrwD8biSEnCuorMY6jZaU4Xibo3r3eC-/s300/download.png"  , url = "https://www.sport7.co.in/", fanart = "https://i.imgur.com/DVTt1Fv.jpg" , plot = "",  folder = True,isPlayable = False  )

      

def agenda(params):
    
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##            [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR white]AGE[COLOR gold]NDA[COLOR orange] DEPORTIVA           [COLOR lime]##[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
          
    plugintools.add_item(action = "agendas_deportivas" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)


    import requests,re
    url = 'http://perillas.mendelux.es/agenda_deportiva.txt'
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()     
    #cap = requests.get(url)
    #captur = cap.text
    matches = re.findall(r'(?s)<P>(.*?)</P>|<([^>]+).*?<([^>]+)', url, re.DOTALL)
    
    for seccion, partido, enlace in matches:
        plugintools.add_item ( action = "resolve_acestream" , title = "[B][UPPERCASE][COLOR yellow]" + seccion + "[COLOR lime]" + partido + "[/COLOR][/UPPERCASE][/B]" , url = enlace, thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png"  , fanart = "https://i.imgur.com/DVTt1Fv.jpg" , folder = False , isPlayable = True )

def agenda2(params):


    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##            [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR white]AGE[COLOR gold]NDA[COLOR orange] DEPORTIVA           [COLOR lime]##[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
          
    plugintools.add_item(action = "agendas_deportivas" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)


    #import requests,re
    url = "https://www.platinsport.com/"
    #cap = requests.get(url)
    #captur = cap.text    
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip () 
    
    fecha =  re.findall(r'(?s)<tr>\n.+?<span style.*?>(.*?)<', url, re.DOTALL)
    fecha_agenda = fecha[0]
    matches = re.findall(r'(?s).*?<td>.*?src="([^"]+).*?<td>([^<]+).*?(https.*?)"', url, re.DOTALL)    
    
    plugintools.add_item ( action = "" , title = "[B][UPPERCASE][COLOR lime]" + fecha_agenda + "[/COLOR][/UPPERCASE][/B]",thumbnail="", fanart="", folder=False)
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    for thumb, title, url in matches:
        evento = title.strip()
        plugintools.add_item ( action = "resolve_agenda2" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url, extra = evento, thumbnail = thumb , fanart = "https://i.imgur.com/DVTt1Fv.jpg" , folder = True , isPlayable = False )

def resolve_agenda2(params):
    
    url = params.get("url")
    thumb = params.get("thumbnail")
    title = params.get("extra")
    cap = requests.get(url)
    captur = cap.text     
    partido = plugintools.find_single_match(captur, "(?s)<h3><strong>.*?([a-zA-Z0-9 İ:]+)")
    cont = int(len(partido))
    tabs = "  "
    for t in range(cont):
        tabs = tabs + " "
    plugintools.add_item ( action = "" , title = "[B][UPPERCASE][COLOR aqua]" + tabs + "Evento\n" + "[COLOR whitesmoke]" + partido + "[/COLOR][/UPPERCASE][/B]",thumbnail=thumb, fanart="", folder=False)
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    
    matches = re.findall(r'(?s).*?(\[.*?)\nace.*?\/\/(\w{,40})', captur, re.DOTALL)
    for title,url in matches:
        plugintools.add_item ( action = "resolve_acestream" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url, thumbnail = thumb  , fanart = "https://i.imgur.com/DVTt1Fv.jpg" , folder = False , isPlayable = True )


def agenda3(params):
    

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##            [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR white]AGE[COLOR gold]NDA[COLOR orange] DEPORTIVA           [COLOR lime]##[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail = "https://i.postimg.cc/W1LjykC6/Picsart-22-10-30-16-51-56-087-removebg-preview.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
          
    plugintools.add_item(action = "agendas_deportivas" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.postimg.cc/wB8ch8c6/volver.png", fanart = "https://i.imgur.com/DVTt1Fv.jpg", folder = True )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)


    #import requests,re
    url = params.get("url")
    #cap = requests.get(url)
    #captur = cap.text  (?s)<h3 class=.*?post-title.*?>.*?>(.*?)<.*?b>(.*?)<.*?\/>.*?\/>|<b>([a-zA-Z0-9\.\[\] ]+)<|<a href="ac.*?\/\/([\S]+)"  
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip () 

    titulos = re.findall(r'(?s)<h3 class=.*?post-title.*?>.*?>(.*?)<', url, re.DOTALL)
    matches = re.findall(r'(?s)<b>([a-zA-Z0-9\.\[\] ]+)<|<a href="(ac.*?):\/\/([\S]+)"', url, re.DOTALL)
 
    canales = []
    urls = []
    cont = 0
        
    for title1 in titulos:
        plugintools.add_item ( action = "" , title = "[B][UPPERCASE][COLOR yellow]" + title1 + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1C7YMCKbB-UQmkzZpyNyb7rc8T5nlC5AUXYFHl9xLjpxM7UMgRFh_T0zb70m3ZkPhVmyfZK9LwbB5nm6oCdi7jiN9SWXZ_q5k7DaYNiAPkIPJF8xZz9SKR65Cyjge4gLjl8bPSjrgMuSpFJJVxRnUU8nhWrwD8biSEnCuorMY6jZaU4Xibo3r3eC-/s300/download.png" , fanart = "https://i.imgur.com/DVTt1Fv.jpg" )
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)    
    for name, title, url in matches: 
        title =  "[COLOR springgreen]" + title 
        plugintools.add_item ( action = "resolve_acestream" , title = "[B][UPPERCASE][COLOR yellow]" + name + title + "[/COLOR][/UPPERCASE][/B]" , thumbnail = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1C7YMCKbB-UQmkzZpyNyb7rc8T5nlC5AUXYFHl9xLjpxM7UMgRFh_T0zb70m3ZkPhVmyfZK9LwbB5nm6oCdi7jiN9SWXZ_q5k7DaYNiAPkIPJF8xZz9SKR65Cyjge4gLjl8bPSjrgMuSpFJJVxRnUU8nhWrwD8biSEnCuorMY6jZaU4Xibo3r3eC-/s300/download.png" , fanart = "https://i.imgur.com/DVTt1Fv.jpg",url = url, folder = False, isPlayable=True)
    
           
                     
  
def extrenosRober(params):
	
   #directory = os.path.abspath('.')
   #myaddon =xbmcaddon .Addon ()
   import pickle
   from io import open
   fichero = open(xbmc.translatePath('special://home/addons/plugin.video.KovertidoTeamTvCine/Extrenos'),'rb')
   mensaje = pickle.load(fichero)
   '''
   #aqui guardamos la lista en un archivo binario
   with open(xbmc.translatePath('special://home/addons/plugin.video.KovertidoTeamTvCine/Extrenos.txt'),mode='r') as f:
      mensaje = f.read()
      archivo = open(xbmc.translatePath('special://home/addons/plugin.video.KovertidoTeamTvCine/Extrenos'),'wb')
      #archivo.write(mensaje)
      pickle.dump(mensaje,archivo)
      archivo.close()
   '''
   matches = re.findall(r'(?s).*?logo.*?"([^"]+).*?group.*?"([^"]+).*?,(.*?)\n.*?ace.*?//(.*?)\.', mensaje, re.DOTALL )
   plugintools.add_item ( action = "elementum" , title = "[B][UPPERCASE][COLOR yellow]" + "torrent" + "[/COLOR][/UPPERCASE][/B]" , url = "magnet:?xt=urn:btih:664EBF593F151228CE5213256130625A196602CF&dn=lightyear&tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2940%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2770%2Fannounce&tr=udp%3A%2F%2Ftracker.tallpenguin.org%3A15710%2Fannounce&tr=udp%3A%2F%2Ftracker.thinelephant.org%3A12710%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce" , folder = False , isPlayable = True )
   for thumb,grup,title, url in matches:
      plugintools.add_item ( action = "resolve_acestream" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = thumb , folder = False , isPlayable = True )
   	    
def openUrl(params):
   url = params.get("url")
   respuesta = xbmcgui.Dialog().yesno("[COLOR blue]"+"KODIvertiDO TEAM"+"[/COLOR]", " Quieres visitar "+url, "No","Si")
   
   if respuesta:
      osWin = xbmc.getCondVisibility('system.platform.windows')
      osOsx = xbmc.getCondVisibility('system.platform.osx')
      osLinux = xbmc.getCondVisibility('system.platform.linux')
      osAndroid = xbmc.getCondVisibility('System.Platform.Android') 
    
      if osOsx:    
           # ___ Open the url with the default web browser
          xbmc.executebuiltin("System.Exec(open "+url+")")
      elif osWin:
           # ___ Open the url with the default web browser
          xbmc.executebuiltin("System.Exec(cmd.exe /c start "+url+")")
      elif osLinux and not osAndroid:
           # ___ Need the xdk-utils package
          xbmc.executebuiltin("System.Exec(xdg-open "+url+")") 
      elif osAndroid:
          # ___ Open media with standard android web browser
          xbmc.executebuiltin("StartAndroidActivity(com.android.browser,android.intent.action.VIEW,,"+url+")")
        
          # ___ Open media with Mozilla Firefox
          xbmc.executebuiltin("StartAndroidActivity(org.mozilla.firefox,android.intent.action.VIEW,,"+url+")")                    
        
          # ___ Open media with Chrome
          xbmc.executebuiltin("StartAndroidActivity(com.android.chrome,,,"+url+")") 
   else:
      xbmcgui.Dialog().notification('Info', 'Cancelando...', xbmcgui.NOTIFICATION_ERROR, 4000) 
      exit(0)

def direct_play(params):
    
    import sys
    import xbmc
    import xbmcgui
    import xbmcplugin
    
    name = params.get('extra')
    url = params.get('url')
    icon = params.get('thumbnail')
       
    li = xbmcgui.ListItem(name, icon)
    li.setInfo(type='Video', infoLabels = {'Title': name,'icon': icon})   
    xbmc.Player().play(url, li, windowed = False)
    

    #addon_handle = int(sys.argv[1])

    #xbmcplugin.setContent(addon_handle, 'movies')
    #listitem = xbmcgui.ListItem('Ironman')
    #listitem.setInfo('video', {'Title': title, 'icon': thumb})
    #xbmc.Player().stop()
    #xbmc.Player().play(url, listitem, windowed = False)
    
    #li = xbmcgui.ListItem('KODIvertiDO Team Video!')
    #xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    #xbmc.player().play(str(url))
    #xbmcplugin.endOfDirectory(addon_handle)

def web(params):
    import webbrowser

    url = params.get("url")
    respuesta = xbmcgui.Dialog().yesno("[COLOR blue]"+"KODIvertiDO TEAM"+"[/COLOR]", " Quieres visitar "+url, "No","Si")
    if respuesta:  
        xbmcgui.Dialog().notification('[COLOR blue]'+'KODIvertiDO TEAM'+'[/COLOR]', '[COLOR lightgreen]'+'Abriendo web browser..'+'[/COLOR]', xbmcgui.NOTIFICATION_INFO, 5000)     
        openUrl(url)            
    else:
        xbmcgui.Dialog().notification('Info', 'Cancelando...', xbmcgui.NOTIFICATION_ERROR, 4000) 
        exit(0)
 
def keyboard_input(default_text="" , title="" , hidden=False):
   keyboard = xbmc.Keyboard ( default_text , title , hidden )
   keyboard.doModal ()

   if (keyboard.isConfirmed ()):
       tecleado = keyboard.getText ()
   else:
       tecleado = ""

   return tecleado

def resolve_resolveurl(params):
   import resolveurl
   finalurl = resolveurl.resolve ( params.get ( "url" ) )
   plugintools.play_resolved_url ( finalurl )

def resolve_without_resolveurl(params):
   import resolveurl
   finalurl = (params.get ( "url" ))
   plugintools.play_resolved_url ( finalurl )

def play(params):
   import resolveurl
   url = (params.get ( "url" ))
   finalurl = url.encode("utf-8", "strict")
   plugintools.play_resolved_url ( finalurl )  
 # Aqui se reproduce el enlace Acestream que le hemos pasado utilizando el parametro id(params.get("plot") es quien recoge la id de cada canal)
def resolve_acestream ( params ) :
   import resolveurl
  # utilizamos el addon horus para teproducir el acestream &iconimage={} ,params.get("thumbnail")
   finalurl = "plugin://script.module.horus?action=play&id={}&title={}".format(params.get("url"),params.get("title"))
   plugintools.log("###############"+finalurl)
   plugintools . play_resolved_url ( finalurl )     

def elementum(params):
    import resolveurl
    finalurl = "plugin://plugin.video.elementum/play?uri=" + params.get ( "url" )
    plugintools.play_resolved_url ( finalurl )

    
class Password:
    def __init__(self):
        self.password = plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]
        self.profile = translatePath(xbmcaddon.Addon().getAddonInfo('profile')) if six.PY3 else translatePath(
            xbmcaddon.Addon().getAddonInfo('profile'))
        self.passfile = self.profile + 'clave.txt'

    def check(self):
        global password_file
        if not os.path.isfile(self.passfile):
            password = xbmcgui.Dialog().input('Introduzca la contraseña para entrar:')
            if password == plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]:
                if not os.path.exists(self.profile): os.makedirs(self.profile)
                password_file = self.passfile
                f = open(password_file, 'w+')
                f.write(password)
                return True
            else:
                return False
        else:
            password_file = self.passfile
            with open(self.passfile, 'r') as f:
                password = f.read()
            if password == plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]:
                return True
            else:
                return False

'''
if Password().check() == True:
        
    plugintools.add_item ( action = "lista_alegres" , title = "[B][UPPERCASE][COLOR yellow]" + "<Lista 1>" + "[/COLOR][/UPPERCASE][/B]" , url = "http://perillas.mendelux.es/alegres.txt" , thumbnail ="https://i.imgur.com/HCiV6ND.jpg", fanart = "https://i.imgur.com/vbd5QBG.jpg" , folder = True , isPlayable = False )
    plugintools.add_item ( action = "lista_alegres_ace" , title = "[B][UPPERCASE][COLOR yellow]" + "<Lista 2>" + "[COLOR lime]" + "  -> NECESITAS ACESTREAM <-" + "[/COLOR][/UPPERCASE][/B]" , url = "http://perillas.mendelux.es/alegres_ace.txt" , thumbnail ="https://i.imgur.com/HCiV6ND.jpg", fanart = "https://i.imgur.com/vbd5QBG.jpg" , folder = True , isPlayable = False )
         
         
else:
    xbmcgui.Dialog().notification('Info', 'Contraseña Incorrecta', xbmcgui.NOTIFICATION_ERROR, 4000)
    #os.remove(password_file)
    iptv(params)
'''
run()

'''
url = "https://justpaste.it/5lk79"
data = plugintools.read(url)
data = plugintools.find_single_match( data , 'Content">.*?<p(.*?)</div>') 
pattern = '(?s).*?\{.*?"name":.*?"([^"]+).*?"image".*?"([^"]+).*?\[.*?"name".*?"([^"]+)'
   
busqueda = plugintools.find_multiple_matches(data,pattern)
'''
