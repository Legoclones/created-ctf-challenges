# WebAuthn 3
Description:
```markdown
Alright, alright, I fixed the bug in my website so now you can't log in as anyone 😡. In other news, have you heard about the sign count value? WebAuthn requires that both the authenticator and server increment this count each time authentication takes place, and the server ensures that the authenticator-provided count is less than the server-stored count.

What that means is that if you can set admin's sign count to be lower than it should, the admin can't sign in anymore!!

https://webauthn3.youcanhack.me

[server.py]
```

Note that the participants must have solved WebAuthn 1 and WebAuthn 2 **before** seeing this challenge.

## Writeup
The bug from WebAuthn 2 has been patched by checking that both credential IDs are the same. However, there's another bug lurking in the code. Namely, in the authentication process, the credential that the signature is being compared to comes from the `userHandle` field, NOT the `id` field. However, the returned `credential_id` value is `id`. Therefore, you can authenticate as your own user, but overwrite the `sign` field of an arbitrary credential. Just like WebAuthn 2, you can get the admin's credential ID through the `/api/login` endpoint.

This is automated in `solve.py`.

**Flag** - `HC{0kay_th3y_r34lly_n33d_t0_m4k3_th3_d0cum3ntati0n_m0r3_cl34r}`

## Hosting
This challenge should be a Docker container that runs `server.py` on port 1337. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
docker compose up -d --build webauthn3
```

To stop the challenge:
```bash
docker compose down
```