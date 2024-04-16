"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
    SensorEntityDescription,
)

from homeassistant.const import UnitOfTemperature
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
from .coordinator import AZRouterDataUpdateCoordinator
from .const import DOMAIN, ATTRIBUTION, SCAN_INTERVAL, MANUFACTURER
from .entities import SENSOR_TYPES, Settings


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    
    pass

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

    sensors = [AZRouterSensor(coordinator, description) for description in SENSOR_TYPES]
    async_add_entities(sensors)
  

class AZRouterSensor(CoordinatorEntity, SensorEntity):
    """Representation of a AZ router sensor."""

    _attr_attribution = ATTRIBUTION

    def __init__(
        self, coordinator: DataUpdateCoordinator, description: SensorEntityDescription
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

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return (
            self.coordinator.data[self.entity_description.key] if self.coordinator.data else None
        )