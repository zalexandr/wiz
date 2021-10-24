![Lint](https://github.com/sbidy/wiz_light/workflows/Lint/badge.svg) ![Pylint](https://github.com/sbidy/wiz_light/workflows/Pylint/badge.svg)

## Check out my latest post in the "Dev.-Blog"!! ![Click!!!](https://github.com/sbidy/wiz_light/discussions/78#discussioncomment-406814)

# :bulb: wiz_light - V 0.4.2 (out for testing)

One short note: If you have multiple (>5) bulb connected to the HASS, please try to bring all online if you restart the HASS service/container.
Because on older HASS version the startup can be slowed down if multiple bulbs are offline.

There is an issue with bulb when these are offline on start up and swichted on if HASS is started. The bulbs will stay in "not available". This seems to be a bug :wink:. **To fix that you have to switch the entry to "disabled" and than back to "enabled" via the UI (small :gear: in the upper left corner of the UI card).**

There are changes in the bulb detection function. I can't test all possible bulb types in real because I have only two of them :wink:.

## :muscle: Change Log
- Workaround in 0.4.2: The bulb FW 1.22.0 breaks the automated kelvin detection. A workaround was added. Final solution still open.
- Small fix in 0.4.1: The Array for the bulb effects now mapped correctly.
- New in 0.4.: The bulb type and featerus will be autodetected.
- New in 0.4.: Fixing some other small issues. Update to pywizlight 0.4.5
- Working ConfigFlow: Now the bulbs can be configured via UI
- Devices Registration: The Bulb now shows up as "Light" device
- [BETA] The colors now "correct" regarding the HS to RGB-CW conversation in the WiZ app. Thanks to @brettonw for incredible work!(should be tested with non-RGB and non-Kelvin bulbs!! )
- Poll Service: Now it is possible to trigger a status update from the bulb via HASS service. This can be helpful for automations (e.g. motion detectors).
- DNS and IPs Support: The bulbs can now be added with an DNS name or ip.
- Bulb Library Moved: The "YAML" file was removed (because of a policy from HASS dev) and moved to the `pywizlight` repo..
- Tones of other fixes, improvement and removed typos :wink:

### Still missing but "Work in Progress":
- Registration of the bulb to HASS via UDP API. There are features to register the HASS to the bulb to send UDP packages to the HASS if the state of the bulb was changed. This will made the Poll Service obsolete.
- A User Documentaion based on HASS Docs. (with screen shots etc.) will be added (soon :wink:)
- 
### Fix "Unavailable" Bug

To fix bulbs which are stuck in a "unavailability" if they are offline at startup:
![gif](https://github.com/sbidy/wiz_light/blob/master/Fix_na_bug.gif)

### What is declined or rejected:

- Change of the speed of the transition from on to off and off->on. This is not supported via the UDP API and can only be configured via WiZ App.
- The Motion Sensor is not integrated

## :information_source: [Development Log](https://github.com/sbidy/wiz_light/discussions/78)

Here you can find some news and updates!!
I try to create a kind of Development Log to trace changes/decissions and made the current overall development status transparent to you!!

## :warning: Discussions

If you have questions or other comments please use the **new** [Discussions Board](https://github.com/sbidy/wiz_light/discussions).

## 📔 DNS / IP Address Tip
If you are using DHCP IP address features and looking for avoiding static IPs for the bulb, you can use the DNS names.
To avoid the mess with the IPs you can use the Hostnames of the bulbs.
The hostname will be created from the last 6 digest of the MAC and the `wiz-` prefix. Example: `wiz-123123` or `wiz-123ABC` .
So you can have dynamic IPs, but this hostname will not change. The MAC address you can find in your router or via `nc`.
One of the next versions of this integration will show the MAC in the "Device Properties" tab. Overall, your DNS resolution should work 😉.

## 🔄 Test Connction
To test the connection between the bulb and your Wi-Fi router, you can use the RSSI value.
You can test the [RSSI ](https://en.wikipedia.org/wiki/Received_signal_strength_indication) with this command: `echo '{"method":"getPilot","env":"pro","params":{}}' | nc -u -w 1 <AddressOfYourBulb> 38899`.
If the RSSI value is close to -100 the signal is not that good. Everything between -70 and 0 should be fine.

## :blue_heart: Kudos and contributions

Thank you [@angadsingh](https://github.com/angadsingh) for making such incredible improvements!

Thanks to [@simora](https://github.com/simora) for creating a HA Switch <-> WiZ Plug integration!

Thanks to [@jarpatus](https://github.com/jarpatus) for the feedback and enhancements!

Thanks to [@ChrisLizon](https://github.com/ChrisLizon) for the review, feedbacks and improvements!

Thanks to [@brettonw](https://github.com/brettonw) for improving the RGB-CW to HU tranistion!

Thanks to [@vodovozovge](https://github.com/vodovozovge) for the "insider support" for the community!

## :flight_departure: Dependencies

This component has a dependency on `pywizlight` which will be installed automatically by Home Assistant.

## :zap: Supported Bulbs

All bulbs from WiZ are supported.

### Bulb Type detection:
```
e.g. ESP01_SHDW1C_31
ESP01 -- defines the module family (WiFi only bulb in this case)
SH -- Single Head light (most bulbs are single heads) / LED Strip
TW -- Tunable White - can only control CCT and dimming; no color
DW -- Dimmable White (most filament bulbs)
RGB -- Fullstack bulb
1C -- Specific to the hardware - defines PWM frequency + way of controlling CCT temperature
31 -- Related to the hardware revision
```


## Pull request in HA core

https://github.com/home-assistant/core/pull/44779

## Installation via HACS (Home Assistant Community Store)
[![Hacs Installtion](http://img.youtube.com/vi/_LTA07ENpBE/0.jpg)](http://www.youtube.com/watch?v=_LTA07ENpBE "Wiz Lightbulbs and Home Assistant walkthrough - 2021 Phillips Hue Killer?")

## Install for testing

1. Logon to your HA or HASS with SSH
2. Got to the HA `custom_components` directory within the HA installation path (if this is not available - create this directory).
3. Run `cd custom_components`
4. Run `git clone https://github.com/sbidy/wiz_light` within the `custom_components` directory
5. Run `mv wiz_light/custom_components/wiz_light/* wiz_light/` to move the files in the correct diretory
6. Restart your HA/HASS service in the UI with `<your-URL>/config/server_control`
7. Add the bulbs either by:
   - HA UI by navigating to "Integrations" -> "Add Integration" -> "WiZ Light"
   - Manually by adding them to `configuration.yaml`

Questions? Check out the github project [pywizlight](https://github.com/sbidy/pywizlight)

## Enable Debug
```YAML
logger:
    default: warning
    logs:
      homeassistant.components.wiz_light: debug
```

## HA config

## You can now use the HASS UI to add the devices/integration.

To enable the platform integration after installation add

```
light:
  - platform: wiz_light
    name: <Name of the device>
    host: <IP of the bulb>
  - platform: wiz_light
    name: <Name of the device#2>
    host: <IP of the bulb#2>
```

If you want to use the integration as switch

```
switch:
  - platform: wiz_light
    name: <Name of the device>
    host: <IP of the socket>
```
