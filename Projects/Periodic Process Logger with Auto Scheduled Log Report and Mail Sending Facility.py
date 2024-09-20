import os
import time
import psutil
import urllib.request
import urllib.error
import smtplib
import schedule
from sys import argv
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import email.encoders

def is_connected():
    try:
        urllib.request.urlopen('https://8.8.4.4', timeout=1)
        return True
    except urllib.error.URLError:
        return False

def MailSender(filename, timestamp):
    try:
        fromaddr = "abhisheknale1309@gmail.com"
        toaddr = "abhishek.nale23@iccs.ac.in"
        passw = "faqhrkctliiprznb"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "System Log Report"

        body = f"""
        Hey there,

        Here is the system log file you requested.

        Timestamp: {timestamp}

        Thanks & Regards,
        Abhiz
        """
        msg.attach(MIMEText(body, 'plain'))

        with open(filename, "rb") as attachment:
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attachment.read())
            email.encoders.encode_base64(p)
            p.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(filename)}")
            msg.attach(p)

        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(fromaddr, passw)  # Use environment variables for security
            s.sendmail(fromaddr, toaddr, msg.as_string())

        print("Log File successfully sent through Mail")

    except Exception as e:
        print(f"Unable to send mail. Error: {e}")

def ProcessLog(log_dir='LogFiles'):
    listprocess = []

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    now = time.ctime()
    Time = now.replace(' ','_').replace(':', '-')
    separator = "_" * 80
    log_path = os.path.join(log_dir, f"SystemLog_{Time}.log")

    f= open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Abhiz Process Logger: " + time.ctime() + "\n")
    f.write(separator + "\n\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)  # Convert bytes to MB
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
            f.write(f"{element}\n")

    print(f"Log file is successfully generated at location {log_path}")

    if is_connected():
        startTime = time.time()
        MailSender(log_path, time.ctime())
        endTime = time.time()

        print(f"Took {endTime - startTime:.2f} seconds to send mail")
    else:
        print("There is no internet connection")

def main():
    if len(argv) != 2:
        print("Error: Invalid number of Arguments")
        print("Usage: python script_name.py <log_directory>")
        exit(1)

    if argv[1] in ("-h", "-H"):
        print("This Script is used to record log of running processes.")
        exit()

    if argv[1] in ('-u', '-U'):
        print("Usage: python script_name.py AbsolutePath_of_Directory")
        exit()
    print("Inside Code")
    try:
        schedule.every(5).seconds.do(ProcessLog, log_dir=argv[1])
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
