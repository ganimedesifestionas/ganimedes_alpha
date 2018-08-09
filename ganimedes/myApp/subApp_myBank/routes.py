"""
Routes and views for the mybank flask sub application.
"""
from .. python_debug_utilities.python_debug_utilities import *
from .. service_bus import * 
import json
from datetime import datetime
from flask import flash, render_template, url_for
from flask import render_template
from flask import request
from flask import make_response, jsonify, redirect, url_for
from flask import abort
from flask_login import current_user, login_required
#from flask_login import login_required, login_user, logout_user


from . import myBank
from json2html import *
import inspect
#from forms import LoginForm, RegistrationForm
#from .. import db
#from ..models import Employee
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
@myBank.errorhandler(404)
def xpage_not_found(e):
    varPageName = request.args.get('url')
    print('xxxqqqqxxxxxxx',varPageName)
    print('xxxqqqqxxxxxxx',e)
    return render_template('404.html'), 404

@myBank.route('/')
######################################################################
### myBank                                                         ###
######################################################################
@myBank.route('/home')
def myBank_home():
    """Renders the about page."""
    return render_template(
        'myBank/myBank_home.html',
        title='myBank',
        year=datetime.now().year,
        message='myBank...application description page.'
    )

@myBank.route('/about')
def myBank_about():
    """Renders the about page."""
    return render_template(
        'myBank/myBank_about.html',
        title='about myBank',
        year=datetime.now().year,
        message='myBank...application description page.'
    )

@myBank.route('/contact')
def myBank_contact():
    """Renders the contact page."""
    return render_template(
        'myBank/myBank_contact.html',
        title='myBank Contact',
        year=datetime.now().year,
        message='our contact page.'
    )

@myBank.route('/accounts', methods=['GET'])
#@subscription_required
@login_required
def myBank_accounts():
    thisRoute=myRoute('',request)
    thisRoute.start()
    error=None
    global ThisUserProfile
    ThisUserProfile=getUserProfile(request)
    if not(ThisUserProfile):
        error='User Profile not found. login'
        thisRoute.message(1021,error)
    else:
        thisRoute.localVar('ThisUserProfile',ThisUserProfile,8)
        try:
            accounts=getAccounts(ThisUserProfile)
        except Exception as e:
            error = e

    if error:
        thisHtml=render_template('myBank/myBank_accounts.html', error=error)
        thisRoute.error(1022,error)
    else:
        thisHtml=render_template('myBank/myBank_accounts.html', accounts=accounts)
        thisRoute.set_result(thisHtml,'OK')

    thisRoute.log_results(4,4,4,8,4)
    thisRoute.finish()
    return thisHtml

