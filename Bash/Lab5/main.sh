wget https://cdn.abcotvs.com/dip/images/959031_082715-ss-dancing-senior-img.jpg?w=1600

wget -q --spider google.com
if [ $? -eq 0 ];
then
echo "online"
else
echo "offline"
fi