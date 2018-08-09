import json
import time
import datetime
import os
import sys
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::: OPEN BANKING GLOBALS                                :::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
process_stack=[]
debug_level=0
force_log=1
force_donotlog=0
environment='sandbox'
master_configuration={}
error_code=0
error_text=''
reply_code=0
response=''
debuglevel_one=0
debuglevel_two=0
debuglevel_three=0
debuglevel_four=0
cfgfile='env.ini'
try:
    configfile=open(cfgfile, 'r')
    environment=configfile.read()
except:
    configfile=open(cfgfile, 'w')
    configfile.write(environment)
configfile.close()
if debug_level>0:
    print('environment=',environment)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
############################################################
############################################################
############################################################
if __name__ == '__main__':
    print(force_log,force_donotlog)

