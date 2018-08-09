import requests
import json
import time
import datetime
import webbrowser
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
from urllib.parse import urlparse
#from utilities import print_active_function_name,print_result,print_request_result,print_return
from openbanking_utilities_module import log_process_start,log_process_finish,log_process_input_param,log_process_result,log_process_value
from openbanking_utilities_module import log_process_section_start,log_process_section_finish,log_http_request_result,log_process_error
from openbanking_configuration_module import get_configuration,get_configuration_param
from openbanking_globals import *
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def boc_get_parameters(api):
    process='get_parameters'
    log_process_start(process)

    bankCodeName='bankofcyprus'
    ts = time.time()
    currentTimeStamp = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')

    bankID=get_configuration_param('bankID',master_configuration,bankCodeName)
    bankName=get_configuration_param('bankName',master_configuration,bankCodeName)
    redirect_uri=get_configuration_param('redirect_uri',master_configuration,bankCodeName)
    app_name=get_configuration_param('application_name',master_configuration,bankCodeName)
    client_id=get_configuration_param('client_id',master_configuration,bankCodeName)
    client_secret=get_configuration_param('client_secret',master_configuration,bankCodeName)
    api_uri=get_configuration_param('api_uri',master_configuration,bankCodeName)
    journeyId=get_configuration_param('journeyId',master_configuration,bankCodeName)
    originSourceId=get_configuration_param('originSourceId',master_configuration,bankCodeName)
    originChannelId=get_configuration_param('originChannelId',master_configuration,bankCodeName)
    originDeptId=get_configuration_param('originDeptId',master_configuration,bankCodeName)
    originUserId=get_configuration_param('originUserId',master_configuration,bankCodeName)
    originEmployeeId=get_configuration_param('originEmployeeId',master_configuration,bankCodeName)
    originTerminalId=get_configuration_param('originTerminalId',master_configuration,bankCodeName)
    correlationId=get_configuration_param('correlationId',master_configuration,bankCodeName)
    lang=get_configuration_param('lang',master_configuration,bankCodeName)
    tppId=get_configuration_param('tppId',master_configuration,bankCodeName)

    functionRequest = 'GET'
    if api=='get_access_token':
        endpoint = 'df-boc-org-sb/sb/psd2/oauth2/token'
    elif api=='get_authorization_token':
        endpoint = 'df-boc-org-sb/sb/psd2/oauth2/token'
    elif api=='get_subscriptionId':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/subscriptions'
    elif api=='get_subscription_details':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/subscriptions/{}'
    elif api=='update_subscription':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/subscriptions/{}'
    elif api=='get_account_subscriptions':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/subscriptions/accounts/{}'
    elif api=='delete_subscription':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/subscriptions/{}'
        functionRequest = 'DELETE'
    elif api=='get_customerConsent':
        endpoint = 'https://sandbox-apis.bankofcyprus.com/df-boc-org-sb/sb/psd2/oauth2/authorize'
    elif api=='get_subscription_Accounts':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/accounts'
    elif api=='get_subscription_Customers':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/customers'
    elif api=='get_Accounts_List':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/accounts'
    elif api=='get_account_details':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/accounts/{}'
    elif api=='get_account_transactions':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/accounts/{}/statement'
    elif api=='get_account_balances':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/accounts/{}/balance'
    elif api=='get_payments':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/payments/accounts/{}'
    elif api=='payment_initiate':
        endpoint = 'df-boc-org-sb/sb/jwssignverifyapi/sign'
    elif api=='payment_create':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/payments'
    elif api=='payment_checkfunds':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/payments/fundAvailability'
        functionRequest = 'POST'
    elif api=='payment_authorize':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/payments/{}/authorize'
    elif api=='get_payment_details':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/payments/{}'
        functionRequest = 'GET'
    elif api=='get_payment_status':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/payments/{}/status'
        functionRequest = 'GET'
    elif api=='delete_payment':
        endpoint = 'df-boc-org-sb/sb/psd2/v1/payments/{}'
        functionRequest = 'DELETE'
    else:
        endpoint = 'df-boc-org-sb/????????????????'
    
    log_process_value('api',api)
    log_process_value('endpoint',endpoint)

    params={
        'bankCodeName'      :bankCodeName
        ,'bankID'           :bankID   
        ,'bankName'         :bankName
        ,'app_Name'         :app_name
        ,'client_id'        :client_id
        ,'client_secret'    :client_secret
        ,'redirect_uri'     :redirect_uri
        ,'api'              :api
        ,'api_uri'          :api_uri
        ,'endpoint'         :endpoint
        ,'function'         :functionRequest
        ,'tppId'            :tppId
        ,'journeyId'        :journeyId
        ,'originSourceId'   :originSourceId
        ,'originChannelId'  :originChannelId
        ,'originDeptId'     :originDeptId
        ,'originUserId'     :originUserId
        ,'originEmployeeId' :originEmployeeId
        ,'originTerminalId' :originTerminalId
        ,'correlationId'    :correlationId
        ,'lang'             :lang
        ,'currentTimeStamp' :datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
        ,'debuglevel_one'   :debuglevel_one
        ,'debuglevel_two'   :debuglevel_two
        ,'debuglevel_three' :debuglevel_three
    }
    log_process_result('api_params',params)

    log_process_finish()
    return params

