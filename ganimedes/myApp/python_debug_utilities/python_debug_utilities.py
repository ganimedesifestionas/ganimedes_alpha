#import json
#import time
#import datetime
#import os
import sys
import inspect

###GLOBALS
global globalProcessStack
global globalDebugConfig
global globalDebugLevel
global globalDebugLevelStartFinish
global globalDebugLevelSection
global globalDebugLevelMessage
global globalDebugLevelError
global globalDebugLevelInputParams
global globalDebugLevelValue
global globalDebugLevelResults
global globalDebugLevelHttp
try:
    globalDebugLevel=globalDebugLevel+0
except:
    globalDebugLevel=1
try:
    globalDebugLevelStartFinish=globalDebugLevelStartFinish+0
except:
    globalDebugLevelStartFinish=1
try:
    globalDebugLevelSection=globalDebugLevelSection+0
except:
    globalDebugLevelSection=1
try:
    globalDebugLevelError=globalDebugLevelError+0
except:
    globalDebugLevelError=1
try:
    globalDebugLevelMessage=globalDebugLevelMessage+0
except:
    globalDebugLevelMessage=1
try:
    globalDebugLevelInputParam=globalDebugLevelInputParam+0
except:
    globalDebugLevelInputParam=1
try:
    globalDebugLevelValue=globalDebugLevelValue+0
except:
    globalDebugLevelValue=1
try:
    globalDebugLevelResults=globalDebugLevelResults+0
except:
    globalDebugLevelResults=1
try:
    globalDebugLevelHttp=globalDebugLevelHttp+0
except:
    globalDebugLevelHttp=1
   
