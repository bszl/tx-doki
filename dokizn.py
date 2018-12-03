from selenium import webdriver
import os
import time
import random
import win32api
import sys
import string
import shutil
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import re
import tkinter as tk
from twilio.rest import Client

accountSID='AC3467e6fb91'
authToken='2a8fc060d0626eeaa73d2'
myNumber='+861576'
twilioNumber='+1154'

def textmyself(message):
    twilioCli = Client(accountSID,authToken)
    twilioCli.messages.create(body=message,from_=twilioNumber,to=myNumber)
#now_time = int(time.time())
#day_time = now_time - now_time % 86400 + time.timezone
#xxx =86400- (now_time - day_time) % 86400
#time.sleep(xxx)
tijc=time.time()
tjc=6*60
timeoutt=60
startt=time.time()
ftgs=10
xygs=8
ticom=30
dir2 = os.getenv('LOCALAPPDATA')
files= os.listdir(dir2+'\Temp')
for file in files: #遍历文件夹
     if 0 == file.find('scoped_dir'):
        shutil.rmtree(dir2+'\\Temp\\'+file)
  # get current working directory 获取当前工作目录

dir1=os.getcwd()
print(dir1)
flagjc=1



f = open(dir1 + '\canshu' + '.txt', 'r', encoding='UTF-8-sig')
line = f.readlines()
f.close()
f = open(dir1 + '\初始' + '.txt', 'r', encoding='UTF-8-sig')
chu = f.readlines()
f.close()
nn =len(chu)
ftrs=int( line[0].rstrip('\n'))
ftjg=int(line[1].rstrip('\n'))
fjyn=line[2].rstrip('\n')
tztj=line[3].rstrip('\n')
tzmd=line[4].rstrip('\n')
lids=line[5].rstrip('\n')
listd=re.split('\t',lids)
global listd
xxn=len(listd)
xx=0
timesid=[]
for i in range(0,nn):
    timesid.append(time.time()-ftjg)

tcjs=5
ectt=60
eaty=0.5
js = "window.scrollTo(0, document.body.scrollHeight)"

tiei = 1
# 设置最长的超时时间

chromedriver = "chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
option = webdriver.ChromeOptions()
option.add_argument('lang=zh_CN.UTF-8')
# 更换头部
option.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
#prefs = {"profile.managed_default_content_settings.images":2}
#option.add_experimental_option("prefs",prefs)
option.add_argument('disable-infobars')
driver = webdriver.Chrome(desired_capabilities=capa,chrome_options=option)
flagqq=1
#def checkfin(dir1):
 #   f = open(dir1 + '\发帖预备' + '.txt', 'r', encoding='UTF-8-sig')
  #  ftyb = f.readlines()
   # f.close()
#    lftyb=len(ftyb)
 #   f = open(dir1 + '\发帖号' + '.txt', 'r', encoding='UTF-8-sig')
  #  ftyb = f.readlines()
   # f.close()
   # lfth = len(ftyb)
def getnlist0(dir1):
    f = open(dir1 + '\canshu' + '.txt', 'r', encoding='UTF-8-sig')
    line = f.readlines()
    f.close()
    tzmd = line[4].rstrip('\n')
    isl=re.split('-',tzmd)
    return isl

def getnlist(dir1):
    isl = []
    f = open(dir1 + '\初始' + '.txt', 'r', encoding='UTF-8-sig')
    chu = f.readlines()
    f.close()
    f = open(dir1 + '\异常' + '.txt', 'r', encoding='UTF-8-sig')
    yc = f.readlines()
    f.close()

    for i in yc:
        ycsp = re.split('\t', i)
        ycg = int(ycsp[4])
        ysb = int(ycsp[3])
        if ysb>ycg and ycg==0:
            isl.append(ycsp[0])
    try:
        if len(isl)>0:
            textmyself(' '.join(isl))
    except:
        aixx=0
    for i,cu in enumerate(chu):
        isl.append(str(i+1))
    '''
    for i ,cu in enumerate(chu):
        sep = re.split('\t', cu)
        flagft = sep[2].rstrip('\n')
        if flagft=='1':
            isl.append(str(i+1))
    '''
    return isl

def post_one0(dir1,driver):


    WebDriverWait(driver, ectt, eaty).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_fans_new"]'))).click()

    handles = driver.window_handles
    start = time.time()
    while len(handles) < 2 and time.time() - start < ticom:
        time.sleep(eaty)
        WebDriverWait(driver, ectt, eaty).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_fans_new"]'))).click()
        handles = driver.window_handles
    driver.switch_to.window(handles[1])
    icon = WebDriverWait(driver, ectt, eaty).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="note_title"]')))
    icon.click()

    f = open(dir1 + '\doki标题' + '.txt', 'r', encoding='UTF-8-sig')
    linebt = f.readlines()
    f.close()
    tttt = linebt[random.sample(range(0, (len(linebt))), 1)[0]].rstrip('\n')
    icon.send_keys(tttt)
    icon = WebDriverWait(driver, ectt, eaty).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="note_content"]')))
    time.sleep(0.1)
    icon.click()
    icon.send_keys(tttt)
    icon = driver.find_elements_by_xpath('//*[@id="note_pub"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", icon[0])
    time.sleep(0.1)
    icon[0].click()
    f.close()

    fid = WebDriverWait(driver, ectt, eaty).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'meta_like')))
    icon = driver.find_elements_by_class_name("meta_like")
    fid = re.split('noteid=', driver.current_url)
    start = time.time()
    while len(fid) < 2 and time.time() - start < 20:
        time.sleep(eaty)
        fid = re.split('noteid=', driver.current_url)
    icon = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/span[1]')
    start = time.time()
    while len(icon) == 0 and time.time() - start < 20:
        time.sleep(eaty)
        icon = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/span[1]')
    nameccld = icon[0].text
    aa = fid[1].rstrip("\n") + '\t' + str(i) + '\t' + nameccld +'\t'+tttt+ '\t' + str(int(time.time())) + '\t0' * (
    nn + 1) + '\t' + '\n'
    nr = re.split('\t', aa)
    nr[i+4] = '90'
    fth = '\t'.join(nr)
    #####f = open(dir1 + '\发帖预备' + '.txt', 'a', encoding='UTF-8-sig')
    f = open(dir1 + '\发帖预备' + '.txt', 'r', encoding='UTF-8-sig')
    ftyb = f.readlines()
    f.close()
    listftyb=[]
    for yyy in ftyb:
        ybid = re.split('\t', yyy)
        yid = ybid[3] + '\t' + ybid[4]
        listftyb.append(yid)
    if (nameccld +'\t'+tttt) in listftyb:
        f = open(dir1 + '\删除' + '.txt', 'r', encoding='UTF-8-sig')
        linebt1 = f.readlines()
        f.close()
        linebt1[i] = linebt1[i].rstrip("\n") + '\t' + fid[1].rstrip("\n") + '\n'
        fh = open(dir1 + "\\" + '删除.txt', 'w', encoding='UTF-8')
        for lll in linebt1:
            fh.write(lll)
        fh.close()
    else:
        f = open(dir1 + '\发帖预备' + '.txt', 'a', encoding='UTF-8-sig')
        f.write('0\t'+fth)
        f.close()



        ########

    timesid[i-1]=time.time()
    flagjc = 0
    driver.close()
    driver.switch_to.window(handles[0])

    ################################################3
