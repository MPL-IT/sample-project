""" This is a sample module."""

def greetings(name):
    """ Says hello to someone.

    :param name: str, whom to say hello to
    :return: str, greeting
    """

    if name == 'LeChuck':
        raise ValueError

    return 'Hello, ' + name + '!'
