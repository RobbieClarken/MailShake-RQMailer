from rqmailer import RQMailer
import pytest
from mock import MagicMock, call


@pytest.yield_fixture
def mailer():
    queue = MagicMock()
    yield RQMailer(queue)


def test_send_messages_enqueues_messages(mailer):
    mailer.send_messages('message 1', 'message 2')
    expected_call = call('mailworker.send_messages', 'message 1', 'message 2')
    assert mailer.queue.enqueue.call_args == expected_call


def test_send_enques_a_message(mailer):
    mailer.send(subject='Hi!')
    (_, queued_message), _ = mailer.queue.enqueue.call_args
    assert queued_message.subject == 'Hi!'


def test_can_set_sender_func():
    queue = MagicMock()
    mailer = RQMailer(queue, sender_func='module.function')
    mailer.send_messages('message')
    assert queue.enqueue.call_args == call('module.function', 'message')
