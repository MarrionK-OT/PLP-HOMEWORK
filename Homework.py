# homework_challenge.py

print("📂 Welcome to the File Reader & Writer Challenge!\n")

# Step 1: Ask the user for a filename
filename = input("👉 Please enter the filename you want to read: ")

try:
    # Step 2: Try to open and read the file
    with open(filename, "r") as infile:
        content = infile.read()
    
    print("\n✅ File read successfully!\n")
    print("📖 Original Content:")
    print(content)
    
    # Step 3: Modify the content (uppercase + word count)
    word_count = len(content.split())
    modified = content.upper()
    
    # Step 4: Write to output.txt
    with open("output.txt", "w") as outfile:
        outfile.write("PROCESSED VERSION:\n")
        outfile.write(modified + "\n\n")
        outfile.write(f"WORD COUNT: {word_count}\n")
    
    print("\n✨ Modified version saved to 'output.txt'")
    print(f"📝 Word Count: {word_count}")
    print("🎉 All done, great job!")

# Error handling
except FileNotFoundError:
    print("❌ Oops! That file doesn’t exist. Please check the name and try again.")
except PermissionError:
    print("❌ Permission denied. You can’t read this file.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
