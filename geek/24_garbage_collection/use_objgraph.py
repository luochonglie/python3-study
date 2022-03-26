import objgraph
import xdot

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

objgraph.show_refs([a], filename='show_refs.png')
objgraph.show_backrefs([a], filename='show_backrefs.png')
xdot.dot.parser()
