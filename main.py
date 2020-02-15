from selenium import webdriver
from time import sleep
from random import randint

from secrets import username, password

import csv

class ReviseBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')

    def login(self):
        self.driver.get('https://smartrevise.online/')

        sleep(2)

        fb_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/a[1]')
        fb_btn.click()

        email_in = self.driver.find_element_by_xpath('//*[@id="Email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="Password"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('/html/body/div/div/div[1]/section/form/div[4]/button')
        login_btn.click()

    def course(self):
        c_btn = self.driver.find_element_by_xpath('/html/body/div/div[3]/a/div/div')
        c_btn.click()

    def checkNone(self):
        n_btn = self.driver.find_element_by_xpath('//*[@id="tf-selectnone"]')
        n_btn.click()

        update_btn = self.driver.find_element_by_xpath('//*[@id="topicfilterform"]/div/div[3]/input')
        update_btn.click()

    def checkAll(self):
        n_btn = self.driver.find_element_by_xpath('//*[@id="tf-selectall"]')
        n_btn.click()

        update_btn = self.driver.find_element_by_xpath('//*[@id="topicfilterform"]/div/div[3]/input')
        update_btn.click()

    def clickStart(self):
        s_btn = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/a')
        s_btn.click()

    def idk(self):
        idk_btn = self.driver.find_element_by_xpath('//*[@id="answercontainer"]/div[5]/a')
        idk_btn.click()

    def randomO(self):
        o = randint(1,4)

        oC_btn = self.driver.find_element_by_xpath(f'//*[@id="answercontainer"]/div[3]/a')
        oC_btn.click()

    def next(self):
        try:
            n_btn = self.driver.find_element_by_xpath('//*[@id="lnkNext"]')
            n_btn.click()

        except:
            n2_btn = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div')
            n2_btn.click()
        
    def logQ(self):
        q_elem = self.driver.find_element_by_xpath('//*[@id="questiontext"]')
        q = q_elem.text

        print(q)
        o1_elem = self.driver.find_element_by_xpath('//*[@id="answercontainer"]/div[1]/a')
        o1 = o1_elem.text
        print(o1)
        o2_elem = self.driver.find_element_by_xpath('//*[@id="answercontainer"]/div[2]/a')
        o2 = o2_elem.text
        print(o2)
        o3_elem = self.driver.find_element_by_xpath('//*[@id="answercontainer"]/div[3]/a')
        o3 = o3_elem.text
        print(o3)
        o4_elem = self.driver.find_element_by_xpath('//*[@id="answercontainer"]/div[4]/a')
        o4 = o4_elem.text
        print(o4)

        with open('answers.csv', 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            inF = False
            for row in reader:
                if q in row[0] and (o1 in row[1] or o2 in row[1] or o3 in row[1] or o4 in row[1]):
                    print("Already in file")
                    r = row
                    inF = True
                    break
                 
            if inF == True:
                if r[1] == o1:
                    o1_elem.click()
                    
                if r[1] == o2:
                    o2_elem.click()
                    
                if r[1] == o3:
                    o3_elem.click()
                    
                if r[1] == o4:
                    o4_elem.click()
            else:
                print("aaaaaa")
                
                correct = int(input("Correct Option: "))

                arr = [o1,o2,o3,o4]
                correctAnsIndex = correct-1
                correctAns = arr[correctAnsIndex]

                arrBtn = [o1_elem,o2_elem,o3_elem,o4_elem]
                arrBtn[correctAnsIndex].click()

                aC = input("Was it correct? ").upper()[0]
                if aC == "Y":
                    with open('answers.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([q, correctAns])

                else:
                    aCA = int(input("What is the correct answer? "))
                    with open('answers.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([q, arr[aCA]])
            
bot = ReviseBot()
bot.login()
bot.course()
#bot.checkAll()
bot.clickStart()

while True:
    sleep(3)
    bot.logQ()
    sleep(1)
    bot.next()
