#! /bin/bash

OK=0
for f in test/test_*py; do
   echo "Running $f:"
   PYTHONPATH=timediff python $f
   if [ "$?" -ne 0 ]; then
      OK=1
   fi
done
set -x

exit $OK
