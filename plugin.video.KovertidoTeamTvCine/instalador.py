import uservar
import xbmc, xbmcgui, urllib, sys, time, uservar, os
import wizard as wiz
import downloader,extract

COLOR1         = uservar.COLOR1
COLOR2         = uservar.COLOR2

#urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'

import xbmcgui
# import urllib2
import socket
import kodi
import time
ADDON_ID         = uservar.ADDON_ID
ADDONTITLE       = uservar.ADDONTITLE
ADDON            = wiz.addonId(ADDON_ID)
VERSION          = wiz.addonInfo(ADDON_ID,'version')
ADDONPATH        = wiz.addonInfo(ADDON_ID, 'path')
DIALOG           = xbmcgui.Dialog()
DP               = xbmcgui.DialogProgress()
HOME             = xbmc.translatePath('special://home/')
LOG              = xbmc.translatePath('special://logpath/')
PROFILE          = xbmc.translatePath('special://profile/')
TEMPDIR          = xbmc.translatePath('special://temp')
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
KODIV            = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
#if KODIV > 17:
	#import zfile as zipfile
#else:
import zipfile

def packInstaller(name, url):
    import xbmcvfs
    #if not wiz.workingURL(url) == True: wiz.LogNotify("[COLOR %s]Instalador de Addons[/COLOR]" % COLOR1, '[COLOR %s]%s:[/COLOR] [COLOR %s]Zip Url Invalida[/COLOR]' % (COLOR1, name, COLOR2)); return
    if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
    DP.create(ADDONTITLE,'[COLOR %s]Descargando:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name))
    urlsplits = url.split('/')
    lib = xbmcvfs.makeLegalFilename(os.path.join(PACKAGES, urlsplits[-1]))
    try: os.remove(lib)
    except: pass
    downloader.download(url, lib, DP)
    title = '[COLOR %s]Instalando:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name)
    DP.update(0, '[COLOR %s]Espera[/COLOR]' % COLOR2)
    extract.all(lib,ADDONS,DP)
    installed = grabAddons(lib)
    wiz.addonDatabase(installed, 1, True)
    DP.close()
    wiz.LogNotify("[COLOR %s]Instalador de Addons[/COLOR]" % COLOR1, '[COLOR %s]%s: Instalado![/COLOR]' % (COLOR2, name))
    wiz.ebi('UpdateAddonRepos()')
    wiz.ebi('UpdateLocalAddons()')
    wiz.refresh()


def addonInstaller(plugin, url):
    import uservar
    import xbmc, xbmcgui, urllib, sys, time, uservar, os
    import wizard as wiz
    import downloader,extract
    url = None
    #url='http://perillas.mendelux.es/plugin.video.stubevavoo2.zip'
    ADDONFILE      = 'http://perillas.mendelux.es/addons.txt'
    if  'http://' in ADDONFILE :
    #if  not ADDONFILE == 'http://':
        if url == None: url = ADDONFILE
        ADDONWORKING = wiz.workingURL(url)
        if ADDONWORKING == True:
            link = wiz.textCache(url).replace('\n','').replace('\r','').replace('\t','').replace('repository=""', 'repository="none"').replace('repositoryurl=""', 'repositoryurl="http://"').replace('repositoryxml=""', 'repositoryxml="http://"')
            match = re.compile('name="(.+?)".+?lugin="%s".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % plugin).findall(link)
            if len(match) > 0:
                for name, url, repository, repositoryxml, repositoryurl, icon, fanart, adult, description in match:
                    if os.path.exists(os.path.join(ADDONS, plugin)):
                        do        = ['[COLOR lime][B]Abrir Addon[/B][/COLOR]', '[COLOR red][B]Borrar Addon[/B][/COLOR]']
                        selected = DIALOG.select("[COLOR %s][COLOR yellow][B]Addon ya instalado, que quieres hacer?[/B][/COLOR]" % COLOR2, do)
                        if selected == 0:
                            wiz.ebi('RunAddon(%s)' % plugin)
                            xbmc.sleep(500)
                            return True
                        elif selected == 1:
                            wiz.cleanHouse(os.path.join(ADDONS, plugin))
                            try: wiz.removeFolder(os.path.join(ADDONS, plugin))
                            except: pass
                            if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Quieres borrar la carpeta addon_data de:" % COLOR2, "[COLOR %s]%s[/COLOR]?[/COLOR]" % (COLOR1, plugin), yeslabel="[COLOR springgreen]Borrar[/COLOR]", nolabel="[COLOR red]Saltar[/COLOR]"):
                                removeAddonData(plugin)
                            wiz.refresh()
                            return True
                        else:
                            return False
                    repo = os.path.join(ADDONS, repository)
                    if not repository.lower() == 'none' and not os.path.exists(repo):
                        wiz.log("Repository not installed, installing it")
                        if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to install the repository for [COLOR %s]%s[/COLOR]:" % (COLOR2, COLOR1, plugin), "[COLOR %s]%s[/COLOR]?[/COLOR]" % (COLOR1, repository), yeslabel="[COLOR springgreen]Yes Install[/COLOR]", nolabel="[COLOR red]No Skip[/COLOR]"):
                            ver = wiz.parseDOM(wiz.openURL(repositoryxml), 'addon', ret='version', attrs = {'id': repository})
                            if len(ver) > 0:
                                repozip = '%s%s-%s.zip' % (repositoryurl, repository, ver[0])
                                wiz.log(repozip)
                                if KODIV >= 17: wiz.addonDatabase(repository, 1)
                                installAddon(repository, repozip)
                                wiz.ebi('UpdateAddonRepos()')
                                wiz.ebi('UpdateLocalAddons()')
                                wiz.log("Installing Addon from Kodi")
                                install = installFromKodi(plugin)
                                wiz.log("Install from Kodi: %s" % install)
                                if install:
                                    wiz.refresh()
                                    return True
                            else:
                                wiz.log("[Addon Installer] Repository not installed: Unable to grab url! (%s)" % repository)
                        else: wiz.log("[Addon Installer] Repository for %s not installed: %s" % (plugin, repository))
                    elif repository.lower() == 'none':
                        wiz.log("No repository, installing addon")
                        pluginid = plugin
                        zipurl = url
                        installAddon(plugin, url)
                        wiz.refresh()
                        return True
                    else:
                        wiz.log("Repository installed, installing addon")
                        install = installFromKodi(plugin, False)
                        if install:
                            wiz.refresh()
                            return True
                    if os.path.exists(os.path.join(ADDONS, plugin)): return True
                    ver2 = wiz.parseDOM(wiz.openURL(repositoryxml), 'addon', ret='version', attrs = {'id': plugin})
                    if len(ver2) > 0:
                        url = "%s%s-%s.zip" % (url, plugin, ver2[0])
                        wiz.log(str(url))
                        if KODIV >= 17: wiz.addonDatabase(plugin, 1)
                        installAddon(plugin, url)
                        wiz.refresh()
                    else:
                        wiz.log("no match"); return False
            else: wiz.log("[Addon Installer] Invalid Format")
        else: wiz.log("[Addon Installer] Text File: %s" % ADDONWORKING)
    else: wiz.log("[Addon Installer] Not Enabled.")

def installFromKodi(plugin, over=True):
    if over == True:
        xbmc.sleep(2000)
    #wiz.ebi('InstallAddon(%s)' % plugin)
    wiz.ebi('RunPlugin(plugin://%s)' % plugin)
    if not wiz.whileWindow('yesnodialog'):
        return False
    xbmc.sleep(500)
    if wiz.whileWindow('okdialog'):
        return False
    wiz.whileWindow('progressdialog')
    if os.path.exists(os.path.join(ADDONS, plugin)): return True
    else: return False

def installAddon(name, url):
    #if not wiz.workingURL(url) == True: wiz.LogNotify("[COLOR %s]Instalador de Addons[/COLOR]" % COLOR1, '[COLOR %s]%s:[/COLOR] [COLOR %s]Url del Zip Invalida[/COLOR]' % (COLOR1, name, COLOR2)); return
    if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
    DP.create(ADDONTITLE,'[COLOR %s]Descargando:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, 'complemento'))
    urlsplits = url.split('/')
    lib=os.path.join(PACKAGES, urlsplits[-1])
    try: os.remove(lib)
    except: pass
    downloader.download(url, lib, DP)
    title = '[COLOR %s]Instalando:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, 'complemento')
    DP.update(0, '[COLOR %s]Espera[/COLOR]' % COLOR2)
    extract.all(lib,ADDONS,DP)
    #DP.update(0,'[COLOR %s]Instalando Dependencias[/COLOR]' % COLOR2)
    installed(name)
    installlist = grabAddons(lib)
    wiz.log(str(installlist))
    wiz.addonDatabase(installlist, 1, True)
    #installDep(name, DP)
    DP.close()
    wiz.ebi('UpdateAddonRepos()')
    wiz.ebi('UpdateLocalAddons()')
    wiz.refresh()
    #for item in installlist:
        #if item.startswith('skin.') == True and not item == 'skin.shortcuts':
            #if not BUILDNAME == '' and DEFAULTIGNORE == 'true': wiz.setS('defaultskinignore', 'true')
            #wiz.swapSkins(item, 'Skin Installer')

def installDep(name, DP=None):
    dep=os.path.join(ADDONS,name,'addon.xml')
    if os.path.exists(dep):
        source = open(dep,mode='r'); link = source.read(); source.close();
        match  = wiz.parseDOM(link, 'import', ret='addon')
        for depends in match:
            if not 'xbmc.python' in depends:
                if not DP == None:
                    DP.update(0, '[COLOR %s]%s[/COLOR]' % (COLOR1, depends))
                try:
                    add   = xbmcaddon.Addon(id=depends)
                    name2 = add.getAddonInfo('name')
                except:
                    #wiz.createTemp(depends)
                    #if KODIV >= 17: wiz.addonDatabase(depends, 1)
                    pass
                # continue
                # dependspath=os.path.join(ADDONS, depends)
                # if not os.path.exists(dependspath):
                    # zipname = '%s-%s.zip' % (depends, match2[match.index(depends)])
                    # depzip = urljoin("%s%s/" % (MODURL2, depends), zipname)
                    # if not wiz.workingURL(depzip) == True:
                        # depzip = urljoin(MODURL, '%s.zip' % depends)
                        # if not wiz.workingURL(depzip) == True:
                            # wiz.createTemp(depends)
                            # if KODIV >= 17: wiz.addonDatabase(depends, 1)
                            # continue
                    # lib=os.path.join(PACKAGES, '%s.zip' % depends)
                    # try: os.remove(lib)
                    # except: pass
                    # DP.update(0, '[COLOR %s]Downloading Dependency:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, depends),'', 'Please Wait')
                    # downloader.download(depzip, lib, DP)
                    # xbmc.sleep(100)
                    # title = '[COLOR %s]Installing Dependency:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, depends)
                    # DP.update(0, title,'', 'Please Wait')
                    # percent, errors, error = extract.all(lib,ADDONS,DP, title=title)
                    # if KODIV >= 17: wiz.addonDatabase(depends, 1)
                    # installed(depends)
                    # installDep(depends)
                    # xbmc.sleep(100)
                    # DP.close()
                    
def installed(addon):
    url = os.path.join(ADDONS,addon,'addon.xml')
    if os.path.exists(url):
        try:
            list  = open(url,mode='r'); g = list.read(); list.close()
            name = wiz.parseDOM(g, 'addon', ret='name', attrs = {'id': addon})
            icon  = os.path.join(ADDONS,addon,'icon.png')
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id":1, "method": "Addons.SetAddonEnabled", "params": { "addonid": "plugin.video.stubevavoo2 ", "enabled": true }}')
            wiz.LogNotify('[COLOR %s]%s[/COLOR]' % (COLOR1, 'Tv Vaboo'), '[COLOR %s]Addon Enabled[/COLOR]' % COLOR2, '2000', icon)
        except: pass


def removeAddon(addon, name, over=False):
    if not over == False:
        yes = 1
    else:
        yes = DIALOG.yesno(ADDONTITLE, '[COLOR %s]Are you sure you want to delete the addon:'% COLOR2, 'Name: [COLOR %s]%s[/COLOR]' % (COLOR1, name), 'ID: [COLOR %s]%s[/COLOR][/COLOR]' % (COLOR1, addon), yeslabel='[COLOR springgreen]Remove Addon[/COLOR]', nolabel='[COLOR red]Don\'t Remove[/COLOR]')
    if yes == 1:
        folder = os.path.join(ADDONS, addon)
        wiz.log("Removing Addon %s" % addon)
        wiz.cleanHouse(folder)
        xbmc.sleep(200)
        try: shutil.rmtree(folder)
        except Exception  as e: wiz.log("Error removing %s" % addon, xbmc.LOGNOTICE)
        removeAddonData(addon, name, over)
    if over == False:
        wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]%s Removed[/COLOR]" % (COLOR2, name))

def removeAddonData(addon, name=None, over=False):
    if addon == 'all':
        if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Quieres eliminar [COLOR %s]TODOS[/COLOR] los datos de la carpeta Addon_data?[/COLOR]' % (COLOR2, COLOR1), yeslabel='[COLOR springgreen]Eliminar Data[/COLOR]', nolabel='[COLOR red]No Eliminar[/COLOR]'):
            wiz.cleanHouse(ADDOND)
        else: wiz.LogNotify('[COLOR %s]Borrar Addon_data[/COLOR]' % COLOR1, '[COLOR %s]Cancelado![/COLOR]' % COLOR2)
    elif addon == 'uninstalled':
        if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Quieres eliminar [COLOR %s]TODOS[/COLOR] los datos de la carpeta Addon_data de addons desinstalados?[/COLOR]' % (COLOR2, COLOR1), yeslabel='[COLOR springgreen]Eliminar Data[/COLOR]', nolabel='[COLOR red]No Eliminar[/COLOR]'):
            total = 0
            for folder in glob.glob(os.path.join(ADDOND, '*')):
                foldername = folder.replace(ADDOND, '').replace('\\', '').replace('/', '')
                if foldername in EXCLUDES: pass
                elif os.path.exists(os.path.join(ADDONS, foldername)): pass
                else: wiz.cleanHouse(folder); total += 1; wiz.log(folder); shutil.rmtree(folder)
            wiz.LogNotify('[COLOR %s]Clean up Uninstalled[/COLOR]' % COLOR1, '[COLOR %s]%s Folders(s) Removed[/COLOR]' % (COLOR2, total))
        else: wiz.LogNotify('[COLOR %s]Remove Addon Data[/COLOR]' % COLOR1, '[COLOR %s]Cancelled![/COLOR]' % COLOR2)
    elif addon == 'empty':
        if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Quieres eliminar [COLOR %s]TODAS[/COLOR] las carpetas vacias de userdata?[/COLOR]' % (COLOR2, COLOR1), yeslabel='[COLOR springgreen]Borrar Data[/COLOR]', nolabel='[COLOR red]No Eliminar[/COLOR]'):
            total = wiz.emptyfolder(ADDOND)
            wiz.LogNotify('[COLOR %s]Borrar carpetas vacias[/COLOR]' % COLOR1, '[COLOR %s]%s Carpeta(s) Borradoas[/COLOR]' % (COLOR2, total))
        else: wiz.LogNotify('[COLOR %s]Borrar carpetas vacias[/COLOR]' % COLOR1, '[COLOR %s]Cancelados![/COLOR]' % COLOR2)
    else:
        addon_data = os.path.join(USERDATA, 'addon_data', addon)
        if addon in EXCLUDES:
            wiz.LogNotify("[COLOR %s]Plugin protegido[/COLOR]" % COLOR1, "[COLOR %s]No esta permitido eliminarlo[/COLOR]" % COLOR2)
        elif os.path.exists(addon_data):
            if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Quieres borrar de addon_data:[/COLOR]' % COLOR2, '[COLOR %s]%s[/COLOR]' % (COLOR1, addon), yeslabel='[COLOR springgreen]Eliminar Data[/COLOR]', nolabel='[COLOR red]No eliminar[/COLOR]'):
                wiz.cleanHouse(addon_data)
                try:
                    shutil.rmtree(addon_data)
                except:
                    wiz.log("Error deleting: %s" % addon_data)
            else:
                wiz.log('Addon data for %s was not removed' % addon)
    wiz.refresh()
    
def grabAddons(path):

    zfile = zipfile.ZipFile(path)
    addonlist = []
    for item in zfile.infolist():
        if str(item.filename).find('addon.xml') == -1: continue
        info = str(item.filename).split('/')
        if not info[-2] in addonlist:
            addonlist.append(info[-2])
    return addonlist