def boc_prepare_request_standard(access_token,subscriptionId,api_params,url_parameter=''):
    process='prepare_standard_request'
    log_process_start(process)

    headers = {
        'content-type': 'application/json',
        'accept': 'application/json',
        #'app_name': api_params['app_Name'],
        'journeyId': api_params['journeyId'],
        #'originSourceId': api_params['originSourceId'], 
        #'originChannelId': api_params['originChannelId'],
        #'originDeptId': api_params['originDeptId'],
        #'originUserId': api_params['originUserId'],
        #'originEmployeeId':api_params['originEmployeeId'],
        #'originTerminalId': api_params['originTerminalId'],
        #'correlationId': api_params['correlationId'],
        #'lang': api_params['lang'],
        'tppId': api_params['tppId'],
        'timeStamp': api_params['currentTimeStamp'],
        #'Authorization': 'Bearer {}'.format(access_token),
        #'subscriptionId': subscriptionId,
        #'lang': ''
    }
    #print('headers=',headers)
    #print('--------')
    #params = params_standard.copy()
    if subscriptionId:
        if subscriptionId!='':
            header_subscriptionId={'subscriptionId': subscriptionId}
            headers.update(header_subscriptionId)
    if access_token:
        if access_token!='':
            header_token={'Authorization': 'Bearer {}'.format(access_token)}
            headers.update(header_token)
    if api_params['originSourceId'] !='':
        headers.update({'originSourceId': api_params['originSourceId']})
    if api_params['originUserId'] !='':
        headers.update({'originUserId': api_params['originUserId']})
    if api_params['originEmployeeId'] !='':
        headers.update({'originEmployeeId': api_params['originEmployeeId']})
    if api_params['originChannelId'] !='':
        headers.update({'originChannelId': api_params['originChannelId']})
    if api_params['originDeptId'] !='':
        headers.update({'originDeptId': api_params['originDeptId']})
    if api_params['originChannelId'] !='':
        headers.update({'originChannelId': api_params['originChannelId']})
    if api_params['originTerminalId'] !='':
        headers.update({'originTerminalId': api_params['originTerminalId']})
    if api_params['correlationId'] !='':
        headers.update({'correlationId': api_params['correlationId']})
    if api_params['lang'] !='':
        headers.update({'lang': api_params['lang']})
    if api_params['lang'] !='':
        headers.update({'lang': api_params['lang']})

    log_process_result('headers',headers)

    params = {
        'client_id': api_params['client_id'],
        'client_secret': api_params['client_secret'],
    }
    log_process_result('params',params)

    url=api_params['api_uri']+api_params['endpoint'].format(url_parameter)
    log_process_result('api_url',url)

    request_params={
        'headers'       :headers
        ,'parameters'   :params
        ,'url'          :url
    }
    log_process_result('request_params',request_params)

    log_process_finish()
    return request_params
    

################################################################
### access tokens                                            ###
################################################################
def boc_get_access_token():
    api='get_access_token'
    log_process_start(api)

    access_token=''
    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard('','',api_params)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    headers = {
        'accept': 'application/json'
    }
    payload = {
        'grant_type': 'client_credentials',
        'client_id': api_params['client_id'],
        'client_secret': api_params['client_secret'],
        'scope': 'TPPOAuth2Security'
    }
    r = requests.post(api_url,data=payload,headers=headers)
    reply_code=r.status_code
    response = r.json()
    if not r.status_code == requests.codes.ok:
        access_token=None
        error_text=r.text
        error_code=1
    else:
        access_token = response['access_token']        

    log_process_result('access_token',access_token)
    log_process_finish()
    return access_token

def boc_get_authorization_token(access_token,authorization_code):
    api='get_authorization_token'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,'',api_params)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.post(api_url,headers=headers,params=params)
    headers = {
        'accept': 'application/json'
    }
    payload = {
        'code': authorization_code,
        'client_id': api_params['client_id'],
        'client_secret': api_params['client_secret'],
        'grant_type': 'authorization_code',
        'scope': 'UserOAuth2Security'
    }

    r = requests.post(api_url,headers=headers,data=payload)
    reply_code=r.status_code
    response = r.json()
    if not r.status_code == requests.codes.ok:
        authorization_token=None
        error_text=r.text
        error_code=1
    else:
        authorization_token = response['access_token']        

    log_process_result('authorization_token',authorization_token)

    log_process_finish()
    return authorization_token

################################################################
### subscription apis                                        ###
################################################################
def boc_get_subscription_details(access_token,subscriptionId):   
    api='get_subscription_details'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,'',api_params,subscriptionId)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.get(api_url,headers=headers,params=params)
    reply_code=r.status_code
    response = r.json()
    if api_params['debuglevel_two']>0:
        print(r.status_code,r.json())

    #print(r.header)
    #print(r.data)

    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None

    log_process_finish()
    return response

def boc_get_subscription_selectedAccounts(access_token,subscriptionId):   ###even if pending
    api='get_subscription_selectedAccounts'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    subscription_details=boc_get_subscription_details(access_token,subscriptionId)
    
    if not subscription_details:
        error_text=r.text
        error_code=1
        acts=[] #None
    else:
        acts=subscription_details[0]['selectedAccounts']
        
    log_process_finish()
    return acts

def boc_get_subscription_Accounts(access_token,subscriptionId):   
    api='get_subscription_Accounts'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.get(api_url,headers=headers,params=params)
    reply_code=r.status_code
    response = r.json()
    #print(r.status_code,r.json())
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=[] #None
        
    log_process_finish()
    return response

def boc_get_subscription_Customers(access_token,subscriptionId):   
    api='get_subscription_Customers'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.get(api_url,headers=headers,params=params)
    reply_code=r.status_code
    response = r.json()
    #print(r.status_code,r.json())
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=[] #None
        
    log_process_finish()
    return response

def boc_delete_subscription(access_token,subscriptionId):
    api='delete_subscription'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,'',api_params,subscriptionId)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.delete(api_url,headers=headers,params=params)
    reply_code=r.status_code
    #response = r.json()
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
        response = {"message":"subscription "+subscriptionId+" not found"}
    else:
        #fix: when 200 to return text message as json
        response = {"message":"OK-subscription "+subscriptionId+" Deleted"}
    log_process_finish()
    return response
################################################################
### accounts apis                                            ###
################################################################
def boc_list_accounts(access_token,subscriptionId):   
    api='get_Accounts_List'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    if debuglevel_two>0:
        print('---api_url---',api_url)
        print('---headers---',headers)
        print('---params---',params)

    r = requests.get(api_url,headers=headers,params=params)
    reply_code=r.status_code
    response = r.json()
    
    if debuglevel_three>0:
        print(r.status_code,r.text)
        
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
    log_process_finish()
    return response

def boc_get_account_details(access_token, subscriptionId, account_id):
    api='get_account_details'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params,account_id)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.get(api_url,headers=headers,params=params)
    reply_code=r.status_code
    response = r.json()
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
    log_process_finish()
    return response
def boc_get_account_balances(access_token, subscriptionId, account_id):
    api='get_account_balances'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params,account_id)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.get(api_url,headers=headers,params=params)
    reply_code=r.status_code
    response = r.json()
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
    log_process_finish()
    return response
def boc_get_account_transactions(access_token, subscriptionId, account_id,sdate='',edate='',ntrans=9999):
    api='get_account_transactions'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params,account_id)
    api_url=request_params['url']
    headers=request_params['headers']
    params_standard=request_params['parameters']
    params_transactions = {
        'startDate': '01/01/2010'
        ,'endDate': '31/12/2018'
        ,'maxCount': ntrans
    }
    params = params_standard.copy()
    params.update(params_transactions)

    r = requests.get(api_url,headers=headers,params=params)
    reply_code=r.status_code
    response = r.json()
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
    log_process_finish()
    return response
