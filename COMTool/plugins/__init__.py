from . import dbg
from . import protocol
from .import terminal
from . import gragh
# from . import myplugin

pluginClasses = [gragh.Plugin, dbg.Plugin, terminal.Plugin, protocol.Plugin]
# pluginClasses.append(myplugin.Plugin)

builtinPlugins = {}
for c in pluginClasses:
    builtinPlugins[c.id] = c




