python3 stam_corpse.py > corpse_1.csv
python3 topic_find.py > issue_B-T-B.csv
echo "./issue_B-T-B.csv" > input.txt
python3 BXB.py < input.txt > B-Topic-B_ans.csv