def boc_get_account_subscriptions(access_token,account_id):
    api='get_account_subscriptions'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,'',api_params,account_id)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.get(api_url,headers=headers,params=params)
    reply_code=r.status_code
    response = r.json()
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=[]
    log_process_finish()
    return response
################################################################
### payments apis                                            ###
################################################################
def boc_payment_fundsavailability(access_token,subscriptionId,payment):
    api='payment_checkfunds'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']

    paymentData=json.dumps(payment)

    r = requests.post(api_url,headers=headers,params=params,data=paymentData)
    reply_code=r.status_code
    response = r.json()

    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
    else:
        response=1
    
    log_process_finish()
    return response

def boc_get_payments(access_token, subscriptionId,accountId):
    api='get_payments'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params,accountId)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.get(api_url,headers=headers,params=params)
    reply_code=r.status_code
    response = r.json()
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
    log_process_finish()
    return response


def boc_get_payment_status(access_token,subscriptionId,payment_id):
    api='get_payment_status'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params,payment_id)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.get(api_url,headers=headers,params=params)
    if not r.status_code == requests.codes.ok:
        raise Exception(r.text)
    payments = r.json()
    #res=print_result('payment_status=',payments)
    log_process_finish()
    return payments

def boc_delete_payment(access_token,subscriptionId,payment_id):
    api='delete_payment'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params,payment_id)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.delete(api_url,headers=headers,params=params)
    reply_code=r.status_code
    response = r.json()
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
    log_process_finish()
    return response

def boc_get_payment_details(access_token,subscriptionId,payment_id):
    api='get_payment_details'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params,payment_id)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    r = requests.get(api_url,headers=headers,params=params)
    reply_code=r.status_code
    response = r.json()
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
    #payment_details = r.json()
    #res=print_result('payment_details=',payment_details)
    log_process_finish()
    return response
################################################################
### create payment apis                                      ###
################################################################
def boc_payment_initiate(access_token, subscriptionId, DBaccountId ,CRaccountId,Amount,Currency,Details):
    api='payment_initiate'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    params.update({'subscriptionId': subscriptionId})    

    paym = {
        "debtor":{"bankId":"","accountId":DBaccountId},
        "creditor":{"bankId":"","accountId":CRaccountId,"name":"zorbas","address":"athalassas"},
        "transactionAmount":{"amount":Amount,"currency":Currency,"currencyRate":""},
        "paymentDetails":Details,
        "endToEndId":"",
        "terminalId":"",
        "branch":"",
        "executionDate":"",
        "valueDate":"",
        #"RUB":{"voCode":"lezeidne","BIK":"ublepipunzokcevjozejkedhanticew","INN":"topajimpopcuvirobil","correspondentAccount":"6226014357403233"}
        #"totalDebitAmount":{"amount":Amount,"currency":Currency,"currencyRate":""},
        "refNumber":"123456789"
        }

    paymentRequest=json.dumps(paym)
    #the reverse is: paym=json.loads(paymentRequest)

    if api_params['debuglevel_two']>0:
        print('url-----',api_url)
        print('params----',params)
        print('headers---',headers)
        print('data------',paymentRequest)

    
    r = requests.post(api_url,headers=headers,params=params,data=paymentRequest)
    #print(r)
    #reply_code=r.status_code
    #response = r.json()
    if api_params['debuglevel_two']>0:
        print('results---',r.status_code,r.text)
    
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
    else:
        response = r.json()
        #{
        #'payload': '...',
        #'signatures': [
            #    {'protected': 'eyJhbGciOiJSUzI1NiJ9''signature': '...'}
            #]
        #}
        payload = response['payload']
        #res=print_result('payload=',payload)
        signatures = response['signatures']
        #res=print_result('signatures=',signatures)
    log_process_finish()
    return response

def boc_payment_create(access_token, subscriptionId, payload):
    api='payment_create'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    params.update({'subscriptionId': subscriptionId})    

    paymentData=json.dumps(payload)
    #res=print_result('paymentLoad=',paymentData)
    #paymentData=payLoad
    #print('@@@@@',payLoad)
    #print('@@@@@',signature)
    if api_params['debuglevel_two']>0:
        print('url-----',api_url)
        print('params----',params)
        print('headers---',headers)
        print('data------',paymentData)
    
    r = requests.post(api_url,headers=headers,params=params,data=paymentData)
    if api_params['debuglevel_two']>0:
        print('results---',r.status_code,r.text)
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
    else:
        response = r.json()
        payment = r.json()
        #{
        #   "authCodeNeeded": true,
        #    "payment": {
        #        "paymentId": "PmtId000001_1518607567498",
        #        "transactionTime": "1511779237",
        #        "status": {
        #            "code": "PNDG",
        #            "description": [
        #                "Payment in pending status"
        #            ],
        #            "refNumber": "CYP12345"
        #        },
        #        "debtor": {
        #            "bankId": "",
        #            "accountId": "351012345671"
        #        },
        #        "creditor": {
        #            "bankId": "",
        #            "accountId": "351092345672",
        #            "name": null,
        #            "address": null
        #        },
        #        "transactionAmount": {
        #            "amount": 3.55,
        #            "currency": "EUR",
        #            "currencyRate": "string"
        #        },
        #        "charges": null,
        #        "totalCharges": "1100.00",
        #        "endToEndId": "string",
        #        "paymentDetails": "test sandbox ",
        #        "terminalId": "string",
        #        "branch": "",
        #        "RUB": null,
        #        "executionDate": "14/02/2018",
        #        "valueDate": "14/02/2018",
        #        "totalDebitAmount": null
        #    }
        #}
        paymAuthNeeded=payment['authCodeNeeded']
        paym=payment['payment']
        paymentId=paym['paymentId']

    log_process_finish()
    return response

def boc_payment_authorize(access_token, subscriptionId, paymentId,authorization_code):
    api='payment_authorize'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,subscriptionId,api_params,paymentId)
    api_url=request_params['url']
    headers=request_params['headers']
    params=request_params['parameters']
    params.update({'subscriptionId': subscriptionId})    

    auth = {"transactionTime": api_params['currentTimeStamp'],"authCode": authorization_code}
    authData=json.dumps(auth)
    if api_params['debuglevel_two']>0:
        print('url-----',api_url)
        print('params----',params)
        print('headers---',headers)
        print('data------',authData)
    
    r = requests.post(api_url,headers=headers,params=params,data=authData)
    reply_code=r.status_code
    if api_params['debuglevel_two']>0:
        print('results---',r.status_code,r.text)

    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
        paymStatus=r.text
    else:
        #response = r.json()
        #{
        #  "code": "CLPT",
        #  "description": [
        #    " The transaction has passed all validations and was successfully posted in bank systems"
        #  ],
        #  "refNumber": "1524485123473408"
        #}
        reply_code=r.status_code
        response = r.json()
        paymStatus=response['code']
        paymRefNum=response['refNumber']
        paymStatusDesc=response['description']
    log_process_finish()
    return response

