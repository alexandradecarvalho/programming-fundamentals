## Introduction to Linux environment for Python programmers

###### this is an adaptation of the introduction document provided by Professor João Rodrigues, Professor António Neves and Professor Artur Pereira



#### Topics

- Introduction to UNIX Operative System.
- Command-line interface.
- Editing and execution Python programs.

Although not essential to Python (or any other language) programming, Linux system is very popular among programmers and other specialized users. 

##### Objectives:

* Open and use a text editor or an integrated programming environment to write Python programs.
* Open a terminal emulator and use the command-line to invoke Python's interpreter.
* Navigate through the file system in either graphic mode or text mode.
* Search and execute programs.

To know a little bit more or to gain some experience with the system, one can install Linux on their computer. The next section discusses some installation alternatives. The following sections explain how to use Linux to edit and execute programs and how to execute basic tasks. There is also a section on the command line use, with the most common commands.



#### Linux Installation

There are various ways of installing a Linux system into a computer already with other operating system installed. These ways differ in their complexity, but also in their versatility and performance during usage.

##### Dual-boot

In this way, Linux system is installed directly into its own disk partition, in parallel with the pre-existing system. So, every time you open your computer, you must choose which system you prefer to start. Once it starts, the system has direct access to all hardware and hits maximum performance, but to alternate between systems it is needed a system reboot. This is the traditional installation way, but there is also a more complex one in which it is needed to "shrink" the pre-existing system's partition. In this process, there is also some risk of corrupting the disk.

##### Virtual Machine Installation

In this way, Linux system is installed in a virtual machine, which is a computer, simulated by a program (called virtualizer), which runs inside the pre-existent operating system. The virtual machine has to put aside some resources from the real computer while sharing them with the other programs of the host system. This affects the client system's performance, as well as the host system's. However,  the alternation  between systems can be made instantaneously. The installation doesn't have great risks and it's not very complex, but it sometimes requires some adjustments depending on the machine.

##### Windows Subsystem for Linux (WSL)

In Windows 10 systems, it is now possible to add an official Microsoft extension that allows the installation and execution of Linux programs, directly in a Windows system. This is not full virtualization, and even though resource sharing is more efficient, you don't end up with a pure Linux system. Despite the limitations, this way allows for a functional command line, with access to thousands of UNIX programs and it is easy to install. With some extra software, you can also use Linux programs in graphic mode and not just text mode. 



If you have Windows 10 and intend to only use Linux sporadically, and especially in text mode, then WSL is the most reasonable solution. If you intend to use a full Linux system but are still going to keep using the current system as the main system, or if you feel the need to alternate frequently between systems, then a virtualized system should be the best option. If you intend to explore Linux more seriously and frequently, then you should probably opt for dual-boot installation.



#### UNIX Command Line  

When the UNIX system was created (circa 1970), computers were essentially controlled by consoles, or text terminals: devices with a keyboard and a screen, connected by cable to a central computer and where one could only visualize text. The interaction with the system was made by writing in commands, with the keyboard, and observing the answer produced on the screen by the programs in execution. Nowadays, there are graphic environments in UNIX, which allow the visualization of both textual and graphic information, and the interaction by virtual manipulation of graphic objects, through a mouse, keyboard, or other devices.

Despite the new interaction means, through graphic environments, it is still possible, and sometimes even preferable, to use a command-line interface for some operations. In a graphic environment, this can be accomplished by using a terminal emulator, a program that opens a window in which one can introduce commands, line by line, and watch the generated responses, just like in an "old fashioned" terminal.



##### Exercise 1

Open a terminal window, by clicking on its icon or pressing the Super key + writing "terminal" in the search box. When the prompt comes up in the command line, execute the command **date**. Notice that the response was printed immediately after, in a concise, distraction-free way, and with very few explanations. This behavior is usual in many UNIX commands and typical of a certain style defended by the system's creators. Simple but effective.



##### Exercise 2

Execute the **cal** command and see the result. Find out in which week-day you were born, passing your month and year of birth as an argument. **Example:** `cal jan 2001`
UNIX commands always follow the same form: "`command argument1 argument2 ...`". Here, the command is the name of the program to be executed and the arguments are optional sequences of characters, separated by spaces, which can exist, depending on the program.
In the command line, it is possible to obtain an already written command, using the up and down keys. It is, then, possible to modify it to make a new command, for example, by adding different arguments. Another useful functionality is the auto-completion of commands or arguments when these are already partially written, by pressing the tab key.



###### 2.1 File System Navigation

As in many other operating systems, UNIX stores information in a hierarchical structure, formed by directories, subdirectories and files. The root directory of this tree is simply represented by "/". Each user has its directory in this tree, from which they can see, create and manage their entire subtree of directories and files: this is called the personal directory, or home directory. When the user logs in, the system places them in this directory. To know which is your current directory, execute the command **pwd**. It must show a name such as /home/ana.costa, which indicates that you are in ana.costa's directory, a subdirectory of home, a subdirectory of the root "/". To list the content of the current directory, execute the command **ls**. You should see a file (and directories) list, of those inside the current directory, such as arca Desktop Examples.
In the case above, there are two subdirectories and a soft link, a special type of file that serves as a shortcut to other file or directory. Depending on the system's configuration, the names in this list can appear with different colours or special symbols that aren't part of the name (/, @, *), to indicate the type of the file.  In a graphic environment, the same information is available in a visual representation. Try, for example, to open a file browser and chose "Home" to see the contents of your home directory.

