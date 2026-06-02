# Copyright 2026 Louis Masarei-Boulton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from typing import Literal, TypeAlias
from pathlib import Path
from functools import lru_cache

import pygame as pg

from ._custom_types import Colour, AColour

_FontFamily: TypeAlias = Path | str | None
_FontDescriptor: TypeAlias = tuple[_FontFamily, int]  # (fam, size)

@lru_cache(maxsize=32)
def _get_font_obj(fam: _FontFamily, size: int) -> pg.font.Font:
    """Helper to generate font objects."""
    path_str = str(fam) if fam is not None else None
    return pg.font.Font(path_str, size)

@lru_cache(maxsize=1024)
def _render_text_surface(
        text: str,
        colour: Colour | AColour,
        font_family_or_desc: pg.font.Font | _FontDescriptor,
        rotation: float = 0
    ) -> pg.Surface:
        """Renders and rotates a text surface, fully cached."""
        if isinstance(font_family_or_desc, pg.font.Font):
            font_obj = font_family_or_desc
        else:
            fam, size = font_family_or_desc
            font_obj = _get_font_obj(fam, size)

        img = font_obj.render(text, True, colour)
        if rotation != 0:
            img = pg.transform.rotate(img, rotation)

        return img

def draw_text(
        *,
        surface: pg.Surface, pos: tuple[int, int],
        horiz_align: Literal['left', 'centre', 'right'],
        vert_align: Literal['top', 'centre', 'bottom'],
        text: str, colour: Colour | AColour,
        font_family: pg.font.Font | _FontDescriptor,
        rotation: float = 0
    ) -> None:
    """Draws text to the given surface at the specified
    position with the given alignment and rotation.
    Uses `lru_cache` to improve performance."""

    # Fetch the pre-rendered (and potentially pre-rotated) surface from cache
    # Note: font_family needs to be a hashable type (like tuple or Font) for this to work.
    img = _render_text_surface(text, colour, font_family, rotation)
    rect = img.get_rect()

    # Horizontal alignment
    if horiz_align == "left":
        rect.left = pos[0]
    elif horiz_align == "centre":
        rect.centerx = pos[0]
    elif horiz_align == "right":
        rect.right = pos[0]
    else:
        raise ValueError(f"Invalid horiz_align: {horiz_align!r}")

    # Vertical alignment
    if vert_align == "top":
        rect.top = pos[1]
    elif vert_align == "centre":
        rect.centery = pos[1]
    elif vert_align == "bottom":
        rect.bottom = pos[1]
    else:
        raise ValueError(f"Invalid vert_align: {vert_align!r}")

    surface.blit(img, rect)
