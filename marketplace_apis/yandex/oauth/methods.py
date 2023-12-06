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
    def _get_tokens(
        client_id: str,
        client_secret: str,
        token: str,
        type_: str,
        token_field: None | str = None,
    ) -> dict:
        auth_data = base64.b64encode(f"{client_id}:{client_secret}".encode())
        answer = httpx.post(
            API_PATH["oauth_token"],
            headers={
                "Content-type": "application/x-www-form-urlencoded",
                "Authorization": f"Basic {auth_data.decode()}",
            },
            data={
                "grant_type": type_,
                token_field if token_field else type_: token,
            },
        )
        return answer.json()

    @staticmethod
    def get_tokens_by_code(client_id: str, client_secret: str, code: int) -> dict:
        """# noqa: E501
        Get access and refresh token by code
        https://yandex.ru/dev/market/partner-api/doc/ru/concepts/how-to-use-refresh-token#get-tokens
        :param client_id: app client id
        :param client_secret: app client secret
        :param code: code, that you got after auth
        :return: dict with access_token, expires_in, token_type and refresh_token keys
        """
        return OAuthMethods._get_tokens(
            client_id, client_secret, code, "authorization_code", "code"
        )

    @staticmethod
    def get_tokens_by_refresh(
        client_id: str, client_secret: str, refresh_token: str
    ) -> dict:
        """
        Get new access and refresh token by old refresh token
        :param client_id: app client id
        :param client_secret: app client secret
        :param refresh_token: refresh token
        :return: dict with access_token, expires_in, token_type and refresh_token keys
        """
        return OAuthMethods._get_tokens(
            client_id, client_secret, refresh_token, "refresh_token"
        )