@myBank.route('/account_details', methods=['GET'])
#@subscription_required
@login_required
def myBank_account_details():
    thisRoute=myRoute('',request)
    thisRoute.start()
    error=None
    global ThisUserProfile
    ThisUserProfile=getUserProfile(request)
    if not(ThisUserProfile):
        error='User Profile not found. login'
        thisRoute.message(1021,error)
    else:
        thisRoute.localVar('ThisUserProfile',ThisUserProfile,8)
        varAccountID = request.args.get('account_id')
        if not varAccountID:
            error = 'Account id url parameter is missing!'
            thisRoute.message(1022,error)
        else:
            thisRoute.localVar('varAccountID',varAccountID,4)
            try:
                varAccountDetails=getAccountDetails(ThisUserProfile,varAccountID)
            except Exception as e:
                error = e

    if error:
        thisHtml=render_template('myBank/myBank_account_details.html', error=error)
        thisRoute.error(1022,error)
    else:
        varAccountDetailsHtml=json2html.convert(json = varAccountDetails[0], table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
        varHtmlPage=render_template('myBank/myBank_account_details.html')
        thisHtml=varHtmlPage.replace('@account_details@',varAccountDetailsHtml)
        thisRoute.set_result(thisHtml,'OK')

    thisRoute.log_results(4,4,4,8,4)
    thisRoute.finish()
    return thisHtml

@myBank.route('/account_transactions', methods=['GET'])
#@subscription_required
@login_required
def myBank_account_transactions():
    thisRoute=myRoute('',request)
    thisRoute.start()
    error=None
    global ThisUserProfile
    ThisUserProfile=getUserProfile(request)
    if not(ThisUserProfile):
        error='User Profile not found. login'
        thisRoute.message(1021,error)
    else:
        thisRoute.localVar('ThisUserProfile',ThisUserProfile,8)
        varAccountID = request.args.get('account_id')
        if not varAccountID:
            error = 'Account id url parameter is missing!'
            thisRoute.message(1022,error)
        else:
            thisRoute.localVar('varAccountID',varAccountID,4)
            try:
                varAccountStatement=getAccountStatement(ThisUserProfile,varAccountID)
                varAccountInfo=varAccountStatement[0]['account']
                varAccountTransactions=varAccountStatement[0]['transaction']
            except Exception as e:
                error = e

    if error:
        thisHtml=render_template('myBank/myBank_account_transactions.html', error=error)
        thisRoute.error(1022,error)
    else:
        varAccountStatementHtml=json2html.convert(json = varAccountStatement, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
        varHtmlPage=render_template('myBank/myBank_account_transactions.html',transactions=varAccountTransactions,accountinfo=varAccountInfo)
        thisHtml=varHtmlPage.replace('@statement@',varAccountStatementHtml)
        thisRoute.set_result(thisHtml,'OK')

    thisRoute.log_results(4,4,4,8,4)
    thisRoute.finish()
    return thisHtml

@myBank.route('/transactions', methods=['GET'])
#@subscription_required
@login_required
def myBank_transactions():
    thisRoute=myRoute('',request)
    thisRoute.start()
    error=None
    global ThisUserProfile
    ThisUserProfile=getUserProfile(request)
    if not(ThisUserProfile):
        error='User Profile not found. login'
        thisRoute.message(1021,error)
    else:
        thisRoute.localVar('ThisUserProfile',ThisUserProfile,8)
        try:
            varTransactions=getTransactions(ThisUserProfile)
        except Exception as e:
            error = e

    if error:
        thisHtml=render_template('myBank/myBank_transactions.html', error=error)
        thisRoute.error(1022,error)
    else:
        varTransactionsHtml=json2html.convert(json = varTransactions, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
        varHtmlPage=render_template('myBank/myBank_transactions.html')
        thisHtml=varHtmlPage.replace('@transactions@',varTransactionsHtml)
        thisRoute.set_result(thisHtml,'OK')

    thisRoute.log_results(4,4,4,8,4)
    thisRoute.finish()
    return thisHtml

@myBank.route('/payments', methods=['GET','POST'])
#@subscription_required
@login_required
def myBank_payments():
    thisRoute=myRoute('',request)
    thisRoute.start()
    error=None
    global ThisUserProfile
    ThisUserProfile=getUserProfile(request)
    if not(ThisUserProfile):
        error='User Profile not found. login'
        thisRoute.message(1021,error)
    else:
        thisRoute.localVar('ThisUserProfile',ThisUserProfile,8)
        try:
            varPayments=getPayments(ThisUserProfile)
        except Exception as e:
            error = e

    if error:
        thisHtml=render_template('myBank/myBank_payments.html', error=error)
        thisRoute.error(1022,error)
    else:
        varPaymentsHtml=json2html.convert(json = varPayments, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
        varHtmlPage=render_template('myBank/myBank_payments.html')
        thisHtml=varHtmlPage.replace('@payments@',varPaymentsHtml)
        thisRoute.set_result(thisHtml,'OK')

    thisRoute.log_results(4,4,4,8,4)
    thisRoute.finish()
    return thisHtml


@myBank.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('myBank/admin_dashboard.html', title="Dashboard")