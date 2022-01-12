from selenium import webdriver

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
