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
import base64

import httpx

from marketplace_apis.yandex.endpoints import API_PATH


class OAuthMethods:
    @staticmethod
    def get_tokens_by_code(
        client_id: str, client_secret: str, code: int
    ) -> tuple[str, str]:
        # TODO: complete it! (yea-yea, its bad to commit not-working code, i know)
        auth_data = base64.b64encode(f"{client_id}:{client_secret}".encode())
        _ = httpx.post(
            API_PATH["oauth_token"],
            headers={
                "Content-type": "application/x-www-form-urlencoded",
                "Authorization": f"Basic {auth_data.decode()}",
            },
            data={"grant_type": "authorization_code", "code": code},
        )
