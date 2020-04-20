from selenium import webdriver
import time
import json 

class InstaBot:
  def __init__(self, username, pw):
    self.username=username
    self.driver= webdriver.Chrome('/home/admin/code/unfollowed/chromedriver')
    self.driver.get("https://instagram.com")
    time.sleep(2)
    #self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
    self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
.send_keys(username)
    self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
.send_keys(pw)
    self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
.click()
    time.sleep(2)

    self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
  

  def get_unfollowers(self):
    self.driver.find_element_by_xpath('//a[contains(@href,"/{}")]'.format(self.username)).click()
    time.sleep(1)
    self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
    following=self._get_names()
    self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
    followers=self._get_names()
    not_following_back=[user for user in following if user not in followers]
    print(not_following_back)
  def _get_names(self):
    time.sleep(1)
    scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
    last_ht, ht=0,1
    while last_ht !=ht:
      last_ht = ht
      time.sleep(1)
      ht=self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""", scroll_box)
    links=scroll_box.find_elements_by_tag_name('a')
    names=[name.text for name in links if name.text!='']
  
    #close button
    self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]").click()
    return names


with open("credentials.json", "r") as f:
  my_dict=json.load(f)

username=my_dict["username"]
password=my_dict["pw"]

mybot=InstaBot(username, password)
mybot.get_unfollowers()


