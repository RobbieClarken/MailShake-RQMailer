from mailshake import BaseMailer


class RQMailer(BaseMailer):

    def __init__(self, queue):
        self.queue = queue

    def send_messages(self, *messages):
        return self.queue.enqueue('mailworker.send_messages', *messages)
