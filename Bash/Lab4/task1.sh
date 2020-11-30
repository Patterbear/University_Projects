touch Diary.txt
open Diary.txt

x = 1
while [[ $x -le 5 ]]
do
  read input
  echo $input >> Diary.txt
  x=$(( $x + 1 ))
done