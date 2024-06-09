from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

all_names = ['Sandeepm', '999999999', 'Bot']
msg = 'Good Morning'
count = 3

input('Enter anything after scanning QR code')

for name in all_names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('input-container')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('compose-btn-send')
        button.click()
