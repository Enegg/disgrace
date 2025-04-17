from contextvars import ContextVar

state = ContextVar[object]("state")
