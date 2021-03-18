echo "Running algo container"

sleep 1

echo "ip link"
ip link

echo "ip route:"
ip route

echo "ip addr"
ip addr

echo "Ping:"

while true
do
  ping -c 5 -i 1 192.168.255.5
  ping -c 5 -i 1 192.168.255.6
  ping -c 5 -i 1 192.168.255.9
  ping -c 5 -i 1 192.168.255.10
done
