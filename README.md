# MailShake-RQMailer

[MailShake](https://github.com/jpscaletti/MailShake) mailer for sending email
via [RQ](http://python-rq.org/).


## Usage

In your app:

```python
from rqmailer import RQMailer
from rq import Queue
from redis import Redis

queue = Queue(connection=Redis())
mailer = RQMailer(queue)

mailer.send(
    subject='Hi',
    text_content='Hello world!',
    from_email='from@example.com',
    to=['mary@example.com', 'bob@example.com']
)
```

On the server authorized to send email, run a RQ worker in a folder containing
a module named `mailworker.py` with a `send_messages` function that accepts a
variable number of `MailShake.EmailMessage`s. For example:

```python
from mailshake import SMTPMailer
mailer = SMTPMailer()
send_messages = mailer.send_messages
```
