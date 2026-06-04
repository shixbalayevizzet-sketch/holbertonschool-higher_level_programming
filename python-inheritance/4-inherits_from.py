#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited 
    (directly or indirectly) from the specified class; otherwise False.
    """
    # type(obj) returns the class of the object.
    # We check if that class is a subclass of a_class,
    # but specifically exclude the case where the class IS a_class.
    return isinstance(type(obj), type) and issubclass(type(obj), a_class) and type(obj) is not a_class
