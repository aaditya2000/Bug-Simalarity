echo "temp_component.csv" | python3 BXB.py > BCB_ans.csv
echo "temp_author.csv" | python3 BXB.py > BDB_ans.csv
echo "temp_file.csv" | python3 BXB.py > BFB_ans.csv
echo  "temp_component.csv\ntemp_component.csv" | python3 BXBXB.py > BCBCB_ans.csv
echo  "temp_component.csv\ntemp_author.csv" | python3 BXBXB.py > BCBDB_ans.csv
echo  "temp_component.csv\ntemp_file.csv" | python3 BXBXB.py > BCBFB_ans.csv

echo  "temp_file.csv\ntemp_component.csv" | python3 BXBXB.py > BFBCB_ans.csv
echo  "temp_file.csv\ntemp_author.csv" | python3 BXBXB.py > BFBDB_ans.csv
echo  "temp_file.csv\ntemp_file.csv" | python3 BXBXB.py > BFBFB_ans.csv

echo  "temp_author.csv\ntemp_file.csv" | python3 BXBXB.py > BDBFB_ans.csv
echo  "temp_author.csv\ntemp_author.csv" | python3 BXBXB.py > BDBDB_ans.csv
echo  "temp_author.csv\ntemp_component.csv" | python3 BXBXB.py > BDBCB_ans.csv

sh ngram_topic.sh 
sh topic.sh 