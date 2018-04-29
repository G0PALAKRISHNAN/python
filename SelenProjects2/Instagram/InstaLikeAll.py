from time import sleep

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
driver.maximize_window()
driver.implicitly_wait(30)

login = driver.find_element_by_xpath("//button[contains(text(),'Log in with Facebook')]")
login.click()
driver.find_element_by_xpath("//input[@name='email']").send_keys("kk7030@gmail.com")
driver.find_element_by_xpath("//input[@name='pass']").send_keys("Kitty@2811")
driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()

# likes = driver.find_elements_by_xpath("//span[@class='_8scx2 coreSpriteHeartOpen']")
j=0
for j in range(10):
    i=0
    for i in range(2):
        sleep(1)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(1)
    likes = driver.find_elements_by_xpath("//span[@class='_8scx2 coreSpriteHeartOpen']")
    # link = driver.find_element_by_xpath("//span[@class='_8scx2 coreSpriteHeartOpen']/../../../..//header/div[2]/div/div/a")
    for like in likes:
        like.click()
        # print(link.text)