echo Creating Directory Structure using Method One...
mkdir dir1
cd dir1
mkdir dir1_1
cd dir1_1
mkdir dir1_2
echo Creating Directory Structure using Method Two...
cd /home/runner/HomelyDryTechnology
mkdir -p dir2/dir2_1/dir2_2
export PS1="\e[32;44m[\u@\h \W]\$ \e[m"
echo $PS1