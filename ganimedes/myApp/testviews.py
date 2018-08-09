"""
Routes and views for the flask application.
"""

from datetime import datetime
from BocApi_FlaskWebProject import app
from flask import render_template, request, make_response, jsonify, redirect, url_for
from decorators import access_token_required,subscription_required
from utils import generate_access_token, list_accounts, get_account_details, get_account_transactions, get_payments, initiate_payment, confirm_payment
from apisboc import boc_get_access_token,boc_get_subscriptionId,boc_get_customer_Consent,boc_get_authorization_token,boc_update_subscription
from apisboc import boc_get_subscription_Accounts,boc_get_subscription_details,boc_delete_subscription
from apisboc import boc_list_accounts,boc_get_account_details,boc_get_account_balances,boc_get_account_transactions,boc_get_account_subscriptions
from apisboc import boc_get_payments,boc_payment_initiate,boc_payment_create,boc_payment_authorize
import requests
#import requests_oauthlib
#from requests_oauthlib import OAuth2Session
#from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import os
import urllib
from urllib.parse import urlparse
from json2html import *


@app.route('/')
def index():
    print('route-/')
    return render_template('home.html')

@app.route('/home')
def home():
    """Renders the home page."""
    print('route-/home')
    return render_template('index.html',title='Home Page',year=datetime.now().year)

@app.route('/contact')
def contact():
    """Renders the contact page."""
    print('route-/contact')
    return render_template('contact.html',title='Contact',year=datetime.now().year,message='Your contact page.')

@app.route('/about')
def about():
    """Renders the about page."""
    print('route-/about')
    return render_template('about.html',title='About',year=datetime.now().year,message='Your application description page.')


@app.route('/login', methods=['POST', 'GET'])
def bocsubscription():
        print('')
        print('###START###/login','---'+request.method)
        access_token = None
        subscriptionId = None
        xsubscriptionId='Subid000001-1532001577088'
        response = '?'
        resp = make_response(render_template('login.html'))
        access_token = request.cookies.get('access_token')
        if not access_token:
            try:
                access_token = boc_get_access_token()
            except Exception as e:
                response = "Failed to generate access token: {}".format(e)
                return render_template('login.html', response=response)
            if access_token:
                resp.set_cookie('access_token', access_token)
        if access_token:
            response = 'access_token OK'
       
        subscriptionId = request.cookies.get('subscriptionId')
        if not subscriptionId:
            subscriptionId=xsubscriptionId
            print('   ###login:retrieved subscriptionId from cfg',subscriptionId)
            if subscriptionId:
                subscriptionDetails=boc_get_subscription_details(access_token,subscriptionId)
                subscription_status=subscriptionDetails[0]['status']
                print('   ###login:subscriptionStatus',subscription_status)
                if subscription_status:
                    if subscription_status != 'ACTV':
                        response = 'ERROR:subscription status is '+ subscription_status
                        return render_template('login.html', response=response)
                    else:
                        response = 'OK-subscription status is '+ subscription_status
                        resp = make_response(render_template('login.html', response=response))
                        resp.set_cookie('subscriptionId',subscriptionId)    
                        resp.set_cookie('access_token', access_token)
                        return(resp)
                else:
                    response = 'subscription update FAILED'
                    return render_template('login.html', response=response)
            else:
                response='subscriptionId from cfg failed... get a new one'
                return render_template('login.html', response=response)
        else:
            response = 'subscriptionId retrieved from cookies: '+subscriptionId
            print('   ###login:retrieved subscriptionId from cookies',subscriptionId)
            return render_template('login.html', response=response)


@app.route('/bocauth', methods=['POST', 'GET'])
def boccredentials():
    print('')
    print('###START###/bocauth','---'+request.method)
    if request.method == 'POST':
        access_token = None
        subscriptionId = None
        response = 'Access token successfully generated!'
        resp = make_response(render_template('bocauthenticate.html', response=response))
        try:
            access_token = boc_get_access_token()
        except Exception as e:
            response = "Failed to generate access token: {}".format(e)
       
        if access_token:
            resp.set_cookie('access_token', access_token)
            try:
                subscriptionId = boc_get_subscriptionId(access_token)
            except Exception as e:
                response = "Failed to get subscriptionId: {}".format(e)
            if subscriptionId:
                resp.set_cookie('subscriptionId', subscriptionId)
                try:
                    customerconsent = boc_get_customer_Consent(subscriptionId)
                except Exception as e:
                    response = "Failed to get customerconsent: {}".format(e)

        resp = make_response(render_template('bocauthenticate.html', response=response))
        if access_token:
            resp.set_cookie('access_token', access_token)
        if subscriptionId:
            resp.set_cookie('subscriptionId', subscriptionId)
        return resp
    else:
        access_token = request.cookies.get('access_token')
        subscriptionId = request.cookies.get('subscriptionId')
        authorization_code = request.cookies.get('authorization_code')
        authorization_token = request.cookies.get('authorization_token')
        if not access_token:
            return render_template('bocauthenticate.html', response='You have not generated access token yet!')
        else:
            return render_template('bocauthenticate.html')
   

