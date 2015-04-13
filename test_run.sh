SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

$SCRIPT_DIR/FAQhtmlConverter.py $SCRIPT_DIR/instructions

echo
echo "check gedit and browser now. Enjoy:-) "
echo
sleep 1
gedit $SCRIPT_DIR/instructions/instructions.txt &
xdg-open $SCRIPT_DIR/instructions/html/instructions.txt.html &
