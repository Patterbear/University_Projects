read number
count=0
total=0

for (( count=1; count<=number; count+=1 ))
do
  total=$(( $total + $count ))
done

echo $total