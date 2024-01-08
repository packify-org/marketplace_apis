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

from marketplace_apis.yandex.base import MarketApiBaseModel
from marketplace_apis.yandex.campaign.settings_local_region import (
    CampaignSettingsLocalRegion,
)


@dataclass
class CampaignSettings(MarketApiBaseModel):
    """Настройки магазина"""

    countryRegion: int
    """Идентификатор региона, в котором находится магазин."""
    shopName: str
    """Наименование магазина на Яндекс Маркете.
    Если наименование отсутствует, значение параметра выводится — ``null``."""
    useOpenStat: bool
    """Признак использования внешней интернет-статистики. Возможные значения:
        
    * ``false`` — внешняя интернет-статистика не используется.
    * ``true`` — внешняя интернет-статистика используется."""
    localRegion: CampaignSettingsLocalRegion
    """Информация о своем регионе магазина."""
    showInContext: bool | None = None
    """Признак размещения магазина на сайтах партнеров Яндекс Дистрибуции.
    Возможные значения:

    * ``false`` — магазин не размещен на сайтах партнеров Яндекс Дистрибуции.
    * ``true`` — магазин размещен на сайтах партнеров Яндекс Дистрибуции."""
    showInPremium: bool | None = None
    """Признак показа предложений магазина в рекламном блоке над
    результатами поиска (Спецразмещение).
    Возможные значения:

    * ``false`` — предложения не показываются в блоке Спецразмещения.
    * ``true`` — предложения показываются в блоке Спецразмещения."""
