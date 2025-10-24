# Middleware 5
Description:
```markdown
Complicated web infrastructure has your traefik passing through many different points before reaching the final destination. Sometimes this can lead to problems...

https://middleware-5.youcanhack.me

[middleware.zip]
```

## Writeup
[CVE-2025-47952](https://github.com/traefik/traefik/security/advisories/GHSA-vrch-868g-9jx5) contains a vulnerability where URL decoding isn't done on incoming paths when deciding what route to take. If the backend DOES do the URL decoding (like Nginx), then this discrepancy can lead to an attacker bypassing Traefik middlewares. In our case, the `/admin` is protected by a Traefik basic authentication middleware, but can be bypassed by doing `/welcome/%2e%2e/admin` as this matches the Traefik `/welcome` PrefixPath directive, but Nginx decodes it into `/admin`.

```bash
curl 'https://middleware-5.youcanhack.me/welcome/%2e%2e/admin' --path-as-is
```

**Flag** - `HC{did_y0u_kn0w_it_was_CVE-2025-47952_0r_did_y0u_just_disc0ver_it_y0urself?}`

## Hosting
This challenge should be a Docker container that runs the Traefik reverse proxy on port 80. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
docker compose up -d --build
```

To stop the challenge:
```bash
docker compose down
```