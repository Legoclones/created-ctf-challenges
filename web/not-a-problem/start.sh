# run admin bot in the background
node /ctf/admin_bot.js &

# run Flask server
while true; do
    su - ctf -c "python3 /ctf/server.py"
done