class Node(object):
    """A Node."""
    def __init__(self, name, parent=0):
        super(Node, self).__init__()
        self._name = name
        if parent is Node:
            self._parent = parent
        self._children = []

    def name():
        doc = "The name property defines the Node"
        def fget(self):
            return self._name
        def fset(self, value):
            self._name = value
        def fdel(self):
            del self._name
        return locals()
    name = property(**name())

    def parent():
        doc = "The parent property contains the parent of this Node"
        def fget(self):
            return self._parent
        def fset(self, value):
            if value is not Node:
                raise TypeError("value is not a node.")
            self._parent = value
            value.add_child(self)
        def fdel(self):
            del self._parent
        return locals()
    parent = property(**parent())

    def children():
        doc = "The children property contains the children of this Node"
        def fget(self):
            return self._children
        def fdel(self):
            del self._children
        return locals()
    children = property(**children())

    def add_child(self, v):
        if v is not Node:
            raise TypeError("v is not a Node.")
        self._children.append(v)
        v._parent = self

    def own_update(self, t):
        pass

    def update(self, t):
        self.own_update(t)
        for child in self.children:
            child.update(t)
