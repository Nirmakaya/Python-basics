# Method 1
import win32com.client as win32


olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')

# construct email item object
mailItem = olApp.CreateItem(0)
mailItem.Subject = 'Execution Run Error'
mailItem.BodyFormat = 1
mailItem.Body = 'Execution Run Failed, Check Attached Screenshot for details'
mailItem.To = 'Suryansh.prasad@in.ey.com'
mailItem.Sensitivity  = 2

# To attach a file to the email :
filename = '\\test_ExecutionRunPROD_CV_M.py_Test_ExecutionRun_test_execution_run[chrome].png'
attachment  = 'C:\dev\Asterisk_TataMotors_DLP\Tests' + filename
mailItem.Attachments.Add(attachment)

# optional (account you want to use to send the email)
# mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item('<email@gmail.com')))

mailItem.Display()
#mailItem.Save()
mailItem.Send()






# # Method 2
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email.mime.text import MIMEText
# from email import encoders
#
# ## FILE TO SEND AND ITS PATH
# filename = '\\test_ExecutionRunPROD_CV_M.py_Test_ExecutionRun_test_execution_run[chrome].png'
# SourcePathName  = 'C:\dev\Asterisk_TataMotors_DLP\Tests' + filename
#
# msg = MIMEMultipart()
# msg['From'] = 'Suryansh.Prasad@in.ey.com'
# msg['To'] = 'Suryansh.Prasad@in.ey.com'
# msg['Subject'] = 'Execution Run'
# body = 'Body of the message goes in here'
# msg.attach(MIMEText(body, 'plain'))
#
# ## ATTACHMENT PART OF THE CODE IS HERE
# attachment = open(SourcePathName, 'rb')
# part = MIMEBase('application', "octet-stream")
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
# msg.attach(part)
#
# server = smtplib.SMTP('smtp.office365.com', 587)  ### put your relevant SMTP here
# server.starttls()
# server.ehlo()
# server.login('s.subhash.sarda@accenture.com', '8905252846')  ### if applicable
# server.send_message(msg)
# server.quit()