@app.route('/authorization')
def authorization():
    print('')
    print('###START###/authorization','---'+request.method)
    print('   ...back from boc 1bank ...')
    print ('  '+request.url)
    access_token = request.cookies.get('access_token')
    subscriptionId = request.cookies.get('subscriptionId')
    #print('   ...access token='+access_token)
    #print('   ...subscriptionId='+subscriptionId)
    #print('   ----------------------------------')

    parsed = urlparse(request.url)
    #print(parsed)
    querystring=parsed.query
    xcode = querystring.split('=',1)
    code=xcode[1]
    #print('   ...authorization code='+code)
    response = 'receive authorization from the customer....'

    if code:
       response = 'authorization received from the customer'
       authorization_token=boc_get_authorization_token(code)
       if authorization_token:
            response = 'authorization token OK'
            print('   ...authorization token='+authorization_token)
            what=boc_get_subscription_details(access_token,subscriptionId)

            subscription_status=boc_update_subscription(subscriptionId,authorization_token,code,what)
            if subscription_status:
                if subscription_status != 'ACTV':
                    response = 'ERROR:subscription status is '+ subscription_status
                else:
                    response = 'OK-subscription status is '+ subscription_status
            else:
                response = 'subscription update FAILED'
       else:      
            response = 'authorization token FAILED'
    else:
        response = 'authorzation from the customer FAILED'

    resp = make_response(render_template('bocauthenticate.html', response=response))

    if authorization_token:
        resp.set_cookie('authorization_token', authorization_token)
        resp.set_cookie('authorization_code', code)
        account_id='351092345672'
        message='test-test-test-test-test-test-test-test-test'
        amount='1.11'
        beneficiary='1212121212'
        #signature=boc_payment_initiate(authorization_token,subscriptionId,account_id ,beneficiary,amount,'EUR',message)
        #payment=boc_payment_create(authorization_token, subscriptionId, signature)
        #if error:
        #    return render_template('payments.html', error=error)
        #else:
        #    return render_template('payments.html', payments=payments, payment=payment, accounts=accounts)


    return resp


@app.route('/authenticate', methods=['POST', 'GET'])
def credentials():
    print('')
    print('###START###/authenticate','---'+request.method)
    if request.method == 'POST':
        access_token = None
        response = 'Access token successfully generated!'
        try:
            access_token = generate_access_token()
        except Exception as e:
            response = "Failed to generate access token: {}".format(e)

        resp = make_response(render_template(
            'authenticate.html', response=response))
        if access_token:
            resp.set_cookie('access_token', access_token)
        return resp
    else:
        access_token = request.cookies.get('access_token')
        if not access_token:
            return render_template('authenticate.html', response='You have not generated access token yet!')
        else:
            return render_template('authenticate.html')


@app.route('/revoke', methods=['POST'])
@access_token_required
def revoke():
    print('')
    print('###START###/revoke','---'+request.method)
    resp = make_response(render_template('revoke.html'))
    resp.set_cookie('access_token', '', expires=0)
    return resp


@app.route('/accounts', methods=['GET'])
#@subscription_required
def accounts():
    print('')
    print('###START###/accounts','---'+request.method)
    error = None
    subscriptionId=None
    subscriptionId = request.cookies.get('subscriptionId')
    if subscriptionId:
        print('   ###accounts:retrieved subscriptionId from cookies',subscriptionId)
    else:
        print('   ###accounts:subscriptionId from cookies FAILED')
        error='subscriptionId from cookies FAILED'
        return render_template('bocaccounts.html', error=error)

    access_token = boc_get_access_token()
    try:
        accounts = boc_get_subscription_Accounts(access_token,subscriptionId)
    except Exception as e:
        error = e

    if error:
        return render_template('bocaccounts.html', error=error)
    else:
        return render_template('bocaccounts.html', accounts=accounts)

