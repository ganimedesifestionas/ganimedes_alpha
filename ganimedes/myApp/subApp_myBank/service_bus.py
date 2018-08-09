import json
import time
import datetime
import webbrowser
import os
import sys
#from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
from urllib.parse import urlparse
#from utilities import print_active_function_name,print_result,print_request_result,print_return
#from openbanking_utilities_module import log_process_start,log_process_finish,log_process_input_param,log_process_result,log_process_value
#from openbanking_utilities_module import log_process_section_start,log_process_section_finish,log_http_request_result,log_process_error
#from openbanking_globals import *
#from openbanking_service_module import *
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def getAccounts(parUserProfile):   
    """
    Accounts(parUserProfile)
    """
    #service_module='myBank_service_module'
    #service_name='get_Accounts_Service'
    #service_result={}
    #service_message='?'
    #service_return_code=0
    #service_error_code=''

    #log_process_start(service_name)
   
    #log_process_input_param('parUserProfile',parUserProfile)

    #try:
    #    service_result=get_Accounts_Service(parUserProfile)
    #except:
    #    service_result={}
    #    service_message='ABEND'
    #    service_return_code=0
    #    service_error_code='9001'

    #log_process_result('service_message',service_message)
    #log_process_result('service_return_code',service_return_code)

    #log_process_finish()
    service_result=[{'bankId': '12345671', 'accountId': '351012345671', 'accountAlias': 'ANDREAS', 'accountType': 'CURRENT', 'accountName': 'ANDREAS MICHAEL', 'IBAN': 'CY11002003510000000012345671', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}, {'bankId': '234567200', 'accountId': '351092345672', 'accountAlias': 'DEMETRIS', 'accountType': 'CARD', 'accountName': 'DEMETRIS KOSTA', 'IBAN': 'CY96002003510000009234567200', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}, {'bankId': '1234567300', 'accountId': '351012345673', 'accountAlias': 'GEORGE', 'accountType': 'SAVINGS', 'accountName': 'GEORGE ANDREOU', 'IBAN': 'CY34002003510000001234567300', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}, {'bankId': '1234567400', 'accountId': '351012345674', 'accountAlias': 'CHRISTOS', 'accountType': '30d NOTICE', 'accountName': 'CHRISTOS SAVVA', 'IBAN': 'CY56002003510000001234567400', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}]

    return service_result


