from github import Github
import base64

# personal access token
g = Github('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')

# username/repository
repo = g.get_repo('patilvinmay/Test')

# Get contents of the repository
contents = repo.get_contents("")

# List to store file names containing the search string
search_string = "OLD_WAREHOUSE"
matching_files = []

# Iterate through all files
while contents:
    file_content = contents.pop(0)

    # Check if its python file, then replace
    if file_content.type == "file" and str(str(str(file_content.path).split("/")[-1]).split(".")[-1]) == "py":
        # Get file name
        current_content = repo.get_contents(file_content.path)
        # Decode file content
        current_decoded_content = base64.b64decode(file_content.content).decode('utf-8')
        # Check match string
        if search_string in str(current_decoded_content):
            matching_files.append(file_content.name)
            # Replace old string with new
            new_content = str(current_decoded_content).replace("OLD_WAREHOUSE", "NEW_WAREHOUSE")
            commit_message = "Updated file with NEW_WAREHOUSE"
            # Update file with New Warehouse
            repo.update_file(file_content.path, commit_message, new_content, file_content.sha)
    # Recursive
    elif file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))

# Print the file names containing the search string
print("Files containing '{}' in their contents:".format(search_string))
for file_name in matching_files:
    print(file_name)
