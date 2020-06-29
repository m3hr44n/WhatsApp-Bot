#python project
#mehraan kiya
#roshanamooz
#pip install selenium
from selenium import webdriver

driver = webdriver.Chrome()


driver.get('https://web.whatsapp.com/')

names = input('Enter Names with comma (name1,name2,...) : => ')
a = names.split(',')

names = list(a)

msg = input('Enter msg : => ')

count = int (input ('how many times??? : => '))


input('Enter Anything....')

for name in names:



    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

    user.click()

    msg_box = driver.find_element_by_class_name('_3uMse ')




    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_1U1xa')
        button.click()

    

