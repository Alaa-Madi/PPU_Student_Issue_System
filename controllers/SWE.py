# from .models import db
from gluon.dal import DAL, Field

def student():
    return dict()

def head():
    return dict()

def advisor():
    return dict()

def index():
    return dict()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

def home():
    if auth.user:
        name = db.auth_user(auth.user.id).first_name
        response.flash = f"Welcome back, {name}!"
    else:
        response.flash = "Welcome to my app!"
    return {}

def showissue():
    issue = db.executesql("SELECT * FROM issue", as_dict=True)
    return dict(issue=issue)


def report_an_issue():
    return locals()


def massege():
    return locals()

def assign_issue():
    return locals()

def Decision():
    issue = db.executesql("SELECT Title,status,head_ID,student_ID, advisor_ID  FROM issue WHERE status = 'wait'", as_dict=True)
    return dict(issue=issue)

def Genarate_Report():
    return locals()

def Make_Decision():
    return locals()

def View_Reported_Issue():
    issue = db.executesql("SELECT * FROM issue WHERE status = 'done'", as_dict=True)
    return dict(issue=issue)
