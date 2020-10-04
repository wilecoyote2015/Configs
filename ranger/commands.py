# This is a sample commands.py.  You can add your own commands here.
#
# Please refer to commands_full.py for all the default commands and a complete
# documentation.  Do NOT add them all here, or you may end up with defunct
# commands when upgrading ranger.

# A simple command for demonstration purposes follows.
# -----------------------------------------------------------------------------

from __future__ import (absolute_import, division, print_function)

# You can import any python module as needed.
import os

# You always need to import ranger.api.commands here to get the Command class:
from ranger.api.commands import Command


class open_line(Command):
    """:open_line <line number>

    Move to a line and then move right
    """

    def execute(self):
        if self.arg(1):
            line_target = self.rest(1)
        else:
            self.fm.notify('Missing line number to jump to', bad=True)
            
        try: 
            line_int = int(line_target)
        except:
            self.fm.notify('Line number {} is not an integer value.'.format(line_target), bad=True)

        self.fm.move(to=line_int)
        self.fm.move(right=1)
