"""AzRouter numeric settings entities"""
from __future__ import annotations

from homeassistant.components.number import (
    NumberDeviceClass,
    NumberEntity,
    NumberEntityDescription,
)

from dataclasses import dataclass
from homeassistant.const import UnitOfTemperature, UnitOfPower, EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .coordinator import AZRouterDataUpdateCoordinator, SENSOR_TYPES
from .const import DOMAIN, ATTRIBUTION, MANUFACTURER, AZ_POST_HEADERS
import logging
from .entities import NUMBER_TYPES, Settings
import aiohttp
from .msg_templates import AZ_update_template


logger = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities):
    settings = Settings(
        IPAddress = config.data[CONF_IP_ADDRESS],
        name = config.data[CONF_NAME]
    )

    hassData = hass.data[DOMAIN]
    if 'coordinator' in hassData:
        coordinator = hassData['coordinator']
    else:
        hassData['coordinator'] = coordinator = AZRouterDataUpdateCoordinator(hass, config)

    numbers = [AZRouterNumber(coordinator, description) for description in NUMBER_TYPES]
    async_add_entities(numbers)


class AZRouterNumber(CoordinatorEntity, NumberEntity):
    """Representation of a AZ router sensor."""

    _attr_attribution = ATTRIBUTION

    def __init__(
        self, coordinator: DataUpdateCoordinator, description: NumberEntityDescription
    ) -> None:
        """Initialize the AZ router sensor."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{DOMAIN}-{description.key}-{coordinator.device_name}"
      
    @property
    def device_info(self):
        """Return the device info."""
        return DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={(DOMAIN, self.platform.config_entry.unique_id)},
            manufacturer=MANUFACTURER,
            model="A-Z Router smart",
            name="AzRouter", 
        )

    async def write_data(self, url, power_limit, target_temp):
        async with aiohttp.ClientSession() as session:
            postData = AZ_update_template.format(power_limit=power_limit, target_temp=target_temp)

            async with session.post(url, headers=AZ_POST_HEADERS, data=postData.encode('utf-8')) as response:
                # Assuming the API returns JSON data
                status = response.status
                data = await response.text()
                return data

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return (
            self.coordinator.data[self.entity_description.key] if self.coordinator.data else None
        )

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        url = self.coordinator.URLSrc['settings']
        if hasattr(self.coordinator, 'data') and self.coordinator.data and 'target_temp' in self.coordinator.data:
            self.coordinator.data[self.entity_description.key] = value

            target_temp = self.coordinator.data['target_temp']
            power_limit = self.coordinator.data['power_limit']

            await self.write_data(url, power_limit, target_temp)