#  Copyright 2020-2024 Capypara and the SkyTemple Contributors
#
#  This file is part of SkyTemple.
#
#  SkyTemple is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SkyTemple is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SkyTemple.  If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations

from collections.abc import Callable

from ndspy.rom import NintendoDSRom

from skytemple_files.common.i18n_util import _
from skytemple_files.common.ppmdu_config.data import (
    GAME_REGION_EU,
    GAME_REGION_US,
    GAME_REGION_JP,
    GAME_VERSION_EOS,
    Pmd2Data,
)
from skytemple_files.common.util import read_u32
from skytemple_files.patch.category import PatchCategory
from skytemple_files.patch.handler.abstract import AbstractPatchHandler

NEW_INSTRUCTION = 0xE1A00000
OFFSET_RAM_EU = 0x204F66C
OFFSET_RAM_US = 0x204F334
OFFSET_RAM_JP = 0x204F68C


class RemoveBodySizeCheckPatchHandler(AbstractPatchHandler):
    @property
    def name(self) -> str:
        return "RemoveBodySizeCheck"

    @property
    def description(self) -> str:
        return _("Removes the total body size check before entering a dungeon.")

    @property
    def author(self) -> str:
        return "Frostbyte"

    @property
    def version(self) -> str:
        return "0.1.0"

    @property
    def category(self) -> PatchCategory:
        return PatchCategory.IMPROVEMENT_TWEAK

    def is_applied(self, rom: NintendoDSRom, config: Pmd2Data) -> bool:
        arm9 = config.bin_sections.arm9
        arm9_bytes = rom.arm9
        if config.game_version == GAME_VERSION_EOS:
            if config.game_region == GAME_REGION_EU:
                return read_u32(arm9_bytes, OFFSET_RAM_EU - arm9.loadaddress) == NEW_INSTRUCTION
            elif config.game_region == GAME_REGION_US:
                return read_u32(arm9_bytes, OFFSET_RAM_US - arm9.loadaddress) == NEW_INSTRUCTION
            elif config.game_region == GAME_REGION_JP:
                return read_u32(arm9_bytes, OFFSET_RAM_JP - arm9.loadaddress) == NEW_INSTRUCTION
        raise NotImplementedError()

    def apply(self, apply: Callable[[], None], rom: NintendoDSRom, config: Pmd2Data) -> None:
        # Apply the patch
        apply()

    def unapply(self, unapply: Callable[[], None], rom: NintendoDSRom, config: Pmd2Data) -> None:
        raise NotImplementedError()
