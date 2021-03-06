#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SMPTE 240M Colourspace
======================

Defines the *SMPTE 240M* colourspace:

-   :attr:`SMPTE_240M_COLOURSPACE`.

See Also
--------
`RGB Colourspaces Jupyter Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/models/rgb.ipynb>`_

References
----------
.. [1]  Society of Motion Picture and Television Engineers. (1999).
        ANSI/SMPTE 240M-1995 - Signal Parameters - 1125-Line High-Definition
        Production Systems, 1–7. Retrieved from
        http://car.france3.mars.free.fr/\
HD/INA-%2026%20jan%2006/SMPTE%20normes%20et%20confs/s240m.pdf
.. [2]  Society of Motion Picture and Television Engineers. (2004). SMPTE C
        Color Monitor Colorimetry. In RP 145:2004 (Vol. RP 145:200).
        doi:10.5594/S9781614821649
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.colorimetry import ILLUMINANTS
from colour.models.rgb import (RGB_Colourspace, normalised_primary_matrix,
                               oetf_SMPTE240M, eotf_SMPTE240M)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'SMPTE_240M_PRIMARIES', 'SMPTE_240M_ILLUMINANT', 'SMPTE_240M_WHITEPOINT',
    'SMPTE_240M_TO_XYZ_MATRIX', 'XYZ_TO_SMPTE_240M_MATRIX',
    'SMPTE_240M_COLOURSPACE'
]

SMPTE_240M_PRIMARIES = np.array([
    [0.630, 0.340],
    [0.310, 0.595],
    [0.155, 0.070],
])
"""
*SMPTE 240M* colourspace primaries.

SMPTE_240M_PRIMARIES : ndarray, (3, 2)
"""

SMPTE_240M_ILLUMINANT = 'D65'
"""
*SMPTE 240M* colourspace whitepoint name as illuminant.

SMPTE_240M_ILLUMINANT : unicode
"""

SMPTE_240M_WHITEPOINT = (
    ILLUMINANTS['CIE 1931 2 Degree Standard Observer'][SMPTE_240M_ILLUMINANT])
"""
*SMPTE 240M* colourspace whitepoint.

SMPTE_240M_WHITEPOINT : ndarray
"""

SMPTE_240M_TO_XYZ_MATRIX = normalised_primary_matrix(SMPTE_240M_PRIMARIES,
                                                     SMPTE_240M_WHITEPOINT)
"""
*SMPTE 240M* colourspace to *CIE XYZ* tristimulus values matrix.

SMPTE_240M_TO_XYZ_MATRIX : array_like, (3, 3)
"""

XYZ_TO_SMPTE_240M_MATRIX = np.linalg.inv(SMPTE_240M_TO_XYZ_MATRIX)
"""
*CIE XYZ* tristimulus values to *SMPTE 240M* colourspace matrix.

XYZ_TO_SMPTE_240M_MATRIX : array_like, (3, 3)
"""

SMPTE_240M_COLOURSPACE = RGB_Colourspace(
    'SMPTE 240M',
    SMPTE_240M_PRIMARIES,
    SMPTE_240M_WHITEPOINT,
    SMPTE_240M_ILLUMINANT,
    SMPTE_240M_TO_XYZ_MATRIX,
    XYZ_TO_SMPTE_240M_MATRIX,
    oetf_SMPTE240M,
    eotf_SMPTE240M)  # yapf: disable
"""
*SMPTE 240M* colourspace.

SMPTE_240M_COLOURSPACE : RGB_Colourspace
"""
