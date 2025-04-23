export DIRECTORY=/$(cat /dev/urandom | tr -dc a-f0-9 | fold -w32 | head -n1)
docker compose up -d --build