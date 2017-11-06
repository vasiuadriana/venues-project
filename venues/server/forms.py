from wtforms import Form, SelectMultipleField


class UsersForm(Form):
    users_select = SelectMultipleField('Users', choices=[])
