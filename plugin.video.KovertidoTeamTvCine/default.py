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
myaddon =xbmcaddon .Addon ()

if six.PY2:
   translatePath = xbmc.translatePath
   LOG = xbmc.LOGNOTICE
elif six.PY3:
   translatePath = xbmcvfs.translatePath
   LOG = xbmc.LOGINFO

def run():                                                              
   plugintools.log("---> KodivertidoTeamTvCine.run <---")  
   plugintools.set_view(plugintools.LIST)    
                                                                         
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
       
   plugintools.set_view(plugintools.LIST) 

   plugintools.add_item(action = "" , title = "[COLOR lime][B]#######[COLOR aqua]##################[COLOR lime]####[/B][/COLOR]", thumbnail ="https://i.imgur.com/yMUqrM3.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

   plugintools.add_item(action = "" , title = "[COLOR lime][B]##         [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]Tv[COLOR blue]C[COLOR yellow]i[COLOR aqua]n[COLOR yellow]e         [COLOR lime]##[/B][/COLOR]",  thumbnail ="https://i.imgur.com/yMUqrM3.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg", folder = False )

   plugintools.add_item(action = "" , title = "[COLOR lime][B]#######[COLOR aqua]##################[COLOR lime]####[/B][/COLOR]", thumbnail ="https://i.imgur.com/yMUqrM3.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

   plugintools.add_item(action = "" , title = "", thumbnail ="https://i.imgur.com/yMUqrM3.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg", folder = False )

   plugintools.add_item(action = "openUrl" , title = "[COLOR white][B] Únete a Telegram [COLOR lime]<https://t.me/kodivertidoteam>[/B][/COLOR]" , thumbnail = "https://i.imgur.com/yMUqrM3.jpg" , url = "https://t.me/kodivertidoteam" , fanart = "https://i.imgur.com/cE1QfPa.jpg" , folder = True,isPlayable=False )

   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
   
   plugintools.add_item(action = "iptv" , title = "[COLOR lime][B]>[COLOR yellow]IP[COLOR gold]TV[COLOR lime]<[/B][/COLOR]" , thumbnail = "https://i.imgur.com/GgGFDmd.jpg"  , url = "", fanart = "https://i.imgur.com/xdn0NDc.jpg" , plot = "",  folder = True,isPlayable = False  )
   
   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
   
   plugintools.add_item(action = "cine" , title = "[COLOR lime][B]>[COLOR gold]CINE [COLOR yellow]ESTRENOS[COLOR lime]<[/B][/COLOR]" , thumbnail = "https://i.imgur.com/iPMtAVo.jpg"  , fanart = "https://i.imgur.com/cE1QfPa.jpg" , plot = "",  folder = True,isPlayable = False  )
   

#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################       
#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################
#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################


def iptv(params):

   plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/GgGFDmd.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg",  folder = False )

   plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]I[COLOR blue]P[COLOR yellow]T[COLOR aqua]V                                                    [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/GgGFDmd.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg",  folder = False )

   plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/GgGFDmd.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg",  folder = False )

   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

   plugintools.add_item(action = "main_list" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/GgGFDmd.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg", folder = True )

   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
   
   plugintools.add_item(action = "iptv1" , title = "[COLOR lime][B]->LISTA 1<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/kVXxRxi.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg", folder = True )

   plugintools.add_item(action = "iptv2" , title = "[COLOR lime][B]->LISTA 2<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/MYxB48N.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg", folder = True )

   plugintools.add_item(action = "iptv3" , title = "[COLOR lime][B]->LISTA 3<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/OqADwwu.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg", folder = True )

   plugintools.add_item(action = "iptv4" , title = "[COLOR lime][B]->LISTA 4<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/niIFp0G.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg", folder = True )

   plugintools.add_item(action = "canalesacestream" , title = "[COLOR yellow][B]->LISTA ACESTREAM<- [COLOR lime]*<[COLOR red]Necesario Acestream[COLOR lime]>*[/B][/COLOR]", thumbnail ="https://i.imgur.com/OqADwwu.jpg", fanart = "https://i.imgur.com/xdn0NDc.jpg", folder = True )
  
    

def iptv1(params):
	
    import requests,re
    url = 'http://perillas.mendelux.es/tesla.txt'
    llamada = requests.get(url)
    #status = str(llamada.status_code)
    #plugintools.log("El codigo de la llamada es " + status)
    datos = llamada.text
    grupos = re.findall(r'(?s).*?group-title="([^"]+)',datos)
    
    almacen_grupos = []
    
    for grupo in grupos:
        if grupo not in almacen_grupos:
            almacen_grupos.append(grupo)
    for t in range(len(almacen_grupos)):
        plugintools . add_item ( action = "iptv1_res" , title =  '[COLOR lime][B]' + almacen_grupos[t] + '[/B][/COLOR]', extra =almacen_grupos[t], fanart = 'https://i.imgur.com/xdn0NDc.jpg' , thumbnail = 'https://i.imgur.com/GgGFDmd.jpg',folder = True)

def iptv1_res(params):
    
    seleccion = (params.get("extra")).strip()
    url = "http://perillas.mendelux.es/tesla.txt"
    llamada = requests.get(url)
    status = str(llamada.status_code)
    plugintools.log("El codigo de la llamada es " + status)
    datos = llamada.text
    thumb_defecto = "https://i.imgur.com/s8SbdSa.jpg"
    
    match = re.findall(r'(?s).*?name="([^"]+).*?logo="(.*?)".*?group.*?"([^"]+).*?(http://tesla27.space:2082/abel2/abel2/[0-9]+)',datos)
    
    for title, thumb, group, url in match:
        if thumb == '':
            thumb = thumb_defecto
        if seleccion in group.strip():
            plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title+ "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = 'https://i.imgur.com/xdn0NDc.jpg' , folder = False , isPlayable = True )
 
def iptv2(params):   
	
    url = "http://perillas.mendelux.es/rodri.txt"
    llamada = requests.get(url)
    datos = llamada.text
    grupos = re.findall(r'(?s).*?group-title="([^"]+)',datos)
    
    almacen_grupos = []
    
    for grupo in grupos:
        if grupo not in almacen_grupos:
            almacen_grupos.append(grupo)
    for t in range(len(almacen_grupos)):
        plugintools . add_item ( action = "iptv2_res" , title =  '[COLOR lime][B]' + almacen_grupos[t] + '[/B][/COLOR]', extra =almacen_grupos[t], fanart = 'https://i.imgur.com/xdn0NDc.jpg' , thumbnail = 'https://i.imgur.com/GgGFDmd.jpg',folder = True)

def iptv2_res(params):
    seleccion = (params.get("extra")).strip()
    url = "http://perillas.mendelux.es/rodri.txt"
    llamada = requests.get(url)
    datos = llamada.text
    
    matches = re.findall(r'(?s).*?name="([^"]+).*?logo="([^"]+).*?group-title="([^"]+).*?(http://tvstarlife.com:25461/Rodriguez/2022/[0-8]+)', datos, re.DOTALL )
    for title, thumb,grup, url in matches:
        if grup.strip() in seleccion:
            plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = thumb , folder = False , isPlayable = True )


def iptv3(params):   
	
    url = "http://perillas.mendelux.es/numeroca.txt"
    llamada = requests.get(url)
    datos = llamada.text
    grupos = re.findall(r'(?s).*?group-title="([^"]+)',datos)
    
    almacen_grupos = []
    
    for grupo in grupos:
        if grupo not in almacen_grupos:
            almacen_grupos.append(grupo)
    for t in range(len(almacen_grupos)):
        plugintools . add_item ( action = "iptv3_res" , title =  '[COLOR lime][B]' + almacen_grupos[t] + '[/B][/COLOR]', extra =almacen_grupos[t], fanart = 'https://i.imgur.com/xdn0NDc.jpg' , thumbnail = 'https://i.imgur.com/GgGFDmd.jpg',folder = True)

def iptv3_res(params):
    seleccion = (params.get("extra")).strip()
    url = "http://perillas.mendelux.es/numerica.txt"
    llamada = requests.get(url)
    datos = llamada.text
    
    matches = re.findall(r'(?s).*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http://lemon.catchmeifyo.com:8000/6485419851/6394981750/[0-9]+)', datos, re.DOTALL )
    for title, thumb,grup, url in matches:
        if grup.strip() in seleccion:
            plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = thumb , folder = False , isPlayable = True )


def iptv4(params):   
	
  
    almacen_grupos = ["CANALES GENERALISTAS","CANALES DEPORTE","CANALES CINE","CANALES MUSICALES","CANALES SERIES Y ENTRETENIMIENTO",
                      "CANALES DOCUMENTALES","CANALES INFANTILES Y JUVENILES","CANALES AUTONÓMICOS","CANALES NOTICIAS"]
    
    for t in range(len(almacen_grupos)):
        plugintools . add_item ( action = "iptv4_res" , title =  '[COLOR lime][B]' + almacen_grupos[t] + '[/B][/COLOR]', extra =almacen_grupos[t], fanart = 'https://i.imgur.com/xdn0NDc.jpg' , thumbnail = 'https://i.imgur.com/niIFp0G.jpg',folder = True)

def iptv4_res(params):
       
    almacen_grupos = ["CANALES GENERALISTAS","CANALES DEPORTE","CANALES CINE","CANALES MUSICALES","CANALES SERIES Y ENTRETENIMIENTO",
                      "CANALES DOCUMENTALES","CANALES INFANTILES Y JUVENILES","CANALES AUTONÓMICOS","CANALES NOTICIAS"]
    seleccion = (params.get("extra")).strip()
    url = "http://perillas.mendelux.es/crt.txt"
    llamada = requests.get(url)
    datos = llamada.text
    
    matches = re.findall(r'(?s).*?name="([^"]+).*?logo="([^"]+).*?group-title="([^"]+).*?(http://stariptv.org:8080/hamza2022/123456/[0-9]+)', datos, re.DOTALL )
    for title, thumb,grup, url in matches:
        if grup.strip() in seleccion:
            plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = thumb , folder = False , isPlayable = True )
     

