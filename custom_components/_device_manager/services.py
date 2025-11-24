# config/custom_components/device_manager/services.py

import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import async_get as get_dev_reg
from homeassistant.helpers.entity_registry import async_get as get_ent_reg

_LOGGER = logging.getLogger(__name__)

async def async_remove_device_and_entities(hass: HomeAssistant, device_id: str) -> None:
    """
    指定した device_id のデバイスと、
    それに関連付けられたエンティティをすべて削除する。
    """
    dev_reg = get_dev_reg(hass)
    ent_reg = get_ent_reg(hass)

    # 1) まずそのデバイスに紐づくエンティティを取得して削除
    entries = list(ent_reg.async_entries_for_device(device_id))
    for entry in entries:
        _LOGGER.info("Removing entity %s", entry.entity_id)
        ent_reg.async_remove(entry.entity_id)

    # 2) エンティティを消したあとでデバイスを削除
    _LOGGER.info("Removing device %s", device_id)
    dev_reg.async_remove_device(device_id)
