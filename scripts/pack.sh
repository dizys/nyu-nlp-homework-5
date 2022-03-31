#!/usr/bin/env bash

shell_dir=$(dirname "$0")
project_dir=$(cd "$shell_dir/.."; pwd)
src_dir=$project_dir/src
bin_dir=$project_dir/bin
data_dir=$project_dir/data
out_dir=$project_dir/out
submission_dir=$project_dir/submission

# Delete old submission dir
rm -rf $submission_dir

# Create submission dir if it doesn't exist
mkdir -p $submission_dir

# Copy files needed to be submitted
cp $src_dir/main.py $submission_dir
cp $out_dir/WSJ_23.chunk $submission_dir
cp $project_dir/README.txt $submission_dir

# Create zip file
cd $submission_dir
zip -r zz2960-HW5.zip *
