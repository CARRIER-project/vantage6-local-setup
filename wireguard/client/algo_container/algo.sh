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

ping -i 1 10.13.13.3
