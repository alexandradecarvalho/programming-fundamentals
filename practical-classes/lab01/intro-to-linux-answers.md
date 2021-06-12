## Introduction to Linux environment for Python programmers - RESOLVED



#### Exercise 1 - Open a terminal window and execute the command **date**

```bash
alexis@jarvis:~/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01$ date
qui 10 jun 2021 12:48:59 WEST
```



#### Exercise 2 - Execute the **cal** command and see the result

```bash
alexis@jarvis:~/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01$ cal
     Junho 2021       
do se te qu qu se sá  
       1  2  3  4  5  
 6  7  8  9 10 11 12  
13 14 15 16 17 18 19  
20 21 22 23 24 25 26  
27 28 29 30           
                      
alexis@jarvis:~/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01$ cal jan 2000
    Janeiro 2000      
do se te qu qu se sá  
                   1  
 2  3  4  5  6  7  8  
 9 10 11 12 13 14 15  
16 17 18 19 20 21 22  
23 24 25 26 27 28 29  
30 31                 

```



#### Exercise 2.1 - To know which is your current directory, execute the command **pwd**

```bash
alexis@jarvis:~/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01$ pwd
/home/alexis/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01
alexis@jarvis:~/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01$ ls
intro-to-linux-answers.md  intro-to-linux.md  practicalguide.md  README.md
alexis@jarvis:~/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01$ ls -a
.   intro-to-linux-answers.md  practicalguide.md
..  intro-to-linux.md          README.md
alexis@jarvis:~/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01$ ls -l
total 28
-rw-rw-r-- 1 alexis alexis  1047 jun 10 15:28 intro-to-linux-answers.md
-rw-rw-r-- 1 alexis alexis 13059 jun 10 12:50 intro-to-linux.md
-rw-rw-r-- 1 alexis alexis  2558 jun 10 00:03 practicalguide.md
-rw-rw-r-- 1 alexis alexis   719 jun 10 12:46 README.md
alexis@jarvis:~/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01$ ls -la
total 36
drwxrwxr-x 2 alexis alexis  4096 jun 10 15:28 .
drwxrwxr-x 3 alexis alexis  4096 jun  9 16:29 ..
-rw-rw-r-- 1 alexis alexis  1047 jun 10 15:28 intro-to-linux-answers.md
-rw-rw-r-- 1 alexis alexis 13059 jun 10 12:50 intro-to-linux.md
-rw-rw-r-- 1 alexis alexis  2558 jun 10 00:03 practicalguide.md
-rw-rw-r-- 1 alexis alexis   719 jun 10 12:46 README.md
alexis@jarvis:~/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01$ ll
total 36
drwxrwxr-x 2 alexis alexis  4096 jun 10 15:28 ./
drwxrwxr-x 3 alexis alexis  4096 jun  9 16:29 ../
-rw-rw-r-- 1 alexis alexis  1047 jun 10 15:28 intro-to-linux-answers.md
-rw-rw-r-- 1 alexis alexis 13059 jun 10 12:50 intro-to-linux.md
-rw-rw-r-- 1 alexis alexis  2558 jun 10 00:03 practicalguide.md
-rw-rw-r-- 1 alexis alexis   719 jun 10 12:46 README.md
```



#### Exercise 3 - Execute the following commands and interpret the results

```bash
alexis@jarvis:~/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01$ ls -l /   
total 84
lrwxrwxrwx   1 root root     7 mai  2 21:27 bin -> usr/bin
drwxr-xr-x   4 root root  4096 jun  7 10:23 boot
drwxr-xr-x   2 root root  4096 mai  2 21:29 cdrom
drwxr-xr-x  21 root root  4940 jun 10 16:24 dev
drwxr-xr-x 136 root root 12288 jun  9 11:54 etc
drwxr-xr-x   3 root root  4096 mai  2 21:30 home
lrwxrwxrwx   1 root root     7 mai  2 21:27 lib -> usr/lib
lrwxrwxrwx   1 root root     9 mai  2 21:27 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 mai  2 21:27 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 mai  2 21:27 libx32 -> usr/libx32
drwx------   2 root root 16384 mai  2 21:26 lost+found
drwxr-xr-x   2 root root  4096 fev  9 18:47 media
drwxr-xr-x   2 root root  4096 fev  9 18:47 mnt
drwxr-xr-x   5 root root  4096 jun  7 11:51 opt
dr-xr-xr-x 431 root root     0 jun 10 09:29 proc
drwx------   8 root root  4096 mai 12 00:12 root
drwxr-xr-x  40 root root  1140 jun 10 20:17 run
lrwxrwxrwx   1 root root     8 mai  2 21:27 sbin -> usr/sbin
drwxr-xr-x  19 root root  4096 jun  9 13:09 snap
drwxr-xr-x   2 root root  4096 fev  9 18:47 srv
dr-xr-xr-x  13 root root     0 jun 10 09:29 sys
drwxrwxrwt  60 root root 12288 jun 10 20:27 tmp
drwxr-xr-x  14 root root  4096 fev  9 18:48 usr
drwxr-xr-x  14 root root  4096 fev  9 18:56 var
```

