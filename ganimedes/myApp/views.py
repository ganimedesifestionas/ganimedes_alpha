"""
Routes and views for the flask application.
"""

import json
from datetime import datetime
from flask import render_template
from flask import request, make_response, jsonify, redirect, url_for
from myApp import app
#from app_service_module import *

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='ganimedes Contact',
        year=datetime.now().year,
        message='our contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='ganimedes...application description page.'
    )
######################################################################
### myBank                                                         ###
######################################################################
@app.route('/myBank_home')
def myBank_home():
    """Renders the about page."""
    return render_template(
        'myBank_home.html',
        title='myBank',
        year=datetime.now().year,
        message='myBank...application description page.'
    )

@app.route('/myBank_about')
def myBank_about():
    """Renders the about page."""
    return render_template(
        'myBank_about.html',
        title='about myBank',
        year=datetime.now().year,
        message='myBank...application description page.'
    )

@app.route('/myBank_contact')
def myBank_contact():
    """Renders the contact page."""
    return render_template(
        'myBank_contact.html',
        title='myBank Contact',
        year=datetime.now().year,
        message='our contact page.'
    )

@app.route('/myBank_accounts', methods=['GET'])
#@subscription_required
def myBank_accounts():
    error = None
    ThisUserProfile=None
    ThisUserProfile = request.cookies.get('ThisUserProfile')
    #if ThisUserProfile:
    #    print('   ###accounts:retrieved user from cookies',ThisUserProfile)
    #else:
    #    print('   ###accounts:user from cookies FAILED')
    #    error='ThisUserProfile from cookies FAILED'
    #    return render_template('myBank_accounts.html', error=error)
    UserProfile={
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

    try:
        accounts=getAccounts(ThisUserProfile)
    except Exception as e:
        error = e

    if error:
        return render_template('myBank_accounts.html', error=error)
    else:
        return render_template('myBank_accounts.html', accounts=accounts)

@app.route('/myBank_account_details', methods=['GET'])
#@subscription_required
def myBank_account_details():
    #print('')
    #print('###START###/account_details','---'+request.method)
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
        x=render_template('myBank_account_details.html')
        xx=x.replace('@account_details@',thtml)
        return xx

@app.route('/myBank_account_transactions', methods=['GET'])
#@subscription_required
def myBank_account_transactions():
    #print('')
    #print('###START###/account_details','---'+request.method)
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
