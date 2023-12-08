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
from datetime import date

from marketplace_apis.common.enums import Day
from marketplace_apis.yandex.base import MarketApiBaseModel
from marketplace_apis.yandex.campaigns.settings_time_period import (
    CampaignSettingsTimePeriod,
)


@dataclass
class CampaignSettingsSchedule(MarketApiBaseModel):
    """Расписание работы службы доставки в своем регионе."""

    availableOnHolidays: bool
    """Признак работы службы доставки в государственные праздники. Возможные значения.

    * ``false`` — служба доставки не работает в праздничные дни.
    * ``true`` — служба доставки работает в праздничные дни."""
    customHolidays: list[date]
    """Список дней, в которые служба доставки не работает.
    Дни магазин указал в личном кабинете на Маркете."""
    customWorkingDays: list[date]
    """Список выходных и праздничных дней, в которые служба доставки работает.
    Дни магазин указал в личном кабинете на Маркете."""
    period: CampaignSettingsTimePeriod
    """Период, за который рассчитывается итоговый список нерабочих дней службы
    доставки."""
    totalHolidays: list[date]
    """Итоговый список нерабочих дней службы доставки. Список рассчитывается с учетом
    выходных, нерабочих дней и государственных праздников. Информацию по ним магазин
    указывает в личном кабинете на Маркете."""
    weeklyHolidays: list[Day]
    """Список выходных дней недели и государственных праздников."""
