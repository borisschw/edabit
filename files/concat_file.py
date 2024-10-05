# read files contant from a directory and create a new file with all the content
import os

def concat_files(directory, output_file):

    #create list of files in the directory by decending order
    files = os.listdir(directory)
    files.sort(reverse=False)


    with open(output_file, 'w') as outfile:
        for filename in files:
            with open(os.path.join(directory, filename)) as infile:
                outfile.write(infile.read())

def main():
    #get directory path and output file name from user
    directory = input('Enter the directory path: ')
    output_file = input('Enter the output file name: ')
    concat_files(directory, output_file)




if __name__ == '__main__':
    main()