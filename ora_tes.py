from datetime import datetime
from subprocess import Popen, PIPE
import win32com.client as win32
# import datetime
import sys

# Return the special search log deatil in esearh.csv and filter by search log no


def get_search_list(file, searchlog):
    searchloglist = []
    f = open(file)
    lines = f.read().splitlines()
    for i in range(0, len(lines)):
        if lines[i].find(searchlog) != -1:
            searchloglist.append(lines[i])
    return searchloglist

# Return a list of sql scripts


def read_files(file):
    f = open(file)
    lines = f.read().splitlines()
    filelist = []
    for i in range(0, len(lines)):
        filelist.append(lines[i])
    return filelist

# Execute the sql scripts via Popen


def run_sql_script(connstr, file):
    sqlplus = Popen(['sqlplus', '-S', connstr],
                    stdin=PIPE, stdout=PIPE, stderr=PIPE)
    sqlplus.stdin.write('@' + file)
    return sqlplus.communicate()

# To send Mail via local Outlock client


def send_outlook_mail(receiver, subject, body=None, attachment=None):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = receiver
    mail.Subject = subject
    mail.Body = body
    # mail.HTMLBody = '<h2>lase check the attchement!</h2>'# this field is optional
    # In case you want to attach a file to the email
    if len(attachment) == 0:
        print ("No attachment.")
    else:
        for a in attachment:
            mail.Attachments.Add(a)
            print ("Add attachment:" + a)
        mail.Send()


def main(connstr, searchloglist, searchlogno):
    searchloglist = get_search_list(searchloglist, searchlogno)
    strs = searchloglist[0].split(',')
    slogno = strs[0]
    suser = strs[1]
    sscripts = strs[2]
    sattachment = strs[3]
    if len(sattachment) == 0:
        list_attachment = []
    else:
        list_attachment = sattachment.split(';')
    for sline in read_files(sscripts):
        tbegin = datetime.now().strftime(timefmt)
        print (tbegin + "\tStarting execute script:" + sline)
        output, error = run_sql_script(connstr, sline)
        tend = datetime.now().strftime(timefmt)
        tdelta = datetime.strptime(tend, timefmt) - \
            datetime.strptime(tbegin, timefmt)
        print (tend + "\tComplete execute script:" + sline + "\telapsed: " +str(tdelta))
        print error
    send_outlook_mail(suser, slogno + '_' +
                      datetime.now().strftime("%Y%m%d"), '', list_attachment)


timefmt = "%Y-%m-%d %H:%M:%S"
timestampstr = datetime.now().strftime(timefmt)


# main(database_connect_str, search_log_standard_list, searchno)
connstr = sys.argv[1]
filename = sys.argv[2]
searchno = sys.argv[3]
main(connstr, filename, searchno)

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
