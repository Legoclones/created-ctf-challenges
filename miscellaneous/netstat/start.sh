for file in /scripts/*; do 
    (python3 $file &)
done

/etc/init.d/ssh start

while true; do
    sleep 100
done