def cine(params):
	
    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/GgGFDmd.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##                    [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR lightpink]C[COLOR blue]I[COLOR yellow]N[COLOR aqua]E                                 [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/GgGFDmd.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "[COLOR lime][B]##########################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/GgGFDmd.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg",  folder = False )

    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
   
    plugintools.add_item(action = "" , title = "[COLOR magenta][UPPERCASE][B]Necesitas tener instalado acestream.[/B][/COLOR][/UPPERCASE]" , thumbnail = "" , url = "" , fanart = "" )
   
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

    url = "http://perillas.mendelux.es/etn.txt"
    llamada = requests.get(url)
    datos = llamada.text
    matches = re.findall(r'(?s).*?logo.*?"([^"]+).*?group.*?"([^"]+).*?,(.*?)\n.*?ace.*?//(.*?)\.', datos, re.DOTALL )
    for thumb,grup,title, url in matches:
        plugintools.add_item ( action = "resolve_acestream" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = thumb , folder = False , isPlayable = True )
    
    plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)
    plugintools.add_item(action = "main_list" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/GgGFDmd.jpg", fanart = "https://i.imgur.com/cE1QfPa.jpg", folder = True )


def canalesacestream(params):
       
   plugintools.set_view(plugintools.LIST)
   
   plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/hSi2VIS.jpg", fanart = "https://i.imgur.com/lHvis9j.jpg",  folder = False )

   plugintools.add_item(action = "" , title = "[COLOR lime][B]##                       [COLOR gold]K[COLOR lime]o[COLOR aqua]d[COLOR yellow]i[COLOR white]v[COLOR fuchsia]e[COLOR blue]r[COLOR aqua]t[COLOR gold]i[COLOR pink]d[COLOR red]o[COLOR fuchsia]Team [COLOR blue]Ace[COLOR yellow]stream                       [COLOR lime]##[/B][/COLOR]", thumbnail ="https://i.imgur.com/hSi2VIS.jpg", fanart = "https://i.imgur.com/lHvis9j.jpg",  folder = False )

   plugintools.add_item(action = "" , title = "[COLOR lime][B]#####################################[/B][/COLOR]", thumbnail ="https://i.imgur.com/hSi2VIS.jpg", fanart = "https://i.imgur.com/lHvis9j.jpg",  folder = False )

   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)

   plugintools.add_item(action = "main_list" , title = "[COLOR fuchsia][B]->Volver al menu<-[/B][/COLOR]", thumbnail ="https://i.imgur.com/hSi2VIS.jpg", fanart = "https://i.imgur.com/lHvis9j.jpg", folder = True )

   plugintools.add_item(action = "" , title = "", thumbnail="", fanart="", folder=False)  

   url3 = "https://antonieta.futbolgratis.workers.dev/"
   request_headers = []
   request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"] )
   read_url, response_headers = plugintools.read_body_and_headers ( url3 , headers = request_headers )
   url = read_url.strip ()
   matches = re.findall(r'(?s).*?<a href="acestream://(.*?)".*?>([^<]+)', url, re.DOTALL )   
   for url, title in matches:
      title.strip()
      plugintools.add_item(action = "resolve_acestream",title="[COLOR yellow][B]" + title + "[/COLOR][/B]",  url = url, thumbnail = "https://i.imgur.com/PUj0KAx.jpg", fanart = "https://i.imgur.com/Yd9lDfr.jpg", folder = False, isPlayable = True)


     
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
  # utilizamos el addon horus para teproducir el acestream
   finalurl = "plugin://script.module.horus?action=play&id={}&title={}&iconimage={}".format(params.get("url"),params.get("title"),params.get("thumbnail"))
   plugintools.log("###############"+finalurl)
   plugintools . play_resolved_url ( finalurl )     

def elementum(params):
    import resolveurl
    finalurl = "plugin://plugin.video.elementum/play?uri=" + params.get ( "url" )
    plugintools.play_resolved_url ( finalurl )


 
run()
