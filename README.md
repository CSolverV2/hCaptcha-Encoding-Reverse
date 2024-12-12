# hCaptcha-Encoding-Reverse

Fully reversed hCaptcha event encoding function written in python

Hello, I'm cypher, this is a project of mine where I reverse engeneered the way hCaptcha encodes event values

# Info

In hCaptcha's `hsw` (fingerprinting system) they have events which contains data about the user

This data includes, timezone, gpu, useragent, and more identifying data

Some of this data is encoded, and looks like this:
- `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36` -> `v%v1^lrp%X1^5%^.Yw.Q:orOhHpHSKK,%3dz7GOV%HWrS%XRWmH#%NYNYNY . :H!R02P%^.Yw.Q:r0M=ME`
- `Europe/Madrid` -> `Mv=THPoULjzJD7G$Ryd}cA/w#xi~Ikm,:bF5rn-W!3shZQ0lqp).428(NS6KXY1BIr0IMz:HKR0*e%eCt_9`
- `ANGLE (Intel, Intel(R) Iris(R) Xe Graphics (0x00009A49) Direct3D11 vs_5_0 ps_5_0, D3D11)` -> `%3SHol-V%XiVSHol-%XiV4r0-%H{%4mr2KM0#%XL1,LNNNN5NV%  /.omH0r/%NUQU4J%3NUQU4K%X  /./`

And some other data, but you understand what this does, it makes it unreadable and encodes it

With this script you have two things: 
- encoder sandbox (in javascript)
- encoder reverse (in py)

# Usage

Simply open `encode.py` and scroll to the bottom of the code

```
encoder = Encoder('cc9cbcc44893d9601186ed793b76ac72a56a3e176be51252819b38f7d2f1f97c')

res = encoder.encode('America/Los_Angeles')
print(res)
```

Modify the string `cc9cbcc44893d9601186ed793b76ac72a56a3e176be51252819b38f7d2f1f97c` to the version to encode for since certain values change for different versions

Then, run `encoder.py` and it will fetch some dynamic values required for encoding, then encode your value and print it

# Contact

If you need help or are interested in stuff like this, please contact me on discord or telegram: 

- Telegram -> `@CSolverV2` | https://t.me./csolver
- Discord -> `csolver.ai` | https://discord.gg/CBr7taaYeh
