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

from enum import StrEnum, IntEnum


class WarehouseWorkingDay(IntEnum):
    """Рабочие дни склада."""

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class WarehouseStatus(StrEnum):
    """Статус склада.
    .. table:: Соответствие статусов склада со статусами с личном кабинете:
    =====================  ============================
      Статус Seller API	     Статус в личном кабинете
    =====================  ============================
    new                    Активируется
    created                Активный
    disabled               В архиве
    blocked                Заблокирован
    disabled_due_to_limit  На паузе
    error                  Ошибка
    =====================  ============================
    """

    NEW = "new"
    """Активируется"""
    CREATED = "created"
    """Активный"""
    DISABLED = "disabled"
    """В архиве"""
    BLOCKED = "blocked"
    """Заблокирован"""
    DISABLED_DUE_TO_LIMIT = "disabled_due_to_limit"
    """На паузе"""
    ERROR = "error"
    """Ошибка"""


class FirstMileType(StrEnum):
    """Тип первой мили — DropOff или Pickup."""

    DROP_OFF = "DropOff"
    PICKUP = "Pickup"
