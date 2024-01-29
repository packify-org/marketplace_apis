# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (C) 2023  Anatoly Raev
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

FILTER_PREFIX_LENGTH = len("filter_")
WITH_PREFIX_LENGTH = len("with_")


def kwargs_to_filters(kwargs) -> tuple[dict, dict]:
    filter_ = {}
    with_ = {}
    for k, v in kwargs.items():
        k: str
        if k.startswith("filter_"):
            filter_[k[FILTER_PREFIX_LENGTH:]] = v
        elif k.startswith("with_"):
            with_[k[WITH_PREFIX_LENGTH:]] = v
    return filter_, with_
