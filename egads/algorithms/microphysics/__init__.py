"""
EGADS microphysics algorithms. See EGADS Algorithm Documentation for more info.
"""

__author__ = "ohenry"
__date__ = "2018-03-05 11:13"
__version__ = "1.1"

import logging
try:
    from .diameter_effective_dmt import *
    from .diameter_mean_raf import *
    from .diameter_median_volume_dmt import *
    from .extinction_coeff_dmt import *
    from .mass_conc_dmt import *
    from .number_conc_total_dmt import *
    from .number_conc_total_raf import *
    from .sample_area_oap_all_in_raf import *
    from .sample_area_oap_center_in_raf import *
    from .sample_area_scattering_raf import *
    from .sample_volume_general_raf import *
    from .surface_area_conc_dmt import *
    logging.info('egads [microphysics] algorithms have been loaded')
except Exception:
    logging.exception('an error occurred during the loading of a [microphysics] algorithm')
