# config/custom_components/device_manager/config_flow.py
import voluptuous as vol
from homeassistant import config_entries
from . import DOMAIN

@config_entries.HANDLERS.register(DOMAIN)
class DeviceManagerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Device Manager Config Flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema({}),
            )
        return self.async_create_entry(title="Device Manager", data={})