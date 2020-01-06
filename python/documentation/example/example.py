"""This is my module doctring.

It explains what the module does.

"""


__all__ = ["Foo"]


class Foo:
    """This is my class dosctring.

    The class has certain attributes.

    Attributes:
        name: Name of the object.

    """

    def __init__(self):
        """This is my init docstring."""
        self.name = None

    def change_name(self, name: str = "bar") -> str:
        """This is my method dosctring.

        This explains what the method does.

        Args:
            name: new name
        Raises:
            ValueError: When name is not string
        Returns:
            name merged with class


        """
        self.name = name

        if not isinstance(name, str):
            raise ValueError("name must be string")

        return self.__class__ + name


if __name__ == "__main__":
    foo = Foo()
    foo.name()
