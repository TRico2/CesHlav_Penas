"""AzRouter Integration Coordinator."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
    SensorEntityDescription,
)
from homeassistant.const import UnitOfTemperature, UnitOfPower
from .const import DOMAIN, SCAN_INTERVAL, AZ_GET_HEADERS
from .entities import SENSOR_TYPES, NUMBER_TYPES
from datetime import datetime, timedelta, timezone
import aiohttp
import logging

logger = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the AzRouter platform."""
    coordinator = AZRouterDataUpdateCoordinator(hass)
    await coordinator.async_refresh()

    if not coordinator.last_update_success:
        raise UpdateFailed("Initial data fetch failed!")



class AZRouterDataUpdateCoordinator(DataUpdateCoordinator):
    """AzRouter Data Coordinator."""

    def __init__(self, hass: HomeAssistant, config: ConfigEntry):
        """Initialize the data coordinator."""
        super().__init__(
            hass,
            logger=logger,
            name=DOMAIN,
            update_method=self._async_update_data,
            update_interval=SCAN_INTERVAL,
        )
        self.URLSrc = {'status': f'http://{config.data[CONF_IP_ADDRESS]}/api/v1/status',
                       'devices': f'http://{config.data[CONF_IP_ADDRESS]}/api/v1/devices',
                       'power': f'http://{config.data[CONF_IP_ADDRESS]}/api/v1/power',
                       'settings': f'http://{config.data[CONF_IP_ADDRESS]}/api/v1/device/settings',
                       }
        self.device_name = config.data[CONF_NAME]

    async def fetch_data(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=AZ_GET_HEADERS) as response:
                status = response.status
                if status == 200:
                    # Assuming the API returns JSON data
                    data = await response.json()
                    return data
                else:
                    return None

    async def _async_update_data(self):
        """Fetch data from the AzRouterT API."""
        try:
            self.statusData = await self.fetch_data(self.URLSrc['status'])
            self.devicesData = await self.fetch_data(self.URLSrc['devices'])
            self.powerData = await self.fetch_data(self.URLSrc['power'])
            data = {}
            if self.devicesData:
                data['temp_current'] = self.devicesData[0]['power']['temperature']
                data['target_temp'] = self.devicesData[0]['settings'][0]['power']['targetTemperature']
                data['power_limit'] = self.devicesData[0]['settings'][0]['power']['max']
            if self.powerData:
                data['InPowerL1'] = self.powerData['input']['power'][0]['value']
                data['InPowerL2']= self.powerData['input']['power'][1]['value']
                data['InPowerL3']= self.powerData['input']['power'][2]['value']
                data['OutPowerL1'] = self.powerData['output']['power'][0]['value']
                data['OutPowerL2']= self.powerData['output']['power'][1]['value']
                data['OutPowerL3']= self.powerData['output']['power'][2]['value']
            return data
        except Exception as error:
            raise UpdateFailed(f"Error fetching data: {error}") from error