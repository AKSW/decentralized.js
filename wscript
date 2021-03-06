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

import os

APPNAME = 'decentralized.js'
VERSION = '0.0'

XPINAME = '%s@mirix.org.xpi' % APPNAME

def configure(cfg):
    cfg.check_tool('zip', tooldir=os.path.abspath('waftools'))

def build(bld):
    bld(features='subst', source='install.rdf.in', target='install.rdf',
        VERSION=VERSION)
    bld(features='zip', source=['install.rdf'], target=XPINAME)
    bld.install_files("${PREFIX}", XPINAME)
