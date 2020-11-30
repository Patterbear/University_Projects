count=0

for (( count=1; count<=5; count+=1 ))
do
  read -p "Directory $count name: " dirname
  mkdir $dirname
  touch $dirname/diary.txt
done

echo $total