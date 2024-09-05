import atexit
import os
import platform
import uuid

import bpy

from .. import bl_info, utils
from ..vendor.mixpanel import BufferedConsumer, Mixpanel
from ..vendor.requests.sessions import Session

_UID_FILE = "uid"
_UID_PATH = ".config/gscatter/"
_TOKEN = os.getenv("MIXPANELTOKEN") or 'a010ba8974d9238dbc8546cf8b3c1ac3'
_BUFSIZE = 20
_API_HOST = "api-eu.mixpanel.com"
_DEFAULT_PROPS = {
    'Addon Version': str(bl_info.get('version')),
    'Blender Version': bpy.app.version_string,
    'OS': platform.system(),
}


class _SessionWithIpOverride:

    def __init__(self, session: Session):
        self._session = session

    def post(self, url: str, data: dict, auth: dict, timeout: float, verify: bool):
        data['ip'] = 1
        return self._session.post(url=url, data=data, auth=auth, timeout=timeout, verify=verify)


_mp_consumer = BufferedConsumer(_BUFSIZE, api_host=_API_HOST)
_mp_consumer._consumer._session = _SessionWithIpOverride(_mp_consumer._consumer._session)
_mp = Mixpanel(_TOKEN, consumer=_mp_consumer)


def track(event: str, properties: dict = None, ignorePrefs: bool = False):
    try:
        if uidFileExists():
            if properties is None:
                properties = {}

            uid = readUidFile()
            properties.update(_DEFAULT_PROPS)

            if ignorePrefs:
                _mp.track(uid, event, properties)
                return

            prefs = utils.getters.get_preferences()
            if prefs.tracking_interaction:
                _mp.track(uid, event, properties)
    except Exception as e:
        print(e)


def getAbsoluteUidFilename() -> str:
    userdir = os.path.expanduser("~")
    absUidFilename = os.path.join(userdir, _UID_PATH, _UID_FILE)
    return absUidFilename


def uidFileExists() -> bool:
    return os.path.exists(getAbsoluteUidFilename())


def createUidFile(uid: str = None):
    if uidFileExists():
        removeUidFile()

    if uid is None:
        uid = str(uuid.uuid4())

    userdir = os.path.expanduser("~")
    path = os.path.join(userdir, _UID_PATH)
    if not os.path.exists(path):
        os.makedirs(path)

    with open(getAbsoluteUidFilename(), 'w') as f:
        f.write(uid)


def readUidFile() -> str:
    uid = ''
    with open(getAbsoluteUidFilename(), 'r') as f:
        uid = f.readline().strip("\n")
    return uid


def removeUidFile():
    absUidFilename = getAbsoluteUidFilename()
    os.remove(absUidFilename)


def getUid() -> str:
    prefs = utils.getters.get_preferences()
    return prefs.uid


def setUid(uid: str):
    prefs = utils.getters.get_preferences()
    prefs.uid = uid
    bpy.ops.wm.save_userpref()


def uidIsSet() -> bool:
    prefs = utils.getters.get_preferences()
    if prefs.uid == '':
        return False
    return True


def finalize():
    _mp._consumer.flush()


atexit.register(finalize)