@app.route('/account_details', methods=['GET'])
#@subscription_required
def account_details():
    print('')
    print('###START###/account_details','---'+request.method)
    error = None
    account_id = request.args.get('account_id')
    if not account_id:
        error = 'Account id url parameter is missing!'
    else:
        subscriptionId = request.cookies.get('subscriptionId')
        access_token = boc_get_access_token()
        try:
            details = boc_get_account_details(access_token, subscriptionId, account_id)
        except Exception as e:
            error = e
    if error:
        return render_template('bocaccount_details.html', error=error)
    else:
        thtml=json2html.convert(json = details[0], table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
        x=render_template('bocaccount_details.html')
        xx=x.replace('@account_details@',thtml)
        return xx

@app.route('/transactions', methods=['GET'])
@subscription_required
def account_transactions():
    print('')
    print('###START###/transactions','---'+request.method)
    account_id = request.args.get('account_id')
    error = None
    access_token = boc_get_access_token()
    subscriptionId = request.cookies.get('subscriptionId')
    #print('   ...subscriptionId',subscriptionId)
    try:
        statement = boc_get_account_transactions(access_token, subscriptionId,  account_id)
    except Exception as e:
        error = e

    if not account_id:
        error = 'Account id url parameter is missing!'

    if error:
        return render_template('boctransactions.html', error=error)
    else:
        accountinfo=statement[0]['account']
        transactions=statement[0]['transaction']
#                input = {
#                "name": "json2html",
#                "description": "Converts JSON to HTML tabular representation"
#                }
        thtml=json2html.convert(json = statement, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
        x=render_template('boctransactions.html', transactions=transactions,accountinfo=accountinfo)
        xx=x.replace('@statement@',thtml)
        return xx

@app.route('/account_subscriptions', methods=['GET'])
def account_subscriptions():
    print('')
    print('###START###/account_subscriptions','---'+request.method)
    error = None
    account_id = request.args.get('account_id')
    #print('   ...account_id',account_id)
    access_token = boc_get_access_token()
    subscriptionId = request.cookies.get('subscriptionId')
    if not account_id:
        error = 'Account id url parameter is missing!'
    else:
        try:
            subscriptions = boc_get_account_subscriptions(access_token,account_id)
        except Exception as e:
            error = e

    if error:
        return render_template('bocaccount_subscriptions.html', error=error)
    else:
        return render_template('bocaccount_subscriptions.html', subscriptions=subscriptions)


@app.route('/payments', methods=['GET', 'POST'])
#@access_token_required
def payments():
    print('')
    print('###START###/payments','---'+request.method)
    error = None
    #access_token = boc_get_access_token()
    subscriptionId = request.cookies.get('subscriptionId')
    if request.method == 'GET':
        try:
            access_token = boc_get_access_token()
            accounts = boc_get_subscription_Accounts(access_token,subscriptionId)
            payments=None
            for acct in accounts:
                accountId=acct['accountId']
                payments1 = boc_get_payments(access_token,subscriptionId,accountId)
                if not payments:
                    payments = payments1
                else:
                    payments.update(payments1)
            if not payments:
                payments=[]
        except Exception as e:
            error = e

        if error:
            return render_template('payments.html', error=error)
        else:
            return render_template('payments.html', payments=payments, accounts=accounts)

    elif request.method == 'POST':
        amount = request.form['amount']
        account_id = request.form['account_id']
        beneficiary = request.form['beneficiary']
        name = request.form['name']
        message = request.form['message']

        if None in [amount, account_id, beneficiary, name, message]:
            error = 'Form data missing!'
        if error:
            return render_template('payments.html', error=error)
        print ('###',account_id,beneficiary)
        print ('###',amount,name,message)
        # Generate the payload
        payload = {
            "amount": amount,
            "creditor": {
                "account": {
                    "_type": "IBAN",
                    "value": beneficiary
                },
                "message": message,
                "name": name,
                "reference": {
                    "_type": "RF",
                    "value": "RF18539007547034"
                }
            },
            "currency": "EUR",
            "debtor": {
                "_accountId": account_id
            }
        }

        subscriptionId = request.cookies.get('subscriptionId')

        try:
            access_token = boc_get_access_token()
        except Exception as e:
            error = e
            return render_template('payments.html', error=error)

        res=boc_payment_fundsavailability(access_token,subscriptionId,payload)
        if res != 'OK':
            return render_template('payments.html', error=res)
            
        #try:
        #    customerconsent = boc_get_customer_Consent(subscriptionId)
        #except Exception as e:
        #    response = "Failed to get customerconsent: {}".format(e)
        #    return render_template('payments.html', error=response)
        try:
            signature=boc_payment_initiate(access_token,subscriptionId,account_id ,beneficiary,amount,'EUR',message)
        except Exception as e:
            error = e
            return render_template('payments.html', error=error)

        try:
            payment=boc_payment_create(access_token, subscriptionId, signature)
        except Exception as e:
            error = e
            return render_template('payments.html', error=error)

        access_token = boc_get_access_token()
        accounts = boc_get_subscription_Accounts(access_token,subscriptionId)
        payments=None
        for acct in accounts:
            accountId=acct['accountId']
            payments1 = boc_get_payments(access_token,subscriptionId,accountId)
            if not payments:
                payments = payments1
            else:
                payments.update(payments1)

        if not payments:
            payments=[]

        return render_template('payments.html', payments=payments, payment=payment, accounts=accounts)
            

@app.route('/confirm_payment', methods=['POST'])
@access_token_required
def confirm_payments():
    error = None
    access_token = request.cookies.get('access_token')
    try:
        payment_id = request.form['payment_id']
        payment = confirm_payment(access_token, payment_id)
        payments = get_payments(access_token)
        accounts = list_accounts(access_token)
    except Exception as e:
        error = e
    if error:
        return render_template('payments.html', error=error)
    else:
        return redirect(url_for('payments'))

