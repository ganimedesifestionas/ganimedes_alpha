#import json
#import time
#import datetime
#import webbrowser
#import os
import sys
#from http.server import BaseHTTPRequestHandler, HTTPServer
#import urllib
#from urllib.parse import urlparse
from . openbanking_services import openbanking_services_functions
from . python_debug_utilities.python_debug_utilities import *
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def getUserProfile(parRequest):
    """
    getUserProfile(parRequest)
    """
    thisService=myServiceBusService(sys._getframe().f_code.co_name)
    thisService.start()
    thisService.input_param('parRequest',parRequest,9)
    ThisUserProfile = parRequest.cookies.get('ThisUserProfile')
    ThisUserProfile={
          'originUserId': '1524'
        , 'originSourceId': ''
        , 'originChannelId': ''
        , 'originDeptId': ''
        , 'originEmployeeId': ''
        , 'originTerminalId': ''
        , 'subscriptions': [
            {'BankID':'bankofcyprus'
             ,'payments_subscriptionID': 'Subid000001-1533034651745'
             ,'accounts_subscriptionID': 'Subid000001-1533034634064'}
            ,{'BankID':'hellenicbank'
             ,'payments_subscriptionID': 'Subid000001-1533034651745'
             ,'accounts_subscriptionID': 'Subid000001-1533034634064'}
            ]
        }
    if ThisUserProfile:
        thisService.set_result(ThisUserProfile)
    else:
        thisService.error(1013,'no user profile')
        raise Exception (thisService.message)

    thisService.log_results(4,4,4,8,4)
    thisService.finish()
    return thisService.result
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def getAccounts(parUserProfile):   
    """
    getAccounts(parUserProfile)
    """
    thisService=myServiceBusService(sys._getframe().f_code.co_name)
    thisService.start()
    thisService.input_param('parUserProfile',parUserProfile,8)

    varResult=[]
    try:
        varResult=openbanking_services_functions.getAccounts_Service(parUserProfile)
        if not(varResult):
            thisService.error(1001,'no accounts')
            raise Exception (thisService.message)
        else:
            thisService.set_result(varResult)
    except Exception as error_text:   
        thisService.error(1002,error_text)
        raise Exception (thisService.message)
        
    thisService.log_results(4,4,4,8,4)
    thisService.finish()
    return thisService.result

def getAccountDetails(parUserProfile,parAccountID):   
    """
    getAccountDetails(parUserProfile,parAccountID)
    """
    thisService=myServiceBusService(sys._getframe().f_code.co_name)
    thisService.start()
    thisService.input_param('parUserProfile',parUserProfile,8)
    thisService.input_param('parAccountID',parAccountID,4)

    varResult=[]
    try:
        varResult=openbanking_services_functions.getAccountDetails_Service(parUserProfile,parAccountID)
        if not(varResult):
            thisService.error(1003,'no account details')
            raise Exception (thisService.message)
        else:
            thisService.set_result(varResult)
    except Exception as error_text:   
        thisService.error(1002,error_text)
        raise Exception (thisService.message)

    thisService.log_results(4,4,4,8,4)
    thisService.finish()
    return thisService.result

def getAccountStatement(parUserProfile,parAccountID):   
    """
    getAccountStatement(parUserProfile,parAccountID)
    """
    thisService=myServiceBusService(sys._getframe().f_code.co_name)
    thisService.start()
    thisService.input_param('parUserProfile',parUserProfile,8)
    thisService.input_param('parAccountID',parAccountID,4)

    varResult=[]
    try:
        varResult=openbanking_services_functions.getAccountStatement_Service(parUserProfile,parAccountID)
        if not(varResult):
            thisService.error(1004,'no account transactions')
            raise Exception (thisService.message)
        else:
            thisService.set_result(varResult)
    except Exception as error_text:   
        thisService.error(1002,error_text)
        raise Exception (thisService.message)

    thisService.log_results(4,4,4,8,4)
    thisService.finish()
    return thisService.result

def getTransactions(parUserProfile):   
    """
    getTransactions(parUserProfile)
    """
    thisService=myServiceBusService(sys._getframe().f_code.co_name)
    thisService.start()
    thisService.input_param('parUserProfile',parUserProfile,8)

    varResult=[]
    try:
        varResult=openbanking_services_functions.getTransactions_Service(parUserProfile)
        if not(varResult):
            thisService.error(1006,'no transactions')
            raise Exception (thisService.message)
        else:
            thisService.set_result(varResult)
    except Exception as error_text:   
        thisService.error(1002,error_text)
        raise Exception (thisService.message)
        
    thisService.log_results(4,4,4,8,4)
    thisService.finish()
    return thisService.result

def getPayments(parUserProfile):   
    """
    getPayments(parUserProfile)
    """
    thisService=myServiceBusService(sys._getframe().f_code.co_name)
    thisService.start()
    thisService.input_param('parUserProfile',parUserProfile,8)

    varResult=[]
    try:
        varResult=openbanking_services_functions.getPayments_Service(parUserProfile)
        if not(varResult):
            thisService.error(1006,'no payments')
            raise Exception (thisService.message)
        else:
            thisService.set_result(varResult)
    except Exception as error_text:   
        thisService.error(1002,error_text)
        raise Exception (thisService.message)
        
    thisService.log_results(4,4,4,8,4)
    thisService.finish()
    return thisService.result
