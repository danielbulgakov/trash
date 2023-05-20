# Python script to concatenate files in on file
# that can be used to fill latex verbatim content

import os

# Returns list of paths to all files in passed dir and all its subdirs
def get_list_of_files(dir_path) :
    files_list = []
    for dir_path, _, files in os.walk(dir_path):
        for file in files:
            files_list.append(os.path.join(dir_path, file))
    return files_list

# Return list of file names by its path and root path
def get_list_of_file_names(files_list, name_pattern) :
    names_list = []
    for file in files_list :
        names_list.append(file.lstrip(name_pattern).split("\\")[-1])
    return names_list

# Saves all content of files in paths list in latex style
def save_to_file(files_list, file_names, file_path, line_max_len) :
    with open(file_path, "w", encoding="utf8") as new_file:
        for ind, file in enumerate(files_list):
            new_file.write(get_header(file_names[ind]))
            with open(file, encoding="utf8") as f:
                for line in f:
                    if (len(line) < line_max_len) :
                        new_file.write(line)
                    else :
                        new_file.write(line[:len(line)//2] + "\n")
                        new_file.write(line[len(line)//2:])
                new_file.write("\n")
            new_file.write(get_trail())

# Returns header in latex style
def get_header(file_name) :
    return "\\par { %s } \n \\begin{lstlisting}[language=Kotlin] \n " % file_name

#Return footer in latex style
def get_trail():
    return "\\end{lstlisting} \n"

# Main
def run() :
    root = "D:\Study\mobile_aurora_labs\lab6\\app\src\main\java\com\example\lab6"
    save = "C:\\Users\\bulga\\OneDrive\\Desktop\\concat.txt"
    str_max_len = 1000

    file_list = get_list_of_files(root)
    names_list = get_list_of_file_names(file_list, root)

    save_to_file(file_list, names_list, save, str_max_len)

run()