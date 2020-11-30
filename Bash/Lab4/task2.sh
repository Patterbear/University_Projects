read number
count=0
total=0

while [[ $count -le $number ]]
do
total=$(( $total + $count ))
count=$(( $count + 1 ))
done

echo $total