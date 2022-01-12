from selenium import webdriver
import time
driver = webdriver.Chrome()

# x, y だけスクロール
driver.execute_script('window.scrollTo(x, y)')

# 下に少しずつスクロール
height = 100
while height < 3000:
    driver.execute_script(f'window.scrollTo(0, {height}')
    height += 100

# 一番下までスクロール
height = driver.execute_script('return document.body.scrollHeight')
driver.execute_script(f'window.scrollTo(0, {height}')

# 繰り返し一番下までスクロール
height = driver.execute_script('return document.body.scrollHeight')
new_height = 0

while True:
    driver.execute_script(f'window.scrollTo(0, {height}')
    new_height = driver.execute_script('return document.body.scrollHeight')
    time.sleep(3)

    if height == new_height:
        break
    height = new_height

