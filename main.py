import csv

# Define the path to your input and output files
input_file_path = '/Users/javiercastellon/Desktop/flashcards/flashcards.txt'  # Update this to your file's path
output_file_path = '/Users/javiercastellon/Desktop/flashcards/flashcards.csv'    # Define where you want to save the CSV

# Function to parse the .txt file and convert it to a list of tuples (question, answer)
def parse_qa_file(input_path):
    with open(input_path, 'r') as file:
        lines = file.readlines()
    
    qa_pairs = []
    temp_q = ''
    temp_a = ''
    for line in lines:
        if line.startswith("**Q:**"):
            temp_q = line.replace("**Q:** ", "").strip()
        elif line.startswith("**A:**"):
            temp_a = line.replace("**A:** ", "").strip()
            qa_pairs.append((temp_q, temp_a))
            temp_q, temp_a = '', ''  # Reset for the next pair
    return qa_pairs

# Function to write the parsed QA pairs to a CSV file
def write_to_csv(output_path, qa_pairs):
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Answer"])  # Header
        for pair in qa_pairs:
            writer.writerow(pair)

# Execute the parsing and writing
qa_pairs = parse_qa_file(input_file_path)
write_to_csv(output_file_path, qa_pairs)

print(f"Converted {len(qa_pairs)} Q&A pairs to CSV format at '{output_file_path}'")
