# WebAuthn Series
## WebAuthn 1
Description:
```markdown
Passwords are SO OLD SCHOOL, passwordless authentication is the way of the future! [WebAuthentication](https://w3c.github.io/webauthn/) is a pretty cool spec, so I wrote my website to use it. However, I'm not much of a front-end guy, so all I've left you with is an API. Can you log in?

https://webauthn.youcanhack.me

[server.py]
```

## Writeup
The point of this challenge is to force participants to understand how WebAuthn works. Normally, a UI with JavaScript is provided so that a simple button press forces the browser to interact with the authenticator device and do everything in the background. For this reason, only the API was provided, so that participants have to break down the protocol themselves and figure out how to interact with it properly to log in. Between the `py_webauthn` docs, the official spec, and other online sources, I figured out how to script registering and logging in with WebAuthn.

See `solve1.py`.

**Flag** - `HC{now_db_br34ch3s_dont_l34k_h4sh3s}`

## WebAuthn 2
Description:
```markdown
Alright, so you now know how to use WebAuthn. [But can you hack it](https://essay.utwente.nl/98532/1/Chen_MA_EEMCS.pdf)?? If you can log in as admin, you'll get a flag.

This challenge uses the same files and remote server as WebAuthn 1.

When both WebAuthn 1 and WebAuthn 2 are completed, WebAuthn 3 will open up.
```

## Writeup
Now that the participant understands how to interact with it, they are expected to figure out where the bugs are. Namely, WebAuthn relying parties (aka, the server) needs to check that the credential ID created during registration doesn't already exist. Authenticators randomly generate this, so during normal usage this should never happen. Also, registration request objects include the credential ID twice - once in the `id` header (and `rawId` is checked to be the same), and once encoded inside the `response.attestationObject.authData` encoded section. While both are normally the same, this server never checks that. While it does ensure that the `id` header is unique (doesn't already exist), the `verified.credential_id` value returned comes from the `response.attestationObject.authData` section.

Therefore, if the attacker knows the credential ID of admin, then they can register a new user with the same credential ID. This means both admin and the new user are tied to the same credential, and that credential is overwritten by the one the attacker specifies. In order to get the admin's credential ID (which is randomly generated), the attacker can pretend to start the login process as admin. When starting the login process, the credential IDs of the (optionally specified) user are returned (per the WebAuthn specification).

This is automated in `solve2.py`.

**Flag** - `HC{okay_but_webauthn_is_so_complicated_like_why}`

# Hosting
This challenge should be a Docker container that runs `server.py` on port 1337. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
docker compose up -d --build webauthn
```

To stop the challenge:
```bash
docker compose down
```