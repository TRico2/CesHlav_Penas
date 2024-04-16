
AZ_update_template = '''
{{
  "data": {{
    "common": {{
      "priority": 1,
      "id": 1,
      "name": "Bojler",
      "status": 4,
      "signal": -29,
      "type": 1,
      "sn": "N/A",
      "fw": "002.000.000.0418",
      "hw": 210
    }},
    "power": {{
      "output": [
        0,
        0,
        0
      ],
      "boost": 0,
      "temperature": 16
    }},
    "settings": [
      {{
        "power": {{
          "max": {power_limit},
          "target": 100000,
          "targetTemperature": {target_temp},
          "targetTemperatureBoost": 50
        }},
        "boost": {{
          "mode": 0,
          "windows": [
            {{
              "enabled": 1,
              "start": 1080,
              "stop": 1260
            }},
            {{
              "enabled": 1,
              "start": 1080,
              "stop": 1260
            }},
            {{
              "enabled": 1,
              "start": 1080,
              "stop": 1260
            }}
          ]
        }}
      }},
      {{
        "power": {{
          "max": 2400,
          "target": 10,
          "targetTemperature": 40,
          "targetTemperatureBoost": 60
        }},
        "boost": {{
          "mode": 0,
          "windows": [
            {{
              "enabled": 1,
              "start": 1080,
              "stop": 1260
            }},
            {{
              "enabled": 1,
              "start": 1080,
              "stop": 1260
            }},
            {{
              "enabled": 1,
              "start": 1080,
              "stop": 1260
            }}
          ]
        }}
      }}
    ]
  }}
}}
'''

AZ_update_template = AZ_update_template.replace(' ', '')
AZ_update_template = AZ_update_template.replace('\n', '')