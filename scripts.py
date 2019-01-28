# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("filename.csv") 
# Preview the first 5 lines of the loaded data 
data.head()

# Pretty-print an entire Pandas Series / DataFrame
 
print(df.to_string())



import ftplib
server = 'ftp.byethost9.com'
username = 'b9_23355630'
password = '95wZ98^WVyvq1GhkLK8'
ftp_connection = ftplib.FTP(server, username, password)
remote_path = "/htdocs/"
ftp_connection.cwd(remote_path)
fh = open("example.csv", 'rb')
ftp_connection.storbinary('STOR example.csv', fh)
fh.close()


import os
import ftplib
server = 'ftp.byethost9.com'
username = 'b9_23355630'
password = '95wZ98^WVyvq1GhkLK8'
session = ftplib.FTP(server,username,password)
remote_path = "/htdocs/"
session.cwd(remote_path)
file = open('example.csv','rb')                  # file to send
session.storbinary('STOR '+'example.csv', file)     # send the file
file.close()                                    # close file and FTP
session.quit()

'''
%Anaconda3% python.exe %Anaconda3% cwp.py %Anaconda3% "%Anaconda3% python.exe" "%Anaconda3% Scripts/jupyter-notebook-script.py" %HOME%

"%Anaconda3% \python.exe" "%Anaconda3% \cwp.py" "%Anaconda3%" "%Anaconda3% \Scripts\jupyter-notebook.exe"

C:\Program Files (x86)\Microsoft Visual Studio\Shared\Anaconda3_64\Scripts\jupyter-notebook.exe

"%Anaconda3% \python.exe" "%Anaconda3%\cwp.py" "%Anaconda3%"  "%Anaconda3%/python.exe" "%Anaconda3%/Scripts/jupyter-notebook-script.py"

"%Anaconda3%\python.exe" "%Anaconda3%\cwp.py" "%Anaconda3%"  "%Anaconda3%/python.exe" "%Anaconda3%/Scripts/jupyter-notebook-script.py" "%cd%"
'''