Files that start with “.” aren't usually listed. These are hidden files, which usually store the configuration data of many programs. To list all directory files, including the hidden ones, you must execute **ls -a**.

Sometimes, it is needed to list some file attributes besides their name. To make this possible, use **ls -l** = **ll** ou **ls -la**.

```bash
total 88
drwx------ 13 ana.costa users 4096 2007-01-26 14:03 .
drwxr-xr-x 3 root root 4096 2007-01-25 10:52 ..
drwx------ 1 ana.costa users 0 2007-01-26 08:00 arca
drwxr-xr-x 2 ana.costa users 4096 2007-01-25 10:52 Desktop
lrwxrwxrwx 1 ana.costa users 26 2007-01-25 10:52 Examples -> ...
```

The main attributes shown in these long listings are **the type of file** (from the character in the left: d for directory, - for normal file, 1 for soft link, etc), **permissions** (3 sets of 3 characters each: indicate the (r)eading, (w)riting and e(x)ecution/search permissions, regarding the file owner, the other elements of its group and the remaining users), **property** (which indicates which user and group own the file), **size** in bytes, **date and time** of the last modification, and file **name**. 




There are other important commands to watch and manipulate directories, such as:
**cd dir** — changes current directory to dir.
**cd** — changes current directory to the home directory.
**mkdir dir** — creates a new directory called dir.
**rmdir dir** — removes the dir directory, as long as it is empty.

The argument **dir** can be passed either as an absolute or relative path. If it's an absolute path, it indicates the path to the desired directory from the root of the entire file system, and it is like `/subdir1/.../subdirN`. If it's a relative path, **dir** indicates the path to the desired directory from the current directory and it is like `subdir1/.../subdirN`.

In each directory, there are always two special names: “.” and “..”, which represent the current directory and the parent directory, the directory where the current one belongs to.



##### Exercise 3

Execute the following commands and interpret the results:

```bash
ls -l /
cd /
pwd
ls -l
cd usr
ls
cd local/src
pwd
ls
cd ../../bin
ls
cd
pwd
```



##### Exercise 4

Try using a graphic file manager to navigate through the same directories of the last exercise.



##### Exercise 5

Create a subdirectory called **pf** and, inside it, a directory called lab01.



#### File Manipulation

Linux (UNIX) provides several commands for file manipulation:
**cat fic** — prints the content of the file called fic in the standard output device (by default, the screen).
**rm fic** — removes the file fic (This operation cannot be undone!)
**mv fic1 fic2** — changes the name of the file fic1 to fic2.
**mv fic dir** — moves the file fic inside directory dir.
**cp fic1 fic2** — creates a copy of the file fic1 called fic2.
**cp fic dir** — creates a copy of the file fic inside directory dir.
**head fic** — shows the first lines of the text file fic.
**tail fic** — shows the last lines of the text file fic.
**less fic** — shows the content of the text file fic, page by page, allowing navigation through the up and down arrow keys and this context is left via the key Q.
**grep pattern fic** — selects fic's lines that contain the text indicated by the pattern.
**wc fic** — counts the number of lines, words and characters of the file fic.
**sort fic** — sorts fic's lines.
**find dir -name fic** — searches for a file named fic inside directory dir.

Furthermore, there are other commands such as cut, paste, tr, etc. All these commands can be evoked using special optional arguments which configure their way of working.



##### Exercise 6

Download the provided file for lab01, and extract its content for the lab01 directory that you have created in the previous exercise. Print the content of the file **[primeiro.py](https://github.com/alexandradecarvalho/programming-fundamentals/blob/main/practical-classes/lab01/primeiro.py)** on the screen. Try some other commands from the list above.



#### Get Help

Linux has many instant help mechanisms for most of its commands. Two of the main ones are accessed through the commands **man** and **info**, the first one being common in all UNIX systems and the second more specific to the GNU project. Many commands also accept a flag **--help**, which presents a summary of its way of use. For example, to find out many execution options of the ls command, you can execute `man ls`, or `info ls`, or `ls --help`.
**Note:** To navigate through the pages of the man or info commands, one can use direction/arrow keys. To leave such pages and return to the command line, one must press Q. 



#### Python Programming Environment



##### Editing

Open the **[primeiro.py](https://github.com/alexandradecarvalho/programming-fundamentals/blob/main/practical-classes/lab01/primeiro.py)** program with a text editor. The Linux system includes several text editors to your choosing. However, we recommend *geany*, or *gedit*, or even *gvim* (VI editor), for their friendly graphic interface and automatic syntax highlighting for Python (and other languages as well). It is also possible to launch any editor or program from the command line, through a command such as `geany &`.



##### Execution

The file you just edited is usually called the "source program". The next step is to execute the developed program. This is done using the command **python3 [primeiro.py](https://github.com/alexandradecarvalho/programming-fundamentals/blob/main/practical-classes/lab01/primeiro.py)** in the terminal. If there aren't any errors, the execution's result should show up in the terminal. If there are any syntax or execution errors, these will be shown in the same order as they were detected. In that case, you must try to identify the cause of the first error and edit the program to fix it.