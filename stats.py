def get_num_of_words(text_contents):
    return len(text_contents.split())

def get_character_counts(text_contents):
    character_counts={}
    for c in text_contents:
        unique_character=c.lower()
        if unique_character not in character_counts:
            character_counts[unique_character]=1
        else:
            character_counts[unique_character]+=1
        
    return character_counts

def sort_on(summary_record):
    return summary_record["count"]

def get_character_count_summary(character_counts):
    character_count_summary=[]
    for character, count in character_counts.items():
        character_count_summary.append({"char": character, "count": count})
    
    character_count_summary.sort(key=sort_on, reverse=True)

    return character_count_summary


            

        
        
        
        


        