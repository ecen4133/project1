#!/bin/bash

h1=`md5sum good.py | awk '{print $1}'`
h2=`md5sum evil.py | awk '{print $1}'`

if [ "$h1" != "$h2" ]; then
    echo "Failed MD5 collision: different hashes:"
    echo $h1
    echo $h2
    exit -1
fi

echo "Matching hashes ($h1)"

cp good.py a.py
m1=`python3 a.py`
rm a.py

cp evil.py a.py
m2=`python3 a.py`
rm a.py

if [ "$m1" != "Use SHA-256 instead!" ]; then
    echo "good.py output the wrong thing!"
    exit -1
fi

if [ "$m2" != "MD5 is perfectly secure!" ]; then
    echo "evil.py output the wrong thing!"
    exit -1
fi


echo "Test passed!"
