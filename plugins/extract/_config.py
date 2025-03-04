#!/usr/bin/env python3
""" Default configurations for extract """

import logging
import os

from lib.config import FaceswapConfig

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class Config(FaceswapConfig):
    """ Config File for Extraction """

    def set_defaults(self):
        """ Set the default values for config """
        logger.debug("Setting defaults")
        self.set_globals()
        self._defaults_from_plugin(os.path.dirname(__file__))

    def set_globals(self):
        """
        Set the global options for extract
        """
        logger.debug("Setting global config")
        section = "global"
        self.add_section(title=section, info="Options that apply to all extraction plugins")
        self.add_item(
            section=section,
            title="allow_growth",
            datatype=bool,
            default=False,
            group="settings",
            info="[Nvidia Only]. Enable the Tensorflow GPU `allow_growth` configuration option. "
                 "This option prevents Tensorflow from allocating all of the GPU VRAM at launch "
                 "but can lead to higher VRAM fragmentation and slower performance. Should only "
                 "be enabled if you are having problems running extraction.")
        self.add_item(
            section=section,
            title="aligner_min_scale",
            datatype=float,
            min_max=(0.0, 1.0),
            rounding=2,
            default=0.07,
            group="filters",
            info="Filters out faces below this size. This is a multiplier of the minimum "
                 "dimension of the frame (i.e. 1280x720 = 720). If the original face extract "
                 "box is smaller than the minimum dimension times this multiplier, it is "
                 "considered a false positive and discarded. Faces which are found to be "
                 "unusually smaller than the frame tend to be misaligned images, except in "
                 "extreme long-shots. These can be usually be safely discarded.")
        self.add_item(
            section=section,
            title="aligner_max_scale",
            datatype=float,
            min_max=(0.0, 10.0),
            rounding=2,
            default=2.00,
            group="filters",
            info="Filters out faces above this size. This is a multiplier of the minimum "
                 "dimension of the frame (i.e. 1280x720 = 720). If the original face extract "
                 "box is larger than the minimum dimension times this multiplier, it is "
                 "considered a false positive and discarded. Faces which are found to be "
                 "unusually larger than the frame tend to be misaligned images except in extreme "
                 "close-ups. These can be usually be safely discarded.")
        self.add_item(
            section=section,
            title="aligner_distance",
            datatype=float,
            min_max=(0.0, 25.0),
            rounding=1,
            default=15,
            group="filters",
            info="Filters out faces who's landmarks are above this distance from an 'average' "
                 "face. Values above 15 tend to be fairly safe. Values above 10 will remove more "
                 "false positives, but may also filter out some faces at extreme angles.")
        self.add_item(
            section=section,
            title="save_filtered",
            datatype=bool,
            default=False,
            group="filters",
            info="If enabled, saves any filtered out images into a sub-folder during the "
                 "extraction process. If disabled, filtered faces are deleted. Note: The faces "
                 "will always be filtered out of the alignments file, regardless of whether you "
                 "keep the faces or not.")
