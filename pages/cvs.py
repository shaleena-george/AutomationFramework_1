from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:/Users/Shalu/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# if (driver.findElement(By.xpath("BUTTON[@class='added-manually'][text()='Delete'])[1]".isDisplayed()):
 #   driver.findElement(By.xpath("(//button[@type='button'])[2]")).click();
  #  print(Delete button is present)
#else:
 #   print("Delete button is not there") */

element1 = driver.find_elements_by_xpath("//BUTTON[@onclick='addElement()'][text()='Add Element']")
element1.click()
element = driver.find_elements_by_xpath("(//BUTTON[@class='added-manually'][text()='Delete'])[1]")
element1.click()
element = driver.find_elements_by_xpath("(//BUTTON[@class='added-manually'][text()='Delete'])[2]")
element.close()