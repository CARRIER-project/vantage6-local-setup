echo "Running algo container"

sleep 1

echo "wg show output:"
wg show

echo "modprobe wireguard:"
modprobe wireguard

echo "ip link"
ip link

echo "ip route:"
ip route

echo "Ping:"

while true
do
  ping -c 5 -i 1 10.13.13.1
  ping -c 5 -i 1 10.13.13.2
  ping -c 5 -i 1 10.13.13.3
  ping -c 5 -i 1 10.13.13.4
done
