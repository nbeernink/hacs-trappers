from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    sensors = [
        TrappersSensor(coordinator, "balance", "Trappers Balance", "Trappers", "mdi:bicycle", SensorStateClass.TOTAL),
        TrappersSensor(coordinator, "workdays", "Trappers Workdays", "Days", "mdi:calendar-clock", None),
        TrappersSensor(coordinator, "total_trips", "Total Trappers Trips", "Trips", "mdi:counter", None),
        TrappersSensor(coordinator, "last_registration", "Trappers Last Registration", None, "mdi:calendar-check", None),
        TrappersSensor(coordinator, "last_reward", "Trappers Last Reward", "Trappers", "mdi:star-circle", None),
    ]

    async_add_entities(sensors)

class TrappersSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, key, name, unit, icon, state_class):
        super().__init__(coordinator)
        self._key = key
        self._attr_name = name
        self._attr_unique_id = f"trappers_{key}"
        self._attr_native_unit_of_measurement = unit
        self._attr_icon = icon
        self._attr_state_class = state_class

    @property
    def native_value(self):
        return self.coordinator.data.get(self._key)
