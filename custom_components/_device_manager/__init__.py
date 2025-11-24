# config/custom_components/device_manager/__init__.py
import logging
import voluptuous as vol
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_DEVICE_ID
from homeassistant.helpers import device_registry as dr
from .services import async_remove_device_and_entities  # 前に作った services.py

_LOGGER = logging.getLogger(__name__)
DOMAIN = "device_manager"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """ロード時にCoordinatorを初期化し、サービス登録も行う"""
    # --- 既存の Coordinator セットアップなど ---
    # （ここに Coordinator 初期化コードが入ります）

    # サービス登録
    def handle_remove_device(call):
        device_id = call.data[CONF_DEVICE_ID]
        hass.async_create_task(
            async_remove_device_and_entities(hass, device_id)
        )

    hass.services.async_register(
        DOMAIN,
        "remove_device",
        handle_remove_device,
        schema=vol.Schema({
            vol.Required(CONF_DEVICE_ID): str
        })
    )
    _LOGGER.debug("Registered service %s.remove_device", DOMAIN)

    return True