def boc_make_payment(access_token,subscriptionId,DBaccountId,CRaccountId,Amount,Currency,Details):
    api='make_payment'
    log_process_start(api)

    paymentId=None    
    api_params=boc_get_parameters(api)
    paym={'bankId':'?','accountId':DBaccountId,'transaction':{'amount':Amount,'currency':Currency,'currencyRate':''}}
    
    fundsavail=boc_payment_fundsavailability(access_token,subscriptionId,paym)
    if fundsavail != 1:
        return None

    signature=boc_payment_initiate(access_token, subscriptionId, DBaccountId ,CRaccountId,Amount,Currency,Details)
    if not signature:
        return None
    
    payment=boc_payment_create(access_token, subscriptionId, signature)
    if not payment:
        return None
    
    if api_params['debuglevel_three']>0:
        print('payment---',payment)

    paymAuthNeeded=payment['authCodeNeeded']
    paym=payment['payment']
    paymentId=paym['paymentId']
    paymstatus=paym['status']
    paymentRefNum=paymstatus['refNumber']
    paymentStatusCode=paymstatus['code']
    paymentStatusDesc=paymstatus['description'][0]

    if api_params['debuglevel_two']>0:
        print('paymAuthNeeded=',paymAuthNeeded)
        print('paymentId=',paymentId)
        print('paymentRefNum=',paymentRefNum)
        print('paymentStatusCode=',paymentStatusCode)
        print('paymentStatusDesc=',paymentStatusDesc)

##    if paymAuthNeeded==True:
##        result=boc_payment_authorize(access_token, subscriptionId, paymentId)
##        print(result)
##        if result:
##            paymentStatusCode=result['code']
##            paymRefNum=result['refNumber']
##            paymStatusDesc=result['description']
##            print('paymentStatusCode=',paymentStatusCode)
##            print('paymStatusDesc=',paymStatusDesc)
##            print('paymRefNum=',paymRefNum)
##        else:
##            print('@@@ERROR-not authorized')
##    else:
##        print('paymentId=',paymentId)
##        print('paymentRefNum=',paymentRefNum)
##        print('paymentStatusCode=',paymentStatusCode)
##        print('paymentStatusDesc=',paymentStatusDesc)

    log_process_finish()
    return payment

def boc_authorize_payment(access_token,subscriptionId,paymentId):
    api='authorize_payment'

    api_params=boc_get_parameters(api)
    result='?'
    payment_status=boc_get_payment_status(access_token,subscriptionId,paymentId)
    #payment_details=boc_get_payment_details(access_token,subscriptionId,paymentId)
    statusCode=payment_status['status']['code']
    #print(statusCode)
    if statusCode!='PNDG':
        result='this payment is not PNDG'
    else:
        msg="enter the OTP for payment id {paymentID}:".format(paymentID=paymentId)
        authorization_code = input(msg)

        authorization_result=boc_payment_authorize(access_token,subscriptionId,paymentId,authorization_code)
        print('authorization_result=',authorization_result)
        
        if authorization_result:
            paymStatus=authorization_result['code']
            paymRefNum=authorization_result['refNumber']
            paymStatusDesc=authorization_result['description']
            print('paymStatus=',paymStatus)
            print('paymStatusDesc=',paymStatusDesc[0])
            print('paymRefNum=',paymRefNum)
            result=json.dumps(paymStatus)+'-'+json.dumps(paymStatusDesc)+'-'+json.dumps(paymRefNum)
        else:
            result='ERROR-not authorized:'+error_text
            
    log_process_finish()
    return result         


################################################################
### create subscription apis                                 ###
################################################################
def boc_get_subscriptionId(access_token,SubscriptionRequest):   
    api='get_subscriptionId'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(access_token,'',api_params)
    api_url=request_params['url']
    headers=request_params['headers']
    headers.update({'app_name': api_params['app_Name']})
    params=request_params['parameters']
    r = requests.post(api_url,headers=headers,params=params,data=SubscriptionRequest)
    reply_code=r.status_code
    response = r.json()
    if not((r.status_code == requests.codes.ok) or (r.status_code == 201)):
        error_text=r.text
        error_code=1
        response=None
        subscriptionId=None
    else:
        subscriptionId = response['subscriptionId']
    log_process_finish()
    return subscriptionId
def boc_get_customer_Consent(subscriptionId):
    api='get_customerConsent'
    log_process_start(api)

    api_params=boc_get_parameters(api)

    url=api_params['endpoint']+"?"
    url=url+"response_type=code"
    url=url+"&redirect_uri="+api_params['redirect_uri']
    url=url+"&scope=UserOAuth2Security"
    url=url+"&client_id="+api_params['client_id']
    url=url+"&subscriptionid="+subscriptionId

    webbrowser.open(url, new=0)
    log_process_finish()
    return 1

def boc_update_subscription(subscriptionId,authorization_token,authorization_code,subscription_options):   
    api='update_subscription'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    request_params=boc_prepare_request_standard(authorization_token,'',api_params,subscriptionId)
    api_url=request_params['url']
    if api_params['debuglevel_three']>0:
        print('url-----',api_url)
    params=request_params['parameters']
    params.update({'subscriptionId': subscriptionId})    
    if api_params['debuglevel_three']>0:
        print('params----',params)

    headers=request_params['headers']
    if api_params['debuglevel_three']>0:
        print('headers---',headers)
    if api_params['debuglevel_three']>0:
        print('data------',subscription_options)
    
    r = requests.patch(api_url,headers=headers,params=params,data=subscription_options)
    if api_params['debuglevel_three']>0:
        print(r,r.json())

    reply_code=r.status_code
    response = r.json()
    if not r.status_code == requests.codes.ok:
        error_text=r.text
        error_code=1
        response=None
        updateStatus=None
    else:
        updateStatus=response['status']

    log_process_finish()
    return updateStatus
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
def wait_for_authorization():
    process='wait_for_user_authorization'
    log_process_start(process)

    authorization_code=None
    codefile = r'''c:\users\user\documents\code.txt'''
    try:
        os.remove(codefile)
    except:
        x=1
    n=0
    #print(n,'waiting....')
    while n<120:
        if ((n % 10) == 0):
            print(n,'waiting....')
            
        time.sleep(1) # Delay for 1 sec
        n=n+1
        #runServer()
        ok=0
        try:
            thefile = open(codefile, 'r')
            ok=1
        except:
            ok=0
        if ok==1:
            authorization_code=thefile.read()
            thefile.close
            print('---code_received---',authorization_code+'<--')
            n=99999    

    log_process_finish()
    return authorization_code
