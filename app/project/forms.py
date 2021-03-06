from ..models import Volunteer

from flask_wtf import FlaskForm as Form
from wtforms import (StringField, DateField, TextAreaField,
                     SelectField, SubmitField, BooleanField,
                     FileField, IntegerField, RadioField)

from wtforms.validators import DataRequired, Optional


class AssignProjectForm(Form):
    vol = SelectField('Volunteer', coerce=int)
    confirmed = BooleanField('Confirmed')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(AssignProjectForm, self).__init__(*args, **kwargs)
        self.vol.choices = [(vol.id, vol.name) for vol in Volunteer.query.order_by(Volunteer.name).all()]


class CommentForm(Form):
    date_reported = DateField('Date Reported', format="%Y-%m-%d")
    body = TextAreaField('Message')
    submit = SubmitField('Submit Comment')


class ProjectCompletionForm(Form):
    expensehour = IntegerField('Expense Hours', description='How many hours', validators=[Optional()])
    solution = TextAreaField('Project Solution', validators=[Optional()])
    imageupload = FileField('Your photo', render_kw={'multiple': True})
    caption = StringField('Add Photo caption')
    sure = BooleanField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ProjectCloseForm(Form):
    comment = TextAreaField('Add Reason for Project Closure', validators=[DataRequired()])
    sure = BooleanField('Confirmed', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ProjectSubmissionForm(Form):
    age_range = RadioField('Age Group:', choices=[('0-17', '0-17'), ('18-64', '18-64'),
                                                  ('65+', '65+')], validators=[DataRequired()])
    refered = BooleanField('Was User Referred?') # should be referred
    date_first_contacted = StringField('Date First Contacted')
    name = StringField('User Name:', validators=[DataRequired()])
    organisation_name = StringField('Organisation Name') # new field
    address_line_1 = StringField('Address Line 1', validators=[DataRequired()])
    address_line_2 = StringField('Address Line 2', validators=[DataRequired()])
    town_city = StringField('Town/City')
    telephone = IntegerField('Telephone')
    mobile = IntegerField('Mobile')
    postcode = StringField('Postcode:', validators=[DataRequired])
    email = StringField('Email:', validators=[Optional()])
    initial_contact = StringField('Initial Contact & useful info', default='Direct')
    service_user_condition = TextAreaField('Service user condition')
    how_they_find_us = TextAreaField('How did they find us?')
    request_title = StringField('Project Title:')
    request_body = TextAreaField('Project Request:', validators=[DataRequired])

    name_2 = StringField('Initiator Name:')
    organisation_name_2 = StringField('Organisation Name') # new field
    address_line_1_2 = StringField('Address Line 1', validators=[DataRequired])
    address_line_2_2 = StringField('Address Line 2', validators=[DataRequired])
    town_city_2 = StringField('Town/City')
    postcode_2 = StringField('Postcode:', validators=[DataRequired])

    telephone_2 = IntegerField('Telephone:', validators=[Optional()])
    mobile_2 = IntegerField('Mobile:', validators=[Optional()])
    email_2 = StringField('Email:', validators=[Optional()])
    relation = StringField('Relationship:', description=' What is the Relationship to Service User')

    donation_discussed = BooleanField('Donation/Expenses Discussed?')
    whom_donation_discussed = StringField('With whom was Donation/Expenses discussed')
    donation_outcome = TextAreaField('Outcome?', validators=[Optional()])

    data_protection = BooleanField('Data Protection Discussed?')
    whom_data_protection_discussed = StringField('With whom was Data Protection Discussed?')
    dat_protection_outcome = TextAreaField('Outcome?', validators=[Optional()])
    submit = SubmitField('Submit')


class EditProjectForm(Form):
    request_title = StringField('Project Title')
    request_body = TextAreaField('Project Request',  description='Describe your problem',
                                 validators=[DataRequired()])
    donation_discussed = BooleanField('Donation/Expenses Discussed?')
    whom_donation_discussed = StringField('With whom was Donation/Expenses discussed')
    donation_outcome = TextAreaField('Outcome?', validators=[Optional()])
    data_protection = BooleanField('Data Protection Discussed?')
    whom_data_protection_discussed = StringField('With whom was Data Protection Discussed?')
    dat_protection_outcome = TextAreaField('Outcome?', validators=[Optional()])
    submit = SubmitField('Submit')


class ProjectPdfSelection(Form):
    selection = SelectField('Create PDF', choices=[('1', 'All'), ('2', 'Ongoing or Awaiting volunteer'),
                                                   ('3', 'Awaiting Volunteer'), ('4', 'Ongoing'),
                                                   ('5', 'Finished or Closed'), ('6', 'Finished'),
                                                   ('7', 'Closed')])
    submit = SubmitField('Download PDF')


class PDFEncryptionForm(Form):
    PdfFile = FileField('Your PDF File')
    password = StringField('Enter Password for Encryption:', validators=[DataRequired()])
    submit = SubmitField('Submit')

