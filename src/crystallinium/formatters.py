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

def format_time(s: float, /) -> str:
    """Format a time in seconds to a human-readable string."""
    hours = s // 3600
    minutes = (s // 60) % 60
    seconds = (s % 60) // 1
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def _test():
    durations = [1, 3600, 7200, 86400, 90000]
    for duration in durations:
        print(f"{duration} seconds is {format_time(duration)}")

if __name__ == "__main__":
    _test()
