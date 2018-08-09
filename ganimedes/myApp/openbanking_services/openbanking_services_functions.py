#import requests
import json
import time
import datetime
import webbrowser
import os
import sys
#from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
from urllib.parse import urlparse
from .. python_debug_utilities.python_debug_utilities import *
import inspect
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def getAccounts_Service(parUserProfile):   
    """
    getAccounts_Service(parUserProfile)
    """
    thisService=myOpenBankingService(sys._getframe().f_code.co_name)
    thisService.start()
    thisService.input_param('parUserProfile',parUserProfile,9)

    varResult=[]
    varAccumulatedResult=[]
    try:
        for subscription in parUserProfile['subscriptions']:
            BankID=subscription['BankID']
            thisService.localVar('BankID',BankID,4)
            subscriptionID=subscription["accounts_subscriptionID"]
            thisService.localVar('subscriptionID',subscriptionID,4)

            varResult=[]
            if BankID=='bankofcyprus':
                varResult=[{'bankId': '12345671', 'accountId': '351012345671', 'accountAlias': 'ANDREAS', 'accountType': 'CURRENT', 'accountName': 'ANDREAS MICHAEL', 'IBAN': 'CY11002003510000000012345671', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}, {'bankId': '234567200', 'accountId': '351092345672', 'accountAlias': 'DEMETRIS', 'accountType': 'CARD', 'accountName': 'DEMETRIS KOSTA', 'IBAN': 'CY96002003510000009234567200', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}, {'bankId': '1234567300', 'accountId': '351012345673', 'accountAlias': 'GEORGE', 'accountType': 'SAVINGS', 'accountName': 'GEORGE ANDREOU', 'IBAN': 'CY34002003510000001234567300', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}, {'bankId': '1234567400', 'accountId': '351012345674', 'accountAlias': 'CHRISTOS', 'accountType': '30d NOTICE', 'accountName': 'CHRISTOS SAVVA', 'IBAN': 'CY56002003510000001234567400', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}]
            elif BankID=='hellenicbank':
                varResult=[{'bankId': 'ABCDEFG', 'accountId': 'hhh12345671', 'accountAlias': 'xxxxANDREAS', 'accountType': 'CURRENT', 'accountName': 'ANDREAS MICHAEL', 'IBAN': 'CY11002003510000000012345671', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}, {'bankId': 'AAAAA', 'accountId': 'hhh092345672', 'accountAlias': 'DEMETRIS', 'accountType': 'CARD', 'accountName': 'DEMETRIS KOSTA', 'IBAN': 'CY96002003510000009234567200', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}, {'bankId': '1234567300', 'accountId': '351012345673', 'accountAlias': 'GEORGE', 'accountType': 'SAVINGS', 'accountName': 'GEORGE ANDREOU', 'IBAN': 'CY34002003510000001234567300', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}, {'bankId': '1234567400', 'accountId': '351012345674', 'accountAlias': 'CHRISTOS', 'accountType': '30d NOTICE', 'accountName': 'CHRISTOS SAVVA', 'IBAN': 'CY56002003510000001234567400', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': []}]
            else:
                thisService.message('Bank not Supported:'+BankID)

            if varResult:
                varAccumulatedResult.extend(varResult)

        if varAccumulatedResult:
            thisService.set_result(varAccumulatedResult)
        else:
            thisService.error(9012,'no accounts')
    except:
        thisService.error(9011,'no subscriptions')
    
    thisService.log_results(4,4,4,8,4)
    thisService.finish()
    return thisService.result

def getAccountDetails_Service(parUserProfile,parAccountID):
    """
    getAccountDetails_Service(parUserProfile,parAccountID)
    """
    thisService=myOpenBankingService(sys._getframe().f_code.co_name)
    thisService.start()
    thisService.input_param('parUserProfile',parUserProfile,9)
    thisService.input_param('parAccountID',parAccountID,4)

    varResult=[]
    varAccumulatedResult=[]
    try:
        for subscription in parUserProfile['subscriptions']:
            BankID=subscription['BankID']
            thisService.localVar('BankID',BankID,4)
            subscriptionID=subscription["accounts_subscriptionID"]
            thisService.localVar('subscriptionID',subscriptionID,4)

            varResult=[]
            if BankID=='bankofcyprus':
                varResult=[{'bankId': '234567200', 'accountId': '351092345672', 'accountAlias': 'DEMETRIS', 'accountType': 'CARD', 'accountName': 'DEMETRIS KOSTA', 'IBAN': 'CY96002003510000009234567200', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': [{'amount': 1000, 'balanceType': 'CURRENT'}, {'amount': 1000, 'balanceType': 'AVAILABLE'}]}]
            elif BankID=='hellenicbank':
                varResult=[{'bankId': '1234567300', 'accountId': '351012345673', 'accountAlias': 'GEORGE', 'accountType': 'SAVINGS', 'accountName': 'GEORGE ANDREOU', 'IBAN': 'CY34002003510000001234567300', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': [{'amount': 1000, 'balanceType': 'CURRENT'}, {'amount': 1000, 'balanceType': 'AVAILABLE'}]}]
            else:
                thisService.message('Bank not Supported:'+BankID)

            if varResult:
                varAccumulatedResult.extend(varResult)

        if varAccumulatedResult:
            thisService.set_result(varAccumulatedResult)
        else:
            thisService.error(9012,'no accounts')
    except:
        thisService.error(9011,'no subscriptions')
    
    thisService.log_results(4,4,4,8,4)
    thisService.finish()
    return thisService.result

    
def getAccountStatement_Service(parUserProfile,parAccountID):
    """
    getAccountStatement_Service(parUserProfile,parAccountID)
    """
    thisService=myOpenBankingService(sys._getframe().f_code.co_name)
    thisService.start()
    thisService.input_param('parUserProfile',parUserProfile,8)
    thisService.input_param('parAccountID',parAccountID,4)

    varResult=[]
    varAccumulatedResult=[]
    try:
        for subscription in parUserProfile['subscriptions']:
            BankID=subscription['BankID']
            thisService.localVar('BankID',BankID,4)
            subscriptionID=subscription["accounts_subscriptionID"]
            thisService.localVar('subscriptionID',subscriptionID,4)

            varResult=[]
            if BankID=='bankofcyprus':
                varResult=[{'account': {'bankId': '234567200', 'accountId': '351092345672', 'accountAlias': 'DEMETRIS', 'accountType': 'CARD', 'accountName': 'DEMETRIS KOSTA', 'IBAN': 'CY96002003510000009234567200', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': [{'amount': 1000, 'balanceType': 'CURRENT'}, {'amount': 1000, 'balanceType': 'AVAILABLE'}]}, 'transaction': [{'id': '12345', 'dcInd': 'CY123', 'transactionAmount': {'amount': 1000, 'currency': 'EUR'}, 'description': 'NEFT TRANSACTION', 'postingDate': '20/11/2017', 'valueDate': '20/12/2017', 'transactionType': 'NEFT', 'merchant': {'name': 'DEMETRIS KOSTA', 'address': {'line1': 'A-123', 'line2': 'APARTMENT', 'line3': 'STREET', 'line4': 'AREA', 'city': 'CITY', 'postalcode': 'CY-01', 'state': 'STATE', 'country': 'CYPRUS'}}, 'terminalId': '12345'}]}]
            elif BankID=='hellenicbank':
                varResult=[{'account': {'bankId': '1234567300', 'accountId': '351012345673', 'accountAlias': 'GEORGE', 'accountType': 'SAVINGS', 'accountName': 'GEORGE ANDREOU', 'IBAN': 'CY34002003510000001234567300', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': [{'amount': 1000, 'balanceType': 'CURRENT'}, {'amount': 1000, 'balanceType': 'AVAILABLE'}]}, 'transaction': [{'id': '12345', 'dcInd': 'CY123', 'transactionAmount': {'amount': 1000, 'currency': 'EUR'}, 'description': 'NEFT TRANSACTION', 'postingDate': '20/11/2017', 'valueDate': '20/12/2017', 'transactionType': 'NEFT', 'merchant': {'name': 'GEORGE ANDREOU', 'address': {'line1': 'A-123', 'line2': 'APARTMENT', 'line3': 'STREET', 'line4': 'AREA', 'city': 'CITY', 'postalcode': 'CY-01', 'state': 'STATE', 'country': 'CYPRUS'}}, 'terminalId': '12345'}]}]
            else:
                thisService.message('Bank not Supported:'+BankID)

            if varResult:
                varAccumulatedResult.extend(varResult)

        if varAccumulatedResult:
            thisService.set_result(varAccumulatedResult)
        else:
            thisService.error(9012,'no accounts')
    except:
        thisService.error(9011,'no subscriptions')
    
    thisService.log_results(4,4,4,8,4)
    thisService.finish()
    return thisService.result

def getTransactions_Service(parUserProfile):   
    """
    getTransactions_Service(parUserProfile)
    """
    thisService=myOpenBankingService(sys._getframe().f_code.co_name)
    thisService.start()
    thisService.input_param('parUserProfile',parUserProfile,9)

    varResult=[]
    varAccumulatedResult=[]
    try:
        for subscription in parUserProfile['subscriptions']:
            BankID=subscription['BankID']
            thisService.localVar('BankID',BankID,4)
            subscriptionID=subscription["accounts_subscriptionID"]
            thisService.localVar('subscriptionID',subscriptionID,4)

            varResult=[]
            if BankID=='bankofcyprus':
                varResult=[{'account': {'bankId': '234567200', 'accountId': '351092345672', 'accountAlias': 'DEMETRIS', 'accountType': 'CARD', 'accountName': 'DEMETRIS KOSTA', 'IBAN': 'CY96002003510000009234567200', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': [{'amount': 1000, 'balanceType': 'CURRENT'}, {'amount': 1000, 'balanceType': 'AVAILABLE'}]}, 'transaction': [{'id': '12345', 'dcInd': 'CY123', 'transactionAmount': {'amount': 1000, 'currency': 'EUR'}, 'description': 'NEFT TRANSACTION', 'postingDate': '20/11/2017', 'valueDate': '20/12/2017', 'transactionType': 'NEFT', 'merchant': {'name': 'DEMETRIS KOSTA', 'address': {'line1': 'A-123', 'line2': 'APARTMENT', 'line3': 'STREET', 'line4': 'AREA', 'city': 'CITY', 'postalcode': 'CY-01', 'state': 'STATE', 'country': 'CYPRUS'}}, 'terminalId': '12345'}]}]
            elif BankID=='hellenicbank':
                varResult=[{'account': {'bankId': '1234567300', 'accountId': '351012345673', 'accountAlias': 'GEORGE', 'accountType': 'SAVINGS', 'accountName': 'GEORGE ANDREOU', 'IBAN': 'CY34002003510000001234567300', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': [{'amount': 1000, 'balanceType': 'CURRENT'}, {'amount': 1000, 'balanceType': 'AVAILABLE'}]}, 'transaction': [{'id': '12345', 'dcInd': 'CY123', 'transactionAmount': {'amount': 1000, 'currency': 'EUR'}, 'description': 'NEFT TRANSACTION', 'postingDate': '20/11/2017', 'valueDate': '20/12/2017', 'transactionType': 'NEFT', 'merchant': {'name': 'GEORGE ANDREOU', 'address': {'line1': 'A-123', 'line2': 'APARTMENT', 'line3': 'STREET', 'line4': 'AREA', 'city': 'CITY', 'postalcode': 'CY-01', 'state': 'STATE', 'country': 'CYPRUS'}}, 'terminalId': '12345'}]}]
            else:
                thisService.message('Bank not Supported:'+BankID)

            if varResult:
                varAccumulatedResult.extend(varResult)

        if varAccumulatedResult:
            thisService.set_result(varAccumulatedResult)
        else:
            thisService.error(9012,'no accounts')
    except:
        thisService.error(9011,'no subscriptions')
    
    thisService.log_results(4,4,4,8,4)
    thisService.finish()
    return thisService.result

def getPayments_Service(parUserProfile):   
    """
    getPayments_Service(parUserProfile)
    """
    thisService=myOpenBankingService(sys._getframe().f_code.co_name)
    thisService.start()
    thisService.input_param('parUserProfile',parUserProfile,9)

    varResult=[]
    varAccumulatedResult=[]
    try:
        for subscription in parUserProfile['subscriptions']:
            BankID=subscription['BankID']
            thisService.localVar('BankID',BankID,4)
            subscriptionID=subscription["payments_subscriptionID"]
            thisService.localVar('subscriptionID',subscriptionID,4)

            varResult=[]
            if BankID=='bankofcyprus':
                varResult=[{'account': {'bankId': '234567200', 'accountId': '351092345672', 'accountAlias': 'DEMETRIS', 'accountType': 'CARD', 'accountName': 'DEMETRIS KOSTA', 'IBAN': 'CY96002003510000009234567200', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': [{'amount': 1000, 'balanceType': 'CURRENT'}, {'amount': 1000, 'balanceType': 'AVAILABLE'}]}, 'transaction': [{'id': '12345', 'dcInd': 'CY123', 'transactionAmount': {'amount': 1000, 'currency': 'EUR'}, 'description': 'NEFT TRANSACTION', 'postingDate': '20/11/2017', 'valueDate': '20/12/2017', 'transactionType': 'NEFT', 'merchant': {'name': 'DEMETRIS KOSTA', 'address': {'line1': 'A-123', 'line2': 'APARTMENT', 'line3': 'STREET', 'line4': 'AREA', 'city': 'CITY', 'postalcode': 'CY-01', 'state': 'STATE', 'country': 'CYPRUS'}}, 'terminalId': '12345'}]}]
            elif BankID=='hellenicbank':
                varResult=[{'account': {'bankId': '1234567300', 'accountId': '351012345673', 'accountAlias': 'GEORGE', 'accountType': 'SAVINGS', 'accountName': 'GEORGE ANDREOU', 'IBAN': 'CY34002003510000001234567300', 'currency': 'EUR', 'infoTimeStamp': '1511779237', 'interestRate': 0, 'maturityDate': '19/11/2018', 'lastPaymentDate': '19/11/2017', 'nextPaymentDate': '19/12/2017', 'remainingInstallments': 10, 'balances': [{'amount': 1000, 'balanceType': 'CURRENT'}, {'amount': 1000, 'balanceType': 'AVAILABLE'}]}, 'transaction': [{'id': '12345', 'dcInd': 'CY123', 'transactionAmount': {'amount': 1000, 'currency': 'EUR'}, 'description': 'NEFT TRANSACTION', 'postingDate': '20/11/2017', 'valueDate': '20/12/2017', 'transactionType': 'NEFT', 'merchant': {'name': 'GEORGE ANDREOU', 'address': {'line1': 'A-123', 'line2': 'APARTMENT', 'line3': 'STREET', 'line4': 'AREA', 'city': 'CITY', 'postalcode': 'CY-01', 'state': 'STATE', 'country': 'CYPRUS'}}, 'terminalId': '12345'}]}]
            else:
                thisService.message('Bank not Supported:'+BankID)

            if varResult:
                varAccumulatedResult.extend(varResult)

        if varAccumulatedResult:
            thisService.set_result(varAccumulatedResult)
        else:
            thisService.error(9012,'no accounts')
    except:
        thisService.error(9011,'no subscriptions')
    
    thisService.log_results(4,4,4,8,4)
    thisService.finish()
    return thisService.result

    
    