globalDebugConfig={
    'globalDebugLevel':globalDebugLevel
    ,'globalDebugLevelStartFinish':globalDebugLevelStartFinish
    ,'globalDebugLevelSection':globalDebugLevelSection
    ,'globalDebugLevelError':globalDebugLevelError
    ,'globalDebugLevelMessage':globalDebugLevelMessage
    ,'globalDebugLevelInputParam':globalDebugLevelInputParam
    ,'globalDebugLevelValue':globalDebugLevelValue
    ,'globalDebugLevelResults':globalDebugLevelResults
    ,'globalDebugLevelHttp':globalDebugLevelHttp
    }
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::: DEBUG UTILITIES                                     :::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class myRoute:
    def __init__(self,parRouteName='',parRequest=None):
        if not parRouteName:
            parRouteName=inspect.stack()[1][3]
        self.process_type = 'route'
        self.module = 'routes'
        self.service_name=parRouteName
        self.return_code = 0
        self.error_code = 0
        self.result = []
        self.message = ''
        self.messages = []
        self.request=parRequest
        self.input_params=[]
        self.local_vars=[]
        self.sections=[]

    def start(self,parLogLevel=1):
        print('************************************************')
        log_process_route_start(self,parLogLevel)
        print('************************************************')
    def finish(self):
        log_process_finish(self)
        print('************************************************')
    def input_param(self,parParamName,parParamValue,parlogLevel=1):
        varParam={parParamName:parParamValue}
        self.input_params.extend(varParam)
        log_process_input_param(parParamName,parParamValue,parlogLevel)
    def localVar(self,parVarName,parVarValue,parlogLevel=1):
        varLocalVar={parVarName:parVarValue}
        self.local_vars.extend(varLocalVar)
        log_process_value(parVarName,parVarValue,parlogLevel)
    def message(self,parErrorCode,parMessage,parLogLevel=1):
        self.message=parMessage
        self.messages.extend(parMessage)
        log_process_message('warning',parMessage,parLogLevel)
    def error(self,parErrorCode,parErrorMessage,parLogLevel=1):
        self.message=parErrorMessage
        self.error_code=parErrorCode
        self.return_code=0
        log_process_error(self.message,parLogLevel)
        #log_process_finish(self)

    def set_result(self,parResult,parMessage='OK'):
        self.result=parResult
        self.message=parMessage
        self.return_code=1
        self.error_code=0

    def log_results(self,parlogLevelRetCode=1,parlogLevelErrCode=1,parlogLevelMessage=1,parlogLevelResult=1,parlogLevelWarnings=1):
        log_process_result('return_code',self.return_code,parlogLevelRetCode)
        log_process_result('error_code',self.error_code,parlogLevelErrCode)
        log_process_result('message',self.message,parlogLevelMessage)
        log_process_result('result',self.result,parlogLevelResult)
        for message in self.messages:
            log_process_result('warning',message,parlogLevelWarnings)

    dumps = lambda self: repr(self)
    __str__ = lambda self: self.dumps()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class myServiceBusService:
    def __init__(self,parServiceName='',parRequest=None):
        if not parServiceName:
            parServiceName=inspect.stack()[1][3]
        self.process_type = 'servicebus_service'
        self.module = 'service_bus'
        self.service_name=parServiceName
        self.return_code = 0
        self.error_code = 0
        self.result = []
        self.message = ''
        self.messages = []
        self.request=parRequest
        self.input_params=[]
        self.local_vars=[]
        self.sections=[]

    def start(self,parLogLevel=1):
        log_process_start(self,parLogLevel)
    def finish(self):
        log_process_finish(self)
    def input_param(self,parParamName,parParamValue,parlogLevel=1):
        varParam={parParamName:parParamValue}
        self.input_params.extend(varParam)
        log_process_input_param(parParamName,parParamValue,parlogLevel)
    def localVar(self,parVarName,parVarValue,parlogLevel=1):
        varLocalVar={parVarName:parVarValue}
        self.local_vars.extend(varLocalVar)
        log_process_value(parVarName,parVarValue,parlogLevel)
    def message(self,parErrorCode,parMessage,parLogLevel=1):
        self.message=parMessage
        self.messages.extend(parMessage)
        log_process_message('warning',parMessage,parLogLevel)
    def error(self,parErrorCode,parErrorMessage,parLogLevel=1):
        self.message=parErrorMessage
        self.error_code=parErrorCode
        self.return_code=0
        log_process_error(self.message,parLogLevel)
        #log_process_finish(self)

    def set_result(self,parResult,parMessage='OK'):
        self.result=parResult
        self.message=parMessage
        self.return_code=1
        self.error_code=0

    def log_results(self,parlogLevelRetCode=1,parlogLevelErrCode=1,parlogLevelMessage=1,parlogLevelResult=1,parlogLevelWarnings=1):
        log_process_result('return_code',self.return_code,parlogLevelRetCode)
        log_process_result('error_code',self.error_code,parlogLevelErrCode)
        log_process_result('message',self.message,parlogLevelMessage)
        log_process_result('result',self.result,parlogLevelResult)
        for message in self.messages:
            log_process_result('warning',message,parlogLevelWarnings)

    dumps = lambda self: repr(self)
    __str__ = lambda self: self.dumps()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class myOpenBankingService:
    def __init__(self,parServiceName='',parRequest=None):
        if not parServiceName:
            parServiceName=inspect.stack()[1][3]
        self.process_type = 'openbanking_service'
        self.module = 'openbanking_services_functions'
        self.service_name=parServiceName
        self.return_code = 0
        self.error_code = 0
        self.result = []
        self.message = ''
        self.messages = []
        self.request=parRequest
        self.input_params=[]
        self.local_vars=[]
        self.sections=[]

    def start(self,parLogLevel=1):
        log_process_start(self,parLogLevel)
    def finish(self):
        log_process_finish(self)
    def input_param(self,parParamName,parParamValue,parlogLevel=1):
        varParam={parParamName:parParamValue}
        self.input_params.extend(varParam)
        log_process_input_param(parParamName,parParamValue,parlogLevel)
    def localVar(self,parVarName,parVarValue,parlogLevel=1):
        varLocalVar={parVarName:parVarValue}
        self.local_vars.extend(varLocalVar)
        log_process_value(parVarName,parVarValue,parlogLevel)
    def message(self,parErrorCode,parMessage,parLogLevel=1):
        self.message=parMessage
        self.messages.extend(parMessage)
        log_process_message('warning',parMessage,parLogLevel)
    def error(self,parErrorCode,parErrorMessage,parLogLevel=1):
        self.message=parErrorMessage
        self.error_code=parErrorCode
        self.return_code=0
        log_process_error(self.message,parLogLevel)
        #log_process_finish(self)

    def set_result(self,parResult,parMessage='OK'):
        self.result=parResult
        self.message=parMessage
        self.return_code=1
        self.error_code=0

    def log_results(self,parlogLevelRetCode=1,parlogLevelErrCode=1,parlogLevelMessage=1,parlogLevelResult=1,parlogLevelWarnings=1):
        log_process_result('return_code',self.return_code,parlogLevelRetCode)
        log_process_result('error_code',self.error_code,parlogLevelErrCode)
        log_process_result('message',self.message,parlogLevelMessage)
        log_process_result('result',self.result,parlogLevelResult)
        for message in self.messages:
            log_process_result('warning',message,parlogLevelWarnings)

    dumps = lambda self: repr(self)
    __str__ = lambda self: self.dumps()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def what_is_my_name():
    print(inspect.stack()[0][0].f_code.co_name)
    print(inspect.stack()[0][3])
    print(inspect.currentframe().f_code.co_name)
    print(sys._getframe().f_code.co_name)
