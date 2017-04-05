import requests
from bs4 import BeautifulSoup
from urllib import request
from config import mainURL

def get_html(url):
	response = request.urlopen(url)
	html = BeautifulSoup(response, "lxml")
	
	return html

def get_wheather(html):
	currentWheather = html.find("div", {"class":"current-weather__thermometer current-weather__thermometer_type_now"}).text
	return currentWheather

def final():
	print(get_wheather(get_html(mainURL)))