# -*- coding: utf-8 -*-
#
# 	Copyright (C) 2012 by Igor E. Novikov
#
# 	This program is free software: you can redistribute it and/or modify
# 	it under the terms of the GNU General Public License as published by
# 	the Free Software Foundation, either version 3 of the License, or
# 	(at your option) any later version.
#
# 	This program is distributed in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# 	GNU General Public License for more details.
#
# 	You should have received a copy of the GNU General Public License
# 	along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from importlib import import_module

from uc2 import _
from uc2 import uc2const
from uc2 import events, msgconst
from uc2.utils.fs import get_file_extension
from fallback import fallback_check, im_loader

LOADERS = {}
SAVERS = {}
CHECKERS = {}


def _get_loader(pid):
    if pid in uc2const.BITMAP_LOADERS: return im_loader
    if not isinstance(pid, str): return None
    if pid in LOADERS: return LOADERS[pid]
    loader = None
    try:
        loader_mod = import_module('uc2.formats.' + pid)
        loader = getattr(loader_mod, pid + '_loader')
    except:
        pass
    LOADERS[pid] = loader
    return loader


def _get_saver(pid):
    if not isinstance(pid, str): return None
    if pid in SAVERS: return SAVERS[pid]
    saver = None
    try:
        saver_mod = import_module('uc2.formats.' + pid)
        saver = getattr(saver_mod, pid + '_saver')
    except:
        pass
    SAVERS[pid] = saver
    return saver


def _get_checker(pid):
    if pid in uc2const.BITMAP_LOADERS: return fallback_check
    if not isinstance(pid, str): return None
    if pid in CHECKERS: return CHECKERS[pid]
    checker = None
    try:
        checker_mod = import_module('uc2.formats.' + pid)
        checker = getattr(checker_mod, 'check_' + pid)
    except:
        pass
    CHECKERS[pid] = checker
    return checker


def get_loader_by_id(pid):
    loader = _get_loader(pid)
    if not loader:
        msg = _('Loader is not found for id %s') % (uc2const.FORMAT_NAMES[pid],)
        events.emit(events.MESSAGES, msgconst.ERROR, msg)
    return loader


def get_loader(path, experimental=False):
    if not os.path.lexists(path): return None
    if not os.path.isfile(path): return None

    ext = get_file_extension(path)
    loader = None
    ld_formats = [] + uc2const.LOADER_FORMATS

    msg = _('Start to search for loader by file extension %s') % (ext.__str__())
    events.emit(events.MESSAGES, msgconst.INFO, msg)

    if experimental:
        ld_formats += uc2const.EXPERIMENTAL_LOADERS
    for item in ld_formats:
        if ext in uc2const.FORMAT_EXTENSION[item]:
            checker = _get_checker(item)
            if checker and checker(path):
                loader = _get_loader(item)
                break

    if loader is None:
        msg = _('Loader is not found or not suitable for %s') % (path)
        events.emit(events.MESSAGES, msgconst.WARNING, msg)
        msg = _('Start to search loader by file content')
        events.emit(events.MESSAGES, msgconst.INFO, msg)

        for item in ld_formats:
            checker = _get_checker(item)
            if not checker is None:
                if checker(path):
                    loader = _get_loader(item)
                    break

    if loader is None:
        msg = _('By file content loader is not found for %s') % (path)
        events.emit(events.MESSAGES, msgconst.WARNING, msg)
        msg = _('Try using fallback loader')
        events.emit(events.MESSAGES, msgconst.INFO, msg)
        if fallback_check(path): loader = im_loader

    if loader is None:
        msg = _('Loader is not found for %s') % (path)
        events.emit(events.MESSAGES, msgconst.ERROR, msg)
    else:
        loader_name = loader.__str__().split(' ')[1]
        msg = _('Loader <%s> is found for %s') % (loader_name, path)
        events.emit(events.MESSAGES, msgconst.OK, msg)
    return loader


def get_saver_by_id(pid):
    saver = _get_saver(pid)
    if not saver:
        msg = _('Saver is not found for id %u') % (pid)
        events.emit(events.MESSAGES, msgconst.ERROR, msg)
    return saver


def get_saver(path, experimental=False):
    ext = get_file_extension(path)
    saver = None
    sv_formats = [] + uc2const.SAVER_FORMATS

    msg = _('Start to search saver by file extension %s') % (ext.__str__())
    events.emit(events.MESSAGES, msgconst.INFO, msg)

    if experimental:
        sv_formats += uc2const.EXPERIMENTAL_SAVERS
    for item in sv_formats:
        if ext in uc2const.FORMAT_EXTENSION[item]:
            saver = _get_saver(item)
            break
    if saver is None:
        msg = _('Saver is not found for %s file format') % (ext.__str__())
        events.emit(events.MESSAGES, msgconst.ERROR, msg)
    else:
        msg = _('Saver is found for extension %s') % (ext.__str__())
        events.emit(events.MESSAGES, msgconst.OK, msg)
    return saver
