import main_app_headers as head

head_list = head.AvitoScraperHead()
url = "https://www.avito.ru/rostovskaya_oblast/bytovaya_elektronika?cd=1&q=e-mu+1616"
url2 = "https://www.avito.ru/all/bytovaya_elektronika?q=emu+1616&s=1"
head_list.get_url(url2)
