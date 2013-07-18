-----FEATURES-----
-Single Word Query
-Text Analysis
-CSV File Anslysis

-----LANGUAGE PROCESSING-----
Querying - words are directly queried from db.csv
Overall Valence/Arousal Calculations - V/A found in text are averaged (weighted by frequency)
Negations - negates word V/A (centered around 4.5)
Modifiers:
	-emphasizers (+/- 1 for V/A)
	-de-emphasizers (opp. of emphasizers for V/A)
Indicator resets for punctuation & conjunctions

-----CONTENTS-----
main.py		Main UI
leia.py		Script that processes text
db.csv		Database of words/synsets
renew.py	Script that updates db.csv with values found in anew.csv
anew.csv	Database of ANEW

-----NEXT STEP-----
1. Add more words
2. Find algorithm for the effect of modifiers
3. Data visualization
4. Overall V/A Calculations? - taking into account the connotations of the words (using global relative frequencies)

-----NOTES-----
combining V/A
-within synsets
-across all synsets
-between people

Ceiling analysis:
Correlation vs features there
Performance variable vs. features there

adding entire anew database