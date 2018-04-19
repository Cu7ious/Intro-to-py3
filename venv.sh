#!/usr/bin/env bash
virtualenv -p `which python${BASH_ARGV[1]}` $BASH_ARGV
