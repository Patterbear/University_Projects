#top
#ps -A
#pstree
#pgrep init
#kill 1

sleep 100 & # this command will create a process will holding on 100 seconds, ‘&’(ampersand) directs the shell to run the command in the background
pidof sleep # check pidof –help in the command line
top # shown all the current processes
kill pidNum # eg: ‘pgrep sleep’ or ‘pidof sleep’
top