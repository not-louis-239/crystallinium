from typing import Literal, TypeAlias
from pathlib import Path

import pygame as pg
from pygame import Surface

from ._custom_types import Colour, AColour

_FontFamily: TypeAlias = Path | str | None
_FontDescriptor: TypeAlias = tuple[_FontFamily, int]

_font_obj_cache: dict[_FontDescriptor, pg.font.Font] = {}


def draw_text(
        *,
        surface: Surface, pos: tuple[int, int],
        horiz_align: Literal['left', 'centre', 'right'],
        vert_align: Literal['top', 'centre', 'bottom'],
        text: str, colour: Colour | AColour,
        font_family: pg.font.Font | _FontDescriptor,
        rotation: float = 0
    ) -> None:
    if isinstance(font_family, pg.font.Font):
        font_obj = font_family
    else:
        fam, size = font_family
        font_obj_profile: _FontDescriptor = (str(fam) if fam is not None else None, size)

        # Cache font objects to save time
        if font_obj_profile not in _font_obj_cache:
            font_obj = pg.font.Font(font_obj_profile[0], font_obj_profile[1])
            _font_obj_cache[font_obj_profile] = font_obj
        else:
            font_obj = _font_obj_cache[font_obj_profile]

    img = font_obj.render(text, True, colour)
    if rotation != 0:
        img = pg.transform.rotate(img, rotation)

    rect = img.get_rect()

    # Horizontal
    if horiz_align == "left":
        rect.left = pos[0]
    elif horiz_align == "centre":
        rect.centerx = pos[0]
    elif horiz_align == "right":
        rect.right = pos[0]
    else:
        raise ValueError(f"Invalid horiz_align: {horiz_align}")

    # Vertical
    if vert_align == "top":
        rect.top = pos[1]
    elif vert_align == "centre":
        rect.centery = pos[1]
    elif vert_align == "bottom":
        rect.bottom = pos[1]
    else:
        raise ValueError(f"Invalid vert_align: {vert_align}")

    surface.blit(img, rect)

