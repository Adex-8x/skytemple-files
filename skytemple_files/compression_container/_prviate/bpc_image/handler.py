#  Copyright 2020-2022 Capypara and the SkyTemple Contributors
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
from typing import Type

from skytemple_files.compression_container.base_handler import CompressionContainerHandler
from skytemple_files.compression_container.protocol import CompressionContainerProtocol


class BpcImgHandler(CompressionContainerHandler):
    @classmethod
    def magic_word(cls) -> bytes:
        return b'BPCIMG'

    @classmethod
    def load_python_model(cls) -> Type[CompressionContainerProtocol]:
        from skytemple_files.compression_container._prviate.bpc_image._pymodel import BpcImageCompressionContainer
        return BpcImageCompressionContainer

    @classmethod
    def load_native_model(cls) -> Type[CompressionContainerProtocol]:
        from skytemple_rust._st_bpc_image_compression import BpcImageCompressionContainer
        return BpcImageCompressionContainer