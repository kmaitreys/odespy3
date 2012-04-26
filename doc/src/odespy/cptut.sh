#!/bin/sh
dest=../../tutorial
cp -r sphinx-rootdir/_build/html $dest
cp wrap_odespy.pdf $dest/odespy.pdf

cat > $dest/README <<EOF
This directory contains the odespy for the package.
The documentation is automatically generated by ../src/odespy/make.sh.
EOF
git add $dest
git commit -am 'Added new official odespy files in doc/tutorial.'

doconce format rst $name
cp $name.rst ../../../../odespy.wiki/Tutorial.rest