#=====================================================
def boc_create_subscription(SubscriptionData):   
    api='new_subscription'
    log_process_start(api)

    api_params=boc_get_parameters(api)

    access_token=boc_get_access_token()
    if not access_token:
        raise Exception(error_text)

    subscription_options=json.loads(SubscriptionData)
    SubscriptionData=json.dumps(subscription_options)

    subscriptionId=boc_get_subscriptionId(access_token,SubscriptionData)
    if not subscriptionId:
        print('ERROR:',error_text)
        return subscriptionId
              
    boc_get_customer_Consent(subscriptionId)
    authorization_code=wait_for_authorization()
    if not authorization_code:
        error_text='authorization NOT received'
        print('ERROR:',error_text)
        subscriptionId=None
        return subscriptionId

    if api_params['debuglevel_two']>0:
        print('subscriptionId=', subscriptionId)
        print('authorization_code=', authorization_code)
        
    #access_token=boc_get_access_token()
    authorization_token=boc_get_authorization_token(access_token,authorization_code)
    if not authorization_token:
        #raise Exception(error_text)
        print('ERROR:',error_text)
        SubscriptionDetails=boc_get_subscription_details(access_token,subscriptionId)
        accounts_list=SubscriptionDetails[0]['selectedAccounts']
        print ('selected_accounts=',accounts_list)
        subscriptionId=None
        return subscriptionId
    
    if api_params['debuglevel_two']>0:
        print('authorization_token=', authorization_token)

    SubscriptionDetails=boc_get_subscription_details(access_token,subscriptionId)
    selected_accounts=SubscriptionDetails[0]['selectedAccounts']
    accounts_options=SubscriptionDetails[0]['accounts']
    payments_options=SubscriptionDetails[0]['payments']
    if api_params['debuglevel_three']>0:
        print ('')
        print ('selected_accounts=',selected_accounts)
        print ('accounts_options=',accounts_options)
        print ('payments_accounts=',payments_options)
    
    NewSubscriptionData = "{\"selectedAccounts\":"+json.dumps(selected_accounts)+",\"accounts\":"+json.dumps(accounts_options)+",\"payments\":"+json.dumps(payments_options)+"}"
    subscriptionData=json.loads(NewSubscriptionData)
    subscription_options=json.dumps(subscriptionData)
    #subscription_options=json.dumps("{\"selectedAccounts\":[{\"accountId\":\"351012345671\"}],\"accounts\":{\"transactionHistory\":true,\"balance\":true,\"details\":true,\"checkFundsAvailability\":true},\"payments\":{\"limit\":64.36,\"currency\":\"EUR\",\"amount\":96.08}}")
    #subscription_options=json.dumps("{\"selectedAccounts\":[{\"accountId\":\"351012345671\"},{\"accountId\":\"351012345673\"},{\"accountId\":\"351012345674\"}],\"accounts\":{\"transactionHistory\":true,\"balance\":true,\"details\":true,\"checkFundsAvailability\":true},\"payments\":{\"limit\":64.36,\"currency\":\"EUR\",\"amount\":96.08}}")
    #less accounts ---subscription_options=json.dumps("{\"selectedAccounts\":[{\"accountId\":\"351012345671\"},{\"accountId\":\"351012345673\"}],\"accounts\":{\"transactionHistory\":true,\"balance\":true,\"details\":true,\"checkFundsAvailability\":true},\"payments\":{\"limit\":64.36,\"currency\":\"EUR\",\"amount\":96.08}}")

    if api_params['debuglevel_two']>0:
        print('')
        print('subscription_options=',subscription_options)
    
    subscription_status=boc_update_subscription(subscriptionId,authorization_token,authorization_code,subscription_options)
    if not subscription_status:
        print('error:',error_text)
        subscriptionId=None
        #raise Exception(error_text)
    else:    
        if api_params['debuglevel_two']>0:
            print('subscription_status=', subscription_status)
        
    log_process_finish()
    return subscriptionId

def clear_pending_subscriptions(accounts):
    api='clear_pending_subscriptions'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    customer_subscriptions=[]
    customer_accounts=set([])
    access_token=boc_get_access_token()
    a=0
    deleted=0
    for account_id in accounts:
        a=a+1
        #print('@@@customer account@@@',a,'account_id=',account_id,'-----')
        subscriptions=boc_get_account_subscriptions(access_token,account_id)
        if subscriptions:
            n=0
            for subscription in subscriptions:
                n=n+1
                subscription_id=subscription['subscriptionId']
                subscription_status=subscription['status']
                if subscription_status=='pending':
                    res=boc_delete_subscription(access_token, subscription_id)
                    if api_params['debuglevel_two']>0:
                        print (res)
                    deleted=deleted+1
    msg='{} pending subscriptions deleted'.format(deleted)
    log_process_finish()
    return msg

def clear_all_subscriptions(accounts):
    api='clear_active_subscriptions'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    customer_subscriptions=[]
    customer_accounts=set([])
    access_token=boc_get_access_token()
    a=0
    deleted=0
    for account_id in accounts:
        a=a+1
        #print('@@@customer account@@@',a,'account_id=',account_id,'-----')
        subscriptions=boc_get_account_subscriptions(access_token,account_id)
        if subscriptions:
            n=0
            for subscription in subscriptions:
                n=n+1
                subscription_id=subscription['subscriptionId']
                subscription_status=subscription['status']
                #if subscription_status=='pending':
                res=boc_delete_subscription(access_token, subscription_id)
                if api_params['debuglevel_two']>0:
                    print (res)
                deleted=deleted+1
    msg='{} subscriptions deleted'.format(deleted)
    log_process_finish()
    return msg

