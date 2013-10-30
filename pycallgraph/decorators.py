from .pycallgraph import PyCallGraph
from .output.graphviz import GraphvizOutput


def pycallgraphthis(outfile='pycallgraph.png', tool='dot'):
    """
    Just drop the decorator on any function you'd like to profile and see a
    call graph of.

        from pycallgraph.decorators import pycallgraphthis

        @pycallgraphthis(outfile='pycallgraph.png')
        def my_method():
            ...

    Note that it may take a short while to build the graph.
    """
    # TODO: Fix bug where basic @pycallgraphthis with no args doesn't work
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            output = GraphvizOutput(
                outfile=outfile,
                tool=tool,
            )
            instance = PyCallGraph(output=output)
            instance.start()
            result = f(*args, **kwargs)
            instance.done()
            return result
        return wrapped_f
    return wrap
