from topics.staks_and_queues.tale_of_two_stacks import MyQueue
import pytest

def test_put_and_peek():
    queue = MyQueue()
    queue.put(10)
    queue.put(20)
    queue.put(30)
    assert queue.peek() == 10

def test_put_pop_and_peek():
    queue = MyQueue()
    queue.put(10)
    queue.put(20)
    queue.put(30)
    assert queue.pop() == 10
    assert queue.peek() == 20

def test_pop_empty_queue():
    queue = MyQueue()
    queue.put(10)
    queue.pop()
    with pytest.raises(IndexError):
        queue.pop()

def test_sequential_operations():
    queue = MyQueue()
    queue.put(10)
    assert queue.peek() == 10
    queue.put(20)
    assert queue.peek() == 10
    assert queue.pop() == 10
    assert queue.peek() == 20
    queue.put(30)
    assert queue.peek() == 20
    assert queue.pop() == 20
    assert queue.peek() == 30
    assert queue.pop() == 30

def test_mixed_operations():
    queue = MyQueue()
    queue.put(5)
    queue.put(10)
    queue.put(15)
    assert queue.pop() == 5
    queue.put(20)
    queue.put(25)
    assert queue.pop() == 10
    assert queue.peek() == 15
    assert queue.pop() == 15
    assert queue.peek() == 20
