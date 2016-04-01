from mailshake import BaseMailer


class RQMailer(BaseMailer):

    """
    MailShake mailer to add messages to a RQ job queue.
    """

    def __init__(self, queue, sender_func='mailworker.send_messages'):
        self.queue = queue
        self.sender_func = sender_func

    def send_messages(self, *messages):
        return self.queue.enqueue(self.sender_func, *messages)
