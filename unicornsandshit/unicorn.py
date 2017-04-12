from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from threading import Timer
import datetime as dt
import unittest
import time
import urllib2

def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

def wait_connection():	
	while(not internet_on()):
		print("Waiting for connection...")
		time.sleep(5)

def unicorn():
    # XPath and http addresses variables initialization
    while True:
		t = dt.date.today() + dt.timedelta(days=15)
		tomorrow = str(t) + "/ora/"
		orari = ["","","","","","","","","",""]
		orari[2] = tomorrow + "10%3A00/etichetta/10%3A00-11%3A00"
		orari[3] = tomorrow + "11%3A00/etichetta/11%3A00-12%3A00"
		orari[4] = tomorrow + "12%3A00/etichetta/12%3A00-13%3A00"
		orari[5] = tomorrow + "13%3A00/etichetta/13%3A00-14%3A00"
		orari[6] = tomorrow + "14%3A00/etichetta/14%3A00-15%3A00"
		orari[7] = tomorrow + "15%3A00/etichetta/15%3A00-16%3A00"
		orari[0] = tomorrow + "08%3A30/etichetta/8%3A30-9%3A00"
		orari[1] = tomorrow + "09%3A00/etichetta/9%3A00-10%3A00"
		orari[8] = tomorrow + "16%3A00/etichetta/16%3A00-17%3A00"
		orari[9] = tomorrow + "17%3A00/etichetta/17%3A00-18%3A00"
		# Waiting for 23:50
		x = datetime.today()
		y = x.replace(day = x.day, hour=23, minute = 50, second = 0, microsecond = 0)
		delta_t = y-x
		secs = delta_t.seconds+1
		wait_connection()
		print("Aspetto le 23:50")
		print(secs)
		time.sleep(secs)
		print("Si comincia!")
		# Driver initialization
		print("Inizializzazione del driver...")
		driver = webdriver.Firefox(executable_path='/home/valdemar/Documents/unicornsandshit/geckodriver')
		wait_connection()
		driver.get("http://static.unive.it/prenotazioni/accesso/?destinazione=%2Flemieprenotazioni")
		print("Fatto!")
		# Authentication data
		print("Ottengo le credenziali...")
		with open('/home/valdemar/Documents/unicornsandshit/auth.txt') as f:
		    lines = f.read().splitlines()
		univeUsername = lines[0]
		univePassword = lines[1]
		print("Fatto!")
		# Select login via credentials
		authButtonXPath =   "//button[@class='check']"
		# Insert credentials and log
		usernameID =        "j_username"
		passwordID =        "j_password"
		loginFormID =       "logon"
		# Waiting for elements to load
		wait_connection()
		print("Aspetto che il form di autenticazione si carichi...")
		authButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(authButtonXPath))
		print("Fatto! Ora premo il bottone...")
		# Button click
		wait_connection()
		authButtonElement.click()
		print("Fatto!")
		# Waiting for fields to load
		wait_connection()
		print("Aspetto il caricamento delle componenti del sito...")
		usernameElement     = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(usernameID))
		passwordElement     = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passwordID))
		loginFormElement  = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(loginFormID))
		print("Fatto! Ora riempio il form...")
		# Filling the form
		wait_connection()
		usernameElement.clear()
		usernameElement.send_keys(univeUsername)
		passwordElement.clear()
		passwordElement.send_keys(univePassword)
		print("Fatto! Eseguo il submit...")
		# Form button submission
		wait_connection()
		loginFormElement.submit()
		print("Fatto!")
		print("Aspetto trenta secondi prima del redirect...")
		time.sleep(30)
		print("Fatto!")
		wait_connection()
		#driver.get("http://static.unive.it/prenotazioni/lemieprenotazioni")
		driver.execute_script("window.location.href='http://static.unive.it/prenotazioni/lemieprenotazioni'")
		print("Vado alle mie prenotazioni...")
		# Marker for page to be loaded
		nomeutenteXPath = "//div[@class='nomeutente']"
		# Waiting for field to load
		nomeutenteElement = WebDriverWait(driver, 3600).until(lambda driver: driver.find_element_by_xpath(nomeutenteXPath))
		# Moving to /prenotazioni/lemieprenotazioni/nuova
		print("Vado alla pagina per le nuove prenotazioni...")
		wait_connection()
		driver.get("http://static.unive.it/prenotazioni/lemieprenotazioni/nuova")
		# Waiting for the page to load
		nomeutenteElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(nomeutenteXPath))
		# Time variables initialization
		x = datetime.today()
		try:
			y = x.replace(day = x.day+1, hour=0, minute = 0, second = 1, microsecond = 0)
		except ValueError:
			y = x.replace(month = x.month +1, day = 1, hour = 0, minute = 0, second = 1, microsecond = 0)
		delta_t = y-x
		secs = delta_t.seconds+1
		print("Aspetto la mezzanotte...")
		print(secs)
		time.sleep(secs)
		print("Si comincia!")
		# Moving to /prenotazioni/p/bas1bianco
		wait_connection()
		print("Prenoto prima l'acquario bianco...")
		driver.get("http://static.unive.it/prenotazioni/p/bas1bianco")
		# Waiting for the page to load
		nomeutenteElement = WebDriverWait(driver, 6).until(lambda driver: driver.find_element_by_xpath(nomeutenteXPath))

		# INIZIO PRENOTAZIONI
		# Acquario Bianco:
		for i in orari:
		    try:
		        # Moving to /prenotazioni/index/preform/giorno/2017-03-02/ora/08%3A30/etichetta/8%3A30-9%3A00 HOUR SELECTION
		        orarioXPath = "//a[@href='/prenotazioni/index/preform/giorno/"+ i + "']"
		        orarioElement = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_xpath(orarioXPath))
		        wait_connection()
		        driver.get("http://static.unive.it/prenotazioni/index/preform/giorno/"+i)
		        # Waiting for "avanti" to load
		        avantiXPath = "//input[@id='avanti']"
		        avantiElement = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_xpath(avantiXPath))
		        # Clicking element
		        wait_connection()
		        avantiElement.click()
		        print("Acquario bianco " + i + " prenotato con successo!")
		    except TimeoutException:
		        print("Acquario bianco " + i + " non prenotato!")
		    # Moving to /prenotazioni/p/bas1bianco
			wait_connection()
		    driver.get("http://static.unive.it/prenotazioni/p/bas1bianco")


		# Acquario Grande:
		print("Fatto! E ora provo a prenotare l'acquario grande...")
		driver.get("http://static.unive.it/prenotazioni/lemieprenotazioni/nuova")
		driver.get("http://static.unive.it/prenotazioni/p/basaulapt")
		for i in orari:
		    try:
		        # Moving to /prenotazioni/index/preform/giorno/2017-03-02/ora/08%3A30/etichetta/8%3A30-9%3A00 HOUR SELECTION
		        orarioXPath = "//a[@href='/prenotazioni/index/preform/giorno/"+ i + "']"
		        orarioElement = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_xpath(orarioXPath))
		        driver.get("http://static.unive.it/prenotazioni/index/preform/giorno/"+i)
		        # Waiting for "avanti" to load
		        avantiXPath = "//input[@id='avanti']"
		        avantiElement = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_xpath(avantiXPath))
		        # Clicking element
		        avantiElement.click()
		        print("Acquario grande " + i + " prenotato con successo!")
		    except TimeoutException:
		        print("Acquario grande " + i + " non prenotato!")
		    # Moving to /prenotazioni/p/bas1bianco
		    driver.get("http://static.unive.it/prenotazioni/p/basaulapt")
	
	
		# Acquario Rosso:
		print("Fatto! E ora provo a prenotare l'acquario rosso...")
		driver.get("http://static.unive.it/prenotazioni/lemieprenotazioni/nuova")
		driver.get("http://static.unive.it/prenotazioni/p/bas1rosso")
		for i in orari:
		    try:
		        # Moving to /prenotazioni/index/preform/giorno/2017-03-02/ora/08%3A30/etichetta/8%3A30-9%3A00 HOUR SELECTION
		        orarioXPath = "//a[@href='/prenotazioni/index/preform/giorno/"+ i + "']"
		        orarioElement = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_xpath(orarioXPath))
		        driver.get("http://static.unive.it/prenotazioni/index/preform/giorno/"+i)
		        # Waiting for "avanti" to load
		        avantiXPath = "//input[@id='avanti']"
		        avantiElement = WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_xpath(avantiXPath))
		        # Clicking element
		        avantiElement.click()
		        print("Acquario rosso " + i + " prenotato con successo!")
		    except TimeoutException:
		        print("Acquario rosso " + i + " non prenotato!")
		    # Moving to /prenotazioni/p/bas1bianco
		    driver.get("http://static.unive.it/prenotazioni/p/bas1rosso")

		print("Fatto! Ora chiudo tutto e va in mona!")
		driver.quit()



unicorn()
