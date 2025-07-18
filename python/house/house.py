def recite(start_verse, end_verse):
    verse_number = start_verse
    nouns = ['house','malt','rat','cat','dog','cow','maiden','man','priest','rooster','farmer','horse','hound']
    adjectives = ['crumpled','horn','forlorn','tattered','torn','shaven','shorn','morn','corn']
    rhyme = []
    while verse_number <= end_verse:
        verse = 'This is the'
        for line_number in range(1,verse_number+1):
            verse += 'that'
            

        verse += ' Jack built.'
        rhyme.append(verse)

    return rhyme



"""
start_verse is where we start, meaning this number should provide some information to the script, i.e. how many nouns that are in the script verse. 
Increase the number by 1 until we have processed the verse number equal to end_verse. 
"""