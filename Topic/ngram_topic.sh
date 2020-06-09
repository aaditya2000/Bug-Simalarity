read  file
echo $file > input.txt
python3 stam_let.py < input.txt > stammed_input.txt

python3 word.py > ngram.txt
echo "ngram.txt" > input.txt
python3 BXB.py < input.txt > B-Tgram-B_ans.csv