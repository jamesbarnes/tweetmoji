
##regex to capture emoji
myre = re.compile(u'['
    u'\U0001F300-\U0001F64F'
    u'\U0001F680-\U0001F6FF'
    u'\u2600-\u26FF\u2700-\u27BF]+', 
    re.UNICODE)

#use this command from the terminal to export the analysis to a csv called emoji_counts.csv
mongoexport --db cooldb --collection tweetcount --type=csv --out emoji_counts.csv --fields emoji,en,fr,es,de,zh,ko,ja,it,ru
