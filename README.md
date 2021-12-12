# seleniumBot
bot with python selenium

ilk olarak python yüklediğinizi varsayarak selenium kuracağız 
komut istemi kısmını açarak yazıyoruz

- pip install selenium 








Geckodriver Dosyası indir
Mozilla firefox kullanacağımız için geckodriver indirmelisiiz.

 - https://github.com/mozilla/geckodriver/releases







 Gecko Deriver Ekleme
kodlarımızın içerisinde 9. satırda

 - webdriver.Firefox(executable_path = 'burayageckodriveruzantısı/geckodriver.exe')
 "burayageckodriveruzantısı" uzantımızı yazıyoruz
 
 
 
 
 Kullanıcı Adı Parola
 37. satırda
  - insta = InstagramBot('kullanıcıadı','parola') kısmına kullanıcı adı ve parolamızı giriyoruz.
 
 
 
 
 
 Çalıştırma
 daha sonra komut satırı üzerinden dosyanın bulunduğu uzantıya gidiyoruz 
 
  - python instaBot.py
 
 yazıyoruz
