name="Benjamin"
echo name
echo $name
echo ${name}
echo "My name is ${name}"
pwd

mkdir -p dir1/dir1_1/dir1_2
mkdir dir2
mkdir dir3

touch lab.txt
touch dir1/lab1.txt
touch dir1/lab2.txt

rm dir1/lab1.txt
rmdir dir1/dir1_1/dir1_2

read -p "Fullname: " fname sname

echo "Firstname: $fname"
echo "Secondname: $sname"

read -p "Number1: " num1
read -p "Number2: " num2

if [ $num1 -gt $num2 ]
then
  echo "Number1 > Number2"
elif [ $num1 -lt $num2 ]
then
  echo "Number1 < Number2"
else
  echo "Number1 = Number2"
fi

for ((i=0; i<10; i+=1))
do
  echo "I:$i"
done