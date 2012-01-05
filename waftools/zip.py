# decentralized.js - decentralized web framework
# Copyright (C) 2011  Matthias-Christian Ott <ott@mirix.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from waflib import Task
from TaskGen import feature
from zipfile import ZipFile, ZIP_DEFLATED

def zip_func(tsk):
    outfile = tsk.outputs[0].abspath()
    # ZipFile does not support incremental changes other than appending files,
    # so the target file is truncated and recreated.
    zip = ZipFile(outfile, 'w', ZIP_DEFLATED)
    for x in tsk.inputs:
        zip.write(x.abspath(), x.relpath())
    zip.close()

Task.task_factory('zip', zip_func, color='BLUE')

@feature('zip')
def process_zip(self):
    src = self.to_nodes(getattr(self, 'source', []))
    tgt = self.path.find_or_declare(getattr(self, 'target', []))
    self.create_task('zip', src, tgt)
    self.source = []
