import os
import re
import docx2txt
from glob import glob

def search_word_docs(keyword):
    """
    Search all Word documents in the current directory for a keyword/phrase.
    Returns matched documents with context around each match.
    """
    results = []
    word_files = glob("*.docx")
    
    if not word_files:
        print("No Word documents found in the current directory.")
        return results
    
    keyword_pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    
    for file_path in word_files:
        try:
            # Extract text from the Word document
            text = docx2txt.process(file_path)
            
            # Search in document title
            title_text = os.path.splitext(os.path.basename(file_path))[0]
            title_matches = list(keyword_pattern.finditer(title_text))
            if title_matches:
                results.append(f"Match in document title: {file_path}")
            
            # Search in document content
            lines = text.split('\n')
            for line in lines:
                if not line.strip():
                    continue
                    
                matches = list(keyword_pattern.finditer(line))
                for match in matches:
                    start_pos = match.start()
                    end_pos = match.end()
                    
                    # Get context (up to 15 chars before and after)
                    context_start = max(0, start_pos - 35)
                    context_end = min(len(line), end_pos + 35)
                    
                    before_text = line[context_start:start_pos]
                    match_text = line[start_pos:end_pos]
                    after_text = line[end_pos:context_end]
                    
                    context = f"...{before_text}{match_text}{after_text}..."
                    results.append(f"Found in {file_path}: {context}")
                    
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
    
    return results

def main():
    print("Word Document Keyword Search Tool")
    print("--------------------------------")
    
    keyword = input("Enter keyword or phrase to search for: ").strip()
    if not keyword:
        print("Error: Keyword cannot be empty.")
        return
    
    print(f"\nSearching for '{keyword}' in Word documents...")
    results = search_word_docs(keyword)
    
    if results:
        print(f"\nFound {len(results)} matches:")
        for idx, result in enumerate(results, 1):
            print(f"{idx}. {result}")
    else:
        print(f"\nNo matches found for '{keyword}'.")

if __name__ == "__main__":
    main()