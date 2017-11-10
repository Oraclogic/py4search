# import cx_Oracle

# connection = cx_Oracle.connect("system", "oracle", "192.168.11.111:1521/ZVCP01RD")

# cursor = connection.cursor()
# cursor.execute("""
# SELECT ename,sal,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') datetime
# FROM scott.emp
# WHERE deptno = :did AND empno > :eid""",
# did = 10,
# eid = 190)
# for row in cursor:
#     print (row)

from subprocess import Popen, PIPE
import win32com.client as win32
import datetime


def get_search_list(file, searchlog):
    searchloglist = []
    f = open(file)
    lines = f.read().splitlines()
    for i in range(0, len(lines)):
        if lines[i].find(searchlog) != -1:
            searchloglist.append(lines[i])
    return searchloglist


def read_files(file):
    f = open(file)
    lines = f.read().splitlines()
    filelist = []
    for i in range(0, len(lines)):
        filelist.append(lines[i])
    return filelist


def run_sql_script(connstr, file):
    sqlplus = Popen(['sqlplus', '-S', connstr],
                    stdin=PIPE, stdout=PIPE, stderr=PIPE)
    sqlplus.stdin.write('@' + file)
    return sqlplus.communicate()


def send_outlook_mail(receiver, subject, body=None, attachment=None):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = receiver
    mail.Subject = subject
    mail.Body = body
    # mail.HTMLBody = '<h2>lase check the attchement!</h2>'# this field is optional
    # In case you want to attach a file to the email
    for a in attachment:
        mail.Attachments.Add(a)
    mail.Send()


def main(connstr, searchloglist, searchlogno):
    searchloglist = get_search_list(searchloglist, searchlogno)
    strs = searchloglist[0].split(',')
    slogno = strs[0]
    suser = strs[1]
    sscripts = strs[2]
    sattachment = strs[3]
    list_attachment = sattachment.split(';')
    for sline in read_files(sscripts):
        output, error = run_sql_script(connstr, sline)
    send_outlook_mail(suser, slogno + '_' +
                      datetime.datetime.now().strftime("%Y%m%d"), '', list_attachment)


# attachment_basedir = ''
subdir = 'zfzhou'
connstr = 'system/oracle@192.168.11.111:1521/ZVCP01RD'
timefmt = "%Y-%m-%d %H:%M:%S"

# output, error = run_sql_script(connstr,"c:\Users\IBM_ADMIN\PycharmProjects\zfzhou\\run_ora.sql")

# filename = basedir + '/' + subdir + '/run_scripts_list.txt'
# file = open(filename, "r")
# for line in file:
#     output, error = run_sql_script(connstr, line)

main(connstr, 'esearch.csv', 'S2000')

# searchloglist=get_search_list('c:\Users\IBM_ADMIN\PycharmProjects\zfzhou\esearch.csv','S2000')
# for i in range(len(searchloglist)):
#     print searchloglist[i]
#############################
# import win32com.client as win32
# outlook = win32.Dispatch('outlook.application')
# mail = outlook.CreateItem(0)
# mail.To = 'krinight@gmail.com;krinight@sina.com'
# mail.Subject = 'Python Mail Test'
# mail.Body = 'Plase check the attchement!'
# # mail.HTMLBody = '<h2>lase check the attchement!</h2>'# this field is optional

# #In case you want to attach a file to the email
# attachment  = "c:\Users\IBM_ADMIN\PycharmProjects\sp.txt"
# mail.Attachments.Add(attachment)

# mail.Send()

# timestr = datetime.datetime.now().strftime(timefmt)
# send_outlook_mail('krinight@sina.com', 'mail test via python ' + timestr, timestr,"c:\Users\IBM_ADMIN\PycharmProjects\sp.txt")
