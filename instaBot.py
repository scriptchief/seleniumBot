from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot      = webdriver.Firefox(executable_path = 'burayageckodriveruzantısı/geckodriver.exe')
		
	def login(self):
		bot = self.bot
		bot.get('https://instagram.com/accounts/login')
		time.sleep(3)
		bot.find_element_by_name('username').send_keys(self.username)
		bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
		time.sleep(3)

	def searchHashtag(self,hashtag):
		bot = self.bot

		bot.get('https://www.instagram.com/explore/tags/' + hashtag) # hashtag uzatınımız

	def likePhotos(self,amount):
		bot = self.bot
		bot.find_element_by_class_name('v1Nh3').click() # kalp iconunun koduna baktık

		i = 1
		while i <= amount:
			time.sleep(1)
			bot.find_element_by_class_name('wpO6b').click() #tıklayacağımız iconun kodunu girdik
			bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()    
			i += 1

		bot.get('https://instagram.com/'+ self.username)

insta = InstagramBot('kullanıcıadı','parola') # kullanıcı adı ve parolamızı gönderiyoruz.
insta.login() # giriş fonksiyonumuzu çağırıyoruz
insta.searchHashtag('logo') # hangi hashtag için arama yapılsın
insta.likePhotos(5) # kaç adet fotoğraf beğenilsin
