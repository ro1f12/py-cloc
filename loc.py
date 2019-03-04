#py cloc
#software enginnering practicatl assignment-1
#SE CS2036
#rofi
#27-02-19
import os
import sys



#function to calculate lines of codes
def py_cloc(fullpath, dirname, comment_tag = "//", macro_tag = "#"):
    #open the file
    with open(fullpath) as f:
        linecount = 0
        blanklines = 0
        comments = 0
        macros = 0

        for line in f:
            linecount += 1

            nospace = line.strip()
            if  not nospace:
                blanklines += 1
            elif nospace.startswith(comment_tag):
                comments += 1
            elif nospace.startswith(macro_tag):
                macros += 1



    #diplay the results
    #print ("-------------------------------------")
    #print ("\tFile: " + splitall(f_name)[-1] + "\t\t")
    print ("-------------------------------------")
    print ("Lines          : " + str(linecount))
    print ("Blank lines:   : " + str(blanklines))
    print ("Macro lines    : " + str(macros))
    print ("Comment lines  : " + str(comments))
    print ("-------------------------------------")
    print ("Lines of code  :" + str(linecount - blanklines - macros - comments))
    print ("-------------------------------------")


#main function
def main():
    if len(sys.argv) < 2:
        print ("\t\tUsage: <program> <file name>")
        quit()

    #file name from commandline arg
    f_name = sys.argv[1]
    if not f_name:
        print ("\t\tUsage: <program> <file name>")
        quit()

    #present working directory
    dirname = os.getcwd()

    #set the full path
    fullpath = os.path.join(dirname, f_name)

    #check the file extension
    extension = os.path.splitext(fullpath)[1]

    #tags for counting macros i.e. #include<...> of #define and comments
    comment_tag = "//"
    macro_tag = "#"
    expected_extension = ".c"


    #comment_tag = "#"
    #macro_tag = "import"
    #expected_extension = ".py"

    #check if the file exists and C-file or not
    if not extension == expected_extension or not os.path.exists(fullpath):
        #print("\t\tError: provide a C file or File does not exits")
        print("\t\tUsage: <Program> <file name>")
        quit()
    #function call for calculating lines of code
    py_cloc(fullpath, dirname, comment_tag, macro_tag)
    #py_cloc(fullpath, dirname)


#driver code
if __name__ == "__main__":

    print("******************************************************************\t")
    print("\t\tLINES OF CODE COUNTER IN PYTHON\t\t")
    print("\t\t\t\tby Rofi\t\t")
    print("******************************************************************\t")

    main()
