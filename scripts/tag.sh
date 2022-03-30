#!/usr/bin/env bash

shell_dir=$(dirname "$0")
project_dir=$(cd "$shell_dir/.."; pwd)
bin_dir=$project_dir/bin
data_dir=$project_dir/data
out_dir=$project_dir/out
java_exe=java
javac_exe=javac

# Run the tagger
$java_exe -cp $bin_dir/.:$bin_dir/maxent-3.0.0.jar:$bin_dir/trove.jar MEtag $out_dir/test.feature $out_dir/model.chunk $out_dir/response.chunk
