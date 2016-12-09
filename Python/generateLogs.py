#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
import stat
logPath = "Path-to-store-logs"
def generateLogs(file_name, log_text, logPath):
        if not os.path.exists(logPath + "/Logs"):
                os.makedirs(logPath + "/Logs")
                os.chmod(logPath + "/Logs",stat.S_IRWXU)
        fo = open(logPath + "/Logs/" + file_name +".txt", "a")
        fo.write(log_text + "\n")
        
# generateLogs("helloWorld", "Hello World, this is Kartheek", logPath)
