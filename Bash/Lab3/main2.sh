mkdir dir1 dir2 dir3 dir4 dir5
rmdir dir4 dir5

touch dir3/text.txt
mv dir3/text.txt dir1

for ((i=2; i<4; i+=1))
do
  echo $i
  cp dir1/text.txt dir$i
done

for((i=1; i<4; i+=1))
do
  rm dir$i/text.txt
  rmdir dir$i
done