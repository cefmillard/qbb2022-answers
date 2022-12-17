for thing in $(grep '>' $1)
do
	echo $thing | cut -d '>' -f 2 | grep -f - metagenomics_data/step0_givendata/KRAKEN/assembly.kraken 
done | cut -d '	' -f 2 

