"""Open directory of current file in shell

Usage:
    1. Store in $sublime/Packages/User
    2. Map to hotkey (e.g. F12)
    3. Press hotkey to open terminal

Tested under Windows 7, 8 and Ubuntu 12.01.

"""


import os
import subprocess
import sublime_plugin

shell = 'cmd' if os.name == 'nt' else 'x-terminal-emulator'


class OpenInShellCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        source_file = self.view.file_name()
        source_dir = os.path.dirname(source_file)
        subprocess.Popen([shell, "/K", "cd %s" % source_dir])
