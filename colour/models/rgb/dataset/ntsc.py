#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
NTSC Colourspace
================

Defines the *NTSC* colourspace:

-   :attr:`NTSC_COLOURSPACE`.

See Also
--------
`RGB Colourspaces Jupyter Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/models/rgb.ipynb>`_

References
----------
.. [1]  International Telecommunication Union. (1998). Recommendation ITU-R
        BT.470-6 - CONVENTIONAL TELEVISION SYSTEMS. Retrieved from
        http://www.itu.int/dms_pubrec/itu-r/rec/bt/\
R-REC-BT.470-6-199811-S!!PDF-E.pdf
"""

from __future__ import division, unicode_literals

from colour.models.rgb import RGB_Colourspace
from colour.models.rgb.dataset.itur_bt_470 import (
    BT470_525_PRIMARIES, BT470_525_WHITEPOINT, BT470_525_ILLUMINANT,
    BT470_525_TO_XYZ_MATRIX, XYZ_TO_BT470_525_MATRIX, BT470_525_COLOURSPACE)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'NTSC_PRIMARIES', 'NTSC_ILLUMINANT', 'NTSC_WHITEPOINT',
    'NTSC_TO_XYZ_MATRIX', 'XYZ_TO_NTSC_MATRIX', 'NTSC_COLOURSPACE'
]

NTSC_PRIMARIES = BT470_525_PRIMARIES
"""
*NTSC* colourspace primaries.

NTSC_PRIMARIES : ndarray, (3, 2)
"""

NTSC_ILLUMINANT = BT470_525_ILLUMINANT
"""
*NTSC* colourspace whitepoint name as illuminant.

NTSC_ILLUMINANT : unicode
"""

NTSC_WHITEPOINT = BT470_525_WHITEPOINT
"""
*NTSC* colourspace whitepoint.

NTSC_WHITEPOINT : ndarray
"""

NTSC_TO_XYZ_MATRIX = BT470_525_TO_XYZ_MATRIX
"""
*NTSC* colourspace to *CIE XYZ* tristimulus values matrix.

NTSC_TO_XYZ_MATRIX : array_like, (3, 3)
"""

XYZ_TO_NTSC_MATRIX = XYZ_TO_BT470_525_MATRIX
"""
*CIE XYZ* tristimulus values to *NTSC* colourspace matrix.

XYZ_TO_NTSC_MATRIX : array_like, (3, 3)
"""

NTSC_COLOURSPACE = RGB_Colourspace(
    'NTSC',
    NTSC_PRIMARIES,
    NTSC_WHITEPOINT,
    NTSC_ILLUMINANT,
    NTSC_TO_XYZ_MATRIX,
    XYZ_TO_NTSC_MATRIX,
    BT470_525_COLOURSPACE.encoding_cctf,
    BT470_525_COLOURSPACE.decoding_cctf)  # yapf: disable
"""
*NTSC* colourspace.

NTSC_COLOURSPACE : RGB_Colourspace
"""
