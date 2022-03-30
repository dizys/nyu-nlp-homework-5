#!/usr/bin/env bash

shell_dir=$(dirname "$0")
project_dir=$(cd "$shell_dir/.."; pwd)
bin_dir=$project_dir/bin
data_dir=$project_dir/data
java_exe=java
javac_exe=javac

# Compile the Java tagger and trainer
$javac_exe -cp $bin_dir/maxent-3.0.0.jar:$bin_dir/trove.jar $bin_dir/*.java
