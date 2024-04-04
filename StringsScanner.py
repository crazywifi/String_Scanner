import os
import tkinter as tk
from tkinter import filedialog

# Function to run strings.exe on DLL and EXE files
def run(PathFolder):
    pathlogs_file = open('Pathlogs.txt', 'w')  # Open Pathlogs.txt file for writing
    for root, dirs, files in os.walk(PathFolder):
        for file in files:
            if file.endswith(('.dll', '.exe')):
                filepath = os.path.join(root, file)
                print(filepath)
                pathlogs_file.write(filepath + '\n')  # Write filepath to Pathlogs.txt
                output_filename = os.path.splitext(file)[0] + '.txt'
                output_path = os.path.join('Output', output_filename)
                os.system('strings.exe -nobanner"{}" > "{}"'.format(filepath, output_path))
    pathlogs_file.close()  # Close Pathlogs.txt file

# Function to handle the GUI and initiate the main process
def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    PathFolder = filedialog.askdirectory(title="Select Directory Path")  # Open directory selection dialog
    if PathFolder:  # If a directory is selected
        print("Selected Directory Path:", PathFolder)
        Output_Folder = 'Output'
        if not os.path.exists(Output_Folder):
            os.makedirs(Output_Folder)
        run(PathFolder)  # Run the main process with the selected directory

# Main function
def main():
    select_directory()

if __name__ == '__main__':
    main()
