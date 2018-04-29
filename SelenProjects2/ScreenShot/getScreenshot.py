from datetime import date, datetime
from time import sleep
from PIL import Image
from selenium import webdriver

driver = webdriver.Chrome ()
a = "http://demo.actitime.com"
driver.get (a)
driver.maximize_window ()
driver.implicitly_wait (30)

sleep (4)
ele = driver.find_element_by_id ("username")

# driver.get_screenshot_as_file("sample1.png")
driver.save_screenshot ("sample2.png")
img = Image.open ("sample2.png")

loc = ele.location
size = ele.size

left = loc["x"]
top = loc["y"]
right = loc['x'] + size["width"]
bottom = loc['y'] + size["height"]

img = img.crop ((left, top, right, bottom))
img.save ("croppedImage1.png")

text1 =": URL "
text2 = ". \nAn image has been taken screenshot as sample2.png and " \
        "is been cropped for some particular part and saved as " \
        "croppedImage1.png"
today = str(date.today())
now = str(datetime.now().time())
# print(today)
# print(now)

text = today+" - "+now+text1+a+text2+"\n"
print(today," - ",now,text1,a,text2,"/n")

# with open('test.txt','r') as f:

with open('logfile.log','a') as f:

    f.write(text)

driver.close ()
