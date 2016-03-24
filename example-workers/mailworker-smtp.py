"""
This module should be renamed 'mailworker.py' and configured for your mail
server.
"""

from mailshake import SMTPMailer

mailer = SMTPMailer()
send_messages = mailer.send_messages
