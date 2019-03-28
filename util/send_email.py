import datetime
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config.setting import *

# 截图方法
def inser_img(driver, filename):

    # 指定截图存放路径
    filepath =os.path.join(report_screenshot ,filename)
    driver.get_screenshot_as_file(filepath)


def get_time():
    return  datetime.datetime.now().strftime('%Y%m%d%H%M%S%f-')+str(random.randint(10,1000))



# 查找最新的测试报告
def latest_report():
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getatime(report_path + '\\' + fn))

    # print("the latest report is " + lists[-1])
    file = os.path.join(report_path, lists[-1])
    return file


# 将测试报告发送到邮件
def send_mail():
    f = open(latest_report(), 'rb')
    mail_content = f.read()
    f.close()

    smtpserver = 'smtp.qq.com'
    subject = 'Web Selenium 自动化测试报告'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = user
    msg['To'] = ','.join(receive)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, pd)

    logging.info("Start send email...")
    smtp.sendmail(user, receive, msg.as_string())
    smtp.quit()
    logging.info("Send email end!")


if __name__ == '__main__':
    print(get_time())
    print(get_time())
