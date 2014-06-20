"""Open directory of current file in explorer

Usage:
    1. Store in $sublime/Packages/User
    2. Map to hotkey (e.g. F11)
    3. Press hotkey to open explorer

Tested under Windows 7, 8 and Ubuntu 12.01.

"""


import os
import platform
import subprocess
import sublime_plugin

mapping = {'Windows': 'explorer',
           'Darwin': 'start',
           'Linux': 'nautilus'}

explorer = mapping.get(platform.system())


class OpenInExplorerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('save')
        source_file = self.view.file_name()
        source_dir = os.path.dirname(source_file)
        subprocess.Popen([explorer, source_dir])
