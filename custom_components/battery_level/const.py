"""
This component provides support for Battery Level.
For more details about this component, please refer to the documentation at
https://home-assistant.io/components/ham/
"""
from datetime import timedelta

VERSION = '1.0.6'

DOMAIN = 'battery_level'
DATA_BL = 'data_{}'.format(DOMAIN)
SIGNAL_UPDATE_BL = "{}_update".format(DOMAIN)

DEFAULT_NAME = 'Battery Level'

NOTIFICATION_ID = '{}_notification'.format(DOMAIN)
NOTIFICATION_TITLE = '{} Setup'.format(DEFAULT_NAME)

ATTR_BATTERY_LEVEL = 'battery_level'
ATTR_FRIENDLY_NAME = 'friendly_name'
ATTR_LOW_BATTERY_ENTITY_IDS = 'entities'
ATTR_UNIT_OF_MEASUREMENT = 'unit_of_measurement'

CONF_NOTIFY = 'notify'
CONF_NOTIFY_ENTITY_ID = 'notifier_entity_id'
CONF_NOTIFY_WHEN = 'notification_time'

CONF_THRESHOLD = 'threshold'
SCAN_INTERVAL = timedelta(minutes=60)
