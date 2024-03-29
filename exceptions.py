class LoopError(Exception):
    pass


class ModeError(Exception):
    pass


class ConditionError(Exception):
    pass


class StackError(Exception):
    pass


class QueueError(Exception):
    pass


class SecurityError(Exception):
    pass


class AlgorithmError(Exception):
    pass


def exception_create(name):
    """
Create Your Customized Exception With Name That You Specify !
    """
    return type(name, (Exception,), {})
