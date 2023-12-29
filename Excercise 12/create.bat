clear
echo "********************"
echo Creating the directory structure of the project
echo "********************"

a=echo `date`
##### This asks the user to create the directory. 
echo enter the name of the directory that you want to create 

read dname

if [ -d "dname" ];
then
echo the directory already exist
else
mkdir $dname
echo new directory $dname has been created 
echo creating subdirectories in $dname
cd $dname
##Directory Structure Creation
mkdir Documentation 
mkdir Examples
mkdir Source
mkdir Tests
echo subdirectories are created 
echo we have created the directory structure for the project on $a
fi
