echo "hello"
sleep 5
ifconfig wlan0 | awk '/inet /{print $2}'
echo "waiting 20 seconds"
sleep 20
glslViewer test.frag img.png -p 5005 -l -f --nocursor --fps 5
