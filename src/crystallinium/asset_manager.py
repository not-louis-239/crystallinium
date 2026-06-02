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

import os
from pathlib import Path

import pygame as pg

class AssetManager:
    def __init__(self) -> None:
        self.root_dir: Path = Path(".")  # can be changed later

        # Centralized caches
        self._images: dict[str, pg.Surface] = {}
        self._sounds: dict[str, pg.mixer.Sound] = {}
        self._fonts: dict[str, Path] = {}

    def set_root_dir(self, path: Path | str) -> None:
        """
        Allows the game developer to point the library to their assets folder, e.g.:
        >>> manager.set_base_directory("./assets")
        """
        self.root_dir = Path(path) if not isinstance(path, Path) else path

    def _validate_fp(self, fp: Path | str) -> None:
        """Check that a file path both exists and is readable."""
        if not os.access(fp, os.R_OK):
            raise PermissionError(f"Permission denied: '{fp}'")
        if not Path(fp).exists():
            raise FileNotFoundError(f"No such file or directory: '{fp}'")

    def register_font(self, alias: str, relative_path: str) -> None:
        """Register a font file with a friendly nickname (alias)."""
        full_path = self.root_dir / relative_path
        self._validate_fp(full_path)
        self._fonts[alias] = full_path

    def get_font_path(self, alias: str) -> Path:
        """Retrieve a registered font path by its alias."""
        if alias not in self._fonts:
            raise ValueError(f"Unregistered font alias '{alias}'. Use register_font(...) to register it.")
        return self._fonts[alias]

    def load_image(self, relative_path: str, *, use_alpha: bool = True) -> pg.Surface:
        """Loads and caches an image dynamically. Returns the Surface."""

        # Use the relative path string as the unique dictionary key
        if relative_path not in self._images:
            full_path = self.root_dir / relative_path

            # Load and optimize the surface for Pygame performance
            self._validate_fp(full_path)
            surface = pg.image.load(full_path)
            surface = surface.convert_alpha() if use_alpha else surface.convert()

            self._images[relative_path] = surface

        return self._images[relative_path]

    def load_sound(self, relative_path: str, *, volume: float | None = None) -> pg.mixer.Sound:
        """Loads and caches a sound dynamically. Returns the Sound object.
        Optionally sets the volume of the sound if the argument is passed."""
        if relative_path not in self._sounds:
            full_path = self.root_dir / relative_path

            # Validate file path, then load the audio object
            self._validate_fp(full_path)
            self._sounds[relative_path] = pg.mixer.Sound(full_path)

        sound = self._sounds[relative_path]
        if volume is not None:
            sound.set_volume(volume)
        return sound

    def clear(self) -> None:
        """Clear all internal caches."""
        self._images.clear()
        self._sounds.clear()
        self._fonts.clear()