def post_one(dir1,driver):
    try:
        post_one0(dir1, driver)
    except:
        handles = driver.window_handles
        if len(handles) > 1:

            driver.switch_to.window(handles[1])
            driver.close()
            driver.switch_to.window(handles[0])
        else:
            driver.switch_to.window(handles[0])

def test_post0(dir1,driver):

    handles = driver.window_handles
    if len(handles) > 1:

        driver.switch_to.window(handles[1])
        driver.close()
        driver.switch_to.window(handles[0])
    else:
        driver.switch_to.window(handles[0])
    f = open(dir1 + '\发帖预备' + '.txt', 'r', encoding='UTF-8-sig')
    ftyb = f.readlines()
    f.close()
    ########################3333
    ftnew = []
    f = open(dir1 + '\异常' + '.txt', 'r', encoding='UTF-8-sig')
    yc = f.readlines()
    f.close()

    ym = ['', '']
    f = open(dir1 + '\初始' + '.txt', 'r', encoding='UTF-8-sig')
    line = f.readlines()
    f.close()
    for ik in range(1, len(line) + 1):
        linesep = re.split('\t', line[ik - 1])
        if linesep[2] == '0':
            ym.append(str(ik))
    for yyy in ftyb:
        ybid = re.split('\t', yyy)
        flagrg = ybid[0]
        ybid = ybid[1:]
        if ybid[1] in ym:
            f = open(dir1 + '\删除' + '.txt', 'r', encoding='UTF-8-sig')
            linebt1 = f.readlines()
            f.close()
            linebt1[int(ybid[1].rstrip("\n"))] = linebt1[int(ybid[1].rstrip("\n"))].rstrip(
                "\n") + '\t' + ybid[0].rstrip("\n") + '\n'
            fh = open(dir1 + "\\" + '删除.txt', 'w', encoding='UTF-8')
            for lll in linebt1:
                fh.write(lll)
            fh.close()

            try:
                aac = re.split('\t', yc[int(ybid[1].rstrip("\n")) - 1])
                aac[2] = str(int(aac[2]) + 1)
                yc[int(ybid[1].rstrip("\n")) - 1] = '\t'.join(aac)
            except:
                for inci in range(len(yc), int(ybid[1].rstrip("\n")) - 1):
                    yc.append(str(inci + 1) + '\t0' + '\t0' + '\t0' + '\t0' + '\t' + '\n')
                yc.append(str(int(ybid[1].rstrip("\n"))) + '\t0' + '\t1' + '\t0' + '\t0' + '\t' + '\n')
        else:


            if  flagrg == '1':

                try:
                    aac = re.split('\t', yc[int(ybid[1].rstrip("\n")) - 1])
                    aac[1] = str(int(aac[1]) + 1)
                    if int(aac[1]) < xygs:
                        f = open(dir1 + '\发帖存着' + '.txt', 'a', encoding='UTF-8-sig')
                        f.write(yyy[2:])
                        f.close()
                        yc[int(ybid[1].rstrip("\n")) - 1] = '\t'.join(aac)
                    elif int(aac[1]) == xygs:
                        f = open(dir1 + '\发帖存着' + '.txt', 'a', encoding='UTF-8-sig')
                        f.write(yyy[2:])
                        f.close()
                        yc[int(ybid[1].rstrip("\n")) - 1] = '\t'.join(aac)
                        ym.append(ybid[1])

                    else:
                        f = open(dir1 + '\删除' + '.txt', 'r', encoding='UTF-8-sig')
                        linebt1 = f.readlines()
                        f.close()
                        linebt1[int(ybid[1].rstrip("\n"))] = linebt1[int(ybid[1].rstrip("\n"))].rstrip(
                            "\n") + '\t' + ybid[0].rstrip("\n") + '\n'
                        fh = open(dir1 + "\\" + '删除.txt', 'w', encoding='UTF-8')
                        for lll in linebt1:
                            fh.write(lll)
                        fh.close()

                        try:
                            aac = re.split('\t', yc[int(ybid[1].rstrip("\n")) - 1])
                            aac[2] = str(int(aac[2]) + 1)
                            yc[int(ybid[1].rstrip("\n")) - 1] = '\t'.join(aac)
                        except:
                            for inci in range(len(yc), int(ybid[1].rstrip("\n")) - 1):
                                yc.append(str(inci + 1) + '\t0' + '\t0' + '\t0' + '\t0' + '\t' + '\n')
                            yc.append(str(int(ybid[1].rstrip("\n"))) + '\t0' + '\t1' + '\t0' + '\t0' + '\t' + '\n')
                except:
                    for inci in range(len(yc), int(ybid[1].rstrip("\n")) - 1):
                        yc.append(str(inci + 1) + '\t0' + '\t0' + '\t0' + '\t0' + '\t' + '\n')
                    yc.append(str(int(ybid[1].rstrip("\n"))) + '\t1' + '\t0' + '\t0' + '\t0' + '\t' + '\n')
                    f = open(dir1 + '\发帖存着' + '.txt', 'a', encoding='UTF-8-sig')
                    f.write(yyy[2:])
                    f.close()

            else:
                if time.time() - int(ybid[4]) < 48*3600:
                    #(time.time() - int(ybid[4])) % 3600 < 300 or
                    if  int(ybid[1]) == i:
                        try:
                            jss = "http://v.qq.com/doki/doki_note/detail?starid=" + listd[xx].rstrip(
                                '\n') + "&noteid=" + ybid[0].rstrip("\n")
                            jsss = 'window.open("' + jss + '")'
                            driver.execute_script(jsss)

                            handles = driver.window_handles
                            start = time.time()
                            while len(handles) < 2 and time.time() - start < ticom:
                                time.sleep(eaty)
                                ###########################
                                handles = driver.window_handles
                            driver.switch_to.window(handles[1])
                            WebDriverWait(driver, 15, eaty).until(
                                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/a/span')))
                            icon = driver.find_elements_by_xpath("/html/body/div[3]/div[3]/a[1]/span")
                            st = icon[0].text
                            if int(st.lstrip('点赞 ').lstrip('已赞 ')) > 0:
                                ftnew.append('1\t' + yyy[2:])
                            else:
                                int('')
                            handles = driver.window_handles
                            if len(handles) > 1:

                                driver.switch_to.window(handles[1])
                                driver.close()
                                driver.switch_to.window(handles[0])
                            else:
                                driver.switch_to.window(handles[0])
                        except:
                            handles = driver.window_handles
                            if len(handles) > 1:

                                driver.switch_to.window(handles[1])
                                driver.close()
                                driver.switch_to.window(handles[0])
                            else:
                                driver.switch_to.window(handles[0])

                            ftnew.append(yyy)
                    else:
                        ftnew.append(yyy)
                else:
                    try:
                        jss = "http://v.qq.com/doki/doki_note/detail?starid=" + listd[xx].rstrip(
                            '\n') + "&noteid=" + ybid[0].rstrip("\n")
                        jsss = 'window.open("' + jss + '")'
                        driver.execute_script(jsss)

                        handles = driver.window_handles
                        start = time.time()
                        while len(handles) < 2 and time.time() - start < ticom:
                            time.sleep(eaty)
                            ###########################
                            handles = driver.window_handles
                        driver.switch_to.window(handles[1])
                        WebDriverWait(driver, 15, eaty).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/a/span')))
                        icon = driver.find_elements_by_xpath("/html/body/div[3]/div[3]/a[1]/span")
                        st = icon[0].text
                        if int(st.lstrip('点赞 ').lstrip('已赞 ')) > 0:
                            ftnew.append('1\t' + yyy[2:])
                        else:
                            int('')
                        handles = driver.window_handles
                        if len(handles) > 1:

                            driver.switch_to.window(handles[1])
                            driver.close()
                            driver.switch_to.window(handles[0])
                        else:
                            driver.switch_to.window(handles[0])
                    except:

                        f = open(dir1 + '\删除' + '.txt', 'r', encoding='UTF-8-sig')
                        linebt1 = f.readlines()
                        f.close()
                        linebt1[int(ybid[1].rstrip("\n"))] = linebt1[int(ybid[1].rstrip("\n"))].rstrip(
                            "\n") + '\t' + ybid[0].rstrip("\n") + '\n'
                        fh = open(dir1 + "\\" + '删除.txt', 'w', encoding='UTF-8')
                        for lll in linebt1:
                            fh.write(lll)
                        fh.close()

                        try:
                            aac = re.split('\t', yc[int(ybid[1].rstrip("\n")) - 1])
                            aac[2] = str(int(aac[2]) + 1)
                            yc[int(ybid[1].rstrip("\n")) - 1] = '\t'.join(aac)
                        except:
                            for inci in range(len(yc), int(ybid[1].rstrip("\n")) - 1):
                                yc.append(str(inci + 1) + '\t0' + '\t0' + '\t0' + '\t0' + '\t' + '\n')
                            yc.append(str(int(ybid[1].rstrip("\n"))) + '\t0' + '\t1' + '\t0' + '\t0' + '\t' + '\n')
                        handles = driver.window_handles
                        if len(handles) > 1:

                            driver.switch_to.window(handles[1])
                            driver.close()
                            driver.switch_to.window(handles[0])
                        else:
                            driver.switch_to.window(handles[0])

        fh = open(dir1 + "\\" + '发帖预备.txt', 'w', encoding='UTF-8')
        for lll in ftnew:
            fh.write(lll)
        fh.close()
        fh = open(dir1 + "\\" + '异常.txt', 'w', encoding='UTF-8')
        for lll in yc:
            fh.write(lll.rstrip("\n") + '\n')
        fh.close()

    #########################33333
    '''
    if len(ftyb)>0:

        try:

            stri = "window.open('http://v.qq.com/doki/star?id=" + listd[0].rstrip('\n') + "&tabid=3');"
            driver.execute_script(stri)
            handles = driver.window_handles
            start = time.time()
            while len(handles) < 2 and time.time() - start < ticom:
                time.sleep(eaty)
                driver.execute_script(js)
                handles = driver.window_handles
            driver.switch_to.window(handles[1])
            icon1 = driver.find_elements_by_class_name("post_title")

            start=time.time()
            js11 = "window.scrollTo(0, document.body.scrollHeight)"
            while 50>len(icon1):
                time.sleep(0.5)
                driver.execute_script(js11)
                icon1 = driver.find_elements_by_class_name("post_title")
                if time.time() - start > 20:
                    break
            wyid=['','']
            icon2 = driver.find_elements_by_class_name('post_title')
            icon1 = driver.find_elements_by_class_name('meta_author')
            icon3 = driver.find_elements_by_class_name('meta_like')
            for icc in range(0,len(icon1)-2):

                tt=icon1[icc+2].text
                tt2 = icon2[icc + 2].text
                wyid.append(tt+'\t'+tt2)




            ftnew=[]
            f = open(dir1 + '\异常' + '.txt', 'r', encoding='UTF-8-sig')
            yc = f.readlines()
            f.close()

            ym=['','']
            f = open(dir1 + '\初始' + '.txt', 'r', encoding='UTF-8-sig')
            line = f.readlines()
            f.close()
            for ik in range(1, len(line) + 1):
                linesep = re.split('\t', line[ik - 1])
                if linesep[2]=='0':
                    ym.append(str(ik))

            for yyy in ftyb:
                ybid = re.split('\t', yyy)
                flagrg=ybid[0]
                ybid = ybid[1:]
                if ybid[1] in ym:
                    f = open(dir1 + '\删除' + '.txt', 'r', encoding='UTF-8-sig')
                    linebt1 = f.readlines()
                    f.close()
                    linebt1[int(ybid[1].rstrip("\n"))] = linebt1[int(ybid[1].rstrip("\n"))].rstrip(
                        "\n") + '\t' + ybid[0].rstrip("\n") + '\n'
                    fh = open(dir1 + "\\" + '删除.txt', 'w', encoding='UTF-8')
                    for lll in linebt1:
                        fh.write(lll)
                    fh.close()

                    try:
                        aac = re.split('\t', yc[int(ybid[1].rstrip("\n")) - 1])
                        aac[2] = str(int(aac[2]) + 1)
                        yc[int(ybid[1].rstrip("\n")) - 1] = '\t'.join(aac)
                    except:
                        for inci in range(len(yc), int(ybid[1].rstrip("\n")) - 1):
                            yc.append(str(inci + 1) + '\t0' + '\t0' + '\t0' + '\t0' + '\t' + '\n')
                        yc.append(str(int(ybid[1].rstrip("\n"))) + '\t0' + '\t1' + '\t0' + '\t0' + '\t' + '\n')
                else:
                    yid = ybid[2]+'\t'+ybid[3]

                    if yid in wyid or flagrg=='1':
                        try:
                            xxxxxx=wyid.index(yid)
                            driver.execute_script("arguments[0].scrollIntoView(true);", icon3[xxxxxx])
                            driver.execute_script('window.scrollBy(0,-400)')
                            icon3[xxxxxx].click()
                        except:
                            asw = 1
                        try:
                            aac = re.split('\t', yc[int(ybid[1].rstrip("\n")) - 1])
                            aac[1] = str(int(aac[1]) + 1)
                            if int(aac[1]) < xygs:
                                f = open(dir1 + '\发帖存着' + '.txt', 'a', encoding='UTF-8-sig')
                                f.write(yyy[2:])
                                f.close()
                                yc[int(ybid[1].rstrip("\n")) - 1] = '\t'.join(aac)
                            elif int(aac[1]) == xygs:
                                f = open(dir1 + '\发帖存着' + '.txt', 'a', encoding='UTF-8-sig')
                                f.write(yyy[2:])
                                f.close()
                                yc[int(ybid[1].rstrip("\n")) - 1] = '\t'.join(aac)
                                ym.append(ybid[1])

                            else:
                                f = open(dir1 + '\删除' + '.txt', 'r', encoding='UTF-8-sig')
                                linebt1 = f.readlines()
                                f.close()
                                linebt1[int(ybid[1].rstrip("\n"))] = linebt1[int(ybid[1].rstrip("\n"))].rstrip(
                                    "\n") + '\t' + ybid[0].rstrip("\n") + '\n'
                                fh = open(dir1 + "\\" + '删除.txt', 'w', encoding='UTF-8')
                                for lll in linebt1:
                                    fh.write(lll)
                                fh.close()

                                try:
                                    aac = re.split('\t', yc[int(ybid[1].rstrip("\n")) - 1])
                                    aac[2] = str(int(aac[2]) + 1)
                                    yc[int(ybid[1].rstrip("\n")) - 1] = '\t'.join(aac)
                                except:
                                    for inci in range(len(yc), int(ybid[1].rstrip("\n")) - 1):
                                        yc.append(str(inci + 1) + '\t0' + '\t0' + '\t0' + '\t0' + '\t' + '\n')
                                    yc.append(str(int(ybid[1].rstrip("\n"))) + '\t0' + '\t1' + '\t0' + '\t0' + '\t' + '\n')
                        except:
                            for inci in range(len(yc), int(ybid[1].rstrip("\n")) - 1):
                                yc.append(str(inci + 1) + '\t0' + '\t0' + '\t0'+ '\t0' + '\t' + '\n')
                            yc.append(str(int(ybid[1].rstrip("\n"))) + '\t1' + '\t0'+ '\t0'+ '\t0'  + '\t' + '\n')
                            f = open(dir1 + '\发帖存着' + '.txt', 'a', encoding='UTF-8-sig')
                            f.write(yyy[2:])
                            f.close()

                    else:
                        if time.time()-int(ybid[4])<38800:
                            if (time.time() - int(ybid[4]))%3600 < 300 or int(ybid[1])==i:
                                try:
                                    jss = "http://v.qq.com/doki/doki_note/detail?starid=" + listd[xx].rstrip(
                                        '\n') + "&noteid=" + ybid[0].rstrip("\n")
                                    jsss = 'window.open("' + jss + '")'
                                    driver.execute_script(jsss)

                                    handles = driver.window_handles
                                    start = time.time()
                                    while len(handles) < 3 and time.time() - start < ticom:
                                        time.sleep(eaty)
                                        ###########################
                                        handles = driver.window_handles
                                    driver.switch_to.window(handles[2])
                                    WebDriverWait(driver, 15, eaty).until(
                                        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/a/span')))
                                    icon = driver.find_elements_by_xpath("/html/body/div[3]/div[3]/a[1]/span")
                                    st = icon[0].text
                                    if int(st.lstrip('点赞 ').lstrip('已赞 ')) > 0:
                                        ftnew.append('1\t' + yyy[2:])
                                    else:
                                        int('')
                                    handles = driver.window_handles
                                    if len(handles) > 2:

                                        driver.switch_to.window(handles[2])
                                        driver.close()
                                        driver.switch_to.window(handles[1])
                                    else:
                                        driver.switch_to.window(handles[1])
                                except:
                                    handles = driver.window_handles
                                    if len(handles) > 2:

                                        driver.switch_to.window(handles[2])
                                        driver.close()
                                        driver.switch_to.window(handles[1])
                                    else:
                                        driver.switch_to.window(handles[1])

                                    ftnew.append(yyy)
                            else :
                                ftnew.append(yyy)
                        else:
                            try:
                                jss = "http://v.qq.com/doki/doki_note/detail?starid=" + listd[xx].rstrip(
                                    '\n') + "&noteid=" + ybid[0].rstrip("\n")
                                jsss = 'window.open("' + jss + '")'
                                driver.execute_script(jsss)

                                handles = driver.window_handles
                                start = time.time()
                                while len(handles) < 3 and time.time() - start < ticom:
                                    time.sleep(eaty)
                                    ###########################
                                    handles = driver.window_handles
                                driver.switch_to.window(handles[2])
                                WebDriverWait(driver, 15, eaty).until(
                                    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/a/span')))
                                icon = driver.find_elements_by_xpath("/html/body/div[3]/div[3]/a[1]/span")
                                st = icon[0].text
                                if int(st.lstrip('点赞 ').lstrip('已赞 '))>0:
                                    ftnew.append('1\t'+yyy[2:])
                                else:
                                    int('')
                                handles = driver.window_handles
                                if len(handles) > 2:

                                    driver.switch_to.window(handles[2])
                                    driver.close()
                                    driver.switch_to.window(handles[1])
                                else:
                                    driver.switch_to.window(handles[1])
                            except:

                                f = open(dir1 + '\删除' + '.txt', 'r', encoding='UTF-8-sig')
                                linebt1 = f.readlines()
                                f.close()
                                linebt1[int(ybid[1].rstrip("\n"))] = linebt1[int(ybid[1].rstrip("\n"))].rstrip(
                                    "\n") + '\t' + ybid[0].rstrip("\n") + '\n'
                                fh = open(dir1 + "\\" + '删除.txt', 'w', encoding='UTF-8')
                                for lll in linebt1:
                                    fh.write(lll)
                                fh.close()

                                try:
                                    aac = re.split('\t', yc[int(ybid[1].rstrip("\n")) - 1])
                                    aac[2] = str(int(aac[2]) + 1)
                                    yc[int(ybid[1].rstrip("\n")) - 1] = '\t'.join(aac)
                                except:
                                    for inci in range(len(yc), int(ybid[1].rstrip("\n")) - 1):
                                        yc.append(str(inci + 1) + '\t0' + '\t0'+ '\t0'+ '\t0'   + '\t' + '\n')
                                    yc.append(str(int(ybid[1].rstrip("\n"))) + '\t0' + '\t1' + '\t0'+ '\t0' + '\t' + '\n')
                                handles = driver.window_handles
                                if len(handles) > 2:

                                    driver.switch_to.window(handles[2])
                                    driver.close()
                                    driver.switch_to.window(handles[1])
                                else:
                                    driver.switch_to.window(handles[1])

            fh = open(dir1 + "\\" + '发帖预备.txt', 'w', encoding='UTF-8')
            for lll in ftnew:
                fh.write(lll)
            fh.close()
            fh = open(dir1 + "\\" + '异常.txt', 'w', encoding='UTF-8')
            for lll in yc:
                fh.write(lll.rstrip("\n") + '\n')
            fh.close()

            handles = driver.window_handles
            if len(handles) > 1:

                driver.switch_to.window(handles[1])
                driver.close()
                driver.switch_to.window(handles[0])
            else:
                driver.switch_to.window(handles[0])
        except:

            handles = driver.window_handles
            if len(handles) > 1:

                driver.switch_to.window(handles[1])
                driver.close()
                driver.switch_to.window(handles[0])
            else:
                driver.switch_to.window(handles[0])
    '''
    return time.time()
def test_post(dir1,driver):
    try:
        test_post0(dir1, driver)
    except:
        handles = driver.window_handles
        if len(handles) > 1:

            driver.switch_to.window(handles[1])
            driver.close()
            driver.switch_to.window(handles[0])
        else:
            driver.switch_to.window(handles[0])

def qiandao(dir1,driver,line,i):
    qngd=['16']
    linesep = re.split('\t', line[i - 1])
    flagqd = linesep[3].rstrip('\n')
    f = open(dir1 + '\初始' + '.txt', 'r', encoding='UTF-8-sig')
    line = f.readlines()
    f.close()

    linesep[4]=linesep[4].rstrip('\n')
    if flagqd != '0':
        for iii,iix in enumerate(qngd):
            handles = driver.window_handles
            if len(handles) > 1:

                driver.switch_to.window(handles[1])
                driver.close()
                driver.switch_to.window(handles[0])
            else:
                driver.switch_to.window(handles[0])

            stri="window.open('http://v.qq.com/doki/star?id="+iix+"');"
            driver.execute_script(stri)
            handles = driver.window_handles
            start = time.time()
            while len(handles) < 2 and time.time() - start < ticom:
                time.sleep(eaty)
                driver.execute_script(js)
                handles = driver.window_handles
            driver.switch_to.window(handles[1])
            try:
                ic = driver.find_elements_by_class_name('mod_btn')
                if ic[3].text == '签到':
                    ic[3].click()
                    try:
                        ic = driver.find_elements_by_class_name('mod_btn')
                        if ic[11].text == '关注':
                            ic[11].click()
                    except:
                        asw = 1
                try:
                    nuu=ic[2].text.lstrip('打榜 x')
                    if nuu != '':
                        linesep[iii+5]=nuu
                except:
                     asw = 1
            except:
                asw = 1
            driver.close()
            driver.switch_to.window(handles[0])


        linesep[3] = str(int(linesep[3]) )
        line[i - 1] = '\t'.join(linesep)
        fh = open(dir1 + "\\" + '初始.txt', 'w', encoding='UTF-8')
        for lll in line:
            fh.write(lll)
        fh.close()



def cxcsh(dir1):
    f = open(dir1 + '\初始' + '.txt', 'r', encoding='UTF-8-sig')
    line = f.readlines()
    f.close()
    f = open(dir1 + '\异常' + '.txt', 'r', encoding='UTF-8-sig')
    yc = f.readlines()
    f.close()
    for i in range(1,len(yc)+1):
        if  int(re.split('\t',yc[i-1])[1])>= xygs:
            linesep = re.split('\t', line[i - 1])
            linesep[2]='0'
            line[i-1] = '\t'.join(linesep)
    fh = open(dir1 + "\\" + '初始.txt', 'w', encoding='UTF-8')
    for lll in line:
        fh.write(lll)
    fh.close()
    return line

def checkday(dir1,driver):
    flagff=False
    f = open(dir1 + '\发帖号' + '.txt', 'r', encoding='UTF-8-sig')
    ftyb = f.readlines()
    f.close()
    f = open(dir1 + '\发帖存着' + '.txt', 'r', encoding='UTF-8-sig')
    lhee = f.readlines()
    f.close()
    if len(ftyb) == 0 and len(lhee)>= (ftrs)*8:
        f = open(dir1 + '\初始' + '.txt', 'r', encoding='UTF-8-sig')
        lhee = f.readlines()
        f.close()
        fh = open(dir1 + "\\" + '初始结束.txt', 'w', encoding='UTF-8')
        for llel in lhee:
            fh.write(llel.rstrip("\n") + '\n')
        fh.close()
        f = open(dir1 + '\初始0' + '.txt', 'r', encoding='UTF-8-sig')
        lhee = f.readlines()
        f.close()
        fh = open(dir1 + "\\" + '初始.txt', 'w', encoding='UTF-8')
        for llel in lhee:
            fh.write(llel.rstrip("\n") + '\n')
        fh.close()
        f = open(dir1 + '\异常' + '.txt', 'r', encoding='UTF-8-sig')
        lhee = f.readlines()
        f.close()
        fh = open(dir1 + "\\" + '异常上轮.txt', 'w', encoding='UTF-8')
        for llel in lhee:
            fh.write(llel.rstrip("\n") + '\n')
        fh.close()
        fh = open(dir1 + "\\" + '异常.txt', 'w', encoding='UTF-8')
        fh.close()
        f = open(dir1 + '\发帖存着' + '.txt', 'r', encoding='UTF-8-sig')
        lhee = f.readlines()
        f.close()
        fh = open(dir1 + "\\" + '发帖号.txt', 'w', encoding='UTF-8')
        for llel in lhee:
            fh.write(llel.rstrip("\n") + '\n')
        fh.close()
        fh = open(dir1 + "\\" + '发帖存着.txt', 'w', encoding='UTF-8')
        fh.close()
        f = open(dir1 + '\canshu' + '.txt', 'r', encoding='UTF-8-sig')
        line = f.readlines()
        f.close()
        line[4] = '-'.join(list(map(str, isl[iis:]))) + '\n'
        print(line[4])
        f = open(dir1 + '\canshu' + '.txt', 'w', encoding='UTF-8-sig')
        for l in line:
            f.write(l)
        f.close()
        flagff=True
    f = open(dir1 + '\canshu' + '.txt', 'r', encoding='UTF-8-sig')
    line = f.readlines()
    f.close()
    tztj = line[3].rstrip('\n')
    if tztj == '写完换人':
        if flagff:
            driver.quit()
            time.sleep(2)
            stri=dir1+fjyn

            win32api.ShellExecute(0, 'open',r''+stri, '', '', 1)

            os._exit(0)
    else:

        shijian=re.split('-',tztj)
        timeline=int(shijian[0])*3600+int(shijian[1])*60+int(shijian[2])
        now_time = int(time.time())
        day_time = now_time - now_time % 86400 + time.timezone
        xxx=(now_time - day_time)% 86400
        if  xxx > timeline:
            driver.quit()
            time.sleep(2)
            stri = dir1.rstrip('\\lwj') + fjyn

            os.chdir(dir1.rstrip('\\lwj'))
            win32api.ShellExecute(0, 'open', r''+stri, '', '', 1)

            os._exit(0)

    return flagff


def butombox(driver,passnum):
    global startt
    startt = time.time()
    global timeoutt
    timeoutt = 120000
    window = tk.Tk()
    window.title('my window')
    window.geometry('200x300''+1200+200')
    window.attributes("-topmost", 1)
    global iiiii
    iiiii = 0
    window.after(timeoutt, window.destroy)
    global on_hit2
    global on_hit3

    on_hit2 = False
    on_hit3 = False

    def hit_mecg():
        global iiiii
        global on_hit2
        if on_hit2 == False:  # 从 False 状态变成 True 状态
            on_hit2 = True
            iiiii = 1
            window.destroy()

    b2 = tk.Button(window, text='成功', width=15, height=2, command=hit_mecg)
    b2.pack()

    def hit_mefq():
        global iiiii
        global on_hit3
        if on_hit3 == False:  # 从 False 状态变成 True 状态

            try:
                iframe = WebDriverWait(driver, 5, 0.5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="_login_frame_quick_"]')))
                print('1')
                driver.switch_to.frame(iframe)
                print('2')
                icon1 = driver.find_elements_by_class_name("inputstyle")
                print(str(len(icon1)))
                icon1[1].send_keys('\b'*20+passnum)
                print('3')
                driver.switch_to.parent_frame()
                driver.switch_to.parent_frame()
                print('4')
            except:
                aixxi=1

    b3 = tk.Button(window, text='输入密码', width=15, height=2, command=hit_mefq)
    b3.pack()

    window.mainloop()
    return iiiii

def quchong(dir1):
    f = open(dir1 + '\发帖号' + '.txt', 'r', encoding='UTF-8-sig')
    lhee = f.readlines()
    f.close()
    fh = open(dir1 + "\\" + '发帖号.txt', 'w', encoding='UTF-8')
    for llel in lhee:
        nr = re.split('\t', llel)
        nnn=len(nr)-6
        aaa=nr[:5]
        for xil in range(1,nnn):
            if nr[xil+4] in (nr[5:xil+4]+nr[(xil+5):]):
                aaa.append('0')
            else:
                aaa.append(nr[xil+4])
        aaa.append('0')

        fh.write(('\t'.join(aaa)) + '\t\n')
    fh.close()
isl=getnlist0(dir1)

while(1):
    for xx in range(0,1):

        for iis, iss in enumerate(isl):
            i=int(iss)
            line=cxcsh(dir1)
            try:

                sf=checkday(dir1,driver)
                if sf:
                    break
                cc=0
                f = open(dir1 + '\发帖号' + '.txt', 'r', encoding='UTF-8-sig')
                lh = f.readlines()
                f.close()
                f = open(dir1 + '\删除' + '.txt', 'r', encoding='UTF-8-sig')
                lhsc = f.readlines()
                f.close()
                ftcount=0
                lhh=[]
                for hhh in lh:
                    try:
                        nr=re.split('\t',hhh)
                        if nr[i+4]== '0':
                            ftcount=ftcount+1
                        lhh.append(hhh.rstrip('\n') + '\n')
                    except:
                        ftcount=ftcount+1
                        lhh.append(hhh.rstrip('\n')+'0\t'+'\n')

                fh = open(dir1 + "\\" + '发帖号.txt', 'w', encoding='UTF-8')
                for lll in lhh:
                    fh.write(lll.rstrip("\n") + '\n')
                fh.close()
                linesep = re.split('\t', line[i - 1])
                flagft = linesep[2].rstrip('\n')
                if ftcount< 1:

                    #or lhsc[i] != '\n'
                    if flagft =='1' :
                        aixx=1
                    else:
                        continue


                flagyc=0
                linesep=re.split('\t',line[i-1])
                timeStamp = int(time.time())
                timeArray = time.localtime(timeStamp)
                otherStyleTime = time.strftime("%H:%M:%S", timeArray)
                print(str(i) + '\t' + otherStyleTime + '\t' + line[i - 1].rstrip('\n'))
                qqpe = linesep[0].rstrip('\n')
                passnum = linesep[1].rstrip('\n')
                flagft = linesep[2].rstrip('\n')

                tiei = 1
                # 设置最长的超时时间

                driver.set_page_load_timeout(60)
                if flagqq==1:
                    driver.get('http://v.qq.com/doki/star?id=' + listd[xx].rstrip('\n') + '&tabid=3')
                driver.maximize_window()

                start = time.time()
                flagtcg=0
                while  time.time() - start < 65:
                    try:
                        handles = driver.window_handles
                        if len(handles) > 1:

                            driver.switch_to.window(handles[1])
                            driver.close()
                            driver.switch_to.window(handles[0])
                        else:
                            driver.switch_to.window(handles[0])
                        icon1 = WebDriverWait(driver, 10, eaty).until(
                            EC.element_to_be_clickable((By.ID, "mod_head_notice_trigger")))
                        ActionChains(driver).move_to_element(icon1).perform()
                        WebDriverWait(driver, 3, eaty).until(
                            EC.element_to_be_clickable(
                                (By.XPATH, '//*[@id="mod_head_notice_pop"]/div/div/div/div[1]/a[4]'))).click()
                    except:
                        tiii=1


                    try:
                        WebDriverWait(driver, 0.7, eaty).until(
                            EC.element_to_be_clickable((By.ID, "mod_head_notice_trigger"))).click()
                    except:
                        time.sleep(0.1)
                    try:
                        WebDriverWait(driver, 1, eaty).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, "btn_qq"))).click()
                    except:
                        time.sleep(0.1)
                    try:
                        iframe=WebDriverWait(driver, 0.7, 0.5).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="_login_frame_quick_"]')))

                        driver.switch_to.frame(iframe)
                        try:
                            iframe = WebDriverWait(driver, 0.7, 0.5).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="ptlogin_iframe"]')))

                            driver.switch_to.frame(iframe)
                        except:
                            time.sleep(0.1)
                        try:
                            WebDriverWait(driver, 1, eaty).until(
                                EC.element_to_be_clickable((By.XPATH, '//*[@id="switcher_plogin"]'))).click()
                        except:
                            time.sleep(0.1)
                        WebDriverWait(driver, 1, eaty).until(EC.presence_of_element_located((By.CLASS_NAME, "inputstyle")))
                        icon1 = driver.find_elements_by_class_name("inputstyle")
                        icon1[0].send_keys('\b' * 14 + qqpe)
                        time.sleep(0.5)
                        icon1[1].send_keys(passnum)
                        time.sleep(0.5)
                        WebDriverWait(driver, ectt, eaty).until(EC.element_to_be_clickable((By.ID,"login_button"))).click()
                        time.sleep(0.5)
                        flagtcg=1
                        break
                    except:
                        time.sleep(0.1)
                        driver.switch_to.parent_frame()
                        driver.switch_to.parent_frame()
                if flagtcg==0:
                    int('')
                driver.switch_to.parent_frame()
                driver.switch_to.parent_frame()
                iframe = driver.find_elements_by_xpath('//*[@id="_login_frame_quick_"]')
                start=time.time()
                while len(iframe) >0 and time.time() - start < 17:
                    time.sleep(eaty)
                    iframe = driver.find_elements_by_xpath('//*[@id="_login_frame_quick_"]')
                    if time.time() - start >15:

                        flagyc=1
                        break

                if flagyc==1:
                    chec = butombox(driver,passnum)
                    driver.switch_to.parent_frame()
                    driver.switch_to.parent_frame()
                    if chec != 1:
                        print('异常1+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

                        WebDriverWait(driver, ectt, eaty).until(
                            EC.element_to_be_clickable((By.ID, "login_close"))).click()



                        f = open(dir1 + '\异常' + '.txt', 'r', encoding='UTF-8-sig')
                        yc = f.readlines()
                        f.close()
                        try:
                            aac = re.split('\t', yc[i - 1])
                            aac[3] = str(int(aac[3]) + 1)
                            yc[i - 1] = '\t'.join(aac)
                        except:
                            for inci in range(len(yc), i - 1):
                                yc.append(str(inci + 1) + '\t0' + '\t0' + '\t0'+ '\t0' + '\t' + '\n')
                            yc.append(str(i) + '\t0' + '\t0' + '\t1'+ '\t0' + '\t' + '\n')
                        fh = open(dir1 + "\\" + '异常.txt', 'w', encoding='UTF-8')
                        for lll in yc:
                            fh.write(lll.rstrip("\n") + '\n')
                        fh.close()


                        continue
                    else:
                        f = open(dir1 + '\异常' + '.txt', 'r', encoding='UTF-8-sig')
                        yc = f.readlines()
                        f.close()
                        try:
                            aac = re.split('\t', yc[i - 1])
                            aac[4] = str(int(aac[4]) + 1)
                            yc[i - 1] = '\t'.join(aac)
                        except:
                            for inci in range(len(yc), i - 1):
                                yc.append(str(inci + 1) + '\t0' + '\t0' + '\t0' + '\t0' + '\t' + '\n')
                            yc.append(str(i) + '\t0' + '\t0' + '\t0' + '\t1' + '\t' + '\n')
                        fh = open(dir1 + "\\" + '异常.txt', 'w', encoding='UTF-8')
                        for lll in yc:
                            fh.write(lll.rstrip("\n") + '\n')
                        fh.close()


                else:
                    f = open(dir1 + '\异常' + '.txt', 'r', encoding='UTF-8-sig')
                    yc = f.readlines()
                    f.close()
                    try:
                        aac = re.split('\t', yc[i - 1])
                        aac[4] = str(int(aac[4]) + 1)
                        yc[i - 1] = '\t'.join(aac)
                    except:
                        for inci in range(len(yc), i - 1):
                            yc.append(str(inci + 1) + '\t0' + '\t0' + '\t0' + '\t0' + '\t' + '\n')
                        yc.append(str(i) + '\t0' + '\t0' + '\t0' + '\t1' + '\t' + '\n')
                    fh = open(dir1 + "\\" + '异常.txt', 'w', encoding='UTF-8')
                    for lll in yc:
                        fh.write(lll.rstrip("\n") + '\n')
                    fh.close()



                #'''
                tijc = test_post(dir1, driver)
                tijc = test_post(dir1, driver)
                #####################################自动发帖
                f = open(dir1 + '\异常' + '.txt', 'r', encoding='UTF-8-sig')
                yc = f.readlines()
                f.close()

                aac = re.split('\t', yc[i - 1])



                if int(time.time() - timesid[i - 1]) > ftjg and flagft == '1' and cc<xygs-int(aac[1]):
                    post_one(dir1, driver)
                    cc=1


                lhn = []
                fstart=time.time()
                f = open(dir1 + '\发帖号' + '.txt', 'r', encoding='UTF-8-sig')
                lh = f.readlines()
                f.close()
                for hhh in lh:
                    if int(time.time() - timesid[i - 1]) > ftjg and flagft == '1'and cc<xygs-int(aac[1]):
                        post_one(dir1, driver)
                        cc=cc+1
                    #if int(time.time() - tijc) > tjc:
                     #   tijc=test_post(dir1, driver)
                    try:
                        nr=re.split('\t',hhh)
                        #if nr.count('1')==nn:

                         #   continue
                        if nr[i+4]!='0':
                            lhn.append(hhh)
                            continue
                        lhn.append(hhh)
                        jss="http://v.qq.com/doki/doki_note/detail?starid="+ listd[xx].rstrip('\n')+"&noteid="+nr[0].rstrip("\n")
                        jsss='window.open("'+jss+'")'
                        driver.execute_script(jsss)

                        handles = driver.window_handles
                        start = time.time()
                        while len(handles) < 2 and time.time() - start < ticom:
                            time.sleep(eaty)
                            ###########################
                            handles = driver.window_handles
                        driver.switch_to.window(handles[1])

                        icon=driver.find_elements_by_xpath( '/html/body/div[3]/div/div')
                        if 0 < len(icon):
                            st= icon[0].text
                            if 0 <= st.find('帖子已删除'):
                                ##http://v.qq.com/bk/biu/doki_note/detail.html

                                del lhn[-1]
                                driver.close()
                                driver.switch_to.window(handles[0])
                                continue
                        if 1>0:
                        #random.sample(string.digits, 1)[0] > '4'

                            icon = driver.find_elements_by_xpath("/html/body/div[3]/div[3]/a[1]/span")
                            st=icon[0].text
                            if 0 <= st.find('已赞'):
                                del lhn[-1]
                                nr[i+4] = st.lstrip('已赞 ')
                                lhn.append('\t'.join(nr))
                            if 0<=st.find('点赞'):

                                icon = driver.find_elements_by_class_name("meta_like")
                                icon[0].click()

                                del lhn[-1]
                                nr[i+4] = st.lstrip('点赞 ')
                                lhn.append('\t'.join(nr))
                            if random.randint(1,5)>1 :
                                icon =driver.find_elements_by_class_name("comment_textarea")
                                driver.execute_script("arguments[0].scrollIntoView(true);", icon[0])
                                driver.execute_script('window.scrollBy(0,-400)')

                                ActionChains(driver).move_to_element_with_offset(icon[0], 50, 50)
                                icon[0].click()
                                f = open(dir1 + '\doki内容' + '.txt', 'r', encoding='UTF-8-sig')
                                linebt = f.readlines()
                                f.close()
                                salt = linebt[random.sample(range(0, (len(linebt))), 1)[0]].rstrip('\n')
                                icon[0].send_keys(salt)
                                start = time.time()
                                while  time.time() - start < 10:
                                    try:
                                        WebDriverWait(driver, 1, eaty).until(
                                            EC.element_to_be_clickable((By.CLASS_NAME, "btn_submit"))).click()

                                        break
                                    except:
                                        ActionChains(driver).move_to_element_with_offset(icon[0], 50, 50)
                                        icon[0].click()
                                        time.sleep(0.3)
                                        icon[0].send_keys(salt)

                        else:

                            icon = driver.find_elements_by_xpath("/html/body/div[3]/div[3]/a[1]/span")
                            st = icon[0].text
                            if 0 <= st.find('已赞'):
                                del lhn[-1]
                                nr[i + 4] = '1'
                                lhn.append('\t'.join(nr))
                            if 0 <= st.find('点赞'):
                                icon = driver.find_elements_by_class_name("meta_like")
                                icon[0].click()
                                del lhn[-1]
                                nr[i + 4] = '1'
                                lhn.append('\t'.join(nr))
                                time.sleep(0.5)
                            if random.randint(1,5)>6 :
                                icon = driver.find_elements_by_class_name("comment_textarea")
                                driver.execute_script("arguments[0].scrollIntoView(true);", icon[0])
                                driver.execute_script('window.scrollBy(0,-400)')

                                ActionChains(driver).move_to_element_with_offset(icon[0], 50, 50)
                                icon[0].click()
                                f = open(dir1 + '\doki内容' + '.txt', 'r', encoding='UTF-8-sig')
                                linebt = f.readlines()
                                f.close()
                                salt = linebt[random.sample(range(0, (len(linebt))), 1)[0]].rstrip('\n')
                                icon[0].send_keys(salt)
                                start = time.time()
                                while time.time() - start < 10:
                                    try:
                                        WebDriverWait(driver, 1, eaty).until(
                                            EC.element_to_be_clickable((By.CLASS_NAME, "btn_submit"))).click()

                                        break
                                    except:
                                        ActionChains(driver).move_to_element_with_offset(icon[0], 50, 50)
                                        icon[0].click()

                                        icon[0].send_keys(salt)

                        try:
                            if int(st.lstrip('点赞 '))>70:
                                del lhn[-1]
                                f = open(dir1 + '\删除' + '.txt', 'r', encoding='UTF-8-sig')
                                linebt1 = f.readlines()
                                f.close()
                                linebt1[int(nr[1].rstrip("\n"))] = linebt1[int(nr[1].rstrip("\n"))].rstrip(
                                    "\n") + '\t' + nr[0].rstrip("\n") + '\n'
                                fh = open(dir1 + "\\" + '删除.txt', 'w', encoding='UTF-8')
                                for lll in linebt1:
                                    fh.write(lll)
                                fh.close()
                                driver.close()
                                driver.switch_to.window(handles[0])
                                continue
                            if int(st.lstrip('已赞 ')) > 71:
                                del lhn[-1]
                                f = open(dir1 + '\删除' + '.txt', 'r', encoding='UTF-8-sig')
                                linebt1 = f.readlines()
                                f.close()
                                linebt1[int(nr[1].rstrip("\n"))] = linebt1[int(nr[1].rstrip("\n"))].rstrip(
                                    "\n") + '\t' + nr[0].rstrip("\n") + '\n'
                                fh = open(dir1 + "\\" + '删除.txt', 'w', encoding='UTF-8')
                                for lll in linebt1:
                                    fh.write(lll)
                                fh.close()
                                driver.close()
                                driver.switch_to.window(handles[0])
                                continue
                        except:
                            time.sleep(0.1)








                        driver.close()
                        driver.switch_to.window(handles[0])
                    except:
                        del lhn[-1]
                        nr[i+4] = '0'
                        lhn.append('\t'.join(nr))
                        handles = driver.window_handles
                        if len(handles) > 1:

                            driver.switch_to.window(handles[1])
                            driver.close()
                            driver.switch_to.window(handles[0])
                        else:
                            driver.switch_to.window(handles[0])
               # '''
                fh = open(dir1 + "\\" + '发帖号.txt', 'w', encoding='UTF-8')
                for lll in lhn:
                    fh.write(lll.rstrip("\n") + '\n')
                fh.close()

                #'''
                ##################################################3删除

                f = open(dir1 + '\删除' + '.txt', 'r', encoding='UTF-8-sig')
                linebt1 = f.readlines()
                f.close()
                lists=re.split('\t',linebt1[i].rstrip('\n'))
                del lists[0]
                linebt1[i] = '\n'
                for hhh in lists:
                    try:
                        jss="http://v.qq.com/doki/doki_note/detail?starid="+ listd[xx].rstrip('\n')+"&noteid="+hhh
                        jsss='window.open("'+jss+'")'
                        driver.execute_script(jsss)

                        handles = driver.window_handles
                        start = time.time()
                        while len(handles) < 2 and time.time() - start < ticom:
                            time.sleep(eaty)
                            ###########################
                            handles = driver.window_handles
                        driver.switch_to.window(handles[1])

                        icon=driver.find_elements_by_xpath( '/html/body/div[3]/div/div')
                        if 0 < len(icon):
                            st= icon[0].text
                            if 0 <= st.find('帖子已删除'):
                                ####http://v.qq.com/bk/biu/doki_note/detail.html
                                driver.close()
                                driver.switch_to.window(handles[0])
                                continue
                        WebDriverWait(driver, 30, eaty).until(
                            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/a[3]/i'))).click()
                        WebDriverWait(driver, 30, eaty).until(
                            EC.element_to_be_clickable((By.XPATH, '//*[@id="ipop"]/div[2]/a[2]'))).click()
                        time.sleep(0.1)
                        driver.close()
                        driver.switch_to.window(handles[0])
                    except:
                        print(str(i)+'没删掉')
                        linebt1[i]=linebt1[i].rstrip('\n')+ '\t' +hhh.rstrip("\n") + '\n'
                        handles = driver.window_handles
                        if len(handles) > 1:

                            driver.switch_to.window(handles[1])
                            driver.close()
                            driver.switch_to.window(handles[0])
                        else:
                            driver.switch_to.window(handles[0])

                if 0<len(lists):
                    fh = open(dir1 + "\\" + '删除.txt', 'w', encoding='UTF-8')
                    for lll in linebt1:
                        fh.write(lll)
                    fh.close()

                ####################################################333333333333发帖2
                f = open(dir1 + '\异常' + '.txt', 'r', encoding='UTF-8-sig')
                yc = f.readlines()
                f.close()

                aac = re.split('\t', yc[i - 1])


                while cc<xygs-int(aac[1]) and ftjg<4000 and flagft == '1':
                    time.sleep(int(abs(ftjg-time.time()+timesid[i-1])))
                    post_one(dir1,driver)
                    tijc = test_post(dir1, driver)
                    cc = cc + 1
                print('gaiguole')
               ##########################################################################
                qiandao(dir1, driver, line, i)
                #####################################333333333


                handles = driver.window_handles
                if len(handles) > 1:

                    driver.switch_to.window(handles[1])
                    driver.close()
                    driver.switch_to.window(handles[0])
                else:
                    driver.switch_to.window(handles[0])
                #'''
                    ################################################3
                icon1 = WebDriverWait(driver, ectt, eaty).until(
                    EC.element_to_be_clickable((By.ID, "mod_head_notice_trigger")))
                start=time.time()
                while  time.time() - start < 17:
                    try:
                        ActionChains(driver).move_to_element(icon1).perform()
                        WebDriverWait(driver, 3, eaty).until(
                            EC.element_to_be_clickable((By.XPATH, '//*[@id="mod_head_notice_pop"]/div/div/div/div[1]/a[4]'))).click()
                        flagqq=0
                        break
                    except:
                        time.sleep(0.5)
                        handles = driver.window_handles
                        if len(handles) > 1:

                            driver.switch_to.window(handles[1])
                            driver.close()
                            driver.switch_to.window(handles[0])
                        else:
                            driver.switch_to.window(handles[0])
                        icon1 = WebDriverWait(driver, 10, eaty).until(
                            EC.element_to_be_clickable((By.ID, "mod_head_notice_trigger")))


            except:
                f = open(dir1 + '\canshu' + '.txt', 'r', encoding='UTF-8-sig')
                line = f.readlines()
                f.close()
                line[4] = '-'.join(list(map(str, isl[iis:])))+'\n'
                print(line[4])
                f = open(dir1 + '\canshu' + '.txt', 'w', encoding='UTF-8-sig')
                for l in line:
                    f.write(l)
                f.close()
                print('++++++++++++登录异常++++++++++++')
                driver.quit()
                flagqq = 1
                driver = webdriver.Chrome(desired_capabilities=capa, chrome_options=option)
        isl = getnlist(dir1)
        aaa=1
        for i in yc:
            ycsp = re.split('\t', i)
            ycg = int(ycsp[4])
            if ycg == 0:
                aaa=0
        if aaa==1 :
            quchong(dir1)




    files = os.listdir(dir2 + '\Temp')
    for file in files:  # 遍历文件夹
        if 0 == file.find('scoped_dir'):
            try:
                shutil.rmtree(dir2 + '\\Temp\\' + file)
            except:

                time.time()








