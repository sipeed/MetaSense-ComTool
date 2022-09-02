import sys
try:
    import parameters
    from i18n import _
    import version
except ImportError:
    from COMTool import parameters
    from COMTool.i18n import _
    from COMTool import version
    
import os
import PyQt5.QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
import time


def HelpInfo():
        return '''\
<h1 style='color:#009688';margin=10px;>{}</h1><br>
<b style="color:#009688;margin = 5px;">v{}</b><br><br>
{} + {}<br>
{}: {}<br>
{}: {}<br>
<div>
    <div><a style="color:#009688;" href="https://github.com/Neutree/COMTool">COMTool</a>{}</div>
    <a style="vertical-align: middle;" href="https://neucrack.com">
        <img src="{}" width=109 height=32/></a>
    <div>{}</div>
    <a style="vertical-align: middle;" href="https://neucrack.com">
        <img src="{}" width=109 height=32/></a>
</div>
{}: <b><a style="color:#009688;" href="https://github.com/Neutree/COMTool#license">LGPL-3.0</a></b><br>
'''.format(
    parameters.appName,
    version.__version__,
    '{}{}.{}'.format(sys.implementation.name, sys.implementation.version.major, sys.implementation.version.minor),
    'PyQt{}'.format(PyQt5.QtCore.QT_VERSION_STR),
    _("Config path"),
    parameters.configFilePath,
    _("Old config backup in"),
    os.path.dirname(parameters.configFilePath,),
    _(' is a Open source project create by'),
    '{}/{}'.format(parameters.dataPath, "assets/neucrack.png"),
    _('and modified by'),
    '{}/{}'.format(parameters.dataPath, parameters.appLogo2),
    _("License"),
)
