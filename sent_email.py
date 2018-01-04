#!/usr/local/bin/python3

import smtplib
import email.mime.multipart
import email.mime.text
import time

msg = email.mime.multipart.MIMEMultipart()
msgFrom = '617322616@qq.com'  # 从该邮箱发送
msgTo = '617322616@qq.com'  # 发送到该邮箱
smtpSever = 'smtp.qq.com'  # 163邮箱的smtp Sever地址
smtpPort = '465'  # 开放的端口
sqm = 'xxx'  # 在登录smtp时需要login中的密码应当使用授权码而非账户密码

msg['from'] = msgFrom
msg['to'] = msgTo

msg['subject'] = "Python自动邮件 - " + \
    time.strftime("%Y-%m-%d %X", time.localtime())  # 获取当前系统时间
content = '''
你好:
这是一封python3发送的邮件
'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)
# smtp = smtplib
# smtp = smtplib.SMTP()
'''
smtplib的connect（连接到邮件服务器）、login（登陆验证）、sendmail（发送邮件）
'''
# smtp.connect(smtpSever, smtpPort)
smtp = smtplib.SMTP_SSL(smtpSever, smtpPort)
smtp.login(msgFrom, sqm)
smtp.sendmail(msgFrom, msgTo, str(msg))
smtp.quit()
