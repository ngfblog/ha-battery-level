"""
This component provides support for Battery Level.
For more details about this component, please refer to the documentation at
https://home-assistant.io/components/ham/
"""
import logging

import voluptuous as vol

from homeassistant.helpers import config_validation as cv

from homeassistant.components.binary_sensor import DOMAIN as BINARY_SENSOR_DOMAIN
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.components.switch import DOMAIN as SWITCH_DOMAIN
from homeassistant.components.lock import DOMAIN as LOCK_DOMAIN
from homeassistant.components.light import DOMAIN as LIGHT_DOMAIN
from homeassistant.components.zwave import DOMAIN as ZWAVE_DOMAIN
from homeassistant.components.climate import DOMAIN as CLIMATE_DOMAIN

from homeassistant.components.notify import DOMAIN as NOTIFY_DOMAIN

from .const import *
from .battery_level_data import BatteryLevelData

DEPENDENCIES = [BINARY_SENSOR_DOMAIN, SENSOR_DOMAIN, SWITCH_DOMAIN, LOCK_DOMAIN, LIGHT_DOMAIN, ZWAVE_DOMAIN,
                CLIMATE_DOMAIN, NOTIFY_DOMAIN]

_LOGGER = logging.getLogger(__name__)

NOTIFY_SCHEMA = vol.Schema({
    vol.Required(CONF_NOTIFY_ENTITY_ID): cv.entity_id,
    vol.Optional(CONF_NOTIFY_WHEN): cv.string,
    vol.Required(CONF_THRESHOLD): vol.All(vol.Coerce(int)),
})

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional(CONF_NOTIFY): NOTIFY_SCHEMA,

    }),
}, extra=vol.ALLOW_EXTRA)


def setup(hass, config):
    """Set up an Home Automation Manager component."""

    try:
        conf = config[DOMAIN]
        conf_notify = conf[CONF_NOTIFY]
        conf_notify_entity_id = conf_notify[CONF_NOTIFY_ENTITY_ID]
        conf_threshold = conf_notify[CONF_THRESHOLD]
        conf_notify_when = None

        if CONF_NOTIFY_WHEN in conf_notify:
            conf_notify_when = conf_notify[CONF_NOTIFY_WHEN]

        notify_data = {
            CONF_NOTIFY_ENTITY_ID: conf_notify_entity_id,
            CONF_NOTIFY_WHEN: conf_notify_when,
            CONF_THRESHOLD: conf_threshold
        }

        _LOGGER.info(f'Configuration of notify: {notify_data}')

        scan_interval = SCAN_INTERVAL

        bl_data = BatteryLevelData(hass, scan_interval, notify_data)

        was_initialized = bl_data.was_initialized()

        if was_initialized:
            hass.data[DATA_BL] = bl_data

        return was_initialized

    except Exception as ex:
        _LOGGER.error(f'Error while initializing BL, exception: {str(ex)}')

        hass.components.persistent_notification.create(
            f'Error: {str(ex)}<br />You will need to restart hass after fixing.',
            title=NOTIFICATION_TITLE,
            notification_id=NOTIFICATION_ID)

        return False
