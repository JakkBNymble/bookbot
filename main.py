def sort_on(dict):
    return dict["count"]
    
def character_count(text):
    char_count = {}
    for chars in text:
        if chars.isalpha() and chars not in char_count:
            char_count[chars] = 1
        elif chars.isalpha():
            char_count[chars] += 1
    return char_count
    
def main(): #define the function
    with open("books/frankenstein.txt") as f: #input logic
        file_contents = f.read() #read content of the file
        word_count = file_contents.split()
        lowered_fc = file_contents.lower()
        results = character_count(lowered_fc)
    char_list = []
    for letter, count in results.items():
        char_list.append({
            "letter": letter,
            "count": count
        })
    char_list.sort(reverse=True, key=sort_on)
    #print(file_contents) #Print for console
    #print(lowered_fc) #Print for console
    #print(results)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(word_count)} words found in the document")
    print("")
    for char in char_list:
        print(f"The '{char['letter']}' character was found {char['count']} times")
    print("--- End report ---")

if __name__ == "__main__":
    main() #Call the function
