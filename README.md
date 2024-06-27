# CesHlav_Penas
Praktická část odborné práce s názvem: Inteligentní řízení fotovoltaické elektrárny a její propojení s chytrou domácností
#### Návod k instalaci integrace:   
1. Složku s integrací vložte do složky config/custom_components v HomeAssistant úložišti   
2. Do souboru configuration.yaml vložte:   

_sensor:_  
_- platform: azrouter_   

#### Návod k použití automatizací:   
1. Automatizace zkopírujte do souboru  automations.yaml v HomeAssistant úložišti
2. Scripty zkopírujte do souboru  scripts.yaml v HomeAssistant úložišti
3. Zkontrolujte, že soubor configuration.yaml obsahuje:

_automation: !include automations.yaml_   
_script: !include scripts.yaml_   

4. Pro funkčnost automatizací je potřeba kromě mnou vytvořené integrace ještě integrací:   
     -Home Assistant Czech Energy Spot Prices (https://github.com/rnovacek/homeassistant_cz_energy_spot_prices)   
     -GoodWe inverter (https://github.com/mletenay/home-assistant-goodwe-inverter)   
     -Forecast.Solar (Dostupné na platformě 