#from openbanking_globals import *
#import openbanking_service_module_BankofCyprus
#import openbanking_service_module_HellenicBank
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def debug_init():
    global globalProcessStack
    global globalDebugConfig
    global globalDebugLevel
    global globalDebugLevelStartFinish
    global globalDebugLevelSection
    global globalDebugLevelMessage
    global globalDebugLevelError
    global globalDebugLevelInputParams
    global globalDebugLevelValue
    global globalDebugLevelResults
    global globalDebugLevelHttp
    try:
        globalDebugLevelStartFinish=globalDebugLevelStartFinish+0
    except:
        globalDebugLevelStartFinish=1
    try:
        globalDebugLevelSection=globalDebugLevelSection+0
    except:
        globalDebugLevelSection=1
    try:
        globalDebugLevelError=globalDebugLevelError+0
    except:
        globalDebugLevelError=1
    try:
        globalDebugLevelMessage=globalDebugLevelMessage+0
    except:
        globalDebugLevelMessage=1
    try:
        globalDebugLevelInputParam=globalDebugLevelInputParam+0
    except:
        globalDebugLevelInputParam=1
    try:
        globalDebugLevelValue=globalDebugLevelValue+0
    except:
        globalDebugLevelValue=1
    try:
        globalDebugLevelResults=globalDebugLevelResults+0
    except:
        globalDebugLevelResults=1
    try:
        globalDebugLevelHttp=globalDebugLevelHttp+0
    except:
        globalDebugLevelHttp=1
   
    globalDebugConfig={
        'globalDebugLevel':globalDebugLevel
        ,'globalDebugLevelStartFinish':globalDebugLevelStartFinish
        ,'globalDebugLevelSection':globalDebugLevelSection
        ,'globalDebugLevelError':globalDebugLevelError
        ,'globalDebugLevelMessage':globalDebugLevelMessage
        ,'globalDebugLevelInputParam':globalDebugLevelInputParam
        ,'globalDebugLevelValue':globalDebugLevelValue
        ,'globalDebugLevelResults':globalDebugLevelResults
        ,'globalDebugLevelHttp':globalDebugLevelHttp
        }
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#def Nolog_InputParam(parProcess,parLogLevel=-1):



