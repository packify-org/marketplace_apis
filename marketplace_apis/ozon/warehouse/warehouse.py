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
from dataclasses import dataclass

from marketplace_apis.ozon.base import SellerApiBaseModel
from marketplace_apis.ozon.warehouse.enums import WarehouseWorkingDay, WarehouseStatus
from marketplace_apis.ozon.warehouse.first_mile import FirstMile


@dataclass
class Warehouse(SellerApiBaseModel):
    """Склад"""

    has_entrusted_acceptance: bool
    """Признак доверительной приёмки. ``true``, если доверительная приёмка включена на
    складе."""
    is_rfbs: bool
    """Признак работы склада по схеме rFBS:

    * ``true`` — склад работает по схеме rFBS;
    * ``false`` — не работает по схеме rFBS."""
    name: str
    """Название склада."""
    warehouse_id: str
    """Идентификатор склада."""
    can_print_act_in_advance: str
    """Возможность печати акта приёма-передачи заранее.
    ``true``, если печатать заранее возможно."""
    first_mile_type: FirstMile
    """Первая миля FBS."""
    has_postings_limit: bool
    """Признак наличия лимита минимального количества заказов. true, если лимит есть."""
    is_karantin: bool
    """Признак, что склад не работает из-за карантина."""
    is_kgt: bool
    """Признак, что склад принимает крупногабаритные товары."""
    is_timetable_editable: bool
    """Признак, что можно менять расписание работы складов."""
    min_postings_limit: int
    """Минимальное значение лимита — количество заказов, которые можно привезти в одной
    поставке."""
    postings_limit: int
    """Значение лимита. -1, если лимита нет."""
    min_working_days: int
    """Количество рабочих дней склада."""
    status: WarehouseStatus
    """Статус склада."""
    working_days: list[WarehouseWorkingDay]
    """Рабочие дни склада."""
