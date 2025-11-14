# core/adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailAddress
from allauth.account.utils import perform_login
from django.shortcuts import redirect

class CustomAccountAdapter(DefaultAccountAdapter):
    def confirm_email(self, request, email_address):
        """
        Automatically log the user in after email verification.
        """
        email_address.set_as_primary()
        email_address.verified = True
        email_address.save()
        user = email_address.user
        perform_login(request, user, email_verification='optional')
        return redirect('/')