#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def log_process_start(parProcess,parLogLevel=-1):
    global globalProcessStack,globalDebugLevelStartFinish
    try:
        globalDebugLevelStartFinish=globalDebugLevelStartFinish+0
    except:
        globalDebugLevelStartFinish=1
    globalDebugLevel=globalDebugLevelStartFinish
    
    if parLogLevel>=0:
        varThisDebugLevel=parLogLevel
    else:
        varThisDebugLevel=globalDebugLevel

    try:
        varThisProcess=globalProcessStack[-1]
        varProcessLevel=varThisProcess['process_level']
        varPrevDebugLevel=varThisProcess['process_debug_level']
    except:
        varProcessLevel=-1
        varPrevDebugLevel=0

    varProcessLevel=varProcessLevel+1
    varDebugOffset='\t'*varProcessLevel    
        
    varThisProcess={
              'varProcessName':parProcess.service_name
             ,'process_type':parProcess.process_type
             ,'process_module':parProcess.module
             ,'process_level':varProcessLevel
             ,'process_debug_level':varThisDebugLevel
             ,'process_debug_offset':varDebugOffset
             }
    try:
        globalProcessStack.append(varThisProcess)
    except:
        globalProcessStack=[]
        globalProcessStack.append(varThisProcess)
        
    if varThisDebugLevel>0 and (varThisDebugLevel>=globalDebugLevel or varPrevDebugLevel>=globalDebugLevel):
        varProcessFullName=varThisProcess['process_module']+'.'+varThisProcess['varProcessName']
        print(varDebugOffset,'==>',varProcessFullName)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def log_process_route_start(parProcess,parLogLevel=-1):
    global globalProcessStack,globalDebugLevelRoute
    try:
        globalDebugLevelStartFinish=globalDebugLevelRoute+0
    except:
        globalDebugLevelRoute=1
    globalDebugLevel=globalDebugLevelRoute
    
    if parLogLevel>=0:
        varThisDebugLevel=parLogLevel
    else:
        varThisDebugLevel=globalDebugLevel

    globalProcessStack=[]
    varProcessLevel=-1
    varPrevDebugLevel=0

    varProcessLevel=varProcessLevel+1
    varDebugOffset='\t'*varProcessLevel    
        
    varThisProcess={
              'varProcessName':parProcess.service_name
             ,'process_type':parProcess.process_type
             ,'process_module':parProcess.module
             ,'process_level':varProcessLevel
             ,'process_debug_level':varThisDebugLevel
             ,'process_debug_offset':varDebugOffset
             }
    try:
        globalProcessStack.append(varThisProcess)
    except:
        globalProcessStack=[]
        globalProcessStack.append(varThisProcess)
        
    if varThisDebugLevel>0 and (varThisDebugLevel>=globalDebugLevel or varPrevDebugLevel>=globalDebugLevel):
        varProcessFullName=varThisProcess['process_module']+'.'+varThisProcess['varProcessName']
        print(varDebugOffset,'==>',varProcessFullName)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def log_process_finish(parProcess):
    global globalProcessStack,globalDebugLevelStartFinish
    try:
        globalDebugLevelStartFinish=globalDebugLevelStartFinish+0
    except:
        globalDebugLevelStartFinish=1
    globalDebugLevel=globalDebugLevelStartFinish

    try:
        varThisProcess=globalProcessStack.pop()
    except:
        log_process_start(parProcess)
        varThisProcess=globalProcessStack.pop()
    
    try:
        varPrevProcess=globalProcessStack[-1]
        varPrevDebugLevel=varPrevProcess['process_debug_level']
    except:
        varPrevDebugLevel=0

    varProcessName=varThisProcess['varProcessName']
    varProcessLevel=varThisProcess['process_level']
    varDebugLevel=varThisProcess['process_debug_level']
    varDebugOffset=varThisProcess['process_debug_offset']    

    if varDebugLevel>0 or varPrevDebugLevel>0:
        varProcessFullName=varThisProcess['process_module']+'.'+varThisProcess['varProcessName']
        print(varDebugOffset,'<==',varProcessFullName)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def log_process_section_start(parSectionName,parLogLevel=-1):
    global globalProcessStack,globalDebugLevelSection
    try:
        globalDebugLevelSection=globalDebugLevelSection+0
    except:
        globalDebugLevelSection=1
    globalDebugLevel=globalDebugLevelSection

    if parLogLevel>=0:
        varThisDebugLevel=parLogLevel
    else:
        varThisDebugLevel=globalDebugLevel

    try:
        varThisProcess=globalProcessStack[-1]
        varProcessLevel=varThisProcess['process_level']
        varPrevDebugLevel=varThisProcess['process_debug_level']
        varThisProcessModule=varThisProcess['process_module']
    except:
        varProcessLevel=-1
        varPrevDebugLevel=0
        varThisProcessModule='?'

    varProcessLevel=varProcessLevel+1
    varDebugOffset='\t'*varProcessLevel    
        
    varThisProcess={
              'varProcessName':parSectionName
             ,'process_type':'program_section'
             ,'process_module':varThisProcessModule
             ,'process_level':varProcessLevel
             ,'process_debug_level':varThisDebugLevel
             ,'process_debug_offset':varDebugOffset
             }

    try:
        globalProcessStack.append(varThisProcess)
    except:
        globalProcessStack=[]
        globalProcessStack.append(varThisProcess)
        
    if varThisDebugLevel>0 and (varThisDebugLevel>=globalDebugLevel or varPrevDebugLevel>=globalDebugLevel):
        print(varDebugOffset,'>>>',varProcessName)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def log_process_section_finish(ParSectionName=''):
    global globalProcessStack,globalDebugLevelSection
    try:
        globalDebugLevelSection=globalDebugLevelSection+0
    except:
        globalDebugLevelSection=1
    globalDebugLevel=globalDebugLevelSection

    try:
        varThisProcess=globalProcessStack.pop()
    except:
        varThisProcess={'varProcessName':'?','process_level':0,'process_debug_level':1,'process_debug_offset':''}
        globalProcessStack=[]
        globalProcessStack.append(varThisProcess)
        varThisProcess=globalProcessStack.pop()

    try:
        varPrevProcess=globalProcessStack[-1]
        varPrevDebugLevel=varPrevProcess['process_debug_level']
    except:
        varPrevDebugLevel=0

    varProcessName=varThisProcess['varProcessName']
    varProcessLevel=varThisProcess['process_level']
    varDebugLevel=varThisProcess['process_debug_level']
    varDebugOffset=varThisProcess['process_debug_offset']    
    if varDebugLevel>0 or varPrevDebugLevel>0:
        print(varDebugOffset,'<<<',varProcessName)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def log_process_input_param(parWhat,parValue,parLogLevel=-1,parPrefix1='',parPrefix2='',parPrefix3=''):
    global globalProcessStack,globalDebugLevelInputParam
    try:
        globalDebugLevelInputParam=globalDebugLevelInputParam+0
    except:
        globalDebugLevelInputParam=1
    globalDebugLevel=globalDebugLevelInputParam

    try:
        varThisProcess=globalProcessStack[-1]
        varProcessName=varThisProcess['varProcessName']
        varProcessLevel=varThisProcess['process_level']
        varDebugLevel=varThisProcess['process_debug_level']
        varDebugOffset=varThisProcess['process_debug_offset']
        varDebugOffset='\t'*(varProcessLevel+1)
    except:
        varDebugOffset='*'
        varDebugLevel=0

    if (globalDebugLevel>0 and globalDebugLevel>=parLogLevel) or (globalDebugLevel<=0 and parLogLevel>9):
        print(varDebugOffset,'->',parWhat,' = ',parValue)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def log_process_result(parWhat,parValue,parLogLevel=-1,parPrefix1='',parPrefix2='',parPrefix3=''):
    global globalProcessStack,globalDebugLevelResult
    try:
        globalDebugLevelResult=globalDebugLevelResult+0
    except:
        globalDebugLevelResult=1
    globalDebugLevel=globalDebugLevelResult

    try:
        varThisProcess=globalProcessStack[-1]
        varProcessName=varThisProcess['varProcessName']
        varProcessLevel=varThisProcess['process_level']
        varDebugLevel=varThisProcess['process_debug_level']
        varDebugOffset=varThisProcess['process_debug_offset']    
        varDebugOffset='\t'*(varProcessLevel+1)    
    except:
        varDebugOffset='*'
        varDebugLevel=0
    if (globalDebugLevel>0 and globalDebugLevel>=parLogLevel) or (globalDebugLevel<=0 and parLogLevel>9):
            prefix=parPrefix1+parPrefix2+parPrefix3
            if (parPrefix1=='' and parPrefix2=='' and parPrefix3==''):
                print(varDebugOffset,'<-',parWhat,' = ',parValue)
            else:
                prefix=parPrefix1+parPrefix2+parPrefix3
                print(varDebugOffset,'<-',prefix,parWhat,' = ',parValue)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def log_process_value(parWhat,parValue,parLogLevel=-1,parPrefix1='',parPrefix2='',parPrefix3=''):
    global globalProcessStack,globalDebugLevelValue
    try:
        globalDebugLevelValue=globalDebugLevelValue+0
    except:
        globalDebugLevelValue=1
    globalDebugLevel=globalDebugLevelValue

    try:
        varThisProcess=globalProcessStack[-1]
        varProcessName=varThisProcess['varProcessName']
        varProcessLevel=varThisProcess['process_level']
        varDebugLevel=varThisProcess['process_debug_level']
        varDebugOffset=varThisProcess['process_debug_offset']    
        varDebugOffset='\t'*(varProcessLevel+1)
    except:
        varDebugOffset='*'
        varDebugLevel=0
    if (globalDebugLevel>0 and globalDebugLevel>=parLogLevel) or (globalDebugLevel<=0 and parLogLevel>9):
        print(varDebugOffset,'o',parWhat,' = ',parValue)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def log_process_message(parWhat,parValue,parLogLevel=-1,parPrefix1='',parPrefix2='',parPrefix3=''):
    global globalProcessStack,globalDebugLevelMessage
    try:
        globalDebugLevelMessage=globalDebugLevelMessage+0
    except:
        globalDebugLevelMessage=1
    globalDebugLevel=globalDebugLevelMessage

    try:
        varThisProcess=globalProcessStack[-1]
        varProcessName=varThisProcess['varProcessName']
        varProcessLevel=varThisProcess['process_level']
        varDebugLevel=varThisProcess['process_debug_level']
        varDebugOffset=varThisProcess['process_debug_offset']    
        varDebugOffset='\t'*(varProcessLevel+1)
    except:
        varDebugOffset='*'
        varDebugLevel=0

    if (globalDebugLevel>0 and globalDebugLevel>=parLogLevel) or (globalDebugLevel<=0 and parLogLevel>9):
        print(varDebugOffset,'+',parWhat,'-',parValue)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def log_http_request_result(r,parLogLevel=-1):
    global globalProcessStack,globalDebugLevelHttp
    try:
        globalDebugLevelHttp=globalDebugLevelHttp+0
    except:
        globalDebugLevelHttp=1
    globalDebugLevel=globalDebugLevelHttp

    if parLogLevel>=0:
        varThisDebugLevel=parLogLevel
    else:
        varThisDebugLevel=globalDebugLevel

    try:
        varThisProcess=globalProcessStack[-1]
        varProcessName=varThisProcess['varProcessName']
        varProcessLevel=varThisProcess['process_level']
        varDebugLevel=varThisProcess['process_debug_level']
        varDebugOffset=varThisProcess['process_debug_offset']    
        varDebugOffset='\t'*varProcessLevel+1    
    except:
        varDebugOffset='*'
        varDebugLevel=0

    if (globalDebugLevel>0 and globalDebugLevel>=parLogLevel) or (globalDebugLevel<=0 and parLogLevel>9):
        print(varDebugOffset,'o http','request    ',' = ',r)
        print(varDebugOffset,'o http','status_code',' = ',r.status_code)
        print(varDebugOffset,'o http','reply      ',' = ',r.text)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def log_process_error(parWhat,parLogLevel=1,parPrefix1='',parPrefix2='',parPrefix3=''):
    global globalProcessStack,globalDebugLevelError
    try:
        globalDebugLevelError=globalDebugLevelError+0
    except:
        globalDebugLevelError=1
    globalDebugLevel=globalDebugLevelError

    try:
        varThisProcess=globalProcessStack[-1]
        varProcessName=varThisProcess['varProcessName']
        varProcessLevel=varThisProcess['process_level']
        varDebugLevel=varThisProcess['process_debug_level']
        varDebugOffset=varThisProcess['process_debug_offset']    
        varDebugOffset='\t'*(varProcessLevel+1)
    except:
        varDebugOffset='*'
        varDebugLevel=0
        varProcessName='?'

    if (globalDebugLevel>0 and globalDebugLevel>=parLogLevel) or (globalDebugLevel<=0 and parLogLevel>9):
        #print(varDebugOffset,'ERROR-->',varProcessName)
        print(varDebugOffset,'ERROR-->',parWhat)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
############################################################
############################################################
############################################################
if __name__ == '__main__':    
    log_process_start('alpha',1)
    log_process_start('beta',)
    log_process_value ('beta-v1','aaaaa')
    log_process_section_start('section----aaa',)
    log_process_value ('beta-v2','bbbbbb')
    log_process_start('gama',0)
    log_process_result('gama-1','111111')
    log_process_result('gama-2','222222',1)
    log_process_finish()
    log_process_value ('beta-v3','ccccc')
    log_process_section_finish('secxxxxx',)
    log_process_result('beta-1','111111')
    log_process_result('beta-2','222222')
    log_process_finish()
    log_process_result('alpha-1','111111')
    log_process_result('alpha-2','222222')
    log_process_finish()