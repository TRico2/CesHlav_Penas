
from homeassistant.const import UnitOfTemperature, UnitOfPower, EntityCategory
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
)
from homeassistant.components.number import (
    NumberDeviceClass,
    NumberEntityDescription,
)
from dataclasses import dataclass


@dataclass
class Settings:
    IPAddress: str
    name: str

NUMBER_TYPES: tuple[NumberEntityDescription, ...] = (
      NumberEntityDescription(
        key='target_temp',
        name='AZRouter Target temperature',
        icon='mdi:thermometer',
        #entity_category=EntityCategory.CONFIG,
        device_class=NumberDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        native_step=5,
        native_min_value=20,
        native_max_value=100,
    ),
    NumberEntityDescription(
        key='power_limit',
        name='AZRouter Max power',
        icon='mdi:home-lightning-bolt-outline',
        device_class=NumberDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        native_step=1,
        native_min_value=0,
        native_max_value=4000,
    ),
)

SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key='temp_current',
        name='AZRouter Temperature',
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
     SensorEntityDescription(
        key='InPowerL1',
        name='AZRouter Input power L1',
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
    ),
     SensorEntityDescription(
        key='InPowerL2',
        name='AZRouter Input power L2',
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
    ),
     SensorEntityDescription(
        key='InPowerL3',
        name='AZRouter Input power L3',
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    SensorEntityDescription(
        key='OutPowerL1',
        name='AZRouter Output power L1',
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
    ),
     SensorEntityDescription(
        key='OutPowerL2',
        name='AZRouter Output power L2',
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
    ),
     SensorEntityDescription(
        key='OutPowerL3',
        name='AZRouter Output power L3',
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
    )
)