def get_customer_subscriptions(accounts,resultoption=''):
    api='get_customer_subscriptions'
    log_process_start(api)

    api_params=boc_get_parameters(api)
    customer_subscriptions=set([])
    customer_accounts=set([])
    customer_subscriptionsaccountsxref=set([])
    access_token=boc_get_access_token()
    a=0
    for account_id in accounts:
        a=a+1
        #print('@@@customer account@@@',a,'account_id=',account_id,'-----')
        subscriptions=boc_get_account_subscriptions(access_token,account_id)
        if subscriptions:
            #n=0
            #for subscription in subscriptions:
            #    n=n+1
            #    subscription_id=subscription['subscriptionId']
            #    subscription_status=subscription['status']
            #    subscription_accounts=boc_get_subscription_selectedAccounts(access_token,subscription_id)
            #    #print('   ',a,account_id,n,subscription_id,subscription_status,len(subscription_accounts))
            n=0
            for subscription in subscriptions:
                n=n+1
                subscription_id=subscription['subscriptionId']
                subscription_status=subscription['status']
                customer_subscriptions.add(subscription_id)
                subscription_accounts=boc_get_subscription_selectedAccounts(access_token,subscription_id)
                #print('      ',a,account_id,n,subscription_id,subscription_status,len(subscription_accounts))
                an=0
                for account in subscription_accounts:
                    an=an+1
                    #print('         ',a,n,an,'acct=',account['accountId'])
                    customer_accounts.add(account['accountId'])
                    xref=account['accountId']+'-->'+subscription_id+'-->'+subscription_status
                    customer_subscriptionsaccountsxref.add(xref)
                    
    if api_params['debuglevel_three']>0:
        print('#1#customer_accounts:')
        #print('#1#customer_accounts=',customer_accounts)
        n=0
        for account in sorted(customer_accounts):
            n=n+1
            print('   ',n,account)

        #print('#2#customer_subscriptions=',customer_subscriptions)
        print('#2#customer_subscriptions:')
        n=0
        for subscriptionid in sorted(customer_subscriptions):
            n=n+1
            #print('   ',n,subscriptionid)

        #print('#3#customer_subscriptionsaccountsxref=',customer_subscriptionsaccountsxref)
        print('#3#customer_subscriptionsaccountsxref:')
        n=0
        for xref in sorted(customer_subscriptionsaccountsxref):
            n=n+1
            #print('   ',n,xref)

    log_process_finish()
	
    if resultoption=='subscriptions':    
        return customer_subscriptions
    if resultoption=='accounts':    
        return customer_accounts
    if resultoption=='xref':    
        return customer_subscriptionsaccountsxref

    return customer_subscriptions

def check_subscriptions():
    process='check_subscriptions'
    log_process_start(process)
    ok=1
    errors=[]
    global master_configuration
    master_configuration=get_configuration()
    banks=get_configuration_param('customer_banks',master_configuration,'')
    log_process_value('banks',banks)
    for bankCodeName in banks:
        res=configuration_check(bankCodeName)
        if res != 'OK':
            error_text='ERROR:'+res
            log_process_error(error_text)
            errors.append(error_text)
            ok=0
            
    if ok==1:
        result='OK'
    else:
        result=json.dumps(errors)
        
    log_process_result('result',result)
    log_process_finish()
    return result
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def configuration_check(bankCodeName):
    process='configuration_check'
    log_process_start(process)
    log_process_input_param('bankCodeName',bankCodeName)
    #::::::::::::::::::::::::::::::::::::
    log_process_section_start('prologue')
    global master_configuration
    cif=get_configuration_param('cif',master_configuration,bankCodeName)
    payments_subscriptionID=get_configuration_param('subscription_payments',master_configuration,bankCodeName)
    accounts_subscriptionID=get_configuration_param('subscription_accounts',master_configuration,bankCodeName)
    accounts_accounts=get_configuration_param('subscription_accounts_accounts',master_configuration,bankCodeName)
    payments_accounts=get_configuration_param('subscription_payments_accounts',master_configuration,bankCodeName)
    log_process_section_finish()
    #::::::::::::::::::::::::::::::::::::
    if not accounts_subscriptionID:
        log_process_section_start('no_accounts_subscriptionID')

        access_token=boc_get_access_token()
        if not access_token:
            raise Exception(error_text)
        
        SubscriptionRequest="{\"accounts\":{\"transactionHistory\":true,\"balance\":true,\"details\":true,\"checkFundsAvailability\":false},\"payments\":{\"limit\":0.00,\"currency\":\"EUR\",\"amount\":0.00}}"
        subsID=boc_create_subscription(SubscriptionRequest)
        if subsID:
            log_process_value('new accounts subscription:', subsID)
            accounts=[]
            subscription_accounts=boc_get_subscription_Accounts(access_token,subsID)
            log_process_value('subscription_accounts=',subscription_accounts)
            a=0
            for account in subscription_accounts:
                a=a+1
                accountId=account['accountId']
                log_process_value('   ',a,accountId)
                accounts.add(accountId)
                
            acccountsList=json.dumps(accounts)
            log_process_value('accounts_accounts=',accountsList)
            update_customer_configuration(bankCodeName,'customer_subscriptions','subscription_accounts',subsID)
            update_customer_configuration(bankCodeName,'customer_subscriptions','subscription_accounts_accounts',accountsList)
            master_configuration=get_configuration()
            if not master_configuration:
                error_text='ERROR: can not retrieve master_configuration'
                log_process_error(error_text)
                #raise Exception(error_text)

            accounts_subscriptionID=get_configuration_param('subscription_accounts',master_configuration,bankCodeName)
            accounts_accounts=get_configuration_param('subscription_accounts_accounts',master_configuration,bankCodeName)
        log_process_section_finish()
    #::::::::::::::::::::::::::::::::::::
    if not payments_subscriptionID:
        log_process_section_start('no_payments_subscriptionID')
        access_token=boc_get_access_token()
        if not access_token:
            raise Exception(error_text)


        SubscriptionRequest="{\"accounts\":{\"transactionHistory\":true,\"balance\":true,\"details\":true,\"checkFundsAvailability\":true},\"payments\":{\"limit\":1000.00,\"currency\":\"EUR\",\"amount\":100.00}}"
        subsID=boc_create_subscription(SubscriptionRequest)
        if subsID:
            log_process_value('new payments subscription:', subsID)
            accounts=[]
            subscription_accounts=boc_get_subscription_Accounts(access_token,subsID)
            log_process_value('subscription_accounts=',subscription_accounts)
            a=0
            for account in subscription_accounts:
                a=a+1
                accountId=account['accountId']
                print('   ',a,accountId)
                accounts.add(accountId)

            acccountsList=json.dumps(accounts)
            log_process_value('payments_accounts=',accountsList)
            update_customer_configuration(bankCodeName,'customer_subscriptions','subscription_payments',subsID)
            update_customer_configuration(bankCodeName,'customer_subscriptions','subscription_payments_accounts',acccountsList)
            master_configuration=get_configuration()
            if not master_configuration:
                error_text='ERROR: can not retrieve master_configuration'
                log_process_error(error_text)
                #raise Exception(error_text)

            payments_subscriptionID=get_configuration_param('subscription_payments',master_configuration,bankCodeName)
            payments_accounts=get_configuration_param('subscription_payments_accounts',master_configuration,bankCodeName)
        log_process_section_finish()
    #::::::::::::::::::::::::::::::::::::
    if not accounts_accounts:
        log_process_section_start('no_accounts')
        access_token=boc_get_access_token()
        if not access_token:
            raise Exception(error_text)

        subsID=accounts_subscriptionID
        if subsID:
            accounts=[]
            subscription_accounts=boc_get_subscription_Accounts(access_token,subsID)
            log_process_value('subscription_accounts=',subscription_accounts)
            a=0
            for account in subscription_accounts:
                a=a+1
                accountId=account['accountId']
                print('   ',a,accountId)
                accounts.append(accountId)

            acccountsList=json.dumps(accounts)            
            log_process_value('accounts_accounts=',acccountsList)
            
            update_customer_configuration(bankCodeName,'customer_subscriptions','subscription_accounts_accounts',acccountsList)
            master_configuration=get_configuration()
            if not master_configuration:
                error_text='ERROR: can not retrieve master_configuration'
                log_process_error(error_text)
                #raise Exception(error_text)

            accounts_accounts=get_configuration_param('subscription_accounts_accounts',master_configuration,bankCodeName)
        log_process_section_finish()
    #::::::::::::::::::::::::::::::::::::
    if not payments_accounts:
        log_process_section_start('no_payments_accounts')
        access_token=boc_get_access_token()
        if not access_token:
            raise Exception(error_text)
        subsID=payments_subscriptionID
        if subsID:
            accounts=[]
            subscription_accounts=boc_get_subscription_Accounts(access_token,subsID)
            log_process_value('subscription_accounts=',subscription_accounts)
            a=0
            for account in subscription_accounts:
                a=a+1
                accountId=account['accountId']
                print('   ',a,accountId)
                accounts.append(accountId)

            acccountsList=json.dumps(accounts)            
            log_process_value('payment_accounts=',acccountsList)
            update_customer_configuration(bankCodeName,'customer_subscriptions','subscription_payments_accounts',acccountsList)
            master_configuration=get_configuration()
            if not master_configuration:
                error_text='ERROR: can not retrieve master_configuration'
                log_process_error(error_text)
                #raise Exception(error_text)

            payments_accounts=get_configuration_param('subscription_payments_accounts',master_configuration,bankCodeName)
        log_process_section_finish()

    #::::::::::::::::::::::::::::::::::::
    log_process_section_start('epilogue')
    cif=get_configuration_param('cif',master_configuration,bankCodeName)
    payments_subscriptionID=get_configuration_param('subscription_payments',master_configuration,bankCodeName)
    accounts_subscriptionID=get_configuration_param('subscription_accounts',master_configuration,bankCodeName)
    accounts_accounts=get_configuration_param('subscription_accounts_accounts',master_configuration,bankCodeName)
    payments_accounts=get_configuration_param('subscription_payments_accounts',master_configuration,bankCodeName)

    log_process_value('cif=',cif)
    log_process_value('payments_subscriptionID=',payments_subscriptionID)
    log_process_value('payments_accounts=',payments_accounts)
    log_process_value('accounts_subscriptionID=',accounts_subscriptionID)
    log_process_value('accounts_accounts=',accounts_accounts)

    if payments_subscriptionID and payments_accounts and accounts_subscriptionID and accounts_accounts:
        result='OK'
    else:
        result='missing subscriptions for bank '+bankCodeName    
    log_process_section_finish()
    #::::::::::::::::::::::::::::::::::::

    log_process_result('result',result)
    log_process_finish()
    return result
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