The command above, **ls -l /**, lists extensively all contents of the directory, in this case "/" (home directory). We can see some soft links, which are the entries that start with l and have "->" in it, to show to where the soft link redirects. The other entries are directories. Then we can see the permission set, 3 groups of 3 characters, highlighting for example the lost+found and root directories, to which only the owner has any type of permission. Then we can see a number, like 14 in the last directory, which represents the number of links or directories inside the directory. Then we can see the user and the group who own the file/directory. Then we can see the size, in bytes, then the date of the last modification and lastly the name. 



```bash
alexis@jarvis:~/Desktop/uni/1ano/1sem/programming-fundamentals/practical-classes/lab01$ cd /
alexis@jarvis:/$
```

The command above, **cd /**, changes the working directory of the shell to, in this case, "/" (home directory). Now, if we write a new command, it will be executed from the new directory passed.



```bash
alexis@jarvis:/$ pwd
/
```

The command above, **pwd**, prints the name of the current working directory of the shell, in this case, "/", because of the last command ("cd"). 



```bash
alexis@jarvis:/$ ls -l
total 84
lrwxrwxrwx   1 root root     7 mai  2 21:27 bin -> usr/bin
drwxr-xr-x   4 root root  4096 jun 12 11:44 boot
drwxr-xr-x   2 root root  4096 mai  2 21:29 cdrom
drwxr-xr-x  21 root root  4900 jun 12 11:21 dev
drwxr-xr-x 136 root root 12288 jun 12 11:43 etc
drwxr-xr-x   3 root root  4096 mai  2 21:30 home
lrwxrwxrwx   1 root root     7 mai  2 21:27 lib -> usr/lib
lrwxrwxrwx   1 root root     9 mai  2 21:27 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 mai  2 21:27 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 mai  2 21:27 libx32 -> usr/libx32
drwx------   2 root root 16384 mai  2 21:26 lost+found
drwxr-xr-x   2 root root  4096 fev  9 18:47 media
drwxr-xr-x   2 root root  4096 fev  9 18:47 mnt
drwxr-xr-x   5 root root  4096 jun  7 11:51 opt
dr-xr-xr-x 403 root root     0 jun 12 11:20 proc
drwx------   8 root root  4096 mai 12 00:12 root
drwxr-xr-x  40 root root  1180 jun 12 11:44 run
lrwxrwxrwx   1 root root     8 mai  2 21:27 sbin -> usr/sbin
drwxr-xr-x  19 root root  4096 jun  9 13:09 snap
drwxr-xr-x   2 root root  4096 fev  9 18:47 srv
dr-xr-xr-x  13 root root     0 jun 12 11:20 sys
drwxrwxrwt  21 root root 12288 jun 12 11:46 tmp
drwxr-xr-x  14 root root  4096 fev  9 18:48 usr
drwxr-xr-x  14 root root  4096 fev  9 18:56 var
```

The command above, **ls -l**, lists extensively all contents of current directory, in this case "/" (home directory). Because we are in directory "/", the commands **ls -l /** and **ls -l** will provide the same result.



```bash
alexis@jarvis:/$ cd usr
alexis@jarvis:/usr$ 
```

The command above, **cd usr**, changes the working directory of the shell to a child directory of the current one, in this case, "usr" - making the current directory "/usr".



```bash
alexis@jarvis:/usr$ ls
bin    include  lib32  libexec  local  share
games  lib      lib64  libx32   sbin   src
```

The command above, **ls**, lists all contents of the current directory, "usr", including files, folders and soft links. In this case, in the console, we can infer all elements are directories, by their listing color. This is probably the largest folder after the home folder as it contains all programs used by a regular user.



```bash
alexis@jarvis:/usr$ cd local/src
alexis@jarvis:/usr/local/src$ 
```

The command above, **cd local/src**, changes the working directory of the shell to a child directory ("src") of the directory "local", which is in turn a child directory of the current one, "/usr".



```bash
alexis@jarvis:/usr/local/src$ pwd
/usr/local/src
```

The command above, **pwd**, prints the name of the current working directory of the shell, in this case, "/usr/local/src" because of all the cd commands executed before.



```bash
alexis@jarvis:/usr/local/src$ ls
alexis@jarvis:/usr/local/src$ 
```

The command above, **ls**, lists all contents of the current directory, "usr/local/src", which we can see is empty. This is the default scenario, but if one compiles and installs a program system-wide, it will be placed here.



```bash
alexis@jarvis:/usr/local/src$ cd ../../bin
alexis@jarvis:/usr/bin$ 
```

The command above, **cd ../../bin**, changes the working directory of the shell to the one passed as argument: "../../bin". The "../" represent a "go back" command. So, in the /usr/local/src directory the command "cd ../" would go back one directory - to /usr/local. This can be used sequentially, so, in the /usr/local/src directory the command "cd ../../" would go back two directories - to /usr. Now, if we append "/bin" we go to a child directory of "/usr" called "bin".



```bash
alexis@jarvis:/usr/bin$ ls
'['                                   mount
 2to3-2.7                             mountpoint
 aa-enabled                           mousetweaks
 aa-exec                              mpartition
 aconnect                             mrd
 acpi_listen                          mren
 add-apt-repository                   mscompress
 addpart                              msexpand
 addr2line                            msgattrib
 alsabat                              msgcat
 alsaloop                             msgcmp
 alsamixer                            msgcomm
 alsatplg                             msgconv
 alsaucm                              msgen
 ambiguous_words                      msgexec
 amidi                                msgfilter
 amixer                               msgfmt
 amuFormat.sh                         msggrep
 aplay                                msginit
 aplaymidi                            msgmerge
 apport-bug                           msgunfmt
 apport-cli                           msguniq
 apport-collect                       mshortname
 apport-unpack                        mshowfat
 appres                               mt
 appstreamcli                         mt-gnu
 apropos                              mtools
 apt                                  mtoolstest
 apt-add-repository                   mtr
 apt-cache                            mtrace
 apt-cdrom                            mtr-packet
 apt-config                           mtype
 aptdcon                              mutter
 apt-extracttemplates                 mv
 apt-ftparchive                       mvn
 apt-get                              mvnDebug
 apt-key                              mxtar
 apt-mark                             myisamchk
 apt-sortpkgs                         myisam_ftdump
 apturl                               myisamlog
 apturl-gtk                           myisampack
 ar                                   my_print_defaults
 arch                                 mysql
 arecord                              mysqladmin
 arecordmidi                          mysqlanalyze
 arm2hpdl                             mysqlbinlog
 as                                   mysqlcheck
 aseqdump                             mysql_config_editor
 aseqnet                              mysqld_multi
 aspell                               mysqld_safe
 aspell-import                        mysqldump
 atobm                                mysqldumpslow
 avahi-browse                         mysqlimport
 avahi-browse-domains                 mysql_migrate_keyring
 avahi-publish                        mysqloptimize
 avahi-publish-address                mysqlpump
 avahi-publish-service                mysqlrepair
 avahi-resolve                        mysqlreport
 avahi-resolve-address                mysql_secure_installation
 avahi-resolve-host-name              mysqlshow
 avahi-set-host-name                  mysqlslap
 awk                                  mysql_ssl_rsa_setup
 axfer                                mysql_tzinfo_to_sql
 b2sum                                mysql_upgrade
 base32                               mzip
 base64                               namei
 basename                             nano
 bash                                 nautilus
 bashbug                              nautilus-autorun-software
 bc                                   nautilus-sendto
 bccmd                                nawk
 bdftopcf                             nc
 bdftruncate                          ncal
 bitmap                               nc.openbsd
 bluemoon                             neqn
 bluetoothctl                         netcat
 bluetooth-sendto                     netkit-ftp
 bmtoa                                netstat
 boltctl                              networkctl
 bootctl                              networkd-dispatcher
 brltty                               newgrp
 brltty-ctb                           ngettext
 brltty-trtxt                         nice
 brltty-ttb                           nisdomainname
 broadwayd                            nl
 browse                               nm
 bsd-from                             nmcli
 bsd-write                            nm-online
 btattach                             nmtui
 btmgmt                               nmtui-connect
 btmon                                nmtui-edit
 bunzip2                              nmtui-hostname
 busctl                               node
 busybox                              node-gyp
 bwrap                                nodejs
 bzcat                                nohup
 bzcmp                                notify-send
 bzdiff                               npm
 bzegrep                              nproc
 bzexe                                npx
 bzfgrep                              nroff
 bzgrep                               nsenter
 bzip2                                nslookup
 bzip2recover                         nstat
 bzless                               nsupdate
 bzmore                               ntfs-3g
 c++                                  ntfs-3g.probe
 c89                                  ntfscat
 c89-gcc                              ntfscluster
 c99                                  ntfscmp
 c99-gcc                              ntfsdecrypt
 cal                                  ntfsfallocate
 calendar                             ntfsfix
 calibrate_ppa                        ntfsinfo
 canberra-gtk-play                    ntfsls
 cancel                               ntfsmove
 captoinfo                            ntfsrecover
 cat                                  ntfssecaudit
 catchsegv                            ntfstruncate
 catman                               ntfsusermap
 cautious-launcher                    ntfswipe
 cc                                   numfmt
 c++filt                              nvidia-bug-report.sh
 chage                                nvidia-cuda-mps-control
 chardet3                             nvidia-cuda-mps-server
 chardetect3                          nvidia-debugdump
 chattr                               nvidia-detector
 chcon                                nvidia-ngx-updater
 check-language-support               nvidia-persistenced
 chfn                                 nvidia-settings
 chgrp                                nvidia-smi
 chmod                                nvidia-xconfig
 choom                                oakdecode
 chown                                obexctl
 chrt                                 objcopy
 chsh                                 objdump
 chvt                                 oclock
 ciptool                              od
 ckbcomp                              oem-getlogs
 cksum                                on_ac_power
 classifier_tester                    opener
 clear                                openssl
 clear_console                        openvt
 cmp                                  opldecode
 cntraining                           orca
 code                                 orca-dm-wrapper
 codepage                             os-prober
 col                                  p11-kit
 colcrt                               pacat
 colrm                                pack200
 column                               pacmd
 combinediff                          pactl
 combine_lang_model                   padsp
 combine_tessdata                     pager
 comm                                 pa-info
 compose                              pamon
 containerd                           paperconf
 containerd-shim                      paplay
 containerd-shim-runc-v1              parec
 containerd-shim-runc-v2              parecord
 corelist                             partx
 cp                                   passwd
 cpan                                 paste
 cpan5.30-x86_64-linux-gnu            pasuspender
 cpanel_json_xs                       patch
 cpio                                 pathchk
 cpp                                  pax11publish
 cpp-9                                pdb2
 crc32                                pdb2.7
 c_rehash                             pdb3
 crontab                              pdb3.8
 csplit                               pdf2dsc
 ctr                                  pdf2ps
 ctstat                               pdfattach
 cupstestppd                          pdfdetach
 curl                                 pdffonts
 cut                                  pdfimages
 cvt                                  pdfinfo
 cvtsudoers                           pdfseparate
 dash                                 pdfsig
 date                                 pdftocairo
 dawg2wordlist                        pdftohtml
 dbus-cleanup-sockets                 pdftoppm
 dbus-daemon                          pdftops
 dbus-launch                          pdftotext
 dbus-monitor                         pdfunite
 dbus-run-session                     peekfd
 dbus-send                            perl
 dbus-update-activation-environment   perl5.30.0
 dbus-uuidgen                         perl5.30-x86_64-linux-gnu
 dc                                   perlbug
 dconf                                perldoc
 dd                                   perli11ndoc
 ddstdecode                           perlivp
 deallocvt                            perlthanks
 debconf                              perror
 debconf-apt-progress                 pf2afm
 debconf-communicate                  pfbtopfa
 debconf-copydb                       pftp
 debconf-escape                       pgrep
 debconf-set-selections               pic
 debconf-show                         pico
 debian-distro-info                   piconv
 deb-systemd-helper                   pidof
 deb-systemd-invoke                   pigz
 dehtmldiff                           pinentry
 delpart                              pinentry-curses
 delv                                 pinentry-gnome3
 desktop-file-edit                    pinentry-x11
 desktop-file-install                 ping
 desktop-file-validate                ping4
 devdump                              ping6
 df                                   pinky
 dfu-tool                             pip
 dh_bash-completion                   pip3
 dh_installxmlcatalogs                pkaction
 dh_perl_openssl                      pkcheck
 dh_python2                           pkcon
 diff                                 pkexec
 diff3                                pkg-config
 diffstat                             pkill
 dig                                  pkmon
 dir                                  pkttyagent
 dircolors                            pl2pm
 dirmngr                              pldd
 dirmngr-client                       plog
 dirname                              plymouth
 dirsplit                             pmap
 discord                              pnm2ppa
 distro-info                          pod2html
 django-admin                         pod2man
 dmesg                                pod2text
 dnsdomainname                        pod2usage
 docker                               podchecker
 dockerd                              podselect
 dockerd-rootless-setuptool.sh        poff
 dockerd-rootless.sh                  pon
 docker-init                          POST
 docker-proxy                         ppdc
 domainname                           ppdhtml
 do-release-upgrade                   ppdi
 dpkg                                 ppdmerge
 dpkg-architecture                    ppdpo
 dpkg-buildflags                      pphs
 dpkg-buildpackage                    pr
 dpkg-checkbuilddeps                  precat
 dpkg-deb                             preconv
 dpkg-distaddfile                     preunzip
 dpkg-divert                          prezip
 dpkg-genbuildinfo                    prezip-bin
 dpkg-genchanges                      prime-select
 dpkg-gencontrol                      prime-supported
 dpkg-gensymbols                      print
 dpkg-maintscript-helper              printafm
 dpkg-mergechangelogs                 printenv
 dpkg-name                            printerbanner
 dpkg-parsechangelog                  printer-profile
 dpkg-query                           printf
 dpkg-scanpackages                    prlimit
 dpkg-scansources                     prove
 dpkg-shlibdeps                       prtstat
 dpkg-source                          ps
 dpkg-split                           ps2ascii
 dpkg-statoverride                    ps2epsi
 dpkg-trigger                         ps2pdf
 dpkg-vendor                          ps2pdf12
 driverless                           ps2pdf13
 du                                   ps2pdf14
 dumpkeys                             ps2pdfwr
 dvipdf                               ps2ps
 dwp                                  ps2ps2
 echo                                 ps2txt
 ed                                   psfaddtable
 edit                                 psfgettable
 editdiff                             psfstriptable
 editor                               psfxtable
 editres                              psicc
 efibootdump                          pslog
 efibootmgr                           pstree
 egrep                                pstree.x11
 eject                                ptar
 elfedit                              ptardiff
 enc2xs                               ptargrep
 encguess                             ptx
 enchant                              pulseaudio
 enchant-2                            pwd
 enchant-lsmod                        pwdx
 enchant-lsmod-2                      py3clean
 env                                  py3compile
 envsubst                             py3versions
 eog                                  pyclean
 eps2eps                              pycompile
 eqn                                  pydoc2
 esc-m                                pydoc2.7
 eutp                                 pydoc3
 evince                               pydoc3.8
 evince-previewer                     pygettext2
 evince-thumbnailer                   pygettext2.7
 ex                                   pygettext3
 expand                               pygettext3.8
 expiry                               pyjwt3
 expr                                 python
 factor                               python2
 faillog                              python2.7
 faked-sysv                           python3
 faked-tcp                            python3.8
 fakeroot                             python3.8-config
 fakeroot-sysv                        python3-config
 fakeroot-tcp                         pyvenv
 fallocate                            pyversions
 false                                qpdldecode
 fc-cache                             quirks-handler
 fc-cat                               ranlib
 fc-conflist                          rbash
 fc-list                              rcp
 fc-match                             rctest
 fc-pattern                           rdma
 fc-query                             readelf
 fc-scan                              readlink
 fc-validate                          realpath
 fgconsole                            recode-sr-latin
 fgrep                                recountdiff
 file                                 red
 file2brl                             rediff
 file-roller                          rename.ul
 filterdiff                           rendercheck
 fincore                              renice
 find                                 reset
 findmnt                              resizecons
 findrule                             resizepart
 firefox                              resolvectl
 fixcvsdiff                           rev
 flipdiff                             rfcomm
 flock                                rgrep
 fmt                                  rimraf
 fold                                 rlogin
 fonttosfnt                           rm
 foo2ddst                             rmdir
 foo2ddst-wrapper                     rmid
 foo2hbpl2                            rmiregistry
 foo2hbpl2-wrapper                    rnano
 foo2hiperc                           rootlesskit
 foo2hiperc-wrapper                   rootlesskit-docker-proxy
 foo2hp                               routef
 foo2hp2600-wrapper                   routel
 foo2lava                             rpcgen
 foo2lava-wrapper                     rrsync
 foo2oak                              rsh
 foo2oak-wrapper                      rstart
 foo2qpdl                             rstartd
 foo2qpdl-wrapper                     rsync
 foo2slx                              rtstat
 foo2slx-wrapper                      runc
 foo2xqx                              runcon
 foo2xqx-wrapper                      run-mailcap
 foo2zjs                              run-parts
 foo2zjs-icc2ps                       run-with-aspell
 foo2zjs-pstops                       rview
 foo2zjs-wrapper                      savelog
 foomatic-rip                         sbattach
 fprintd-delete                       sbkeysync
 fprintd-enroll                       sbsiglist
 fprintd-list                         sbsign
 fprintd-verify                       sbvarsign
 free                                 sbverify
 from                                 scp
 ftp                                  scp-dbus-service
 funzip                               screendump
 fuser                                script
 fusermount                           scriptreplay
 fwupdagent                           sdiff
 fwupdate                             sdptool
 fwupdmgr                             seahorse
 fwupdtool                            sed
 fwupdtpmevlog                        see
 g++                                  select-default-iwrap
 g++-9                                select-editor
 gamemoded                            semver
 gamemoderun                          sensible-browser
 gapplication                         sensible-editor
 gatttool                             sensible-pager
 gcalccmd                             seq
 gcc                                  session-migration
 gcc-9                                sessreg
 gcc-ar                               setarch
 gcc-ar-9                             setfont
 gcc-nm                               setkeycodes
 gcc-nm-9                             setleds
 gcc-ranlib                           setlogcons
 gcc-ranlib-9                         setmetamode
 gcore                                setpci
 gcov                                 setpriv
 gcov-9                               setsid
 gcov-dump                            setterm
 gcov-dump-9                          set_unicharset_properties
 gcov-tool                            setupcon
 gcov-tool-9                          setxkbmap
 gcr-viewer                           sftp
 gdb                                  sg
 gdb-add-index                        sh
 gdbserver                            sha1sum
 gdbtui                               sha224sum
 gdbus                                sha256sum
 gdebi                                sha384sum
 gdebi-gtk                            sha512sum
 gdialog                              shapeclustering
 gdk-pixbuf-csource                   shasum
 gdk-pixbuf-pixdata                   showconsolefont
 gdk-pixbuf-thumbnailer               showkey
 gdmflexiserver                       showrgb
 gdm-screenshot                       shred
 gedit                                shuf
 gencat                               size
 genisoimage                          skill
 geqn                                 slabtop
 GET                                  sleep
 getconf                              slirp4netns
 geteltorito                          slogin
 getent                               slxdecode
 getkeycodes                          smproxy
 getopt                               snap
 gettext                              snapctl
 gettextize                           snapfuse
 gettext.sh                           snice
 ghostscript                          soelim
 ginstall-info                        software-properties-gtk
 gio                                  sort
 gio-querymodules                     sotruss
 gipddecode                           spd-conf
 git                                  spd-say
 git-receive-pack                     speaker-test
 git-shell                            speech-dispatcher
 git-upload-archive                   spellintian
 git-upload-pack                      spice-vdagent
 gjs                                  splain
 gjs-console                          split
 gkbd-keyboard-display                splitdiff
 glib-compile-schemas                 splitfont
 gnome-calculator                     sprof
 gnome-characters                     ss
 gnome-disk-image-mounter             ssh
 gnome-disks                          ssh-add
 gnome-extensions                     ssh-agent
 gnome-font-viewer                    ssh-argv0
 gnome-help                           ssh-copy-id
 gnome-keyring                        ssh-keygen
 gnome-keyring-3                      ssh-keyscan
 gnome-keyring-daemon                 sshpk-conv
 gnome-language-selector              sshpk-sign
 gnome-logs                           sshpk-verify
 gnome-power-statistics               start-pulseaudio-x11
 gnome-screenshot                     startx
 gnome-session                        stat
 gnome-session-custom-session         static-sh
 gnome-session-inhibit                stdbuf
 gnome-session-properties             strace
 gnome-session-quit                   strace-log-merge
 gnome-shell                          strings
 gnome-shell-extension-tool           strip
 gnome-shell-perf-tool                stty
 gnome-system-monitor                 su
 gnome-terminal                       sudo
 gnome-terminal.real                  sudoedit
 gnome-terminal.wrapper               sudoreplay
 gnome-text-editor                    sum
 gnome-thumbnail-font                 symcryptrun
 gnome-www-browser                    sync
 gold                                 system-config-printer
 google-chrome                        system-config-printer-applet
 google-chrome-stable                 systemctl
 gpasswd                              systemd
 gpg                                  systemd-analyze
 gpg-agent                            systemd-ask-password
 gpgcompose                           systemd-cat
 gpgconf                              systemd-cgls
 gpg-connect-agent                    systemd-cgtop
 gpgparsemail                         systemd-delta
 gpgsm                                systemd-detect-virt
 gpgsplit                             systemd-escape
 gpgtar                               systemd-hwdb
 gpgv                                 systemd-id128
 gpg-wks-server                       systemd-inhibit
 gpg-zip                              systemd-machine-id-setup
 gpic                                 systemd-mount
 gprof                                systemd-notify
 gpu-manager                          systemd-path
 grep                                 systemd-resolve
 grepdiff                             systemd-run
 gresource                            systemd-socket-activate
 groff                                systemd-stdio-bridge
 grog                                 systemd-sysusers
 grops                                systemd-tmpfiles
 grotty                               systemd-tty-ask-password-agent
 groups                               systemd-umount
 grub-editenv                         t1ascii
 grub-file                            t1asm
 grub-fstest                          t1binary
 grub-glue-efi                        t1disasm
 grub-kbdcomp                         t1mac
 grub-menulst2cfg                     t1unmac
 grub-mkfont                          tabs
 grub-mkimage                         tac
 grub-mklayout                        tail
 grub-mknetdir                        tar
 grub-mkpasswd-pbkdf2                 taskset
 grub-mkrelpath                       tbl
 grub-mkrescue                        tee
 grub-mkstandalone                    telnet
 grub-mount                           telnet.netkit
 grub-ntldr-img                       tempfile
 grub-render-label                    tesseract
 grub-script-check                    test
 grub-syslinux2cfg                    text2image
 gs                                   tgz
 gsbj                                 tic
 gsdj                                 tificc
 gsdj500                              time
 gsettings                            timedatectl
 gslj                                 timeout
 gslp                                 tload
 gsnd                                 toe
 gst-device-monitor-1.0               top
 gst-discoverer-1.0                   touch
 gst-inspect-1.0                      tput
 gst-launch-1.0                       tr
 gst-play-1.0                         tracepath
 gstreamer-codec-install              traceroute6
 gst-typefind-1.0                     traceroute6.iputils
 gtbl                                 tracker
 gtf                                  transicc
 gtk-builder-tool                     transset
 gtk-encode-symbolic-svg              troff
 gtk-launch                           true
 gtk-query-settings                   truncate
 gtk-update-icon-cache                trust
 gunzip                               tset
 gvfs-cat                             tsort
 gvfs-copy                            ttfread
 gvfs-info                            tty
 gvfs-less                            tzselect
 gvfs-ls                              ua
 gvfs-mime                            ubuntu-advantage
 gvfs-mkdir                           ubuntu-bug
 gvfs-monitor-dir                     ubuntu-core-launcher
 gvfs-monitor-file                    ubuntu-distro-info
 gvfs-mount                           ubuntu-drivers
 gvfs-move                            ubuntu-report
 gvfs-open                            ubuntu-security-status
 gvfs-rename                          ucf
 gvfs-rm                              ucfq
 gvfs-save                            ucfr
 gvfs-set-attribute                   ucs2any
 gvfs-trash                           udevadm
 gvfs-tree                            udisksctl
 gyp                                  ul
 gzexe                                ulockmgr_server
 gzip                                 umount
 h2ph                                 uname
 h2xs                                 unattended-upgrade
 hbpldecode                           unattended-upgrades
 hciattach                            uncompress
 hciconfig                            unexpand
 hcitool                              unicharset_extractor
 hd                                   unicode_start
 head                                 unicode_stop
 HEAD                                 uniq
 helpztags                            unity-scope-loader
 hex2hcd                              unlink
 hexdump                              unlz4
 hipercdecode                         unlzma
 host                                 unmkinitramfs
 hostid                               unpack200
 hostname                             unpigz
 hostnamectl                          unshare
 hwe-support-status                   unsquashfs
 i386                                 unwrapdiff
 i686-linux-gnu-pkg-config            unxz
 ibd2sdi                              unzip
 ibus                                 unzipsfx
 ibus-daemon                          update-alternatives
 ibus-setup                           update-desktop-database
 ibus-table-createdb                  update-manager
 iceauth                              update-mime-database
 ico                                  update-notifier
 iconv                                update-perl-sax-parsers
 id                                   upower
 iecset                               uptime
 ijs_pxljr                            usb-devices
 im-config                            usbhid-dump
 im-launch                            usb_printerid
 info                                 usbreset
 infobrowser                          users
 infocmp                              utmpdump
 infotocap                            uuidgen
 innochecksum                         uuidparse
 inputattach                          uz
 install                              vdir
 install-info                         vi
 install-printerdriver                view
 instmodsh                            viewres
 intel-virtual-output                 vim.tiny
 interdiff                            vmstat
 ionice                               vmwarectrl
 ip                                   volname
 ipcmk                                vstp
 ipcrm                                w
 ipcs                                 wall
 ippfind                              watch
 ipptool                              watchgnupg
 iptables-xml                         wc
 ischroot                             wdctl
 isdv4-serial-debugger                wget
 isdv4-serial-inputattach             whatis
 isodump                              whereis
 isoinfo                              which
 isovfy                               whiptail
 ispell-wrapper                       who
 java                                 whoami
 jexec                                whoopsie
 jjs                                  whoopsie-preferences
 join                                 wordlist2dawg
 journalctl                           word-list-compress
 jpgicc                               wpa_passphrase
 js                                   w.procps
 json_pp                              write
 JSONStream                           X
 kbdinfo                              X11
 kbd_mode                             x11perf
 kbxutil                              x11perfcomp
 kernel-install                       x86_64
 kerneloops-submit                    x86_64-linux-gnu-addr2line
 keyring                              x86_64-linux-gnu-ar
 keytool                              x86_64-linux-gnu-as
 kill                                 x86_64-linux-gnu-c++filt
 killall                              x86_64-linux-gnu-cpp
 kmod                                 x86_64-linux-gnu-cpp-9
 kmodsign                             x86_64-linux-gnu-dwp
 l2ping                               x86_64-linux-gnu-elfedit
 l2test                               x86_64-linux-gnu-g++
 laptop-detect                        x86_64-linux-gnu-g++-9
 last                                 x86_64-linux-gnu-gcc
 lastb                                x86_64-linux-gnu-gcc-9
 lastlog                              x86_64-linux-gnu-gcc-ar
 lavadecode                           x86_64-linux-gnu-gcc-ar-9
 lcf                                  x86_64-linux-gnu-gcc-nm
 ld                                   x86_64-linux-gnu-gcc-nm-9
 ld.bfd                               x86_64-linux-gnu-gcc-ranlib
 ldd                                  x86_64-linux-gnu-gcc-ranlib-9
 ld.gold                              x86_64-linux-gnu-gcov
 less                                 x86_64-linux-gnu-gcov-9
 lessecho                             x86_64-linux-gnu-gcov-dump
 lessfile                             x86_64-linux-gnu-gcov-dump-9
 lesskey                              x86_64-linux-gnu-gcov-tool
 lesspipe                             x86_64-linux-gnu-gcov-tool-9
 lexgrog                              x86_64-linux-gnu-gold
 libnetcfg                            x86_64-linux-gnu-gprof
 libwacom-list-local-devices          x86_64-linux-gnu-ld
 link                                 x86_64-linux-gnu-ld.bfd
 linkicc                              x86_64-linux-gnu-ld.gold
 lintian                              x86_64-linux-gnu-nm
 lintian-info                         x86_64-linux-gnu-objcopy
 linux32                              x86_64-linux-gnu-objdump
 linux64                              x86_64-linux-gnu-pkg-config
 linux-boot-prober                    x86_64-linux-gnu-python3.8-config
 linux-check-removal                  x86_64-linux-gnu-python3-config
 linux-update-symlinks                x86_64-linux-gnu-ranlib
 linux-version                        x86_64-linux-gnu-readelf
 listres                              x86_64-linux-gnu-size
 ln                                   x86_64-linux-gnu-strings
 lnstat                               x86_64-linux-gnu-strip
 loadkeys                             x86_64-pc-linux-gnu-pkg-config
 loadunimap                           xargs
 locale                               xauth
 locale-check                         xbiff
 localectl                            xbrlapi
 localedef                            xcalc
 logger                               xclipboard
 login                                xclock
 loginctl                             xcmsdb
 logname                              xconsole
 look                                 xcursorgen
 lorder                               xcutsel
 lowntfs-3g                           xdg-dbus-proxy
 lp                                   xdg-desktop-icon
 lpoptions                            xdg-desktop-menu
 lpq                                  xdg-email
 lpr                                  xdg-icon-resource
 lprm                                 xdg-mime
 lpstat                               xdg-open
 ls                                   xdg-screensaver
 lsattr                               xdg-settings
 lsblk                                xdg-user-dir
 lsb_release                          xdg-user-dirs-gtk-update
 lscpu                                xdg-user-dirs-update
 lsdiff                               xditview
 lshw                                 xdpyinfo
 lsinitramfs                          xdriinfo
 lsipc                                xedit
 lslocks                              Xephyr
 lslogins                             xev
 lsmem                                xeyes
 lsmod                                xfd
 lsns                                 xfontsel
 lsof                                 xgamma
 lspci                                xgc
 lspgpot                              xgettext
 lstmeval                             xhost
 lstmtraining                         xinit
 lsusb                                xinput
 ltrace                               xkbbell
 luit                                 xkbcomp
 lwp-download                         xkbevd
 lwp-dump                             xkbprint
 lwp-mirror                           xkbvleds
 lwp-request                          xkbwatch
 lz                                   xkeystone
 lz4                                  xkill
 lz4c                                 xload
 lz4cat                               xlogo
 lzcat                                xlsatoms
 lzcmp                                xlsclients
 lzdiff                               xlsfonts
 lzegrep                              xmag
 lzfgrep                              xman
 lzgrep                               xmessage
 lzless                               xmodmap
 lzma                                 xmore
 lzmainfo                             Xorg
 lzmore                               xprop
 m2300w                               xqxdecode
 m2300w-wrapper                       xrandr
 m2400w                               xrdb
 make                                 xrefresh
 make-first-existing-target           x-session-manager
 man                                  xset
 mandb                                xsetmode
 manpath                              xsetpointer
 man-recode                           xsetroot
 mapscrn                              xsetwacom
 mattrib                              xsm
 mawk                                 xstdcmap
 mbadblocks                           xsubpp
 mcat                                 x-terminal-emulator
 mcd                                  xvidtune
 mcheck                               xvinfo
 mclasserase                          Xwayland
 mcomp                                xwd
 mcookie                              x-window-manager
 mcopy                                xwininfo
 md5sum                               xwud
 md5sum.textutils                     x-www-browser
 mdel                                 xxd
 mdeltree                             xz
 mdig                                 xzcat
 mdir                                 xzcmp
 mdu                                  xzdiff
 merge_unicharsets                    xzegrep
 mesa-overlay-control.py              xzfgrep
 mesg                                 xzgrep
 mformat                              xzless
 mftraining                           xzmore
 migrate-pubring-from-classic-gpg     yelp
 mimeopen                             yes
 mimetype                             ypdomainname
 min12xxw                             zcat
 minfo                                zcmp
 mkdir                                zdiff
 mkfifo                               zdump
 mkfontdir                            zegrep
 mkfontscale                          zenity
 mkisofs                              zfgrep
 mkmanifest                           zforce
 mk_modmap                            zgrep
 mknod                                zip
 mksquashfs                           zipcloak
 mktemp                               zipdetails
 mkzftree                             zipgrep
 mlabel                               zipinfo
 mmcli                                zipnote
 mmd                                  zipsplit
 mmount                               zjsdecode
 mmove                                zless
 mokutil                              zmore
 monitor-sensor                       znew
 more                                 zoom
 alexis@jarvis:/usr/bin$ 
```

The command above, **ls**, lists all contents of the current directory, "usr/bin", which is, as we can see, a huge directory. This is because "usr/bin" contains the programs installed by the Linux distribution in use. There are thousands of programs here. Here we can see some different coloured entries: in my case, blue entries, like zoom, represent soft links, and green entries, like znew, are directories or files. 



```bash
alexis@jarvis:/usr/bin$ cd
alexis@jarvis:~$ 
```

The command above, **cd**, changes the working directory of the shell. When used without arguments, like done above, the directory it moves to is the directory "~".



```bash
alexis@jarvis:~$ pwd
/home/alexis
```

The command above, **pwd**, prints the name of the current working directory of the shell, in this case, it shows that "~" is an abbreviation of "/home/alexis", which is my user's home directory. 



#### Exercise 4 - To know which is your current directory, execute the command **pwd**

![https://github.com/alexandradecarvalho/programming-fundamentals/blob/main/img/root.png]()





