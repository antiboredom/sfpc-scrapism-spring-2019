# python3 reddit.py > posts_with_comments.txt

# remove Julian Assange; fish out the sciency stuff
cat posts_with_comments.txt |  tr -d '\r“’‘”_' | tr "\n" " " | tr "—" " " | tr "-" " " | tr -s ' ' | sed 's/\. /. \
/g' | sed 's/\!/!\
/g' | sed 's/\?/?\
/g' | grep -vi rape | grep "hole\|black\|space\|Sagittarius\|star\science" > black_hole.txt

# generate markers that feel like exponential speedup
for i in {1..480}
do
   echo "[[rate +$((10+3*$i)); pbas +$((0.2*$i))]]"
done > marker.txt

paste marker.txt black_hole.txt > black_hole_with_marks.txt
cat black_hole_with_marks.txt | tr -d "\n" | say -v "Fred"
