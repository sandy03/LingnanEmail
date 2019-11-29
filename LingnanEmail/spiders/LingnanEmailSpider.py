# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:03:32 2019

@author: Sandy Lin
"""

import scrapy
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import random
from email.mime.multipart import MIMEMultipart
class LingnanSpider(scrapy.spiders.Spider):
    name="LingnanEmail"
    start_urls=[]
    posts=['professors','associate-professors','instructors','seniorlecturer']
    for i in range(len(posts)):
        for j in range(2):
            url="http://math.sysu.edu.cn/"+posts[i]+"?page="+str(j)
            start_urls.append(url)
    def parse(self,response):
        smtpserver="smtp.qq.com"
        smtpport=465
        sender="2879659350@qq.com"
        receivers=response.xpath('//*[@id="content"]/article/div/div/div[2]/div[2]/div/div/div/div[2]/div//div/div/div[2]/div[1]/p[1]/a/text()').extract()
        with open('email.txt','a')as f:
            for item in receivers:
                f.write(item+'\n')
        """password="usuirnemomrodcde"
        subject="岭南学院学生会“百川交汇”学术论坛邀请信"
        for i in range(len(receivers)):
            msg=MIMEMultipart()
            greetings="<p align='left'>"+"尊敬的老师"+":"+"\n"
            paragraph1="<p style='text-indent:2em'>我是岭南学院学生林臻，岭南学院计划本周周五举办'百川交汇'学术讲座，希望能够邀请您莅临指导，分享学术经验，同时介绍您目前的研究领域</p>"
            paragraph2="<p style='text-indent:2em'>众所周知，交叉学科正成为学术的热门领域。然而，随着科学专业的细分，各个学科之间的壁垒越来越高，不同领域的学者交流也愈发困难。'百川交汇'学术论坛取海纳百川，交通天地之意，旨在打破各个学科之间的壁垒，集合各个专业的顶尖头脑。'百川交汇'助推交叉学科的发展,并希望为不同学科的青年学者提供交流思想，沟通洞见的平台。在学者的思想交流碰撞的过程中，台下的学子也会获益匪浅</p>"
            endings="<p style='right'>林臻</p>"
            date="<p style='right'>2019/11/18</p>"
            body = greetings+"<body><p style='text-indent:2em'>您好</p></body>"+paragraph1+paragraph2+endings+date
            msgtext=MIMEText(body,"html","utf-8")
            msg.attach(msgtext)
            msg["Subject"]=Header(subject,'utf-8')
            try:
                smtp=smtplib.SMTP_SSL(smtpserver,smtpport)
                smtp.login(sender,password)
                smtp.sendmail(sender,receivers[i],msg.as_string())
            except smtplib.SMTPException:
                print("fuck off")
            finally:
                sender1="2879659350@qq.com"
                receivers1="2879659350@qq.com"
                password1="usuirnemomrodcde"
                subject1="发送成功"
                msg1=MIMEMultipart()
                greetings="<p align='left'>"+"尊敬的老师"+":"+"\n"
                paragraph1="<p style='text-indent:2em'>我是岭南学院学生林臻，岭南学院计划本周周五举办'百川交汇'学术讲座，希望能够邀请您莅临指导，分享学术经验，同时介绍您目前的研究领域</p>"
                paragraph2="<p style='text-indent:2em'>众所周知，交叉学科正成为学术的热门领域。然而，随着科学专业的细分，各个学科之间的壁垒越来越高，不同领域的学者交流也愈发困难。'百川交汇'学术论坛取海纳百川，交通天地之意，旨在打破各个学科之间的壁垒，集合各个专业的顶尖头脑。'百川交汇'助推交叉学科的发展,并希望为不同学科的青年学者提供交流思想，沟通洞见的平台。在学者的思想交流碰撞的过程中，台下的学子也会获益匪浅</p>"
                endings="<p style='right'>林臻</p>"
                date="<p style='right'>2019/11/18</p>"
                body1 =greetings+"<body><p style='text-indent:2em'>您好</p></body>"+paragraph1+paragraph2+endings+date
                msgtext1=MIMEText(body1,"html","utf-8")
                msg1.attach(msgtext1)
                msg1["Subject"]=Header(subject1,'utf-8')
                time.sleep(random.randint(3,5))
                try:
                   smtp1=smtplib.SMTP_SSL(smtpserver,smtpport)
                   smtp1.login(sender1,password1)
                   smtp1.sendmail(sender1,receivers1,msg1.as_string())
                except smtplib.SMTPException:
                   print("fuck off")"""