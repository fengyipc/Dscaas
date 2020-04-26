from selenium import webdriver
from time import sleep
from datetime import datetime


url = 'http://www.xxx.com'
username = "admin"
password = "admin"

times = ["14:40-15:20",
         "14:00-14:40",
         "10:00-10:40",
         "10:40-11:20",
         "9:20-10:00",
         "11:20-12:00",
         "15:20-16:00",
         "8:40-9:20",
         "8:00-8:40",
         "16:00-16:40",
         "16:40-17:20",
         "17:20-18:00",
        ]
        
#定时器
now = str(datetime.now())
while(now[11:16] != "07:00"):
    sleep(30)
    now = str(datetime.now())

#打开浏览器
browser = webdriver.Chrome()
browser.get(url)
sleep(5)

signin_flag = False
while(not login_flag):
    try:
        #点击登录按钮
        browser.find_element_by_id('ext-gen33').click()
        sleep(1)
        #输入账号密码，并登录
        browser.find_element_by_id('tname').send_keys(username)
        browser.find_element_by_id('tpass').send_keys(password)
        browser.find_element_by_id('ext-gen63').click()
        sleep(1)
        #确认登录
        browser.find_element_by_id('ext-gen106').click()
        signin_flag = True
    except:
        browser.refresh()
    sleep(3)

order = False

while(not order):
    try:
        #展开预约管理菜单，并选择科目二预约
        browser.find_element_by_class_name('x-tree-elbow-end-plus').click()
        sleep(1)
        
        browser.find_element_by_xpath('.//span[text()="科目二预约管理"]').click()
        sleep(1)

        #选择预约日期
        browser.switch_to_frame("iframe-KM2_YY")
        browser.find_element_by_xpath('.//div[@class="x-form-field-wrap x-form-field-trigger-wrap"]/input').click()
        sleep(0.5)
        if (datetime.now().weekday() != 5):
            browser.find_element_by_xpath('.//td[@title="今天"]/following-sibling::td[1]').click()
        else:
            browser.find_element_by_xpath('.//td[@title="今天"]/../following-sibling::tr[1]/td[1]').click();
        sleep(0.5)

        #查询明天预约安排
        browser.find_element_by_id('btnCX').click()
        sleep(1)

        #如果可预订，则选择预订场次
        for time in times:
            if(browser.find_element_by_xpath('.//div[text()="'+ time +'"]/parent::td[1]/following-sibling::td[1]/div').text != '已预约'):
                browser.find_element_by_xpath('.//div[text()="'+ time +'"]/parent::td[1]/preceding-sibling::td[6]/div').click()
                print("预约时间：" + time)
                order = True
                break
    except:
        #出现错误，则刷新页面重试
        browser.refresh()
        sleep(3)
#提交预约
browser.find_element_by_id('btnSave').click()
print("预约成功时间："+str(datetime.now())[:19])
