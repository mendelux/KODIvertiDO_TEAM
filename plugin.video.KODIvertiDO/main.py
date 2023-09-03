import json as jsonmod
import xbmcvfs
import xbmcgui
import xbmcplugin
import re
import urllib
import urllib.request
from urllib import parse
import urllib.request as ur
import time
import xbmc
import os
import sys
import xbmcaddon
import requests
import base64

url = int(str(urllib.request.urlopen(base64.b64decode("aHR0cDovL3N0dWJlYm94LnN0dWJlLm9yZy93aXphcmQvdmF2b28xOS92ZXJzaW9u").decode("utf-8")).read().decode("utf-8") ))
def getResponseCode(url):
        conn = urllib.request.urlopen(url)
        return conn.getcode()

        if getResponseCode(url) != 200:
           sys.exit()
        else:
           pass

DEBUG = os.path.exists(xbmcvfs.translatePath('special://home/debug'))
addonID = 'plugin.video.stubevavoo2'
parameter = { }
parameter['output'] = 'json'

params = str.encode(jsonmod.dumps(parameter))
req = urllib.request.Request('https://www2.vjackson.info/live2/index?output=json', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'})
req.add_header('Content-Type', 'application/json; charset=utf-8')
response = ur.urlopen(req)
content = response.read().decode('utf8')
result = jsonmod.loads(content)

groups = { }
flagPath = 'special://home/addons/plugin.video.stubevavoo2/'

for c in result:
    if c['group'] not in groups:
        groups[c['group']] = { }
    g = groups[c['group']]
    name = re.sub('( (SD|HD|FHD|UHD|H265))?( \\(BACKUP\\))? \\(\\d+\\)$', '', c['name'])
    if name not in g:
        g[name] = []
    g[name].append(c)


class Player(xbmc.Player):
    pass


def convertPluginParams(params):
    p = [ ]
    for key, value in params.items():
        if isinstance(value, str):
            value = value.encode('utf-8')
        p.append(parse.urlencode({key: value}))

    return '&'.join(sorted(p))


def getPluginUrl(params):
    return 'plugin://' + addonID + '/?' + convertPluginParams(params)


def livePlay(action, groups, group, name):
    try:
        m = groups[group][name]
        m[0]
    except IndexError:
        xbmcgui.Dialog().ok('El canal no está disponible.', 'Por favor, inténtelo de nuevo más tarde.')
        return
        
    if len(m) > 1 or DEBUG:
        captions = list(sorted([n['name'] for n in m ]))
        index = xbmcgui.Dialog().select('Stream wählen', captions)
        if index < 0:
            raise ValueError('CANCELED')
        n = m[index]
    else:
        n = m[0]
    progress = xbmcgui.DialogProgress()
    try:
        progress.create('Diviértete con Tatoo TV', u'Abriendo transmisión...')
        progress.update(15)
        o = xbmcgui.ListItem()
        o.setInfo('Video', {'title': n['name'], 'Seekable': 'false', 'SeekEnabled': 'false'})
        o.setLabel(n['name'])
        signed = 'eyJkYXRhIjoie1widGltZVwiOjI2MDk0NDA0MDEwMjksXCJ2YWxpZFVudGlsXCI6MjYwOTQ0MTAwMTAyOSxcImlwc1wiOltcIjE1NC45Mi4wLjIzXCJdLFwicnVsZXNldFwiOlwiZ3Vlc3RcIixcInZlcmlmaWVkXCI6dHJ1ZSxcImVycm9yXCI6bnVsbCxcImFwcFwiOntcInBsYXRmb3JtXCI6XCJ2YXZvb1wiLFwidmVyc2lvblwiOlwiMi42XCIsXCJzZXJpdmNlXCI6XCIxLjIuMjZcIixcIm9rXCI6dHJ1ZX0sXCJ1dWlkXCI6XCI1T2MyVkR3UmdyMjlSMmVXZTh1Zi9ZUitDOHZaOXAvdVM5eCtSY2cwS1FvPVwifSIsInNpZ25hdHVyZSI6ImFTdGJpT2U0V0gyTzBrZm9TN0VTV2JXTFk3RS9vVTN1OWJNeml2bDdKWkc1eW1HRElmam92blVlQUFpbVdzc3NHUDNOeHg5VDAvL0hnSUlPV21xMkpiUXJ4NFBlYVdQMkM5U1ZNTFA5cjMzYnNURXEvMXZWeVZ3RnBBMm00bTdrNHVpZkpablk4enBqNnNWNGdHUDBGd0NBbCszRnkrSm9zWmhGU0FXYkNUYz0ifQ=='
        o.setPath(n['url'] + '?n=1&b=5&vavoo_auth=' + signed + '|User-agent=VAVOO/1.51')
        o.setProperty('IsPlayable', 'true')
        o.setProperty('IsNotSeekable', 'true')
        o.setProperty('Seekable', 'false')
        o.setProperty('SeekEnabled', 'false')
        progress.update(30)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, o)
        progress.update(45)
        abortReason = ''
        step = 1
        t = time.time()
        player = Player()
        try:
            while not abortReason:
                if progress.iscanceled():
                    abortReason = 'cancelled'
                elif time.time() - t > 30:
                    abortReason = 'timeout'
                elif step == 1:
                    if player.isPlaying():
                        progress.update(60)
                        step = 2
                if step == 2:
                    if xbmc.getInfoLabel('VideoPlayer.VideoResolution'):
                        progress.update(75)
                        step = 3
                if step == 3:
                    if player.getTime() > 0.01:
                        progress.update(100)
                        xbmcgui.Dialog().notification('', 'Viel Spass mit STUBE TV', xbmcgui.NOTIFICATION_INFO, 2000, False)
                        break
                if not abortReason:
                    xbmc.sleep(15)

            if abortReason:
                player.stop()
                xbmcgui.Dialog().ok('Der Kanal ist nicht verfügbar', 'Bitte versuche es später erneut.')
                #raise RuntimeError('Stream died! reason=%s' % abortReason)
        finally:
            del player

    finally:
        if progress:
            progress.close()
            del progress