##################################################
##################################################
##################################################
##################################################
##################################################
##################################################
##################################################
##################################################
if __name__ == '__main__':
    bankCodeName='bankofcyprus'
    #environment='development'
    debuglevel_one=0
    debuglevel_two=0
    debuglevel_three=0
    debuglevel_four=0
    response=''
    error_code=0
    error_text=''
    reply_code=0

    master_configuration=get_configuration()
    if not master_configuration:
        error_text='ERROR: can not retrieve master_configuration'
        raise Exception(error_text)
    #debuglevel_one=1
    #access_token=boc_get_access_token()
    #if not access_token:
    #    raise Exception(error_text)

    res=check_subscriptions()
    if res != 'OK':
        error_text='ERROR:'+res
        raise Exception(error_text)
        sys.exit(0)

    payments_subscriptionID=get_configuration_param('subscription_payments',master_configuration,bankCodeName)
    accounts_subscriptionID=get_configuration_param('subscription_accounts',master_configuration,bankCodeName)
    accounts_accounts=get_configuration_param('subscription_accounts_accounts',master_configuration,bankCodeName)
    payments_accounts=get_configuration_param('subscription_payments_accounts',master_configuration,bankCodeName)
    if debuglevel_three>=0:
        print('=================')
        print(bankCodeName,'payments_subscriptionID=',payments_subscriptionID)
        print(bankCodeName,'payments_accounts=',payments_accounts)
        print(bankCodeName,'accounts_subscriptionID=',accounts_subscriptionID)
        print(bankCodeName,'accounts_accounts=',accounts_accounts)
        print('=================')
    
    #access_token=boc_get_access_token()
    #if not access_token:
    #    raise Exception(error_text)
    print('ALL OK - PROCEED')

    
    access_token=boc_get_access_token()
    if not access_token:
        raise Exception(error_text)

    if 1==1:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('                 accounts');
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        subscription_accounts=boc_list_accounts(access_token,accounts_subscriptionID)
        print(subscription_accounts)
        a=0
        for account in subscription_accounts:
            a=a+1
            accountID=account['accountId']
            print('   ',a,accountID)
        
            account_details=boc_get_account_details(access_token,accounts_subscriptionID,accountID)
            print('   ','account_details=',account_details)

            account_balances=boc_get_account_balances(access_token,accounts_subscriptionID,accountID)
            print('   ','account_balances=',account_balances)

            account_transactions=boc_get_account_transactions(access_token,accounts_subscriptionID,accountID)
            print('      ','account_transactions=',account_transactions)
    
    if 1==2:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('                 create subscriptions');
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

        #res=get_customer_subscriptions(my_accounts)
        #print('1---customer subscriptions=',res)
        msg=clear_pending_subscriptions(my_accounts)
        print(msg)
        #msg=clear_all_subscriptions(my_accounts)
        #print(msg)

        SubscriptionRequest="{\"accounts\":{\"transactionHistory\":true,\"balance\":true,\"details\":true,\"checkFundsAvailability\":true},\"payments\":{\"limit\":64.36373117,\"currency\":\"EUR\",\"amount\":96.08441354}}"
        #subscription_options=json.loads(SubscriptionRequest)
        #SubscriptionRequest=json.dumps(subscription_options)
        subsID=boc_create_subscription(SubscriptionRequest)
        if subsID:
            print('new subscription:', subsID)
            
        res=get_customer_subscriptions(my_accounts)
        print('customer subscriptions=',res)
        sys.exit(0)

    if 1==2:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('                 subscriptions');
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        subscriptionId='Subid000001-1532955588265'
        subscription_details=boc_get_subscription_details(access_token,subscriptionId)
        print('subscription_details=',subscription_details)
        #sys.exit(0)
