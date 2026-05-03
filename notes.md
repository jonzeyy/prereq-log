# Day 1 - Terminal Basics

cd ~/code/prereq-log
code. 

cd .... = take me to that folder
cd ~ = home directory
cd / = root of the file system
pwd = print working directory

ls = list files in current folder
ls -l = detailed list

mkdir .... = make a new directory
touch .... = creates an empty file
rm .... = delete file
rm -r .... = delete everything inside folder
rmdir .... = delete empty folder

cp .... = copy file
mv .....txt .....txt = rename file

cat .... = print file contents to terminal
less .... = view file one page at a time
head .... = view first 10 lines
tail .... = view last 10 lines

man .... = pull uo manual for command
clear = clear terminal 
history = shows history of terminal



echo = print what follows.
> = output into ....
cat = prints out content of a file.

Example: 
echo Terminal Basics >terminalbasics.txt
cat terminalbasics.txt 
"Terminal Basics"

< = take the input from .....

Example: 
cat <terminalbasics.txt
Terminal Basics

There are 4 types of Quoting mechanisms.

- The escape character: A non quoted backslash '\' is the Bash escape character. Preserves the literal value of the next character that follow, removing any special meaning it has. (with the exeption of 'newline')

- Single Quotes: Enclosing a character in single quotes ( '' ) preserves the literal value of each character inside the single quotes. A single quote cannot occur between single quotes. 

- Double Quotes: Enclosing characters in double quotes (‘"’) preserves the literal value of all characters within the quotes, with the exception of ‘$’, ‘`’, ‘\’, and, when history expansion is enabled, ‘!’. When the shell is in POSIX mode (see Bash and POSIX), the ‘!’ has no special meaning within double quotes, even when history expansion is enabled. The characters ‘$’ and ‘`’ retain their special meaning within double quotes (see Shell Expansions). The backslash retains its special meaning only when followed by one of the following characters: ‘$’, ‘`’, ‘"’, ‘\’, or newline. Within double quotes, backslashes that are followed by one of these characters are removed. Backslashes preceding characters without a special meaning are left unmodified

- Dollar ($) single quotes: Charecter sequences in the form of $'string' are treated as special kind of single quotes.

------------------------------------------------------------------------------


Terminal + Git notes:


What is GIT? - Git is a version control system used to track changed to your source code and/or any files or folders. 

Snapshots: Git models the history of a collection of files and folders within some top level directory as a series of "Snapshots". 

Terminology;

    - A file is is called a "blob", which is just a bunch of bytes.
    - A directory is called a "tree", and it maps names to blobs or trees (so directories can contain other directories.) 

eg:

<root> (tree)
|    
+-foo (tree)
| |
| + bar.txt (blob, content = "hello world")
|
+- baz.txt (blob, contents = "git is wonderful")

The top level tree (directory) contains two elements, a tree "foo" (which itself contains one element, a blob (file) "bar.txt") and a blob "baz.txt"


In Git, history is a directed acyclic graph (DAG). 

What does this mean? It means that each snapshot in Git refers to a set of "parents", the snapshots that preceded it. Its a set of parents rather than a single parent (which is the case for linear history) because a snapshot might descend from multiple parents. e.g. merging two branches of development.

Git calls these snapshots "commit"s 

eg: 

O <--- O <--- O <--- O
              ^
               \
                ---- O <--- O


 After the third commit, the history branches into two separate branches. This might correspond to, for example, two separate features being developed in parallel, independently from each other. In the future, these branches may be merged to create a new snapshot that incorporates both of the features, producing a new history tha