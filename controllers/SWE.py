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

# def report_an_issue1():
#     # Retrieve form data
#     title = request.vars.inputState
#     description = request.vars.inputdesc
#     submitter = request.vars.inputsub
#     assignee = request.vars.inputsub1
#     status = request.vars.status
#     created_date = request.vars.inputdate
#     priority = True if 'gridCheck' in request.vars else False
#     head_id = request.vars.head_ID
#     advisor_id = request.vars.advisor_ID
#     student_id = request.vars.student_ID
    
#     # Insert form data into database
#     db.issue.insert(title=title, description=description, submitter=submitter,
#                        assignee=assignee, status=status, created_date=created_date,
#                        priority=priority, head_id=head_id, advisor_id=advisor_id,
#                        student_id=student_id)
    
#     # Redirect to a page indicating success
#     redirect(URL('home.html'))

    # messages.py controller

def massege():
    return locals()