##
##        subscriptionId='Subid000001-1532936259944'
##        res=boc_delete_subscription(access_token, subscriptionId)
##        print (res)
##
##        subscriptionId='Subid000001-1532594181330'
##        res=boc_delete_subscription(access_token, subscriptionId)
##        print (res)
##
##        my_accounts=['351012345671','351092345672','351012345673','351012345674','351012345675']
##        msg=clear_pending_subscriptions(my_accounts)
##        print(msg)

        SubscriptionRequest="{\"accounts\":{\"transactionHistory\":true,\"balance\":true,\"details\":true,\"checkFundsAvailability\":true},\"payments\":{\"limit\":64.36373117,\"currency\":\"EUR\",\"amount\":96.08441354}}"
        subsID=boc_create_subscription(SubscriptionRequest)
        if subsID:
            print('new subscription:', subsID)

        subscriptions=get_customer_subscriptions(my_accounts,'subscriptions')
        #print('customer_subscriptions=',get_customer_subscriptions(my_accounts,'subscriptions'))
        n=0
        for subscriptionId in subscriptions:
            n=n+1
            subscription_details=boc_get_subscription_details(access_token,subscriptionId)
            print(n,'subscription_details=',subscription_details)

        
        #print('customer_accounts=',get_customer_subscriptions(my_accounts,'accounts'))
        #print('customer_accounts_xref=',get_customer_subscriptions(my_accounts,'xref'))

        sys.exit(0) ##stop run
        
    if 1==2:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('                 accounts');
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        account_id='351012345671'
        subscription_Id=None
        subscriptions=boc_get_account_subscriptions(access_token,account_id)
        n=0
        for subscription in subscriptions:
            n=n+1
            subscription_id=subscription['subscriptionId']
            subscription_status=subscription['status']
            print(n,subscription_id,subscription_status)

        if subscription_id:
            subscription_accounts=boc_list_accounts(access_token,subscription_id)
            print(subscription_accounts)
            a=0
            for account in subscription_accounts:
                a=a+1
                account_Id=account['accountId']
                print('   ',n,a,account_Id)
            
                account_details=boc_get_account_details(access_token, subscription_id, account_Id)
                print('      ','account_details=',account_details)

                account_balances=boc_get_account_balances(access_token, subscription_id, account_Id)
                print('      ','account_balances=',account_balances)

                account_transactions=boc_get_account_transactions(access_token, subscription_id, account_Id)
                print('      ','account_transactions=',account_transactions)

    if 1==2:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('                 payments');
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
##        payments_subscriptionID=get_configuration_param('subscription_payments',master_configuration,bankCodeName)
##        accounts_subscriptionID=get_configuration_param('subscription_accounts',master_configuration,bankCodeName)
##        accounts_accounts=get_configuration_param('subscription_accounts_accounts',master_configuration,bankCodeName)
##        payments_accounts=get_configuration_param('subscription_payments_accounts',master_configuration,bankCodeName)

        subscription_accounts=boc_list_accounts(access_token,payments_subscriptionID)
        #print(subscription_accounts)
        #sys.exit(0)
        allPayments=[]
        a=0
        for account in subscription_accounts:
            #print('====',account)
            
            a=a+1
            accountID=account['accountId']
            #print('   ',a,accountID)
            
            payments=boc_get_payments(access_token,payments_subscriptionID,accountID)
            if payments:
                for payment in payments:
                    allPayments.append(payment)
        
        n=0
        for payment in allPayments:
            n=n+1
            paymentID=payment['paymentId']
            DBaccountID=payment['debtor']['accountId']
            CRaccountID=payment['creditor']['accountId']
            CRaccountName=payment['creditor']['name']
            paymentRefNum=payment['status']['refNumber']
            paymentStatusCode=payment['status']['code']
            paymentStatusDesc=payment['status']['description'][0]

            #paystatus=payment['status']
            #print(n,payment_Id)

            #payment_delete=boc_delete_payment(access_token,payments_subscriptionID,paymentID)
            #print(n,'payment_delete=',payment_delete)

            #payment_details=boc_get_payment_details(access_token,payments_subscriptionID,paymentID)
            #print(n,'payment_details=',payment_details)

            #payment_authorize=boc_payment_authorize(access_token, payments_subscriptionID,paymentID)
            #print(n,'payment_authorize=',payment_authorize)


            print(n,paymentID,paymentStatusCode,paymentRefNum,DBaccountID,CRaccountID)
            #print(n,'paymentRefNum=',paymentRefNum)
            #print(n,'paymentStatusCode=',paymentStatusCode)
            #print(n,'paymentStatusDesc=',paymentStatusDesc)
        
        print('-----------------')
        #sys.exit(0)

        paymentID=None
        DBaccountId='351012345671'
        CRaccountId='351092345672'
        Amount=12.23
        Currency='EUR'
        Details='pay zorbas'
        payment=boc_make_payment(access_token,payments_subscriptionID,DBaccountId,CRaccountId,Amount,Currency,Details)
        if not payment:
            print(error_text)
        else:
            paymAuthNeeded=payment['authCodeNeeded']
            paymentID=payment['payment']['paymentId']
            paymstatus=payment['payment']['status']
            paymentRefNum=payment['payment']['status']['refNumber']
            paymentStatusCode=payment['payment']['status']['code']
            paymentStatusDesc=payment['payment']['status']['description'][0]
            print(paymentStatusCode)
            
            payment_status=boc_get_payment_status(access_token,payments_subscriptionID,paymentID)
            payment_details=boc_get_payment_details(access_token,payments_subscriptionID,paymentID)

            print('paymAuthNeeded=',paymAuthNeeded)
            print('paymentID=',paymentID)
            print('paymentRefNum=',paymentRefNum)
            print('paymentStatusCode=',paymentStatusCode)
            print('paymentStatusDesc=',paymentStatusDesc)
        print('-----------------')
        if paymentID:
            res=boc_authorize_payment(access_token,payments_subscriptionID,paymentID)
            print('####payment result####',res)
        print('-----------------')
    
