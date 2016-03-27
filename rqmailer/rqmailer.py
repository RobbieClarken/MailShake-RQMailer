from mailshake import BaseMailer


class RQMailer(BaseMailer):

    """
    MailShake mailer to add messages to a RQ job queue.
    """

    def __init__(self, queue):
        self.queue = queue

    def send_messages(self, *messages):
        return self.queue.enqueue('mailworker.send_messages', *messages)
