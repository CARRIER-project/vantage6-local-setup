OVPN_DATA="ovpn-data-vantage"
SERVER_IP= # Set this to the public IP or URL of your server
CLIENTCONFIGDIR="clientconfigs"

mkdir -p $CLIENTCONFIGDIR
rm -f $CLIENTCONFIGDIR/*.ovpn

docker volume create --name $OVPN_DATA
docker run -v $OVPN_DATA:/etc/openvpn --rm kylemanna/openvpn ovpn_genconfig -u tcp://$SERVER_IP:443 -c
docker run -v $OVPN_DATA:/etc/openvpn --rm -it kylemanna/openvpn ovpn_initpki nopass
docker run -v $OVPN_DATA:/etc/openvpn -d -p 443:1194/tcp --cap-add=NET_ADMIN kylemanna/openvpn

# Create some client configs
for CLIENTNAME in "client1" "client2" "client3" ;
  do
    docker run -v $OVPN_DATA:/etc/openvpn --rm -it kylemanna/openvpn easyrsa build-client-full $CLIENTNAME nopass
    docker run -v $OVPN_DATA:/etc/openvpn --rm kylemanna/openvpn ovpn_getclient $CLIENTNAME > ${CLIENTCONFIGDIR}/${CLIENTNAME}.ovpn
  done
