"""Config flow for AZ router."""
import logging
import voluptuous as vol
from typing import Any, Dict, Optional
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_flow
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME

from .const import DOMAIN

logger = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema({
    vol.Optional(CONF_NAME, description='AZ router device Name'): str,
    vol.Required(CONF_IP_ADDRESS, description='AZ router IP Address'): str
})

class ExampleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input):
        if user_input is not None:
            self.data = user_input
            title = title=f'AZ Router - {user_input[CONF_NAME]}' if user_input[CONF_NAME] else user_input[CONF_IP_ADDRESS]
            return self.async_create_entry(
                title=f'AZ Router - {user_input[CONF_NAME]}',
                data=user_input,
            )

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA
        )