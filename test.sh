#!/usr/bin/env bash
for f in sample*; do
	if diff <("${1:-./a.py}" <sample"$i") output"$i"; then
		printf 'Sample %d: Good\n' "$(( ++j ))"
	else
		printf 'Sample %d: Bad\n' "$(( ++j ))"
	fi

	(( i++ || ++i ))
done