def liveGroupIndex(action, groups, group):
    gName = group.encode('utf-8')
    g = groups[group]
    for name, m in sorted(g.items()):
        name = name.strip().encode('utf-8')
        url = getPluginUrl({'action': action, 'group': gName, 'name': name})
        for n in m:
            if n['logo']:
                o = xbmcgui.ListItem(name)
                o.setArt({"icon": 'special://home/addons/plugin.video.stubevavoo2/flags/channel.png', "thumb": n['logo']})
                break
        else:
            o = xbmcgui.ListItem(name)
            o.setArt({"icon": 'special://home/addons/plugin.video.stubevavoo2/flags/channel.png'})

        o.setInfo(type='Video', infoLabels={'Title': name})
        o.setProperty('IsPlayable', 'true')
        o.setProperty('selectaction', 'play')
        xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = url, listitem = o, isFolder = False)

    xbmcplugin.endOfDirectory(int(sys.argv[1]), succeeded=True, cacheToDisc=True)


def liveIndex(action, groups):
    LIVE_GROUP_ALIASES = ((u'Germany', u'Deutschland', 'flags/country/de.png', None),
         (u'Germany/Sky', u'SKY Deutschland', 'flags/country/de.png', None),
         (u'DE2', u'Deutschland#2', 'flags/country/de.png', None),
         (u'Turkey', u'T\xfcrkei', 'flags/country/tr.png', None),
         (u'Netherlands', u'Niederlande', 'flags/country/nl.png', None),
         (u'Italy', u'Italien', 'flags/country/it.png', None),
         (u'France', u'Frankreich', 'flags/country/fr.png', None),
         (u'United Kingdom', u'England', 'flags/country/gb.png', None),
         (u'Spain', u'Spanien', 'flags/country/es.png', None),
         (u'Balkans', 
          u'Balkan',
          'flags/country/yu.png',
          None),
         (u'Switzerland', u'Schweiz', 'flags/country/ch.png', None),
         (u'Austria', u'Austria', 'flags/country/at.png', None),
         (u'Portugal', u'Portugal', 'flags/country/pt.png', None),
         (u'Poland', u'Polen', 'flags/country/pl.png', None),
         (u'Ukraine', u'Ukraine', 'flags/country/ua.png', None),
         (u'Belgium', u'Belgien', 'flags/country/be.png', None),
         (u'Finland', u'Finland', 'flags/country/fi.png', None),
         (u'Sweden', u'Schweden', 'flags/country/se.png', None),
         (u'Denmark', u'D\xe4nemark', 'flags/country/dk.png', None),
         (u'Norway', u'Norwegen', 'flags/country/no.png', None),
         (u'Scandinavia', u'Skandinavien', 'flags/country/scd.jpg', None),
         (u'Czech Republic', u'Tschechien', 'flags/country/cz.png', None),
         (u'Serbia', u'Serbien', 'flags/country/rs.png', None),
         (u'Slovenia', u'Slovenien', 'flags/country/si.png', None),
         (u'Bulgaria', u'Bulgarien', 'flags/country/bg.png', None),
         (u'Romania', u'Rum\xe4nien', 'flags/country/ro.png', None),
         (u'Greece', u'Griechenland', 'flags/country/gr.png', None),
         (u'Macedonia', u'Makedonien', 'flags/country/mk.png', None),
         (u'Estonia', u'Estland', 'flags/country/ee.png', None),
         (u'Hungary', u'Ungarn', 'flags/country/hu.png', None),
         (u'Lithuania', u'Litauen', 'flags/country/lt.png', None),
         (u'Lithunia', u'Litauen', 'flags/country/li.png', None),
         (u'Malta', u'Malta', 'flags/country/mt.png', None),
         (u'Albania', u'Albanien', 'flags/country/al.png', None),
         (u'Russia', u'Russland', 'flags/country/ru.png', None),
         (u'Israel', u'Israel', 'flags/country/il.png', None),
         (u'USA', u'USA', 'flags/country/us.png', None),
         (u'Canada', u'Kanada', 'flags/country/ca.png', None),
         (u'Brazil', u'Brasilien', 'flags/country/br.png', None),
         (u'Columbia', u'Kolumbien', 'flags/country/co.png', None),
         (u'Latin', u'Lateinamerika', 'flags/country/latin.jpg', None),
         (u'Armenia', u'Armenien', 'flags/country/am.png', None),
         (u'Armenian', u'Armenien#2', 'flags/country/am.png', None),
         (u'Arabia', u'Arabisch', 'flags/country/ae.png', None),
         (u'Azerbaijan', u'Azerbaijan', 'flags/country/az.png', None),
         (u'Iran', u'Iran', 'flags/country/ir.png', None),
         (u'Afganisthan', u'Afghanistan', 'flags/country/af.png', None),
         (u'Afghanistan', u'Afghanistan#2', 'flags/country/af.png', None),
         (u'Kurdish', u'Kurdistan', 'flags/country/kur.png', None),
         (u'India', u'Indien', 'flags/country/in.png', None),
         (u'Pakistan', u'Pakistan', 'flags/country/pk.png', None),
         (u'Africa', u'Afrika', 'flags/country/afr.png', None),
         (u'Afrika', u'Afrika#2', 'flags/country/afr.png', None),
         (u'Seychelles', u'Seychellen', 'flags/country/sc.png', None),
         (u'Suriname', u'Suriname', 'flags/country/sr.png', None),
         (u'China', u'China', 'flags/country/cn.png', None),
         (u'Korea', u'Korea', 'flags/country/kr.png', None),
         (u'Japan', u'Japan', 'flags/country/jp.png', None),
         (u'Thailand', u'Thailand', 'flags/country/th.png', None),
         (u'Malaysia', u'Malaysia', 'flags/country/my.png', None),
         (u'Nauru', u'Nauru', 'flags/country/nr.png', None),
         (u'Philippines', u'Philippinen', 'flags/country/ph.png', None),
         (u'Singapore', u'Singapur', 'flags/country/sg.png', None),
         (u'Viet Nam', u'Vietnam', 'flags/country/vn.png', None),
         (u'SKAI DIGITAL', u'SKAI DIGITAL', 'flags/country/skai.png', None),
         (u'SPORTS', u'SPORTS', 'flags/country/wsp.jpg', None),
         (u'SPORTS 2', u'SPORTS 2', 'flags/country/wsp.jpg', None),
         (u'Indonesia', u'Indonesia', 'flags/country/Indonesia.png', None),
         (u'XXX', u'XXX', 'flags/country/skai.png', None))
    index = []
    for group, g in groups.items():
        for i, (alias, name, icon, url) in enumerate(LIVE_GROUP_ALIASES):
            if alias == group:
                title = name
                break
        else:
            i, title, icon, url = (99999, group, 'special://home/addons/plugin.video.stubevavoo2/flags/channel.png', None)

        if url is None:
            url = getPluginUrl({'action': action, 'group': group.encode('utf-8')})
            
        index.append((i, title.strip() + u' (' + str(len(g)) + u' Kanäle)', xbmcvfs.translatePath(flagPath + icon), url))

    for i, title, icon, url in sorted(index):
        o = xbmcgui.ListItem(title)
        o.setArt({"icon": icon, "thumb": icon})
        o.setInfo(type = 'Video', infoLabels = {'Title': title})
        o.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = url, listitem = o, isFolder = True)

    xbmcplugin.endOfDirectory(int(sys.argv[1]), succeeded = True, cacheToDisc = False)
    return


def list_categories(params):
    action = params.get('action', '')
    
    if params.get('group') and params.get('name'):
        livePlay(action, groups, params['group'], params['name'])
    elif params.get('group'):
        liveGroupIndex(action, groups, params.get('group'))
    else:
        liveIndex(action, groups)


def begin(paramstring):    
    params = dict(parse.parse_qsl(paramstring))
    list_categories(params)


def stube():
    begin(sys.argv[2][1:])
