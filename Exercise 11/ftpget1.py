import ftplib

# path  of the code
a = '/mirrors/ubuntu-cdimage/releases/22.04/release'
# What file is suppose to be downloaded
filename = 'SHA256SUMS'
# Make the connections for the FTP 
ftp = ftplib.FTP("ftp.heanet.ie")
#  login
ftp.login() 

ftp.cwd(a)
# get the file back
ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
# and finally exit 
ftp.quit()