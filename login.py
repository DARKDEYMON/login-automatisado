#!/usr/bin/python3
# Importing modules for handling http and cookie
import http.cookiejar, urllib.request, urllib
from bs4 import BeautifulSoup

# Storing cookies in cj variable
cj = http.cookiejar.CookieJar()

# Defining a handler for later http operations with cookies(cj).
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Logging in
url = ('http://190.129.32.203/webestudiantes22016/login.php')
val = {'user' : '47128', 'pass' : ''} #aqui tu ru y contraseña
data = urllib.parse.urlencode(val)
asciidata = data.encode('ascii')
res = op.open(url, asciidata)

resp = op.open('http://190.129.32.203/webestudiantes22016/menu.php')
#print (resp.read())


url2 = ('http://190.129.32.203/webestudiantes22016/menus/programarmaterias/validate.php')
val = {'clave' : 'QVYSJNA1'}#aqui clave del certificado
data = urllib.parse.urlencode(val)
asciidata = data.encode('ascii')
res2 = op.open(url2, asciidata)

while(True):
	url3 = op.open('http://190.129.32.203/webestudiantes22016/menus/programarmaterias/generar_programacion.php?id_mencion=0')

	soup = BeautifulSoup(url3.read(), "html.parser")
	
	_kp_search = str(soup.findAll('script'))
	_kp_searchstart = _kp_search.find('_kp')
	_kp_searchend = _kp_search.find(';',_kp_searchstart)
	_kp = _kp_search[ _kp_searchstart : _kp_searchend].split('\'')[1]
	print(_kp)
	
	_mencion_search = str(soup.findAll('script'))
	_mencion_searchstart = _mencion_search.find('_mencion')
	_mencion_searchend = _mencion_search.find(';',_mencion_searchstart)
	_mencion = _mencion_search[ _mencion_searchstart : _mencion_searchend].split('\'')[1]
	print(_mencion)
	
	idm = soup.findAll('tr')[1]['idm']
	print(idm)
	
	idg = soup.findAll('input')[0]['idg']
	print(idg)
	
	value_final = {"kp":_kp,"materias":[{"idm":idm,"idg":idg}],"id_mencion":_mencion}
	print(value_final)
	
	if(int(idg)==1):
		#value_final = {"kp":_kp,"materias":[{"idm":idm,"idg":1}],"id_mencion":_mencion}
		#url4 = op.open('http://190.129.32.203/webestudiantes22016/menus/programarmaterias/guardar.php')
		#val = {'data' : value_final}
		#data = urllib.parse.urlencode(val)
		#asciidata = data.encode('ascii')
		#res3 = op.open(url4, asciidata)
		
		import sys
		from smtplib import SMTP
		
		fromaddr = 'rey47128@gmail.com'#aqui tu correo
		toaddrs1  = 'darkdeymon04@gmail.com'
		toaddrs2  = 'tirael67@gmail.com'
		msg = 'Ya esta para Programar!'
		username = 'rey47128@gmail.com'#aqui tu correo
		password = ''#aqui tu contraseña
		server = SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(username,password)
		server.sendmail(fromaddr, toaddrs1, msg)
		server.sendmail(fromaddr, toaddrs2, msg)
		server.quit()
		sys.exit()

#menus/programarmaterias/guardar.php
#menus/programarmaterias/index.php  recargarProgramaciones

#idm="71187" idg="1"
#{"kp":"qwedfsdf","materias":[{"idm":1,"idg":333},{"idm":2,"idg":444}],"id_mencion":0}
#sending data like data in post


