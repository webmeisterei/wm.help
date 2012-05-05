#!/bin/sh

# This script must be executed from the package folder it is located in
# i18ndude should be available in current $PATH (eg by running
# ``export PATH=$PATH:$BUILDOUT_DIR/bin`` when i18ndude is located in your buildout's bin directory)

TYPES="./wm/help"

DOMAIN="wm.help"

i18ndude rebuild-pot --pot ${TYPES}/locales/${DOMAIN}.pot --create ${DOMAIN} --merge ${TYPES}/locales/manual.pot $TYPES

for file in `find ${TYPES}/locales -name ${DOMAIN}.po`
do
    echo Syncing $file ...
    i18ndude sync --pot ${TYPES}/locales/${DOMAIN}.pot $file
    msgfmt -o `dirname $file`/`basename $file .po`.mo $file --no-hash
done


