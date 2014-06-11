"""Open directory of current file in shell

Usage:
    1. Store in $sublime/Packages/User
    2. Map to hotkey (e.g. F12)
    3. Press hotkey to open terminal

Tested under Windows 7, 8 and Ubuntu 12.01.

Motivation:
    When working on Command-line interfaces or programs that require
    being run via an external terminal, the normal process goes like this:
        1. Right click in view
        2. "Open Containing Folder.."
        3. Shift-right click in explorer (Windows)
        4. "Open command window here" (Windows)

    With this plugin, the process may be reduced into this:
        1. Hit F12

"""


import os
import platform
import subprocess
import sublime_plugin

shells = {
    'Windows': 'cmd /K cd {path}',
    'Linux': 'x-terminal-emulator {path}',
    'Darwin': '{path}'
}

shell = shells[platform.system()]


class OpenInShellCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        source_file = self.view.file_name()
        source_dir = os.path.dirname(source_file)
        command = shell.format(path=source_dir)
        subprocess.Popen(command)
