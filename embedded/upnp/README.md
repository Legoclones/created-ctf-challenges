# UPnP
Description:
```markdown
I found that my router has a UPnP service exposed on port 52881 and started interacting with it. Using some basic enumeration tools, I retrieved a list of UPnP actions. The only one that I was able to actually get anything back from is `GetDeviceInfo`, but I can't make any sense of it... can you?

What's the base64-encoded `nonce` value? 

Flag format - `byuctf{base64value}`

[actions.txt] [msg.bin]
```

## Writeup
The list of actions + some OSINT will help you figure out the format being used to convey information here. We found documentation of these actions for the WFAWLANConfig service [here](https://www.wi-fi.org/system/files/WFA_WLANConfig_1_0_Template_1_01.pdf). Values use TLV format and the [Wi-Fi Simple Config specification](https://ndeflib.readthedocs.io/en/stable/records/wifi.html), otherwise known as Wi-Fi Protected Setup, or WPS.

We were able to decode the output from the GetDeviceInfo action using the codes defined in [this header file](https://android.googlesource.com/kernel/common.git/+/bcmdhd-3.10/drivers/net/wireless/bcmdhd/include/proto/wps.h), resulting in the following information:

```python
Device Info:
        Version: b'\x10'
        Message Type: b'\x04'
        UUID_E: b'\x11"3DUfw\x88\x99\xaa\xe8\xda\x00\nt\x88'
        MAC Address: e8:da:00:0a:74:8a
        Nonce: b'gIDGXfYaZe2aIeqhLGzddw=='
        Public Key: b'0BQbFWVulrhfzq0ujnYzDSsawVdrsCbnoyjA4br4z5FmQ3EXTAjuEuySsFGcVIefISVb5ah3Dh+hiARw70I8kONNeEem/LSSRWPRrx2wxIHq2YUsUZvx3UKcFjlRz2kYGxMq6io2hMrzW8VKyhsgyIuztzOf99VuCROdd/CsWAeQl5OCUdu+dehnFcxrfAypRfqN2NZhvrc7QUAyeY2t7jK13WG/EF8Y2JIXdgt1xdlmpaSQRyzrqeO0Ik89ifsr'
        Auth Type Flags: b'\x00a'
        Encr Type Flags: b'\x00\t'
        Conn Type Flags: b'\x01'
        Config Methods: b'\x07\x84'
        SC State: b'\x02'
        Manufacturer: b'Realtek Semiconductor Corp.'
        Model Name: b'RTL8xxx'
        Model Number: b'EV-2010-09-20'
        Serial Number: b'123456789012347'
        Prim Dev Type: b'\x00\x06\x00P\xf2\x04\x00\x01'
        Device Name: b'Realtek Wireless AP'
        RF Band: b'\x01'
        Assoc State: b'\x00\x00'
        Device Pwd ID: b'\x00\x00'
        Config Error: b'\x00\x00'
        OS Version: b'\x10\x00\x00\x00'
        Vendor Ext: b'\x007*\x00\x01 '
```

See `solve.py` for a script that automatically parses the message.

**Flag** - `byuctf{gIDGXfYaZe2aIeqhLGzddw==}`