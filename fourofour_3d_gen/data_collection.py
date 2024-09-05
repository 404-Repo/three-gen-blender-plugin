import bpy
import os
import platform

from mixpanel import Consumer, Mixpanel

_TOKEN = os.getenv("MIXPANELTOKEN") or "7d1f118a18d0f5724763a5992fb18f96"
_BUFSIZE = 20
_API_HOST = "api-eu.mixpanel.com"
_DEFAULT_PROPS = {
    # "Addon Version": str(bl_info.get("version")),
    "Blender Version": bpy.app.version_string,
    "OS": platform.system(),
}


# class _SessionWithIpOverride:

#     def __init__(self, session: Session):
#         self._session = session

#     def post(self, url: str, data: dict, auth: dict, timeout: float, verify: bool):
#         data["ip"] = 1
#         return self._session.post(url=url, data=data, auth=auth, timeout=timeout, verify=verify)


# _mp_consumer = BufferedConsumer(_BUFSIZE, api_host=_API_HOST)
# # _mp_consumer._consumer._session = _SessionWithIpOverride(_mp_consumer._consumer._session)
# _mp = Mixpanel(_TOKEN, consumer=_mp_consumer)
_mp = Mixpanel(
    _TOKEN,
    consumer=Consumer(api_host="api-eu.mixpanel.com"),
)


def track(event: str, properties: dict = {}):
    properties.update(_DEFAULT_PROPS)
    prefs = bpy.context.preferences.addons[__package__].preferences
    uid = prefs.uid

    if prefs.data_collection:
        _mp.track(uid, event, properties)
