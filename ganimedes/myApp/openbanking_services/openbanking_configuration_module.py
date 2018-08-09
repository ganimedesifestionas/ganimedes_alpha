import json
import time
import datetime
import webbrowser
import os
import sys
from openbanking_utilities_module import log_process_start,log_process_finish,log_process_input_param,log_process_result,log_process_value
from openbanking_utilities_module import log_process_section_start,log_process_section_finish,log_http_request_result,log_process_error
from openbanking_globals import *
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::                   CONFIGURATION                     :::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def get_configuration():
    process='get_configuration'
    log_process_start(process)

    app_config=read_application_configuration()
    if not app_config:
        initialize_configuration_application(environment)
        app_config=read_application_configuration()
    if not app_config:
        error_text='application config file not found'
        log_process_error(error_text)

    cust_config=read_customer_configuration()
    if not cust_config:
        initialize_configuration_customer(environment)
        cust_config=read_customer_configuration()
    if not cust_config:
        error_text='customer config file not found'
        log_process_error(error_text)

    if error_code==0:
        master_configuration={}
        master_configuration.update(app_config)
        master_configuration.update(cust_config)
        log_process_result('master_configuration',master_configuration)
    else:
        master_configuration=None
        log_process_result('master_configuration is empty')
        
    log_process_finish(process)
    return(master_configuration)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def initialize_configuration():
    process='initialize_configuration'
    log_process_start(process)
    initialize_configuration_application(environment)
    initialize_configuration_customer(environment)
    log_process_finish(process)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def initialize_configuration_application(environment='sandbox'):
    process='build_application_configuration'
    log_process_start(process)
    log_process_input_param('environment',environment)

    if environment=='sandbox':
        config={    
             'environment':environment
            ,'application_name':'qrp'
            ,'redirect_uri':'http://localhost:5555/authorization'
            ,'correlationId':'ganimedes_ABC001'
            ,'application_banks':['bankofcyprus','hellenicbank']
            ,'bankofcyprus':{
                'bankID':'BOC'
                ,'bankName':'Bank of Cyprus'
                ,'client_id':'52ee828e-a18e-4560-bfed-2d5158e9a507'
                ,'client_secret':'iV7dQ4jH7oJ5pX4fT7nM4lR5sT1bN2oJ2bU1kW5vM7mQ4kB7rV'
                ,'api_uri':'https://sandbox-apis.bankofcyprus.com/'
                ,'redirect_uri':'http://localhost:5555/authorization'
                ,'app_name':'qrp'
                ,'tppId':'singpaymentdata'
                ,'journeyId':'123456789'
                ,'lang':''
            }
            ,'hellenicbank':{
                'bankID':'HBC'
                ,'bankName':'Hellenic'
                ,'client_id':'52ee828e-a18e-4560-bfed-2d5158e9a507'
                ,'client_secret':'iV7dQ4jH7oJ5pX4fT7nM4lR5sT1bN2oJ2bU1kW5vM7mQ4kB7rV'
                ,'api_uri':'https://sandbox-apis.bankofcyprus.com/'
                ,'redirect_uri':'http://localhost:5555/authorization'
                ,'app_name':'qrp'
                ,'tppId':'singpaymentdata'
                ,'journeyId':'123456789'
                ,'lang':''
            }
            ,'originUserId':'1524'
            ,'originSourceId':''
            ,'originChannelId':''
            ,'originDeptId':''
            ,'originEmployeeId':''
            ,'originTerminalId':''
            ,'customer_banks':['bankofcyprus']
            ,'customer_subscriptions':{
                'bankofcyprus':{'cif':'12345','subscription_payments':'','subscription_accounts':'','subscription_payments_accounts':'','subscription_accounts_accounts':''}
                }     
        }
    if environment=='development':
        config={    
             'environment':environment
            ,'application_name':'qrp'
            ,'redirect_uri':'http://localhost:5555/authorization'
            ,'correlationId':'ganimedes_ABC001'
            ,'application_banks':['bankofcyprus','hellenicbank']
            ,'bankofcyprus':{
                'bankID':'BOC'
                ,'bankName':'Bank of Cyprus'
                ,'client_id':'52ee828e-a18e-4560-bfed-2d5158e9a507'
                ,'client_secret':'iV7dQ4jH7oJ5pX4fT7nM4lR5sT1bN2oJ2bU1kW5vM7mQ4kB7rV'
                ,'api_uri':'https://sandbox-apis.bankofcyprus.com/'
                ,'redirect_uri':'http://localhost:5555/authorization'
                ,'app_name':'qrp'
                ,'tppId':'singpaymentdata'
                ,'journeyId':'123456789'
                ,'lang':''
            }
            ,'hellenicbank':{
                'bankID':'HBC'
                ,'bankName':'Hellenic'
                ,'client_id':'52ee828e-a18e-4560-bfed-2d5158e9a507'
                ,'client_secret':'iV7dQ4jH7oJ5pX4fT7nM4lR5sT1bN2oJ2bU1kW5vM7mQ4kB7rV'
                ,'api_uri':'https://sandbox-apis.bankofcyprus.com/'
                ,'redirect_uri':'http://localhost:5555/authorization'
                ,'app_name':'qrp'
                ,'tppId':'singpaymentdata'
                ,'journeyId':'123456789'
                ,'lang':''
            }
            ,'originUserId':'1524'
            ,'originSourceId':''
            ,'originChannelId':''
            ,'originDeptId':''
            ,'originEmployeeId':''
            ,'originTerminalId':''
            ,'customer_banks':['bankofcyprus']
            ,'customer_subscriptions':{
                'bankofcyprus':{'cif':'12345','subscription_payments':'','subscription_accounts':'','subscription_payments_accounts':'','subscription_accounts_accounts':''}
                }     
        }
    if environment=='production':
        config={    
             'environment':environment
            ,'application_name':'qrp'
            ,'redirect_uri':'http://localhost:5555/authorization'
            ,'correlationId':'ganimedes_ABC001'
            ,'application_banks':['bankofcyprus','hellenicbank']
            ,'bankofcyprus':{
                'bankID':'BOC'
                ,'bankName':'Bank of Cyprus'
                ,'client_id':'52ee828e-a18e-4560-bfed-2d5158e9a507'
                ,'client_secret':'iV7dQ4jH7oJ5pX4fT7nM4lR5sT1bN2oJ2bU1kW5vM7mQ4kB7rV'
                ,'api_uri':'https://sandbox-apis.bankofcyprus.com/'
                ,'redirect_uri':'http://localhost:5555/authorization'
                ,'app_name':'qrp'
                ,'tppId':'singpaymentdata'
                ,'journeyId':'123456789'
                ,'lang':''
            }
            ,'hellenicbank':{
                'bankID':'HBC'
                ,'bankName':'Hellenic'
                ,'client_id':'52ee828e-a18e-4560-bfed-2d5158e9a507'
                ,'client_secret':'iV7dQ4jH7oJ5pX4fT7nM4lR5sT1bN2oJ2bU1kW5vM7mQ4kB7rV'
                ,'api_uri':'https://sandbox-apis.bankofcyprus.com/'
                ,'redirect_uri':'http://localhost:5555/authorization'
                ,'app_name':'qrp'
                ,'tppId':'singpaymentdata'
                ,'journeyId':'123456789'
                ,'lang':''
            }
            ,'originUserId':'1524'
            ,'originSourceId':''
            ,'originChannelId':''
            ,'originDeptId':''
            ,'originEmployeeId':''
            ,'originTerminalId':''
            ,'customer_banks':['bankofcyprus']
            ,'customer_subscriptions':{
                'bankofcyprus':{'cif':'12345','subscription_payments':'','subscription_accounts':'','subscription_payments_accounts':'','subscription_accounts_accounts':''}
                }     
        }

    configString=json.dumps(config)
    log_process_result('application configuration',configString)

    cfgfile=configuration_file('app',environment)
    with open(cfgfile, 'w') as configfile:
        configfile.write(configString)
    log_process_finish(process)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def initialize_configuration_customer(environment='sandbox'):
    process='build_customer_configuration'
    log_process_start(process)
    log_process_input_param('environment',environment)
    config={
         'originUserId':'1524'
        ,'originSourceId':''
        ,'originChannelId':''
        ,'originDeptId':''
        ,'originEmployeeId':''
        ,'originTerminalId':''
        ,'customer_banks':['bankofcyprus']
        ,'customer_subscriptions':{
            'bankofcyprus':{'cif':'','subscription_payments':'','subscription_accounts':'','subscription_payments_accounts':'','subscription_accounts_accounts':''}
            }
        }
    configString=json.dumps(config)    
    log_process_result('customer configuration',configString)
    cfgfile=configuration_file('cus',environment)
    with open(cfgfile, 'w') as configfile:
        configfile.write(configString)

    log_process_finish(process)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def update_customer_configuration(bankCodeName,group,what,value):
    process='update_customer_configuration'
    log_process_start(process)

    log_process_input_param('thisbank',bankCodeName)
    log_process_input_param('group',group)
    log_process_input_param('what',what)
    log_process_input_param('value',value)

    config=read_customer_configuration()
    log_process_value('config before',config)

    xvalue=value
    if what=='customer_banks':
        try:
          x=set(config[what])
          x.add(value)
          xvalue=x
        except:
          x=set([])
          x.add(value)
          xvalue=x

    if group=='customer_subscriptions':
        try:
            x1=config['customer_subscriptions']
        except:
            config.update({'customer_subscriptions':''})
            
        try:
            x1=config['customer_subscriptions'][bankCodeName]
        except:
            config.update({'customer_subscriptions':bankCodeName})
        
        x=config['customer_subscriptions'][bankCodeName]
        x.update({what:value})
        xx=config['customer_subscriptions']
        xx.update({bankCodeName:x})
        what='customer_subscriptions'
        xvalue=xx

    config.update({what:xvalue})
    configString=json.dumps(config)    
    log_process_result('config after',configString)

    cfgfile=configuration_file('cus',environment)
    with open(cfgfile, 'w') as configfile:
        configfile.write(configString)
    log_process_finish(process)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def update_application_configuration(bankCodeName,group,what,value):
    process='update_application_configuration'
    log_process_start(process)

    log_process_input_param('thisbank',bankCodeName)
    log_process_input_param('group',group)
    log_process_input_param('what',what)
    log_process_input_param('value',value)

    config=read_application_configuration()
    xvalue=value
    if what=='application_banks' or group=='application_banks':
        try:
          x=set(config['application_banks'])
          x.add(value)
          xvalue=x
        except:
          x=set([])
          x.add(value)
          xvalue=x

    if group=='bank':
        try:
            x1=config[bankCodeName]
        except:
            config.update({bankCodeName:''})
            
        x=config[bankCodeName]
        x.update({what:value})
        what=bankCodeName
        xvalue=x

    config.update({what:xvalue})
    configString=json.dumps(config)
    log_process_result('config after',configString)

    cfgfile=configuration_file('app',environment)
    with open(cfgfile, 'w') as configfile:
        configfile.write(configString)

    log_process_finish(process)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def read_application_configuration():
    process='read_application_configuration'
    log_process_start(process)
    config=None
    configString=None
    cfgfile=configuration_file('app',environment)
    with open(cfgfile, 'r') as configfile:
        configString=configfile.read()

    if configString:
        config=json.loads(configString)
    log_process_result('application_configuration',config)
    log_process_finish(process)
    return config
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def read_customer_configuration():
    process='read_customer_configuration'
    log_process_start(process)
    config=None
    configString=None
    cfgfile=configuration_file('cus',environment)
    with open(cfgfile, 'r') as configfile:
        configString=configfile.read()

    if configString:
        config=json.loads(configString)
    log_process_result('customer_configuration',config)
    log_process_finish(process)
    return config
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def get_configuration_param(what,configuration,thisbank):
    process='get_configuration_param'
    log_process_start(process)
    log_process_input_param('thisbank',thisbank,0)
    log_process_input_param('what',what,0)
    log_process_input_param('from configuration',configuration,0)
    try:
        paramvalue=configuration[what]
    except:
        paramvalue=None
    if paramvalue==None:
        try:
            paramvalue=configuration[thisbank][what]
        except:
            paramvalue=None
    if paramvalue==None:
        try:
            paramvalue=configuration['customer_subscriptions'][thisbank][what]
        except:
            paramvalue=None

    log_process_result(what,paramvalue,0,process+'---'+thisbank+'---')
    log_process_finish(process)
    return paramvalue
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def configuration_file(what,environment):
    cfgfile_name=what+'_'+environment+'.cfg'
    cfgfile_name=cfgfile_name.lower()
    return(cfgfile_name)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
############################################################
############################################################
############################################################
if __name__ == '__main__':
    master_configuration=get_configuration()
    if not master_configuration:
        error_text='ERROR: can not retrieve master_configuration'
        raise Exception(error_text)
    #update_application_configuration('','','environment',environment)    
    #payments_subscriptionID=get_configuration_param('subscription_payments',master_configuration,bankCodeName)
    #accounts_subscriptionID=get_configuration_param('subscription_accounts',master_configuration,bankCodeName)
    #accounts_accounts=get_configuration_param('subscription_accounts_accounts',master_configuration,bankCodeName)
    #payments_accounts=get_configuration_param('subscription_payments_accounts',master_configuration,bankCodeName)
##    if debuglevel_four>=0:
##        print('=================')
##        print(bankCodeName,'payments_subscriptionID=',payments_subscriptionID)
##        print(bankCodeName,'payments_accounts=',payments_accounts)
##        print(bankCodeName,'accounts_subscriptionID=',accounts_subscriptionID)
##        print(bankCodeName,'accounts_accounts=',accounts_accounts)
##        print('=================')
##    print('ALL OK - PROCEED')

