

class ClsRegistrator:
    """
    Decorator, registered classes in special list.
    """

    cls_list_registration = []

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        if self.cls not in self.cls_list_registration:
            self.cls_list_registration.append(self.cls)
        return self.cls(*args, **kwargs)


@ClsRegistrator
class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b


@ClsRegistrator
class B:

    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == "__main__":
    x = A(5, 6)
    d = B(6, 7)

    print(A.cls_list_registration)
