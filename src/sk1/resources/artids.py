# -*- coding: utf-8 -*-
#
#  Copyright (C) 2013 by Igor E. Novikov
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import wx

from sk1.resources import pdids, icons

ART_IDS = {
    # ----- Tools
    pdids.SELECT_MODE: icons.TOOL_SELECT,
    pdids.SHAPER_MODE: icons.TOOL_SHAPER,
    pdids.ZOOM_MODE: icons.TOOL_ZOOM,
    pdids.FLEUR_MODE: icons.TOOL_FLEUR,
    pdids.LINE_MODE: icons.TOOL_CREATE_POLY,
    pdids.CURVE_MODE: icons.TOOL_CREATE_CURVE,
    pdids.RECT_MODE: icons.TOOL_CREATE_RECT,
    pdids.ELLIPSE_MODE: icons.TOOL_CREATE_ELLIPSE,
    pdids.TEXT_MODE: icons.TOOL_CREATE_TEXT,
    pdids.POLYGON_MODE: icons.TOOL_CREATE_POLYGON,

    pdids.FILL_MODE: icons.TOOL_FILL,
    pdids.STROKE_MODE: icons.TOOL_STROKE,
    pdids.GRADIENT_MODE: icons.TOOL_GRADIENT,

    # ----- File menu
    wx.ID_NEW: wx.ART_NEW,
    wx.ID_OPEN: wx.ART_FILE_OPEN,
    wx.ID_SAVE: wx.ART_FILE_SAVE,
    wx.ID_SAVEAS: wx.ART_FILE_SAVE_AS,
    wx.ID_CLOSE: icons.PD_CLOSE,
    wx.ID_PRINT_SETUP: icons.PD_PRINT_PREVIEW,
    wx.ID_PRINT: wx.ART_PRINT,
    wx.ID_EXIT: wx.ART_QUIT,
    # ----- Edit menu
    wx.ID_UNDO: wx.ART_UNDO,
    wx.ID_REDO: wx.ART_REDO,
    wx.ID_CUT: wx.ART_CUT,
    wx.ID_COPY: wx.ART_COPY,
    wx.ID_PASTE: wx.ART_PASTE,
    wx.ID_DELETE: wx.ART_DELETE,
    wx.ID_SELECTALL: icons.PD_SELECTALL,
    wx.ID_PROPERTIES: icons.PD_PROPERTIES,
    wx.ID_PREFERENCES: icons.PD_PREFERENCES,
    # ----- View menu
    wx.ID_ZOOM_100: icons.PD_ZOOM_100,
    wx.ID_ZOOM_IN: icons.PD_ZOOM_IN,
    wx.ID_ZOOM_OUT: icons.PD_ZOOM_OUT,
    pdids.ID_ZOOM_PAGE: icons.PD_ZOOM_PAGE,
    wx.ID_ZOOM_FIT: icons.PD_ZOOM_FIT,
    pdids.ID_ICONIZER: icons.PD_PLUGIN_ICONIZER,
    wx.ID_REFRESH: icons.PD_REFRESH,
    # ----- Layout menu
    pdids.ID_INSERT_PAGE: icons.PD_INSERT_PAGE,
    pdids.ID_DELETE_PAGE: icons.PD_DELETE_PAGE,
    pdids.ID_GOTO_PAGE: icons.PD_GOTO_PAGE,
    pdids.ID_NEXT_PAGE: icons.PD_NEXT_PAGE,
    pdids.ID_PREV_PAGE: icons.PD_PREV_PAGE,
    pdids.ID_GUIDES_AT_CENTER: icons.PD_GUIDES_AT_CENTER,
    pdids.ID_PAGE_FRAME: icons.PD_PAGE_FRAME,
    pdids.ID_PAGE_GUIDE_FRAME: icons.PD_PAGE_GUIDE_FRAME,
    pdids.ID_REMOVE_ALL_GUIDES: icons.PD_REMOVE_ALL_GUIDES,
    # ----- Arrange menu
    pdids.ID_POSITION_PLGN: icons.PD_POSITION_PLGN,
    pdids.ID_RESIZE_PLGN: icons.PD_RESIZE_PLGN,
    pdids.ID_SCALE_PLGN: icons.PD_SCALE_PLGN,
    pdids.ID_ROTATE_PLGN: icons.PD_ROTATE_PLGN,
    pdids.ID_SHEAR_PLGN: icons.PD_SHEAR_PLGN,
    pdids.ID_ROTATE_LEFT: icons.CTX_ROTATE_LEFT,
    pdids.ID_ROTATE_RIGHT: icons.CTX_ROTATE_RIGHT,
    pdids.ID_MIRROR_H: icons.CTX_MIRROR_H,
    pdids.ID_MIRROR_V: icons.CTX_MIRROR_V,
    pdids.ID_COMBINE: icons.PD_COMBINE,
    pdids.ID_BREAK_APART: icons.PD_BREAK,
    pdids.ID_RAISE_TO_TOP: icons.PD_RAISE_TO_TOP,
    pdids.ID_RAISE: icons.PD_RAISE,
    pdids.ID_LOWER: icons.PD_LOWER,
    pdids.ID_LOWER_TO_BOTTOM: icons.PD_LOWER_TO_BOTTOM,
    pdids.ID_GROUP: icons.PD_GROUP,
    pdids.ID_UNGROUP: icons.PD_UNGROUP,
    pdids.ID_UNGROUPALL: icons.PD_UNGROUP_ALL,
    pdids.ID_PATHS_EXCLUSION: icons.PD_PATHS_EXCLUSION,
    pdids.ID_PATHS_FUSION: icons.PD_PATHS_FUSION,
    pdids.ID_PATHS_INTERSECTION: icons.PD_PATHS_INTERSECTION,
    pdids.ID_PATHS_TRIM: icons.PD_PATHS_TRIM,
    pdids.ID_TO_CURVES: icons.PD_TO_CURVES,
    # ----- Paths menu
    pdids.ID_BEZIER_SEL_ALL_NODES: icons.PD_BEZIER_SEL_ALL_NODES,
    pdids.ID_BEZIER_REVERSE_ALL_PATHS: icons.PD_BEZIER_REVERSE_ALL_PATHS,
    pdids.ID_BEZIER_SEL_SUBPATH_NODES: icons.PD_BEZIER_SEL_SUBPATH_NODES,
    pdids.ID_BEZIER_DEL_SUBPATH: icons.PD_BEZIER_DEL_SUBPATH,
    pdids.ID_BEZIER_REVERSE_SUBPATH: icons.PD_BEZIER_REVERSE_SUBPATH,
    pdids.ID_BEZIER_EXTRACT_SUBPATH: icons.PD_BEZIER_EXTRACT_SUBPATH,
    pdids.ID_BEZIER_ADD_NODE: icons.PD_BEZIER_ADD_NODE,
    pdids.ID_BEZIER_DELETE_NODE: icons.PD_BEZIER_DELETE_NODE,
    pdids.ID_BEZIER_ADD_SEG: icons.PD_BEZIER_ADD_SEG,
    pdids.ID_BEZIER_DELETE_SEG: icons.PD_BEZIER_DELETE_SEG,
    pdids.ID_BEZIER_JOIN_NODE: icons.PD_BEZIER_JOIN_NODE,
    pdids.ID_BEZIER_SPLIT_NODE: icons.PD_BEZIER_SPLIT_NODE,
    pdids.ID_BEZIER_SEG_TO_LINE: icons.PD_BEZIER_SEG_TO_LINE,
    pdids.ID_BEZIER_SEG_TO_CURVE: icons.PD_BEZIER_SEG_TO_CURVE,
    pdids.ID_BEZIER_NODE_CUSP: icons.PD_BEZIER_NODE_CUSP,
    pdids.ID_BEZIER_NODE_SMOOTH: icons.PD_BEZIER_NODE_SMOOTH,
    pdids.ID_BEZIER_NODE_SYMMETRICAL: icons.PD_BEZIER_NODE_SYMMETRICAL,

    # ----- Bitmaps menu
    pdids.ID_CONV_TO_CMYK: icons.PD_CONV_TO_CMYK,
    pdids.ID_CONV_TO_RGB: icons.PD_CONV_TO_RGB,
    pdids.ID_CONV_TO_LAB: icons.PD_CONV_TO_LAB,
    pdids.ID_CONV_TO_GRAY: icons.PD_CONV_TO_GRAY,
    pdids.ID_CONV_TO_BW: icons.PD_CONV_TO_BW,
    pdids.ID_INVERT_BITMAP: icons.PD_INVERT_BITMAP,

    # ----- Text menu
    pdids.ID_UPPER_TEXT: icons.PD_TEXT_UPPERCASE,
    pdids.ID_LOWER_TEXT: icons.PD_TEXT_LOWERCASE,
    pdids.ID_CAPITALIZE_TEXT: icons.PD_TEXT_CAPITALIZE,
    pdids.ID_CLEAR_MARKUP: icons.PD_TEXT_CLEAR_MARKUP,

    # ----- Help menu
    pdids.ID_REPORT_BUG: wx.ART_WARNING,
    pdids.ID_APP_WEBSITE: icons.PD_HOME,
    pdids.ID_APP_FBPAGE: icons.PD_FBPAGE,
    wx.ID_ABOUT: icons.PD_ABOUT,
}
