
#! /bin/bash
oldName=$1
newName=$2
path=$3

echo "Old string:$oldName";
echo "New string:$newName";
echo "Directory:$path";

find "$path" -type f -exec sed -i 's/'$oldName'/'$newName'/g' {} +
