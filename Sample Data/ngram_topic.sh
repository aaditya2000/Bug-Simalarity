file="sample.csv"
echo $file > input.txt
python3 stam_let.py < input.txt > stammed_input.txt

python3 word.py
echo "ngram_1.txt" > input.txt
python3 BXB.py < input.txt > B-Tgram-1-B_ans.csv
echo "ngram_2.txt" > input.txt
python3 BXB.py < input.txt > B-Tgram-2-B_ans.csv
echo "ngram_3.txt" > input.txt
python3 BXB.py < input.txt > B-Tgram-3-B_ans.csv
echo "ngram_4.txt" > input.txt
python3 BXB.py < input.txt > B-Tgram-4-B_ans.csv
echo "ngram_5.txt" > input.txt
python3 BXB.py < input.txt > B-Tgram-5-B_ans.csv
echo "ngram_6.txt" > input.txt
python3 BXB.py < input.txt > B-Tgram-6-B_ans.csv
echo "ngram_7.txt" > input.txt
python3 BXB.py < input.txt > B-Tgram-7-B_ans.csv