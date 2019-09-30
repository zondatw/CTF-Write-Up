```text
Kernel Complete Dump File: Full address space is available

Symbol search path is: srv*
Executable search path is: 
Windows 7 Kernel Version 7601 (Service Pack 1) UP Free x64
Product: WinNt, suite: TerminalServer SingleUserTS Personal
Built by: 7601.18741.amd64fre.win7sp1_gdr.150202-1526
Machine Name:
Kernel base = 0xfffff800`02a49000 PsLoadedModuleList = 0xfffff800`02c8d890
Debug session time: Fri Aug  2 22:38:33.721 2019 (UTC + 8:00)
System Uptime: 0 days 0:49:18.389
Loading Kernel Symbols
...............................................................
................................................................
..............................
Loading User Symbols

Loading unloaded module list
...................

A fatal system error has occurred.
Debugger entered on first try; Bugcheck callbacks have not been invoked.

A fatal system error has occurred.

*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

Use !analyze -v to get detailed debugging information.

BugCheck 7E, {ffffffffc0000005, fffffa8003f9c621, fffff88007c6b958, fffff88007c6b1b0}

*** WARNING: Unable to verify timestamp for man.sys
*** ERROR: Module load completed but symbols could not be loaded for man.sys
Probably caused by : man.sys ( man+1ce7 )

Followup:     MachineOwner
---------

```  
OS: Windows 7 Kernel Version 7601 (Service Pack 1) UP Free x64  
Probably caused by : man.sys ( man+1ce7 )  


```text
kd> kbn
 # RetAddr           : Args to Child                                                           : Call Site
00 fffff800`02bafcc2 : ffffffff`c0000005 fffffa80`040c65c0 00000000`00000065 fffff800`02af97e8 : nt!RtlpBreakWithStatusInstruction
01 fffff800`02bb0aae : fffff880`00000003 00000000`00000000 fffff800`02afa040 00000000`0000007e : nt!KiBugCheckDebugBreak+0x12
02 fffff800`02abdfc4 : fffff800`02d5cb30 00000000`0000201a 00000000`00002019 fffff800`02cdf138 : nt!KeBugCheck2+0x71e
03 fffff800`02e30614 : 00000000`0000007e ffffffff`c0000005 fffffa80`03f9c621 fffff880`07c6b958 : nt!KeBugCheckEx+0x104
04 fffff800`02deb231 : 00000000`00000000 00000000`00000000 fffff880`64536553 00000000`000007ff : nt!PspUnhandledExceptionInSystemThread+0x24
05 fffff800`02ae9c4c : fffff8a0`02e629c0 fffff8a0`02e629e8 fffff8a0`02e62a04 fffff8a0`02e62a20 : nt! ?? ::NNGAKEGL::`string'+0x221d
06 fffff800`02ae96cd : fffff800`02c22854 fffff880`07c6bc00 00000000`00000000 fffff800`02a49000 : nt!_C_specific_handler+0x8c
07 fffff800`02ae84a5 : fffff800`02c22854 fffff880`07c6aae8 fffff880`07c6b958 fffff800`02a49000 : nt!RtlpExecuteHandlerForException+0xd
08 fffff800`02af9431 : fffff880`07c6b958 fffff880`07c6b1b0 fffff880`00000000 00000000`00000001 : nt!RtlDispatchException+0x415
09 fffff800`02abd542 : fffff880`07c6b958 fffffa80`040c65c0 fffff880`07c6ba00 fffffa80`018cc090 : nt!KiDispatchException+0x135
0a fffff800`02abbe4a : 00060030`00010002 00000000`00000000 00000000`00000000 00000000`00000000 : nt!KiExceptionDispatch+0xc2
0b fffffa80`03f9c621 : 00000000`0001093a 00000000`00010ba8 ffffffff`ffffffff 00000000`00000080 : nt!KiGeneralProtectionFault+0x10a
0c 00000000`0001093a : 00000000`00010ba8 ffffffff`ffffffff 00000000`00000080 fffff880`033bdce7 : 0xfffffa80`03f9c621
0d 00000000`00010ba8 : ffffffff`ffffffff 00000000`00000080 fffff880`033bdce7 00000000`00000000 : 0x1093a
0e ffffffff`ffffffff : 00000000`00000080 fffff880`033bdce7 00000000`00000000 00000000`00000000 : 0x10ba8
0f 00000000`00000080 : fffff880`033bdce7 00000000`00000000 00000000`00000000 00000000`00000000 : 0xffffffff`ffffffff
10 fffff880`033bdce7 : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : 0x80
11 00000000`00000000 : 00000000`00000000 00000000`00000000 00000000`00000000 fffffa80`03f9c610 : man+0x1ce7
```

```
kd> kvn
 # Child-SP          RetAddr           : Args to Child                                                           : Call Site
00 fffff880`07c6a218 fffff800`02bafcc2 : ffffffff`c0000005 fffffa80`040c65c0 00000000`00000065 fffff800`02af97e8 : nt!RtlpBreakWithStatusInstruction
01 fffff880`07c6a220 fffff800`02bb0aae : fffff880`00000003 00000000`00000000 fffff800`02afa040 00000000`0000007e : nt!KiBugCheckDebugBreak+0x12
02 fffff880`07c6a280 fffff800`02abdfc4 : fffff800`02d5cb30 00000000`0000201a 00000000`00002019 fffff800`02cdf138 : nt!KeBugCheck2+0x71e
03 fffff880`07c6a950 fffff800`02e30614 : 00000000`0000007e ffffffff`c0000005 fffffa80`03f9c621 fffff880`07c6b958 : nt!KeBugCheckEx+0x104
04 fffff880`07c6a990 fffff800`02deb231 : 00000000`00000000 00000000`00000000 fffff880`64536553 00000000`000007ff : nt!PspUnhandledExceptionInSystemThread+0x24
05 fffff880`07c6a9d0 fffff800`02ae9c4c : fffff8a0`02e629c0 fffff8a0`02e629e8 fffff8a0`02e62a04 fffff8a0`02e62a20 : nt! ?? ::NNGAKEGL::`string'+0x221d
06 fffff880`07c6aa00 fffff800`02ae96cd : fffff800`02c22854 fffff880`07c6bc00 00000000`00000000 fffff800`02a49000 : nt!_C_specific_handler+0x8c
07 fffff880`07c6aa70 fffff800`02ae84a5 : fffff800`02c22854 fffff880`07c6aae8 fffff880`07c6b958 fffff800`02a49000 : nt!RtlpExecuteHandlerForException+0xd
08 fffff880`07c6aaa0 fffff800`02af9431 : fffff880`07c6b958 fffff880`07c6b1b0 fffff880`00000000 00000000`00000001 : nt!RtlDispatchException+0x415
09 fffff880`07c6b180 fffff800`02abd542 : fffff880`07c6b958 fffffa80`040c65c0 fffff880`07c6ba00 fffffa80`018cc090 : nt!KiDispatchException+0x135
0a fffff880`07c6b820 fffff800`02abbe4a : 00060030`00010002 00000000`00000000 00000000`00000000 00000000`00000000 : nt!KiExceptionDispatch+0xc2
0b fffff880`07c6ba00 fffffa80`03f9c621 : 00000000`0001093a 00000000`00010ba8 ffffffff`ffffffff 00000000`00000080 : nt!KiGeneralProtectionFault+0x10a (TrapFrame @ fffff880`07c6ba00)
0c fffff880`07c6bb98 00000000`0001093a : 00000000`00010ba8 ffffffff`ffffffff 00000000`00000080 fffff880`033bdce7 : 0xfffffa80`03f9c621
0d fffff880`07c6bba0 00000000`00010ba8 : ffffffff`ffffffff 00000000`00000080 fffff880`033bdce7 00000000`00000000 : 0x1093a
0e fffff880`07c6bba8 ffffffff`ffffffff : 00000000`00000080 fffff880`033bdce7 00000000`00000000 00000000`00000000 : 0x10ba8
0f fffff880`07c6bbb0 00000000`00000080 : fffff880`033bdce7 00000000`00000000 00000000`00000000 00000000`00000000 : 0xffffffff`ffffffff
10 fffff880`07c6bbb8 fffff880`033bdce7 : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : 0x80
11 fffff880`07c6bbc0 00000000`00000000 : 00000000`00000000 00000000`00000000 00000000`00000000 fffffa80`03f9c610 : man+0x1ce7
```

```text
kd> !analyze -v
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (7e)
This is a very common bugcheck.  Usually the exception address pinpoints
the driver/function that caused the problem.  Always note this address
as well as the link date of the driver/image that contains this address.
Arguments:
Arg1: ffffffffc0000005, The exception code that was not handled
Arg2: fffffa8003f9c621, The address that the exception occurred at
Arg3: fffff88007c6b958, Exception Record Address
Arg4: fffff88007c6b1b0, Context Record Address

Debugging Details:
------------------


KEY_VALUES_STRING: 1


STACKHASH_ANALYSIS: 1

TIMELINE_ANALYSIS: 1


DUMP_CLASS: 1

DUMP_QUALIFIER: 402

BUILD_VERSION_STRING:  7601.18741.amd64fre.win7sp1_gdr.150202-1526

SYSTEM_MANUFACTURER:  VMware, Inc.

VIRTUAL_MACHINE:  VMware

SYSTEM_PRODUCT_NAME:  VMware Virtual Platform

SYSTEM_VERSION:  None

BIOS_VENDOR:  Phoenix Technologies LTD

BIOS_VERSION:  6.00

BIOS_DATE:  04/13/2018

BASEBOARD_MANUFACTURER:  Intel Corporation

BASEBOARD_PRODUCT:  440BX Desktop Reference Platform

BASEBOARD_VERSION:  None

DUMP_TYPE:  0

BUGCHECK_P1: ffffffffc0000005

BUGCHECK_P2: fffffa8003f9c621

BUGCHECK_P3: fffff88007c6b958

BUGCHECK_P4: fffff88007c6b1b0

EXCEPTION_CODE: (NTSTATUS) 0xc0000005 - <Unable to get error code text>

FAULTING_IP: 
+0
fffffa80`03f9c621 64a10000000050648925 mov eax,dword ptr fs:[2589645000000000h]

EXCEPTION_RECORD:  fffff88007c6b958 -- (.exr 0xfffff88007c6b958)
ExceptionAddress: fffffa8003f9c621
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 0000000000000000
   Parameter[1]: ffffffffffffffff
Attempt to read from address ffffffffffffffff

CONTEXT:  fffff88007c6b1b0 -- (.cxr 0xfffff88007c6b1b0)
rax=fffffa8003f9c610 rbx=fffffa80040c65c0 rcx=fffffa80036ab5c0
rdx=fffff880033c8138 rsi=fffffa80018cc090 rdi=0000000000000001
rip=fffffa8003f9c621 rsp=fffff88007c6bb98 rbp=0000000007c6bbb0
 r8=fffff80002c3f400  r9=0000000000000000 r10=0000000000000000
r11=fffff80002c3ae80 r12=fffffa80036ab5c0 r13=fffff880033bdcc0
r14=0000000000000000 r15=fffff80000b94080
iopl=0         nv up ei ng nz na po nc
cs=0010  ss=0018  ds=002b  es=002b  fs=0053  gs=002b             efl=00010286
fffffa80`03f9c621 64a10000000050648925 mov eax,dword ptr fs:[2589645000000000h] fs:0053:25896450`00000000=????????
Resetting default scope

CPU_COUNT: 1

CPU_MHZ: e75

CPU_VENDOR:  GenuineIntel

CPU_FAMILY: 6

CPU_MODEL: 9e

CPU_STEPPING: a

CPU_MICROCODE: 6,9e,a,0 (F,M,S,R)  SIG: 96'00000000 (cache) 96'00000000 (init)

DEFAULT_BUCKET_ID:  WIN7_DRIVER_FAULT

PROCESS_NAME:  System

CURRENT_IRQL:  2

FOLLOWUP_IP: 
man+1ce7
fffff880`033bdce7 89442428        mov     dword ptr [rsp+28h],eax

BUGCHECK_STR:  0x7E

READ_ADDRESS:  ffffffffffffffff 

ERROR_CODE: (NTSTATUS) 0xc0000005 - <Unable to get error code text>

EXCEPTION_CODE_STR:  c0000005

EXCEPTION_PARAMETER1:  0000000000000000

EXCEPTION_PARAMETER2:  ffffffffffffffff

ANALYSIS_SESSION_HOST:  MSI

ANALYSIS_SESSION_TIME:  09-20-2019 23:54:01.0329

ANALYSIS_VERSION: 10.0.17763.1 amd64fre

LAST_CONTROL_TRANSFER:  from 000000000001093a to fffffa8003f9c621

STACK_TEXT:  
fffff880`07c6bb98 00000000`0001093a : 00000000`00010ba8 ffffffff`ffffffff 00000000`00000080 fffff880`033bdce7 : 0xfffffa80`03f9c621
fffff880`07c6bba0 00000000`00010ba8 : ffffffff`ffffffff 00000000`00000080 fffff880`033bdce7 00000000`00000000 : 0x1093a
fffff880`07c6bba8 ffffffff`ffffffff : 00000000`00000080 fffff880`033bdce7 00000000`00000000 00000000`00000000 : 0x10ba8
fffff880`07c6bbb0 00000000`00000080 : fffff880`033bdce7 00000000`00000000 00000000`00000000 00000000`00000000 : 0xffffffff`ffffffff
fffff880`07c6bbb8 fffff880`033bdce7 : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : 0x80
fffff880`07c6bbc0 00000000`00000000 : 00000000`00000000 00000000`00000000 00000000`00000000 fffffa80`03f9c610 : man+0x1ce7


THREAD_SHA1_HASH_MOD_FUNC:  8175e3c8753aeb1696959f72ede260ebf3ea14c5

THREAD_SHA1_HASH_MOD_FUNC_OFFSET:  7c2abaddc43a7edcac2d2576e24447b109c16c2f

THREAD_SHA1_HASH_MOD:  8175e3c8753aeb1696959f72ede260ebf3ea14c5

FAULT_INSTR_CODE:  28244489

SYMBOL_STACK_INDEX:  5

SYMBOL_NAME:  man+1ce7

FOLLOWUP_NAME:  MachineOwner

MODULE_NAME: man

IMAGE_NAME:  man.sys

DEBUG_FLR_IMAGE_TIMESTAMP:  0

STACK_COMMAND:  .cxr 0xfffff88007c6b1b0 ; kb

FAILURE_BUCKET_ID:  X64_0x7E_man+1ce7

BUCKET_ID:  X64_0x7E_man+1ce7

PRIMARY_PROBLEM_CLASS:  X64_0x7E_man+1ce7

TARGET_TIME:  2019-08-02T14:38:33.000Z

OSBUILD:  7601

OSSERVICEPACK:  1000

SERVICEPACK_NUMBER: 0

OS_REVISION: 0

SUITE_MASK:  784

PRODUCT_TYPE:  1

OSPLATFORM_TYPE:  x64

OSNAME:  Windows 7

OSEDITION:  Windows 7 WinNt (Service Pack 1) TerminalServer SingleUserTS Personal

OS_LOCALE:  

USER_LCID:  0

OSBUILD_TIMESTAMP:  2015-02-03 10:25:01

BUILDDATESTAMP_STR:  150202-1526

BUILDLAB_STR:  win7sp1_gdr

BUILDOSVER_STR:  6.1.7601.18741.amd64fre.win7sp1_gdr.150202-1526

ANALYSIS_SESSION_ELAPSED_TIME:  78d

ANALYSIS_SOURCE:  KM

FAILURE_ID_HASH_STRING:  km:x64_0x7e_man+1ce7

FAILURE_ID_HASH:  {ceed7a1b-a47b-c452-63c1-012e444d5204}

Followup:     MachineOwner
---------

```

```text
kd> lm
start             end                 module name
fffff800`00bac000 fffff800`00bd6000   kdcom      (deferred)             
fffff800`02a00000 fffff800`02a49000   hal        (deferred)             
fffff800`02a49000 fffff800`03030000   nt         (pdb symbols)          D:\Windows Kits\10\Debuggers\x64\sym\ntkrnlmp.pdb\2E37F962D699492CAAF3F9F4E9770B1D2\ntkrnlmp.pdb
fffff880`00c00000 fffff880`00c19000   vmci       (deferred)             
fffff880`00c19000 fffff880`00c30000   vsock      (deferred)             
fffff880`00c30000 fffff880`00c4a000   mountmgr   (deferred)             
fffff880`00c4a000 fffff880`00c53000   atapi      (deferred)             
fffff880`00c53000 fffff880`00c7d000   ataport    (deferred)             
fffff880`00c7d000 fffff880`00c9a000   lsi_sas    (deferred)             
fffff880`00ca2000 fffff880`00cf1000   mcupdate_GenuineIntel   (deferred)             
fffff880`00cf1000 fffff880`00d05000   PSHED      (deferred)             
fffff880`00d05000 fffff880`00d63000   CLFS       (deferred)             
fffff880`00d63000 fffff880`00dd8000   CI         (deferred)             
fffff880`00dd8000 fffff880`00de0000   intelide   (deferred)             
fffff880`00de0000 fffff880`00df0000   PCIIDEX    (deferred)             
fffff880`00e00000 fffff880`00e15000   partmgr    (deferred)             
fffff880`00e15000 fffff880`00e1e000   compbatt   (deferred)             
fffff880`00e1e000 fffff880`00e2a000   BATTC      (deferred)             
fffff880`00e2a000 fffff880`00e3f000   volmgr     (deferred)             
fffff880`00e3f000 fffff880`00e9b000   volmgrx    (deferred)             
fffff880`00e9c000 fffff880`00f40000   Wdf01000   (deferred)             
fffff880`00f40000 fffff880`00f4f000   WDFLDR     (deferred)             
fffff880`00f4f000 fffff880`00fa6000   ACPI       (deferred)             
fffff880`00fa6000 fffff880`00faf000   WMILIB     (deferred)             
fffff880`00faf000 fffff880`00fb9000   msisadrv   (deferred)             
fffff880`00fb9000 fffff880`00fec000   pci        (deferred)             
fffff880`00fec000 fffff880`00ff9000   vdrvroot   (deferred)             
fffff880`01000000 fffff880`01072000   cng        (deferred)             
fffff880`01072000 fffff880`01094000   tdx        (deferred)             
fffff880`010a3000 fffff880`01106000   storport   (deferred)             
fffff880`01106000 fffff880`01111000   msahci     (deferred)             
fffff880`01111000 fffff880`0111c000   amdxata    (deferred)             
fffff880`0111c000 fffff880`01168000   fltmgr     (deferred)             
fffff880`01168000 fffff880`0117c000   fileinfo   (deferred)             
fffff880`0117c000 fffff880`011da000   msrpc      (deferred)             
fffff880`011da000 fffff880`011f8000   dfsc       (deferred)             
fffff880`01200000 fffff880`0121b000   ksecdd     (deferred)             
fffff880`0121b000 fffff880`0122c000   pcw        (deferred)             
fffff880`0122c000 fffff880`01236000   Fs_Rec     (deferred)             
fffff880`01236000 fffff880`01247000   Npfs       (deferred)             
fffff880`01247000 fffff880`01254000   TDI        (deferred)             
fffff880`0125b000 fffff880`013fe000   Ntfs       (deferred)             
fffff880`01400000 fffff880`01410000   watchdog   (deferred)             
fffff880`01410000 fffff880`01419000   RDPCDD     (deferred)             
fffff880`01419000 fffff880`01422000   rdpencdd   (deferred)             
fffff880`01422000 fffff880`0142b000   rdprefmp   (deferred)             
fffff880`01431000 fffff880`01524000   ndis       (deferred)             
fffff880`01524000 fffff880`01584000   NETIO      (deferred)             
fffff880`01584000 fffff880`015b0000   ksecpkg    (deferred)             
fffff880`015b0000 fffff880`015bf000   vmrawdsk   (deferred)             
fffff880`015bf000 fffff880`015cd000   vga        (deferred)             
fffff880`015cd000 fffff880`015f2000   VIDEOPRT   (deferred)             
fffff880`015f2000 fffff880`015fd000   Msfs       (deferred)             
fffff880`01600000 fffff880`01630000   CLASSPNP   (deferred)             
fffff880`01630000 fffff880`0164d000   usbccgp    (deferred)             
fffff880`0164d000 fffff880`01666000   HIDCLASS   (deferred)             
fffff880`01678000 fffff880`016a2000   cdrom      (deferred)             
fffff880`016a2000 fffff880`016a9000   Beep       (deferred)             
fffff880`016aa000 fffff880`018ae000   tcpip      (deferred)             
fffff880`018ae000 fffff880`018f8000   fwpkclnt   (deferred)             
fffff880`018f8000 fffff880`01944000   volsnap    (deferred)             
fffff880`01944000 fffff880`0194c000   spldr      (deferred)             
fffff880`0194c000 fffff880`01986000   rdyboost   (deferred)             
fffff880`01986000 fffff880`01998000   mup        (deferred)             
fffff880`01998000 fffff880`019a1000   hwpolicy   (deferred)             
fffff880`019a1000 fffff880`019db000   fvevol     (deferred)             
fffff880`019db000 fffff880`019f1000   disk       (deferred)             
fffff880`019f1000 fffff880`019fa000   Null       (deferred)             
fffff880`02600000 fffff880`0262d000   mrxsmb     (deferred)             
fffff880`0262d000 fffff880`0267a000   mrxsmb10   (deferred)             
fffff880`0267a000 fffff880`0269e000   mrxsmb20   (deferred)             
fffff880`026a7000 fffff880`026bc000   lltdio     (deferred)             
fffff880`026bc000 fffff880`026c9000   mouhid     (deferred)             
fffff880`026c9000 fffff880`026e1000   rspndr     (deferred)             
fffff880`026e1000 fffff880`026ea000   vmusbmouse   (deferred)             
fffff880`026ea000 fffff880`027b3000   HTTP       (deferred)             
fffff880`027b3000 fffff880`027d1000   bowser     (deferred)             
fffff880`027d1000 fffff880`027e9000   mpsdrv     (deferred)             
fffff880`03200000 fffff880`0328c000   bthport    (deferred)             
fffff880`0328c000 fffff880`032b8000   rfcomm     (deferred)             
fffff880`032b8000 fffff880`032c8000   BthEnum    (deferred)             
fffff880`032c8000 fffff880`032e8000   bthpan     (deferred)             
fffff880`032f1000 fffff880`032fb000   vmmemctl   (deferred)             
fffff880`032fb000 fffff880`03307000   npf        (deferred)             
fffff880`03307000 fffff880`033b1000   peauth     (deferred)             
fffff880`033b1000 fffff880`033bc000   secdrv     (deferred)             
fffff880`033bc000 fffff880`033cb000   man      T (no symbols)           
fffff880`033dc000 fffff880`033f4000   BTHUSB     (deferred)             
fffff880`03600000 fffff880`03651000   rdbss      (deferred)             
fffff880`03651000 fffff880`0365d000   nsiproxy   (deferred)             
fffff880`0365d000 fffff880`036e6000   afd        (deferred)             
fffff880`036e6000 fffff880`0372b000   netbt      (deferred)             
fffff880`0372b000 fffff880`03736000   ws2ifsl    (deferred)             
fffff880`03736000 fffff880`0373f000   wfplwf     (deferred)             
fffff880`0373f000 fffff880`03765000   pacer      (deferred)             
fffff880`03765000 fffff880`03779000   npcap      (deferred)             
fffff880`03779000 fffff880`03788000   netbios    (deferred)             
fffff880`03788000 fffff880`037a5000   serial     (deferred)             
fffff880`037a5000 fffff880`037c0000   wanarp     (deferred)             
fffff880`037c0000 fffff880`037d4000   termdd     (deferred)             
fffff880`037d4000 fffff880`037df000   mssmbios   (pdb symbols)          D:\Windows Kits\10\Debuggers\x64\sym\mssmbios.pdb\9ECFB21A2AD64292AB8AF8AB1B194C2E1\mssmbios.pdb
fffff880`037df000 fffff880`037ee000   discache   (deferred)             
fffff880`037ee000 fffff880`037ff000   blbdrive   (deferred)             
fffff880`03a0c000 fffff880`03a32000   tunnel     (deferred)             
fffff880`03a32000 fffff880`03a50000   i8042prt   (deferred)             
fffff880`03a50000 fffff880`03a5f000   kbdclass   (deferred)             
fffff880`03a5f000 fffff880`03a68000   vmmouse    (deferred)             
fffff880`03a68000 fffff880`03a77000   mouclass   (deferred)             
fffff880`03a77000 fffff880`03a83000   serenum    (deferred)             
fffff880`03a83000 fffff880`03a8d000   vm3dmp_loader   (deferred)             
fffff880`03a8d000 fffff880`03ace000   vm3dmp     (deferred)             
fffff880`03ace000 fffff880`03bc2000   dxgkrnl    (deferred)             
fffff880`03bc2000 fffff880`03bdc000   rassstp    (deferred)             
fffff880`03bdc000 fffff880`03bff000   luafv      (deferred)             
fffff880`03c00000 fffff880`03c2f000   ndiswan    (deferred)             
fffff880`03c2f000 fffff880`03c4a000   raspppoe   (deferred)             
fffff880`03c4a000 fffff880`03c6b000   raspptp    (deferred)             
fffff880`03c6b000 fffff880`03c72000   loop       (deferred)             
fffff880`03c72000 fffff880`03c73480   swenum     (deferred)             
fffff880`03c7c000 fffff880`03cc2000   dxgmms1    (deferred)             
fffff880`03cc2000 fffff880`03ccf000   usbuhci    (deferred)             
fffff880`03ccf000 fffff880`03d25000   USBPORT    (deferred)             
fffff880`03d25000 fffff880`03d48980   E1G6032E   (deferred)             
fffff880`03d49000 fffff880`03d6d000   HDAudBus   (deferred)             
fffff880`03d6d000 fffff880`03d7e000   usbehci    (deferred)             
fffff880`03d7e000 fffff880`03d82500   CmBatt     (deferred)             
fffff880`03d83000 fffff880`03d99000   intelppm   (deferred)             
fffff880`03d99000 fffff880`03da9000   CompositeBus   (deferred)             
fffff880`03da9000 fffff880`03dbf000   AgileVpn   (deferred)             
fffff880`03dbf000 fffff880`03de3000   rasl2tp    (deferred)             
fffff880`03de3000 fffff880`03def000   ndistapi   (deferred)             
fffff880`03def000 fffff880`03df7080   HIDPARSE   (deferred)             
fffff880`03e00000 fffff880`03e3d000   portcls    (deferred)             
fffff880`03e3d000 fffff880`03e5f000   drmk       (deferred)             
fffff880`03e5f000 fffff880`03e64200   ksthunk    (deferred)             
fffff880`03e65000 fffff880`03e73000   crashdmp   (deferred)             
fffff880`03e73000 fffff880`03e7d000   dump_diskdump   (deferred)             
fffff880`03e7d000 fffff880`03e9a000   dump_LSI_SAS   (deferred)             
fffff880`03e9a000 fffff880`03ead000   dump_dumpfve   (deferred)             
fffff880`03ead000 fffff880`03eb9000   Dxapi      (deferred)             
fffff880`03eb9000 fffff880`03ec7000   monitor    (deferred)             
fffff880`03ec7000 fffff880`03ec8f00   USBD       (deferred)             
fffff880`03ec9000 fffff880`03ed7000   hidusb     (deferred)             
fffff880`03edb000 fffff880`03f1e000   ks         (deferred)             
fffff880`03f1e000 fffff880`03f30000   umbus      (deferred)             
fffff880`03f30000 fffff880`03f8a000   usbhub     (deferred)             
fffff880`03f8a000 fffff880`03f9f000   NDProxy    (deferred)             
fffff880`03f9f000 fffff880`03ffb000   HdAudio    (deferred)             
fffff880`04200000 fffff880`0420c000   PROCEXP152   (deferred)             
fffff880`04217000 fffff880`04248000   srvnet     (deferred)             
fffff880`04248000 fffff880`0425a000   tcpipreg   (deferred)             
fffff880`0425a000 fffff880`042c5000   srv2       (deferred)             
fffff880`042c5000 fffff880`0435e000   srv        (deferred)             
fffff880`0435e000 fffff880`04389000   vmhgfs     (deferred)             
fffff880`04389000 fffff880`043fa000   spsys      (deferred)             
fffff960`000e0000 fffff960`003f0000   win32k     (deferred)             
fffff960`00570000 fffff960`0057a000   TSDDD      (deferred)             
fffff960`00610000 fffff960`00637000   cdd        (deferred)             

Unloaded modules:
fffff880`03218000 fffff880`032a4000   bthport.sys
fffff880`03200000 fffff880`03218000   BTHUSB.sys
fffff880`032d0000 fffff880`032e0000   BthEnum.sys
fffff880`032a4000 fffff880`032d0000   rfcomm.sys
fffff880`033bc000 fffff880`033dc000   bthpan.sys
fffff880`03238000 fffff880`032c4000   bthport.sys
fffff880`03220000 fffff880`03238000   BTHUSB.sys
fffff880`033bc000 fffff880`033cc000   BthEnum.sys
fffff880`032c4000 fffff880`032f0000   rfcomm.sys
fffff880`033cc000 fffff880`033ec000   bthpan.sys
fffff880`03265000 fffff880`032f1000   bthport.sys
fffff880`0324d000 fffff880`03265000   BTHUSB.sys
fffff880`033e8000 fffff880`033f8000   BthEnum.sys
fffff880`033bc000 fffff880`033e8000   rfcomm.sys
fffff880`03200000 fffff880`03220000   bthpan.sys
fffff880`01630000 fffff880`0163e000   crashdmp.sys
fffff880`0163e000 fffff880`01648000   dump_storport.sys
fffff880`01648000 fffff880`01665000   dump_LSI_SAS.sys
fffff880`01665000 fffff880`01678000   dump_dumpfve.sys
```

```text
kd> !threads
Index	TID			TEB				StackBase			StackLimit			DeAlloc			StackSize			ThreadProc
0	0000000000000000	0xfffffa80040c65c0	0xfffffa80035ba168	0xfffffa80035ba168	0x0000000000000000	0x0000000000000000	0x6000000000
Total VM consumed by thread stacks 0x00000000

```

```text
kd> lmDvmman
Browse full module list
start             end                 module name
fffff880`033bc000 fffff880`033cb000   man      T (no symbols)           
    Loaded symbol image file: man.sys
    Image path: \??\C:\Users\FLARE ON 2019\Desktop\man.sys
    Image name: man.sys
    Browse all global symbols  functions  data
    Timestamp:        unavailable (FFFFFFFE)
    CheckSum:         missing
    ImageSize:        0000F000
    Translations:     0000.04b0 0000.04e4 0409.04b0 0409.04e4
    Information from resource tables:
```

```text
kd> !vm
Page File: \??\C:\pagefile.sys
  Current:   2096632 Kb  Free Space:   2085468 Kb
  Minimum:   2096632 Kb  Maximum:      6289896 Kb

Physical Memory:           524158 (    2096632 Kb)
Available Pages:           235317 (     941268 Kb)
ResAvail Pages:            441236 (    1764944 Kb)
Locked IO Pages:                0 (          0 Kb)
Free System PTEs:        33484771 (  133939084 Kb)
Modified Pages:             12633 (      50532 Kb)
Modified PF Pages:          12601 (      50404 Kb)
Modified No Write Pages:        0 (          0 Kb)
NonPagedPool Usage:         28106 (     112424 Kb)
NonPagedPool Max:          382974 (    1531896 Kb)
PagedPool  0:               26504 (     106016 Kb)
PagedPool  1:                3823 (      15292 Kb)
PagedPool  2:                 962 (       3848 Kb)
PagedPool  3:                 926 (       3704 Kb)
PagedPool  4:                 969 (       3876 Kb)
PagedPool Usage:            33184 (     132736 Kb)
PagedPool Maximum:       33554432 (  134217728 Kb)
Processor Commit:             186 (        744 Kb)
Session Commit:              5662 (      22648 Kb)
Syspart SharedCommit 0
Shared Commit:              18111 (      72444 Kb)
Special Pool:                   0 (          0 Kb)
Kernel Stacks:               5537 (      22148 Kb)
Pages For MDLs:               588 (       2352 Kb)
Pages For AWE:                  0 (          0 Kb)
NonPagedPool Commit:            0 (          0 Kb)
PagedPool Commit:           33187 (     132748 Kb)
Driver Commit:               4213 (      16852 Kb)
Boot Commit:                    0 (          0 Kb)
System PageTables:              0 (          0 Kb)
VAD/PageTable Bitmaps:       2115 (       8460 Kb)
ProcessLockedFilePages:         0 (          0 Kb)
Pagefile Hash Pages:            0 (          0 Kb)
Sum System Commit:          69599 (     278396 Kb)
Total Private:             177224 (     708896 Kb)
Misc/Transient Commit:      48960 (     195840 Kb)
Committed pages:           295783 (    1183132 Kb)
Commit limit:             1048316 (    4193264 Kb)

  Pid ImageName                        Commit   SharedCommit        Debt

  6b4 chrome.exe                     88540 Kb           0 Kb        0 Kb
  454 dwm.exe                        80020 Kb           0 Kb        0 Kb
  464 explorer.exe                   64904 Kb           0 Kb        0 Kb
  11c svchost.exe                    63236 Kb           0 Kb        0 Kb
  538 chrome.exe                     52120 Kb           0 Kb        0 Kb
  36c svchost.exe                    52108 Kb           0 Kb        0 Kb
  f04 chrome.exe                     38236 Kb           0 Kb        0 Kb
  8b8 SearchIndexer.exe              27208 Kb           0 Kb        0 Kb
 1228 chrome.exe                     24752 Kb           0 Kb        0 Kb
  b14 chrome.exe                     24224 Kb           0 Kb        0 Kb
  9cc procexp64.exe                  20256 Kb           0 Kb        0 Kb
  2e4 svchost.exe                    15264 Kb           0 Kb        0 Kb
  214 svchost.exe                    13644 Kb           0 Kb        0 Kb
  548 vmtoolsd.exe                   11856 Kb           0 Kb        0 Kb
  4ec svchost.exe                    10564 Kb           0 Kb        0 Kb
  a64 chrome.exe                     10468 Kb           0 Kb        0 Kb
  688 vmtoolsd.exe                    8964 Kb           0 Kb        0 Kb
  4f4 taskhost.exe                    7544 Kb           0 Kb        0 Kb
  7d8 WmiPrvSE.exe                    7392 Kb           0 Kb        0 Kb
  3fc svchost.exe                     6920 Kb           0 Kb        0 Kb
  b40 sppsvc.exe                      6340 Kb           0 Kb        0 Kb
  4bc spoolsv.exe                     5860 Kb           0 Kb        0 Kb
  168 csrss.exe                       5392 Kb           0 Kb        0 Kb
  1d0 services.exe                    4820 Kb           0 Kb        0 Kb
  588 dllhost.exe                     4156 Kb           0 Kb        0 Kb
  334 svchost.exe                     4060 Kb           0 Kb        0 Kb
  1e0 lsass.exe                       3812 Kb           0 Kb        0 Kb
  2b8 svchost.exe                     3744 Kb           0 Kb        0 Kb
  ba8 svchost.exe                     3600 Kb           0 Kb        0 Kb
  254 svchost.exe                     3508 Kb           0 Kb        0 Kb
  a58 KeePass.exe                     3404 Kb           0 Kb        0 Kb
  754 msdtc.exe                       3260 Kb           0 Kb        0 Kb
  648 VGAuthService.exe               3072 Kb           0 Kb        0 Kb
  18c winlogon.exe                    2472 Kb           0 Kb        0 Kb
  1e8 lsm.exe                         2192 Kb           0 Kb        0 Kb
  cb0 cmd.exe                         1864 Kb           0 Kb        0 Kb
  b78 cmd.exe                         1816 Kb           0 Kb        0 Kb
  958 cmd.exe                         1816 Kb           0 Kb        0 Kb
  12c csrss.exe                       1800 Kb           0 Kb        0 Kb
  858 svchost.exe                     1696 Kb           0 Kb        0 Kb
  7b8 chrome.exe                      1676 Kb           0 Kb        0 Kb
  b24 chrome.exe                      1652 Kb           0 Kb        0 Kb
  768 svchost.exe                     1508 Kb           0 Kb        0 Kb
  da0 conhost.exe                     1380 Kb           0 Kb        0 Kb
  aa0 conhost.exe                     1360 Kb           0 Kb        0 Kb
  9b8 conhost.exe                     1352 Kb           0 Kb        0 Kb
  160 wininit.exe                     1316 Kb           0 Kb        0 Kb
  290 vmacthlp.exe                    1268 Kb           0 Kb        0 Kb
   d4 smss.exe                         368 Kb           0 Kb        0 Kb
    4 System                           112 Kb           0 Kb        0 Kb
```


```text
kd> !idt

Dumping IDT: fffff80000b93080

00:	fffff80002abac40 nt!KiDivideErrorFault
01:	fffff80002abad40 nt!KiDebugTrapOrFault
02:	fffff80002abaf00 nt!KiNmiInterrupt	Stack = 0xFFFFF80000BA5000
03:	fffff80002abb280 nt!KiBreakpointTrap
04:	fffff80002abb380 nt!KiOverflowTrap
05:	fffff80002abb480 nt!KiBoundFault
06:	fffff80002abb580 nt!KiInvalidOpcodeFault
07:	fffff80002abb7c0 nt!KiNpxNotAvailableFault
08:	fffff80002abb880 nt!KiDoubleFaultAbort	Stack = 0xFFFFF80000BA3000
09:	fffff80002abb940 nt!KiNpxSegmentOverrunAbort
0a:	fffff80002abba00 nt!KiInvalidTssFault
0b:	fffff80002abbac0 nt!KiSegmentNotPresentFault
0c:	fffff80002abbc00 nt!KiStackFault
0d:	fffff80002abbd40 nt!KiGeneralProtectionFault
0e:	fffff80002abbe80 nt!KiPageFault
10:	fffff80002abc240 nt!KiFloatingErrorFault
11:	fffff80002abc3c0 nt!KiAlignmentFault
12:	fffff80002abc4c0 nt!KiMcheckAbort	Stack = 0xFFFFF80000BA7000
13:	fffff80002abc840 nt!KiXmmException
1f:	fffff80002ab17d0 nt!KiApcInterrupt
2c:	fffff80002abca00 nt!KiRaiseAssertion
2d:	fffff80002abcb00 nt!KiDebugServiceTrap
2f:	fffff80002b098d0 nt!KiDpcInterrupt
37:	fffff80002a30090 hal!HalpApicSpuriousService (KINTERRUPT fffff80002a30000)

3f:	fffff80002a30130 hal!HalpApicSpuriousService (KINTERRUPT fffff80002a300a0)

50:	fffff80002a30270 hal!HalpCmciService (KINTERRUPT fffff80002a301e0)

51:	fffffa8001bdab10 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bdaa80)

52:	fffffa8001bda5d0 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda540)

53:	fffffa8001bda090 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda000)

54:	fffffa8001c07b10 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c07a80)

55:	fffffa8001c07690 *** ERROR: Symbol file could not be found.  Defaulted to export symbols for vmci.sys - 
vmci!DllInitialize+0x1938 (KINTERRUPT fffffa8001c07600)

60:	fffffa8001bdabd0 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bdab40)

61:	fffffa8001c68b10 serial!SerialCIsrSw (KINTERRUPT fffffa8001c68a80)

62:	fffffa8001bda690 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda600)

63:	fffffa8001bda150 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda0c0)

64:	fffffa8001c07bd0 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c07b40)

65:	fffffa8001c07510 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c07480)

66:	fffffa8001c68a50 USBPORT!USBPORT_InterruptService (KINTERRUPT fffffa8001c689c0)

70:	fffffa8001bdac90 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bdac00)

71:	fffffa8001c68bd0 i8042prt!I8042MouseInterruptService (KINTERRUPT fffffa8001c68b40)

72:	fffffa8001bda750 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda6c0)

73:	fffffa8001bda210 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda180)

74:	fffffa8001c07c90 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c07c00)

75:	fffffa8001c075d0 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c07540)

76:	fffffa8001c68810 HDAudBus!HdaController::Isr (KINTERRUPT fffffa8001c68780)

	                 dxgkrnl!DpiFdoLineInterruptRoutine (KINTERRUPT fffffa8001c686c0)

80:	fffffa8001bdad50 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bdacc0)

81:	fffffa8001c68c90 i8042prt!I8042KeyboardInterruptService (KINTERRUPT fffffa8001c68c00)

82:	fffffa8001bda810 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda780)

83:	fffffa8001bda2d0 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda240)

84:	fffffa8001c07d50 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c07cc0)

85:	fffffa8001c07810 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c07780)

86:	fffffa8001c688d0 USBPORT!USBPORT_InterruptService (KINTERRUPT fffffa8001c68840)

90:	fffffa8001bdae10 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bdad80)

92:	fffffa8001bda8d0 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda840)

93:	fffffa8001bda390 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda300)

94:	fffffa8001c07e10 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c07d80)

95:	fffffa8001c078d0 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c07840)

96:	fffffa8001c07390 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c07300)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c07240)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c07180)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c070c0)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c07000)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6bf00)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6be40)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6bd80)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6bcc0)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6bc00)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6bb40)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6ba80)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b9c0)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b900)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b840)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b780)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b6c0)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b600)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b540)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b480)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b3c0)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b300)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b240)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b180)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b0c0)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c6b000)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c68f00)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c68e40)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c68d80)

	                 ataport!IdePortInterrupt (KINTERRUPT fffffa8001c68cc0)

	                 E1G6032E!E1000ISR (NDIS) (KINTERRUPT fffffa8001c68900)

a0:	fffffa8001bdaed0 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bdae40)

a2:	fffffa8001bda990 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda900)

a3:	fffffa8001bda450 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda3c0)

a4:	fffffa8001c07ed0 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c07e40)

a5:	fffffa8001c07990 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c07900)

a6:	fffffa8001c07450 lsi_sas!LSImpiMSIIsr (STORPORT) (KINTERRUPT fffffa8001c073c0)

b0:	fffffa8001c07750 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c076c0)

b1:	fffffa8001bdaf90 ACPI!ACPIInterruptServiceRoutine (KINTERRUPT fffffa8001bdaf00)

b2:	fffffa8001bdaa50 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda9c0)

b3:	fffffa8001bda510 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001bda480)

b4:	fffffa8001c07f90 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c07f00)

b5:	fffffa8001c07a50 pci!ExpressRootPortMessageRoutine (KINTERRUPT fffffa8001c079c0)

c1:	fffff80002a30450 hal!HalpBroadcastCallService (KINTERRUPT fffff80002a303c0)

d1:	fffff80002a304f0 hal!HalpHpetClockInterrupt (KINTERRUPT fffff80002a30460)

d2:	fffff80002a30590 hal!HalpHpetRolloverInterrupt (KINTERRUPT fffff80002a30500)

df:	fffff80002a303b0 hal!HalpApicRebootService (KINTERRUPT fffff80002a30320)

e1:	fffff80002ac88c0 nt!KiIpiInterrupt
e2:	fffff80002a30310 hal!HalpDeferredRecoveryService (KINTERRUPT fffff80002a30280)

e3:	fffff80002a301d0 hal!HalpLocalApicErrorService (KINTERRUPT fffff80002a30140)

fd:	fffff80002a30630 hal!HalpProfileInterrupt (KINTERRUPT fffff80002a305a0)

fe:	fffff80002a306d0 hal!HalpPerfInterrupt (KINTERRUPT fffff80002a30640)

ff:	0000000000000000 

```

```text
kd> lm f
start             end                 module name
fffff800`00bac000 fffff800`00bd6000   kdcom    kdbazis.dll 
fffff800`02a00000 fffff800`02a49000   hal      hal.dll     
fffff800`02a49000 fffff800`03030000   nt       ntkrnlmp.exe
fffff880`00c00000 fffff880`00c19000   vmci     \SystemRoot\system32\DRIVERS\vmci.sys
fffff880`00c19000 fffff880`00c30000   vsock    \SystemRoot\system32\DRIVERS\vsock.sys
fffff880`00c30000 fffff880`00c4a000   mountmgr \SystemRoot\System32\drivers\mountmgr.sys
fffff880`00c4a000 fffff880`00c53000   atapi    \SystemRoot\system32\drivers\atapi.sys
fffff880`00c53000 fffff880`00c7d000   ataport  \SystemRoot\system32\drivers\ataport.SYS
fffff880`00c7d000 fffff880`00c9a000   lsi_sas  \SystemRoot\system32\drivers\lsi_sas.sys
fffff880`00ca2000 fffff880`00cf1000   mcupdate_GenuineIntel \SystemRoot\system32\mcupdate_GenuineIntel.dll
fffff880`00cf1000 fffff880`00d05000   PSHED    \SystemRoot\system32\PSHED.dll
fffff880`00d05000 fffff880`00d63000   CLFS     \SystemRoot\system32\CLFS.SYS
fffff880`00d63000 fffff880`00dd8000   CI       \SystemRoot\system32\CI.dll
fffff880`00dd8000 fffff880`00de0000   intelide \SystemRoot\system32\drivers\intelide.sys
fffff880`00de0000 fffff880`00df0000   PCIIDEX  \SystemRoot\system32\drivers\PCIIDEX.SYS
fffff880`00e00000 fffff880`00e15000   partmgr  \SystemRoot\System32\drivers\partmgr.sys
fffff880`00e15000 fffff880`00e1e000   compbatt \SystemRoot\system32\DRIVERS\compbatt.sys
fffff880`00e1e000 fffff880`00e2a000   BATTC    \SystemRoot\system32\DRIVERS\BATTC.SYS
fffff880`00e2a000 fffff880`00e3f000   volmgr   \SystemRoot\system32\drivers\volmgr.sys
fffff880`00e3f000 fffff880`00e9b000   volmgrx  \SystemRoot\System32\drivers\volmgrx.sys
fffff880`00e9c000 fffff880`00f40000   Wdf01000 \SystemRoot\system32\drivers\Wdf01000.sys
fffff880`00f40000 fffff880`00f4f000   WDFLDR   \SystemRoot\system32\drivers\WDFLDR.SYS
fffff880`00f4f000 fffff880`00fa6000   ACPI     \SystemRoot\system32\drivers\ACPI.sys
fffff880`00fa6000 fffff880`00faf000   WMILIB   \SystemRoot\system32\drivers\WMILIB.SYS
fffff880`00faf000 fffff880`00fb9000   msisadrv \SystemRoot\system32\drivers\msisadrv.sys
fffff880`00fb9000 fffff880`00fec000   pci      \SystemRoot\system32\drivers\pci.sys
fffff880`00fec000 fffff880`00ff9000   vdrvroot \SystemRoot\system32\drivers\vdrvroot.sys
fffff880`01000000 fffff880`01072000   cng      \SystemRoot\System32\Drivers\cng.sys
fffff880`01072000 fffff880`01094000   tdx      \SystemRoot\system32\DRIVERS\tdx.sys
fffff880`010a3000 fffff880`01106000   storport \SystemRoot\system32\drivers\storport.sys
fffff880`01106000 fffff880`01111000   msahci   \SystemRoot\system32\drivers\msahci.sys
fffff880`01111000 fffff880`0111c000   amdxata  \SystemRoot\system32\drivers\amdxata.sys
fffff880`0111c000 fffff880`01168000   fltmgr   \SystemRoot\system32\drivers\fltmgr.sys
fffff880`01168000 fffff880`0117c000   fileinfo \SystemRoot\system32\drivers\fileinfo.sys
fffff880`0117c000 fffff880`011da000   msrpc    \SystemRoot\System32\Drivers\msrpc.sys
fffff880`011da000 fffff880`011f8000   dfsc     \SystemRoot\System32\Drivers\dfsc.sys
fffff880`01200000 fffff880`0121b000   ksecdd   \SystemRoot\System32\Drivers\ksecdd.sys
fffff880`0121b000 fffff880`0122c000   pcw      \SystemRoot\System32\drivers\pcw.sys
fffff880`0122c000 fffff880`01236000   Fs_Rec   \SystemRoot\System32\Drivers\Fs_Rec.sys
fffff880`01236000 fffff880`01247000   Npfs     \SystemRoot\System32\Drivers\Npfs.SYS
fffff880`01247000 fffff880`01254000   TDI      \SystemRoot\system32\DRIVERS\TDI.SYS
fffff880`0125b000 fffff880`013fe000   Ntfs     \SystemRoot\System32\Drivers\Ntfs.sys
fffff880`01400000 fffff880`01410000   watchdog \SystemRoot\System32\drivers\watchdog.sys
fffff880`01410000 fffff880`01419000   RDPCDD   \SystemRoot\System32\DRIVERS\RDPCDD.sys
fffff880`01419000 fffff880`01422000   rdpencdd \SystemRoot\system32\drivers\rdpencdd.sys
fffff880`01422000 fffff880`0142b000   rdprefmp \SystemRoot\system32\drivers\rdprefmp.sys
fffff880`01431000 fffff880`01524000   ndis     \SystemRoot\system32\drivers\ndis.sys
fffff880`01524000 fffff880`01584000   NETIO    \SystemRoot\system32\drivers\NETIO.SYS
fffff880`01584000 fffff880`015b0000   ksecpkg  \SystemRoot\System32\Drivers\ksecpkg.sys
fffff880`015b0000 fffff880`015bf000   vmrawdsk \SystemRoot\system32\DRIVERS\vmrawdsk.sys
fffff880`015bf000 fffff880`015cd000   vga      \SystemRoot\System32\drivers\vga.sys
fffff880`015cd000 fffff880`015f2000   VIDEOPRT \SystemRoot\System32\drivers\VIDEOPRT.SYS
fffff880`015f2000 fffff880`015fd000   Msfs     \SystemRoot\System32\Drivers\Msfs.SYS
fffff880`01600000 fffff880`01630000   CLASSPNP \SystemRoot\system32\drivers\CLASSPNP.SYS
fffff880`01630000 fffff880`0164d000   usbccgp  \SystemRoot\system32\DRIVERS\usbccgp.sys
fffff880`0164d000 fffff880`01666000   HIDCLASS \SystemRoot\system32\DRIVERS\HIDCLASS.SYS
fffff880`01678000 fffff880`016a2000   cdrom    \SystemRoot\system32\DRIVERS\cdrom.sys
fffff880`016a2000 fffff880`016a9000   Beep     \SystemRoot\System32\Drivers\Beep.SYS
fffff880`016aa000 fffff880`018ae000   tcpip    \SystemRoot\System32\drivers\tcpip.sys
fffff880`018ae000 fffff880`018f8000   fwpkclnt \SystemRoot\System32\drivers\fwpkclnt.sys
fffff880`018f8000 fffff880`01944000   volsnap  \SystemRoot\system32\drivers\volsnap.sys
fffff880`01944000 fffff880`0194c000   spldr    \SystemRoot\System32\Drivers\spldr.sys
fffff880`0194c000 fffff880`01986000   rdyboost \SystemRoot\System32\drivers\rdyboost.sys
fffff880`01986000 fffff880`01998000   mup      \SystemRoot\System32\Drivers\mup.sys
fffff880`01998000 fffff880`019a1000   hwpolicy \SystemRoot\System32\drivers\hwpolicy.sys
fffff880`019a1000 fffff880`019db000   fvevol   \SystemRoot\System32\DRIVERS\fvevol.sys
fffff880`019db000 fffff880`019f1000   disk     \SystemRoot\system32\drivers\disk.sys
fffff880`019f1000 fffff880`019fa000   Null     \SystemRoot\System32\Drivers\Null.SYS
fffff880`02600000 fffff880`0262d000   mrxsmb   \SystemRoot\system32\DRIVERS\mrxsmb.sys
fffff880`0262d000 fffff880`0267a000   mrxsmb10 \SystemRoot\system32\DRIVERS\mrxsmb10.sys
fffff880`0267a000 fffff880`0269e000   mrxsmb20 \SystemRoot\system32\DRIVERS\mrxsmb20.sys
fffff880`026a7000 fffff880`026bc000   lltdio   \SystemRoot\system32\DRIVERS\lltdio.sys
fffff880`026bc000 fffff880`026c9000   mouhid   \SystemRoot\system32\DRIVERS\mouhid.sys
fffff880`026c9000 fffff880`026e1000   rspndr   \SystemRoot\system32\DRIVERS\rspndr.sys
fffff880`026e1000 fffff880`026ea000   vmusbmouse \SystemRoot\system32\DRIVERS\vmusbmouse.sys
fffff880`026ea000 fffff880`027b3000   HTTP     \SystemRoot\system32\drivers\HTTP.sys
fffff880`027b3000 fffff880`027d1000   bowser   \SystemRoot\system32\DRIVERS\bowser.sys
fffff880`027d1000 fffff880`027e9000   mpsdrv   \SystemRoot\System32\drivers\mpsdrv.sys
fffff880`03200000 fffff880`0328c000   bthport  \SystemRoot\System32\Drivers\bthport.sys
fffff880`0328c000 fffff880`032b8000   rfcomm   \SystemRoot\system32\DRIVERS\rfcomm.sys
fffff880`032b8000 fffff880`032c8000   BthEnum  \SystemRoot\system32\DRIVERS\BthEnum.sys
fffff880`032c8000 fffff880`032e8000   bthpan   \SystemRoot\system32\DRIVERS\bthpan.sys
fffff880`032f1000 fffff880`032fb000   vmmemctl \SystemRoot\system32\DRIVERS\vmmemctl.sys
fffff880`032fb000 fffff880`03307000   npf      \SystemRoot\system32\drivers\npf.sys
fffff880`03307000 fffff880`033b1000   peauth   \SystemRoot\system32\drivers\peauth.sys
fffff880`033b1000 fffff880`033bc000   secdrv   \SystemRoot\System32\Drivers\secdrv.SYS
fffff880`033bc000 fffff880`033cb000   man      \??\C:\Users\FLARE ON 2019\Desktop\man.sys
fffff880`033dc000 fffff880`033f4000   BTHUSB   \SystemRoot\System32\Drivers\BTHUSB.sys
fffff880`03600000 fffff880`03651000   rdbss    \SystemRoot\system32\DRIVERS\rdbss.sys
fffff880`03651000 fffff880`0365d000   nsiproxy \SystemRoot\system32\drivers\nsiproxy.sys
fffff880`0365d000 fffff880`036e6000   afd      \SystemRoot\system32\drivers\afd.sys
fffff880`036e6000 fffff880`0372b000   netbt    \SystemRoot\System32\DRIVERS\netbt.sys
fffff880`0372b000 fffff880`03736000   ws2ifsl  \SystemRoot\system32\drivers\ws2ifsl.sys
fffff880`03736000 fffff880`0373f000   wfplwf   \SystemRoot\system32\DRIVERS\wfplwf.sys
fffff880`0373f000 fffff880`03765000   pacer    \SystemRoot\system32\DRIVERS\pacer.sys
fffff880`03765000 fffff880`03779000   npcap    \SystemRoot\system32\DRIVERS\npcap.sys
fffff880`03779000 fffff880`03788000   netbios  \SystemRoot\system32\DRIVERS\netbios.sys
fffff880`03788000 fffff880`037a5000   serial   \SystemRoot\system32\DRIVERS\serial.sys
fffff880`037a5000 fffff880`037c0000   wanarp   \SystemRoot\system32\DRIVERS\wanarp.sys
fffff880`037c0000 fffff880`037d4000   termdd   \SystemRoot\system32\DRIVERS\termdd.sys
fffff880`037d4000 fffff880`037df000   mssmbios \SystemRoot\system32\DRIVERS\mssmbios.sys
fffff880`037df000 fffff880`037ee000   discache \SystemRoot\System32\drivers\discache.sys
fffff880`037ee000 fffff880`037ff000   blbdrive \SystemRoot\system32\DRIVERS\blbdrive.sys
fffff880`03a0c000 fffff880`03a32000   tunnel   \SystemRoot\system32\DRIVERS\tunnel.sys
fffff880`03a32000 fffff880`03a50000   i8042prt \SystemRoot\system32\DRIVERS\i8042prt.sys
fffff880`03a50000 fffff880`03a5f000   kbdclass \SystemRoot\system32\DRIVERS\kbdclass.sys
fffff880`03a5f000 fffff880`03a68000   vmmouse  \SystemRoot\system32\DRIVERS\vmmouse.sys
fffff880`03a68000 fffff880`03a77000   mouclass \SystemRoot\system32\DRIVERS\mouclass.sys
fffff880`03a77000 fffff880`03a83000   serenum  \SystemRoot\system32\DRIVERS\serenum.sys
fffff880`03a83000 fffff880`03a8d000   vm3dmp_loader \SystemRoot\system32\DRIVERS\vm3dmp_loader.sys
fffff880`03a8d000 fffff880`03ace000   vm3dmp   \SystemRoot\system32\DRIVERS\vm3dmp.sys
fffff880`03ace000 fffff880`03bc2000   dxgkrnl  \SystemRoot\System32\drivers\dxgkrnl.sys
fffff880`03bc2000 fffff880`03bdc000   rassstp  \SystemRoot\system32\DRIVERS\rassstp.sys
fffff880`03bdc000 fffff880`03bff000   luafv    \SystemRoot\system32\drivers\luafv.sys
fffff880`03c00000 fffff880`03c2f000   ndiswan  \SystemRoot\system32\DRIVERS\ndiswan.sys
fffff880`03c2f000 fffff880`03c4a000   raspppoe \SystemRoot\system32\DRIVERS\raspppoe.sys
fffff880`03c4a000 fffff880`03c6b000   raspptp  \SystemRoot\system32\DRIVERS\raspptp.sys
fffff880`03c6b000 fffff880`03c72000   loop     \SystemRoot\system32\DRIVERS\loop.sys
fffff880`03c72000 fffff880`03c73480   swenum   \SystemRoot\system32\DRIVERS\swenum.sys
fffff880`03c7c000 fffff880`03cc2000   dxgmms1  \SystemRoot\System32\drivers\dxgmms1.sys
fffff880`03cc2000 fffff880`03ccf000   usbuhci  \SystemRoot\system32\DRIVERS\usbuhci.sys
fffff880`03ccf000 fffff880`03d25000   USBPORT  \SystemRoot\system32\DRIVERS\USBPORT.SYS
fffff880`03d25000 fffff880`03d48980   E1G6032E \SystemRoot\system32\DRIVERS\E1G6032E.sys
fffff880`03d49000 fffff880`03d6d000   HDAudBus \SystemRoot\system32\DRIVERS\HDAudBus.sys
fffff880`03d6d000 fffff880`03d7e000   usbehci  \SystemRoot\system32\DRIVERS\usbehci.sys
fffff880`03d7e000 fffff880`03d82500   CmBatt   \SystemRoot\system32\DRIVERS\CmBatt.sys
fffff880`03d83000 fffff880`03d99000   intelppm \SystemRoot\system32\DRIVERS\intelppm.sys
fffff880`03d99000 fffff880`03da9000   CompositeBus \SystemRoot\system32\DRIVERS\CompositeBus.sys
fffff880`03da9000 fffff880`03dbf000   AgileVpn \SystemRoot\system32\DRIVERS\AgileVpn.sys
fffff880`03dbf000 fffff880`03de3000   rasl2tp  \SystemRoot\system32\DRIVERS\rasl2tp.sys
fffff880`03de3000 fffff880`03def000   ndistapi \SystemRoot\system32\DRIVERS\ndistapi.sys
fffff880`03def000 fffff880`03df7080   HIDPARSE \SystemRoot\system32\DRIVERS\HIDPARSE.SYS
fffff880`03e00000 fffff880`03e3d000   portcls  \SystemRoot\system32\drivers\portcls.sys
fffff880`03e3d000 fffff880`03e5f000   drmk     \SystemRoot\system32\drivers\drmk.sys
fffff880`03e5f000 fffff880`03e64200   ksthunk  \SystemRoot\system32\drivers\ksthunk.sys
fffff880`03e65000 fffff880`03e73000   crashdmp \SystemRoot\System32\Drivers\crashdmp.sys
fffff880`03e73000 fffff880`03e7d000   dump_diskdump \SystemRoot\System32\Drivers\dump_diskdump.sys
fffff880`03e7d000 fffff880`03e9a000   dump_LSI_SAS \SystemRoot\System32\Drivers\dump_LSI_SAS.sys
fffff880`03e9a000 fffff880`03ead000   dump_dumpfve \SystemRoot\System32\Drivers\dump_dumpfve.sys
fffff880`03ead000 fffff880`03eb9000   Dxapi    \SystemRoot\System32\drivers\Dxapi.sys
fffff880`03eb9000 fffff880`03ec7000   monitor  \SystemRoot\system32\DRIVERS\monitor.sys
fffff880`03ec7000 fffff880`03ec8f00   USBD     \SystemRoot\system32\DRIVERS\USBD.SYS
fffff880`03ec9000 fffff880`03ed7000   hidusb   \SystemRoot\system32\DRIVERS\hidusb.sys
fffff880`03edb000 fffff880`03f1e000   ks       \SystemRoot\system32\DRIVERS\ks.sys
fffff880`03f1e000 fffff880`03f30000   umbus    \SystemRoot\system32\DRIVERS\umbus.sys
fffff880`03f30000 fffff880`03f8a000   usbhub   \SystemRoot\system32\DRIVERS\usbhub.sys
fffff880`03f8a000 fffff880`03f9f000   NDProxy  \SystemRoot\System32\Drivers\NDProxy.SYS
fffff880`03f9f000 fffff880`03ffb000   HdAudio  \SystemRoot\system32\drivers\HdAudio.sys
fffff880`04200000 fffff880`0420c000   PROCEXP152 \??\C:\Windows\system32\Drivers\PROCEXP152.SYS
fffff880`04217000 fffff880`04248000   srvnet   \SystemRoot\System32\DRIVERS\srvnet.sys
fffff880`04248000 fffff880`0425a000   tcpipreg \SystemRoot\System32\drivers\tcpipreg.sys
fffff880`0425a000 fffff880`042c5000   srv2     \SystemRoot\System32\DRIVERS\srv2.sys
fffff880`042c5000 fffff880`0435e000   srv      \SystemRoot\System32\DRIVERS\srv.sys
fffff880`0435e000 fffff880`04389000   vmhgfs   \SystemRoot\system32\DRIVERS\vmhgfs.sys
fffff880`04389000 fffff880`043fa000   spsys    \SystemRoot\system32\drivers\spsys.sys
fffff960`000e0000 fffff960`003f0000   win32k   \SystemRoot\System32\win32k.sys
fffff960`00570000 fffff960`0057a000   TSDDD    \SystemRoot\System32\TSDDD.dll
fffff960`00610000 fffff960`00637000   cdd      \SystemRoot\System32\cdd.dll

Unloaded modules:
fffff880`03218000 fffff880`032a4000   bthport.sys
fffff880`03200000 fffff880`03218000   BTHUSB.sys
fffff880`032d0000 fffff880`032e0000   BthEnum.sys
fffff880`032a4000 fffff880`032d0000   rfcomm.sys
fffff880`033bc000 fffff880`033dc000   bthpan.sys
fffff880`03238000 fffff880`032c4000   bthport.sys
fffff880`03220000 fffff880`03238000   BTHUSB.sys
fffff880`033bc000 fffff880`033cc000   BthEnum.sys
fffff880`032c4000 fffff880`032f0000   rfcomm.sys
fffff880`033cc000 fffff880`033ec000   bthpan.sys
fffff880`03265000 fffff880`032f1000   bthport.sys
fffff880`0324d000 fffff880`03265000   BTHUSB.sys
fffff880`033e8000 fffff880`033f8000   BthEnum.sys
fffff880`033bc000 fffff880`033e8000   rfcomm.sys
fffff880`03200000 fffff880`03220000   bthpan.sys
fffff880`01630000 fffff880`0163e000   crashdmp.sys
fffff880`0163e000 fffff880`01648000   dump_storport.sys
fffff880`01648000 fffff880`01665000   dump_LSI_SAS.sys
fffff880`01665000 fffff880`01678000   dump_dumpfve.sys
```

```text
kd> !object \driver\
Object: fffff8a000075060  Type: (fffffa8001846a30) Directory
    ObjectHeader: fffff8a000075030 (new version)
    HandleCount: 0  PointerCount: 109
    Directory Object: fffff8a000004720  Name: Driver

    Hash Address          Type                      Name
    ---- -------          ----                      ----
     00  fffffa80018841c0 Driver                    vdrvroot
         fffffa8001da93a0 Driver                    fvevol
         fffffa80024ce060 Driver                    in
     01  fffffa8001848db0 Driver                    Wdf01000
         fffffa8001e69750 Driver                    NetBT
         fffffa80020d1ac0 Driver                    usbuhci
         fffffa8002624060 Driver                    PptpMiniport
     02  fffffa8003774060 Driver                    mpsdrv
     03  fffffa8001ce9550 Driver                    amdxata
         fffffa8001db94e0 Driver                    Disk
         fffffa8001e6d950 Driver                    Psched
         fffffa8002d1d6f0 Driver                    NDProxy
         fffffa80034e1e70 Driver                    lltdio
         fffffa800192cbf0 Driver                    BthEnum
     04  fffffa800369a900 Driver                    HTTP
     06  fffffa8001d73390 Driver                    pcw
         fffffa8001e3d7f0 Driver                    vmrawdsk
         fffffa8001ea7e70 Driver                    blbdrive
         fffffa8001eab430 Driver                    tunnel
         fffffa80020d9560 Driver                    usbehci
         fffffa80018ebd70 Driver                    monitor
     07  fffffa8001be47c0 Driver                    partmgr
     08  fffffa80037f3580 Driver                    PEAUTH
         fffffa800190f290 Driver                    ACPI_HAL
     09  fffffa8001ddc420 Driver                    spldr
         fffffa8001e4f450 Driver                    RDPENCDD
         fffffa8001f09600 Driver                    E1G60
     10  fffffa8003631e70 Driver                    NPF
         fffffa8001ee76f0 Driver                    Rasl2tp
         fffffa8003558e70 Driver                    HidUsb
     11  fffffa800192aad0 Driver                    PnpManager
         fffffa8001ee5620 Driver                    DXGKrnl
     12  fffffa8001bf57c0 Driver                    vsock
         fffffa8001e1f840 Driver                    Null
         fffffa800428d9a0 Driver                    FLARE_Loaded_0
     13  fffffa80036ab5c0 Driver                    FLARE_Loaded_1
         fffffa8001be57c0 Driver                    Compbatt
         fffffa80021b5650 Driver                    RasAgileVpn
     14  fffffa8001ce9360 Driver                    CLFS
         fffffa8001ed1670 Driver                    Serenum
         fffffa80038114a0 Driver                    RFCOMM
     15  fffffa8001be67c0 Driver                    volmgr
         fffffa8001ce5360 Driver                    KSecDD
         fffffa8001e473f0 Driver                    RDPCDD
         fffffa8001e85360 Driver                    Serial
     16  fffffa80037f6580 Driver                    vmmemctl
         fffffa8001bfa7c0 Driver                    msahci
         fffffa8001cdd550 Driver                    CNG
         fffffa80026668c0 Driver                    umbus
     17  fffffa8001cf72d0 Driver                    KSecPkg
         fffffa8001e552e0 Driver                    RDPREFMP
         fffffa8001ebd560 Driver                    i8042prt
         fffffa800263a060 Driver                    msloop
         fffffa8001867080 Driver                    Win32k
     18  fffffa8001ec59d0 Driver                    mouclass
     19  fffffa8001bc9120 Driver                    msisadrv
     20  fffffa8001ebb850 Driver                    kbdclass
     21  fffffa8001db36d0 Driver                    volsnap
         fffffa800356d8a0 Driver                    mouhid
     22  fffffa8001918290 Driver                    WMIxWDM
         fffffa8001e93a60 Driver                    nsiproxy
         fffffa8001e47a40 Driver                    VgaSave
     23  fffffa8001bf37c0 Driver                    vmci
         fffffa8001e592d0 Driver                    tdx
         fffffa8001e83930 Driver                    Wanarpv6
         fffffa80026374a0 Driver                    RasSstp
         fffffa80024c9240 Driver                    BthPan
     24  fffffa8003d33350 Driver                    PROCEXP152
         fffffa8001d53e70 Driver                    BTHUSB
     25  fffffa8002317e70 Driver                    HDAudBus
         fffffa800256e840 Driver                    RasPppoe
     26  fffffa800380aa90 Driver                    secdrv
     28  fffffa8001e8ba80 Driver                    TermDD
         fffffa8003570840 Driver                    rspndr
         fffffa80035719e0 Driver                    vmusbmouse
     29  fffffa8001bd31b0 Driver                    pci
         fffffa8001bef7c0 Driver                    volmgrx
         fffffa8001e9f9c0 Driver                    mssmbios
         fffffa8002d34060 Driver                    HdAudAddService
     30  fffffa8001d774e0 Driver                    NDIS
         fffffa8001e79d90 Driver                    npcap
         fffffa8001ecbc90 Driver                    vm3dmp_loader
         fffffa8001e375a0 Driver                    cdrom
         fffffa8002129800 Driver                    CmBatt
     31  fffffa8001ea3e10 Driver                    discache
         fffffa8002664e70 Driver                    swenum
     32  fffffa8001cf54f0 Driver                    Tcpip
         fffffa8001da13b0 Driver                    rdyboost
         fffffa80020f71c0 Driver                    usbhub
     33  fffffa8001bf67c0 Driver                    atapi
         fffffa8001e3f610 Driver                    Beep
         fffffa8001e71ae0 Driver                    WfpLwf
         fffffa8002165d80 Driver                    intelppm
     34  fffffa8001bf07c0 Driver                    intelide
         fffffa8001c2c570 Driver                    mountmgr
         fffffa8001e63540 Driver                    AFD
         fffffa8002302700 Driver                    NdisTapi
         fffffa800353cd20 Driver                    usbccgp
     35  fffffa80037f7060 Driver                    tcpipreg
         fffffa8001ec7740 Driver                    vmmouse
         fffffa8002d33060 Driver                    ksthunk
     36  fffffa8001867a50 Driver                    ACPI
         fffffa8001bf87c0 Driver                    LSI_SAS
         fffffa8001db96d0 Driver                    hwpolicy
         fffffa8001e77380 Driver                    ws2ifsl
         fffffa80025a1630 Driver                    vm3dmp
         fffffa800218de70 Driver                    CompositeBus
         fffffa80025a0e70 Driver                    NdisWan
```

```text
kd> !drvobj \Driver\Null 
Driver object (fffffa8001e1f840) is for:
 \Driver\Null
Driver Extension List: (id , addr)

Device Object list:
fffffa8001e353a0  
```

```text
kd> dt nt!_EPROCESS
   +0x000 Pcb              : _KPROCESS
   +0x160 ProcessLock      : _EX_PUSH_LOCK
   +0x168 CreateTime       : _LARGE_INTEGER
   +0x170 ExitTime         : _LARGE_INTEGER
   +0x178 RundownProtect   : _EX_RUNDOWN_REF
   +0x180 UniqueProcessId  : Ptr64 Void
   +0x188 ActiveProcessLinks : _LIST_ENTRY
   +0x198 ProcessQuotaUsage : [2] Uint8B
   +0x1a8 ProcessQuotaPeak : [2] Uint8B
   +0x1b8 CommitCharge     : Uint8B
   +0x1c0 QuotaBlock       : Ptr64 _EPROCESS_QUOTA_BLOCK
   +0x1c8 CpuQuotaBlock    : Ptr64 _PS_CPU_QUOTA_BLOCK
   +0x1d0 PeakVirtualSize  : Uint8B
   +0x1d8 VirtualSize      : Uint8B
   +0x1e0 SessionProcessLinks : _LIST_ENTRY
   +0x1f0 DebugPort        : Ptr64 Void
   +0x1f8 ExceptionPortData : Ptr64 Void
   +0x1f8 ExceptionPortValue : Uint8B
   +0x1f8 ExceptionPortState : Pos 0, 3 Bits
   +0x200 ObjectTable      : Ptr64 _HANDLE_TABLE
   +0x208 Token            : _EX_FAST_REF
   +0x210 WorkingSetPage   : Uint8B
   +0x218 AddressCreationLock : _EX_PUSH_LOCK
   +0x220 RotateInProgress : Ptr64 _ETHREAD
   +0x228 ForkInProgress   : Ptr64 _ETHREAD
   +0x230 HardwareTrigger  : Uint8B
   +0x238 PhysicalVadRoot  : Ptr64 _MM_AVL_TABLE
   +0x240 CloneRoot        : Ptr64 Void
   +0x248 NumberOfPrivatePages : Uint8B
   +0x250 NumberOfLockedPages : Uint8B
   +0x258 Win32Process     : Ptr64 Void
   +0x260 Job              : Ptr64 _EJOB
   +0x268 SectionObject    : Ptr64 Void
   +0x270 SectionBaseAddress : Ptr64 Void
   +0x278 Cookie           : Uint4B
   +0x27c UmsScheduledThreads : Uint4B
   +0x280 WorkingSetWatch  : Ptr64 _PAGEFAULT_HISTORY
   +0x288 Win32WindowStation : Ptr64 Void
   +0x290 InheritedFromUniqueProcessId : Ptr64 Void
   +0x298 LdtInformation   : Ptr64 Void
   +0x2a0 Spare            : Ptr64 Void
   +0x2a8 ConsoleHostProcess : Uint8B
   +0x2b0 DeviceMap        : Ptr64 Void
   +0x2b8 EtwDataSource    : Ptr64 Void
   +0x2c0 FreeTebHint      : Ptr64 Void
   +0x2c8 FreeUmsTebHint   : Ptr64 Void
   +0x2d0 PageDirectoryPte : _HARDWARE_PTE
   +0x2d0 Filler           : Uint8B
   +0x2d8 Session          : Ptr64 Void
   +0x2e0 ImageFileName    : [15] UChar
   +0x2ef PriorityClass    : UChar
   +0x2f0 JobLinks         : _LIST_ENTRY
   +0x300 LockedPagesList  : Ptr64 Void
   +0x308 ThreadListHead   : _LIST_ENTRY
   +0x318 SecurityPort     : Ptr64 Void
   +0x320 Wow64Process     : Ptr64 Void
   +0x328 ActiveThreads    : Uint4B
   +0x32c ImagePathHash    : Uint4B
   +0x330 DefaultHardErrorProcessing : Uint4B
   +0x334 LastThreadExitStatus : Int4B
   +0x338 Peb              : Ptr64 _PEB
   +0x340 PrefetchTrace    : _EX_FAST_REF
   +0x348 ReadOperationCount : _LARGE_INTEGER
   +0x350 WriteOperationCount : _LARGE_INTEGER
   +0x358 OtherOperationCount : _LARGE_INTEGER
   +0x360 ReadTransferCount : _LARGE_INTEGER
   +0x368 WriteTransferCount : _LARGE_INTEGER
   +0x370 OtherTransferCount : _LARGE_INTEGER
   +0x378 CommitChargeLimit : Uint8B
   +0x380 CommitChargePeak : Uint8B
   +0x388 AweInfo          : Ptr64 Void
   +0x390 SeAuditProcessCreationInfo : _SE_AUDIT_PROCESS_CREATION_INFO
   +0x398 Vm               : _MMSUPPORT
   +0x420 MmProcessLinks   : _LIST_ENTRY
   +0x430 HighestUserAddress : Ptr64 Void
   +0x438 ModifiedPageCount : Uint4B
   +0x43c Flags2           : Uint4B
   +0x43c JobNotReallyActive : Pos 0, 1 Bit
   +0x43c AccountingFolded : Pos 1, 1 Bit
   +0x43c NewProcessReported : Pos 2, 1 Bit
   +0x43c ExitProcessReported : Pos 3, 1 Bit
   +0x43c ReportCommitChanges : Pos 4, 1 Bit
   +0x43c LastReportMemory : Pos 5, 1 Bit
   +0x43c ReportPhysicalPageChanges : Pos 6, 1 Bit
   +0x43c HandleTableRundown : Pos 7, 1 Bit
   +0x43c NeedsHandleRundown : Pos 8, 1 Bit
   +0x43c RefTraceEnabled  : Pos 9, 1 Bit
   +0x43c NumaAware        : Pos 10, 1 Bit
   +0x43c ProtectedProcess : Pos 11, 1 Bit
   +0x43c DefaultPagePriority : Pos 12, 3 Bits
   +0x43c PrimaryTokenFrozen : Pos 15, 1 Bit
   +0x43c ProcessVerifierTarget : Pos 16, 1 Bit
   +0x43c StackRandomizationDisabled : Pos 17, 1 Bit
   +0x43c AffinityPermanent : Pos 18, 1 Bit
   +0x43c AffinityUpdateEnable : Pos 19, 1 Bit
   +0x43c PropagateNode    : Pos 20, 1 Bit
   +0x43c ExplicitAffinity : Pos 21, 1 Bit
   +0x43c Spare1           : Pos 22, 1 Bit
   +0x43c ForceRelocateImages : Pos 23, 1 Bit
   +0x43c DisallowStrippedImages : Pos 24, 1 Bit
   +0x43c LowVaAccessible  : Pos 25, 1 Bit
   +0x440 Flags            : Uint4B
   +0x440 CreateReported   : Pos 0, 1 Bit
   +0x440 NoDebugInherit   : Pos 1, 1 Bit
   +0x440 ProcessExiting   : Pos 2, 1 Bit
   +0x440 ProcessDelete    : Pos 3, 1 Bit
   +0x440 Wow64SplitPages  : Pos 4, 1 Bit
   +0x440 VmDeleted        : Pos 5, 1 Bit
   +0x440 OutswapEnabled   : Pos 6, 1 Bit
   +0x440 Outswapped       : Pos 7, 1 Bit
   +0x440 ForkFailed       : Pos 8, 1 Bit
   +0x440 Wow64VaSpace4Gb  : Pos 9, 1 Bit
   +0x440 AddressSpaceInitialized : Pos 10, 2 Bits
   +0x440 SetTimerResolution : Pos 12, 1 Bit
   +0x440 BreakOnTermination : Pos 13, 1 Bit
   +0x440 DeprioritizeViews : Pos 14, 1 Bit
   +0x440 WriteWatch       : Pos 15, 1 Bit
   +0x440 ProcessInSession : Pos 16, 1 Bit
   +0x440 OverrideAddressSpace : Pos 17, 1 Bit
   +0x440 HasAddressSpace  : Pos 18, 1 Bit
   +0x440 LaunchPrefetched : Pos 19, 1 Bit
   +0x440 InjectInpageErrors : Pos 20, 1 Bit
   +0x440 VmTopDown        : Pos 21, 1 Bit
   +0x440 ImageNotifyDone  : Pos 22, 1 Bit
   +0x440 PdeUpdateNeeded  : Pos 23, 1 Bit
   +0x440 VdmAllowed       : Pos 24, 1 Bit
   +0x440 CrossSessionCreate : Pos 25, 1 Bit
   +0x440 ProcessInserted  : Pos 26, 1 Bit
   +0x440 DefaultIoPriority : Pos 27, 3 Bits
   +0x440 ProcessSelfDelete : Pos 30, 1 Bit
   +0x440 SetTimerResolutionLink : Pos 31, 1 Bit
   +0x444 ExitStatus       : Int4B
   +0x448 VadRoot          : _MM_AVL_TABLE
   +0x488 AlpcContext      : _ALPC_PROCESS_CONTEXT
   +0x4a8 TimerResolutionLink : _LIST_ENTRY
   +0x4b8 RequestedTimerResolution : Uint4B
   +0x4bc ActiveThreadsHighWatermark : Uint4B
   +0x4c0 SmallestTimerResolution : Uint4B
   +0x4c8 TimerResolutionStackRecord : Ptr64 _PO_DIAG_STACK_RECORD
```

```text
kd> !for_each_module
00: fffff80000bac000  fffff80000bd6000            kdcom kdbazis.dll                                                       
01: fffff80002a00000  fffff80002a49000              hal hal.dll                                                    hal.dll
02: fffff80002a49000  fffff80003030000               nt ntkrnlmp.exe                                          ntkrnlmp.exe
03: fffff88000c00000  fffff88000c19000             vmci \SystemRoot\system32\DRIVERS\vmci.sys                     vmci.sys
04: fffff88000c19000  fffff88000c30000            vsock \SystemRoot\system32\DRIVERS\vsock.sys                            
05: fffff88000c30000  fffff88000c4a000         mountmgr \SystemRoot\System32\drivers\mountmgr.sys                         
06: fffff88000c4a000  fffff88000c53000            atapi \SystemRoot\system32\drivers\atapi.sys                            
07: fffff88000c53000  fffff88000c7d000          ataport \SystemRoot\system32\drivers\ataport.SYS               ataport.SYS
08: fffff88000c7d000  fffff88000c9a000          lsi_sas \SystemRoot\system32\drivers\lsi_sas.sys               lsi_sas.sys
09: fffff88000ca2000  fffff88000cf1000  mcupdate_GenuineIntel \SystemRoot\system32\mcupdate_GenuineIntel.dll                    
0a: fffff88000cf1000  fffff88000d05000            PSHED \SystemRoot\system32\PSHED.dll                                    
0b: fffff88000d05000  fffff88000d63000             CLFS \SystemRoot\system32\CLFS.SYS                                     
0c: fffff88000d63000  fffff88000dd8000               CI \SystemRoot\system32\CI.dll                                       
0d: fffff88000dd8000  fffff88000de0000         intelide \SystemRoot\system32\drivers\intelide.sys                         
0e: fffff88000de0000  fffff88000df0000          PCIIDEX \SystemRoot\system32\drivers\PCIIDEX.SYS                          
0f: fffff88000e00000  fffff88000e15000          partmgr \SystemRoot\System32\drivers\partmgr.sys                          
10: fffff88000e15000  fffff88000e1e000         compbatt \SystemRoot\system32\DRIVERS\compbatt.sys                         
11: fffff88000e1e000  fffff88000e2a000            BATTC \SystemRoot\system32\DRIVERS\BATTC.SYS                            
12: fffff88000e2a000  fffff88000e3f000           volmgr \SystemRoot\system32\drivers\volmgr.sys                           
13: fffff88000e3f000  fffff88000e9b000          volmgrx \SystemRoot\System32\drivers\volmgrx.sys                          
14: fffff88000e9c000  fffff88000f40000         Wdf01000 \SystemRoot\system32\drivers\Wdf01000.sys                         
15: fffff88000f40000  fffff88000f4f000           WDFLDR \SystemRoot\system32\drivers\WDFLDR.SYS                           
16: fffff88000f4f000  fffff88000fa6000             ACPI \SystemRoot\system32\drivers\ACPI.sys                     ACPI.sys
17: fffff88000fa6000  fffff88000faf000           WMILIB \SystemRoot\system32\drivers\WMILIB.SYS                           
18: fffff88000faf000  fffff88000fb9000         msisadrv \SystemRoot\system32\drivers\msisadrv.sys                         
19: fffff88000fb9000  fffff88000fec000              pci \SystemRoot\system32\drivers\pci.sys                       pci.sys
1a: fffff88000fec000  fffff88000ff9000         vdrvroot \SystemRoot\system32\drivers\vdrvroot.sys                         
1b: fffff88001000000  fffff88001072000              cng \SystemRoot\System32\Drivers\cng.sys                              
1c: fffff88001072000  fffff88001094000              tdx \SystemRoot\system32\DRIVERS\tdx.sys                              
1d: fffff880010a3000  fffff88001106000         storport \SystemRoot\system32\drivers\storport.sys             storport.sys
1e: fffff88001106000  fffff88001111000           msahci \SystemRoot\system32\drivers\msahci.sys                           
1f: fffff88001111000  fffff8800111c000          amdxata \SystemRoot\system32\drivers\amdxata.sys                          
20: fffff8800111c000  fffff88001168000           fltmgr \SystemRoot\system32\drivers\fltmgr.sys                           
21: fffff88001168000  fffff8800117c000         fileinfo \SystemRoot\system32\drivers\fileinfo.sys                         
22: fffff8800117c000  fffff880011da000            msrpc \SystemRoot\System32\Drivers\msrpc.sys                            
23: fffff880011da000  fffff880011f8000             dfsc \SystemRoot\System32\Drivers\dfsc.sys                             
24: fffff88001200000  fffff8800121b000           ksecdd \SystemRoot\System32\Drivers\ksecdd.sys                           
25: fffff8800121b000  fffff8800122c000              pcw \SystemRoot\System32\drivers\pcw.sys                              
26: fffff8800122c000  fffff88001236000           Fs_Rec \SystemRoot\System32\Drivers\Fs_Rec.sys                           
27: fffff88001236000  fffff88001247000             Npfs \SystemRoot\System32\Drivers\Npfs.SYS                             
28: fffff88001247000  fffff88001254000              TDI \SystemRoot\system32\DRIVERS\TDI.SYS                              
29: fffff8800125b000  fffff880013fe000             Ntfs \SystemRoot\System32\Drivers\Ntfs.sys                             
2a: fffff88001400000  fffff88001410000         watchdog \SystemRoot\System32\drivers\watchdog.sys                         
2b: fffff88001410000  fffff88001419000           RDPCDD \SystemRoot\System32\DRIVERS\RDPCDD.sys                           
2c: fffff88001419000  fffff88001422000         rdpencdd \SystemRoot\system32\drivers\rdpencdd.sys                         
2d: fffff88001422000  fffff8800142b000         rdprefmp \SystemRoot\system32\drivers\rdprefmp.sys                         
2e: fffff88001431000  fffff88001524000             ndis \SystemRoot\system32\drivers\ndis.sys                     ndis.sys
2f: fffff88001524000  fffff88001584000            NETIO \SystemRoot\system32\drivers\NETIO.SYS                            
30: fffff88001584000  fffff880015b0000          ksecpkg \SystemRoot\System32\Drivers\ksecpkg.sys                          
31: fffff880015b0000  fffff880015bf000         vmrawdsk \SystemRoot\system32\DRIVERS\vmrawdsk.sys                         
32: fffff880015bf000  fffff880015cd000              vga \SystemRoot\System32\drivers\vga.sys                              
33: fffff880015cd000  fffff880015f2000         VIDEOPRT \SystemRoot\System32\drivers\VIDEOPRT.SYS                         
34: fffff880015f2000  fffff880015fd000             Msfs \SystemRoot\System32\Drivers\Msfs.SYS                             
35: fffff88001600000  fffff88001630000         CLASSPNP \SystemRoot\system32\drivers\CLASSPNP.SYS                         
36: fffff88001630000  fffff8800164d000          usbccgp \SystemRoot\system32\DRIVERS\usbccgp.sys                          
37: fffff8800164d000  fffff88001666000         HIDCLASS \SystemRoot\system32\DRIVERS\HIDCLASS.SYS                         
38: fffff88001678000  fffff880016a2000            cdrom \SystemRoot\system32\DRIVERS\cdrom.sys                            
39: fffff880016a2000  fffff880016a9000             Beep \SystemRoot\System32\Drivers\Beep.SYS                             
3a: fffff880016aa000  fffff880018ae000            tcpip \SystemRoot\System32\drivers\tcpip.sys                            
3b: fffff880018ae000  fffff880018f8000         fwpkclnt \SystemRoot\System32\drivers\fwpkclnt.sys                         
3c: fffff880018f8000  fffff88001944000          volsnap \SystemRoot\system32\drivers\volsnap.sys                          
3d: fffff88001944000  fffff8800194c000            spldr \SystemRoot\System32\Drivers\spldr.sys                            
3e: fffff8800194c000  fffff88001986000         rdyboost \SystemRoot\System32\drivers\rdyboost.sys                         
3f: fffff88001986000  fffff88001998000              mup \SystemRoot\System32\Drivers\mup.sys                              
40: fffff88001998000  fffff880019a1000         hwpolicy \SystemRoot\System32\drivers\hwpolicy.sys                         
41: fffff880019a1000  fffff880019db000           fvevol \SystemRoot\System32\DRIVERS\fvevol.sys                           
42: fffff880019db000  fffff880019f1000             disk \SystemRoot\system32\drivers\disk.sys                             
43: fffff880019f1000  fffff880019fa000             Null \SystemRoot\System32\Drivers\Null.SYS                     Null.SYS
44: fffff88002600000  fffff8800262d000           mrxsmb \SystemRoot\system32\DRIVERS\mrxsmb.sys                           
45: fffff8800262d000  fffff8800267a000         mrxsmb10 \SystemRoot\system32\DRIVERS\mrxsmb10.sys                         
46: fffff8800267a000  fffff8800269e000         mrxsmb20 \SystemRoot\system32\DRIVERS\mrxsmb20.sys                         
47: fffff880026a7000  fffff880026bc000           lltdio \SystemRoot\system32\DRIVERS\lltdio.sys                           
48: fffff880026bc000  fffff880026c9000           mouhid \SystemRoot\system32\DRIVERS\mouhid.sys                           
49: fffff880026c9000  fffff880026e1000           rspndr \SystemRoot\system32\DRIVERS\rspndr.sys                           
4a: fffff880026e1000  fffff880026ea000       vmusbmouse \SystemRoot\system32\DRIVERS\vmusbmouse.sys                       
4b: fffff880026ea000  fffff880027b3000             HTTP \SystemRoot\system32\drivers\HTTP.sys                             
4c: fffff880027b3000  fffff880027d1000           bowser \SystemRoot\system32\DRIVERS\bowser.sys                           
4d: fffff880027d1000  fffff880027e9000           mpsdrv \SystemRoot\System32\drivers\mpsdrv.sys                           
4e: fffff88003200000  fffff8800328c000          bthport \SystemRoot\System32\Drivers\bthport.sys                          
4f: fffff8800328c000  fffff880032b8000           rfcomm \SystemRoot\system32\DRIVERS\rfcomm.sys                           
50: fffff880032b8000  fffff880032c8000          BthEnum \SystemRoot\system32\DRIVERS\BthEnum.sys                          
51: fffff880032c8000  fffff880032e8000           bthpan \SystemRoot\system32\DRIVERS\bthpan.sys                           
52: fffff880032f1000  fffff880032fb000         vmmemctl \SystemRoot\system32\DRIVERS\vmmemctl.sys                         
53: fffff880032fb000  fffff88003307000              npf \SystemRoot\system32\drivers\npf.sys                              
54: fffff88003307000  fffff880033b1000           peauth \SystemRoot\system32\drivers\peauth.sys                           
55: fffff880033b1000  fffff880033bc000           secdrv \SystemRoot\System32\Drivers\secdrv.SYS                           
56: fffff880033bc000  fffff880033cb000              man \??\C:\Users\FLARE ON 2019\Desktop\man.sys                 man.sys
57: fffff880033dc000  fffff880033f4000           BTHUSB \SystemRoot\System32\Drivers\BTHUSB.sys                           
58: fffff88003600000  fffff88003651000            rdbss \SystemRoot\system32\DRIVERS\rdbss.sys                            
59: fffff88003651000  fffff8800365d000         nsiproxy \SystemRoot\system32\drivers\nsiproxy.sys                         
5a: fffff8800365d000  fffff880036e6000              afd \SystemRoot\system32\drivers\afd.sys                              
5b: fffff880036e6000  fffff8800372b000            netbt \SystemRoot\System32\DRIVERS\netbt.sys                            
5c: fffff8800372b000  fffff88003736000          ws2ifsl \SystemRoot\system32\drivers\ws2ifsl.sys                          
5d: fffff88003736000  fffff8800373f000           wfplwf \SystemRoot\system32\DRIVERS\wfplwf.sys                           
5e: fffff8800373f000  fffff88003765000            pacer \SystemRoot\system32\DRIVERS\pacer.sys                            
5f: fffff88003765000  fffff88003779000            npcap \SystemRoot\system32\DRIVERS\npcap.sys                            
60: fffff88003779000  fffff88003788000          netbios \SystemRoot\system32\DRIVERS\netbios.sys                          
61: fffff88003788000  fffff880037a5000           serial \SystemRoot\system32\DRIVERS\serial.sys                 serial.sys
62: fffff880037a5000  fffff880037c0000           wanarp \SystemRoot\system32\DRIVERS\wanarp.sys                           
63: fffff880037c0000  fffff880037d4000           termdd \SystemRoot\system32\DRIVERS\termdd.sys                           
64: fffff880037d4000  fffff880037df000         mssmbios \SystemRoot\system32\DRIVERS\mssmbios.sys             mssmbios.sys
65: fffff880037df000  fffff880037ee000         discache \SystemRoot\System32\drivers\discache.sys                         
66: fffff880037ee000  fffff880037ff000         blbdrive \SystemRoot\system32\DRIVERS\blbdrive.sys                         
67: fffff88003a0c000  fffff88003a32000           tunnel \SystemRoot\system32\DRIVERS\tunnel.sys                           
68: fffff88003a32000  fffff88003a50000         i8042prt \SystemRoot\system32\DRIVERS\i8042prt.sys             i8042prt.sys
69: fffff88003a50000  fffff88003a5f000         kbdclass \SystemRoot\system32\DRIVERS\kbdclass.sys                         
6a: fffff88003a5f000  fffff88003a68000          vmmouse \SystemRoot\system32\DRIVERS\vmmouse.sys                          
6b: fffff88003a68000  fffff88003a77000         mouclass \SystemRoot\system32\DRIVERS\mouclass.sys                         
6c: fffff88003a77000  fffff88003a83000          serenum \SystemRoot\system32\DRIVERS\serenum.sys                          
6d: fffff88003a83000  fffff88003a8d000    vm3dmp_loader \SystemRoot\system32\DRIVERS\vm3dmp_loader.sys                    
6e: fffff88003a8d000  fffff88003ace000           vm3dmp \SystemRoot\system32\DRIVERS\vm3dmp.sys                           
6f: fffff88003ace000  fffff88003bc2000          dxgkrnl \SystemRoot\System32\drivers\dxgkrnl.sys               dxgkrnl.sys
70: fffff88003bc2000  fffff88003bdc000          rassstp \SystemRoot\system32\DRIVERS\rassstp.sys                          
71: fffff88003bdc000  fffff88003bff000            luafv \SystemRoot\system32\drivers\luafv.sys                            
72: fffff88003c00000  fffff88003c2f000          ndiswan \SystemRoot\system32\DRIVERS\ndiswan.sys                          
73: fffff88003c2f000  fffff88003c4a000         raspppoe \SystemRoot\system32\DRIVERS\raspppoe.sys                         
74: fffff88003c4a000  fffff88003c6b000          raspptp \SystemRoot\system32\DRIVERS\raspptp.sys                          
75: fffff88003c6b000  fffff88003c72000             loop \SystemRoot\system32\DRIVERS\loop.sys                             
76: fffff88003c72000  fffff88003c73480           swenum \SystemRoot\system32\DRIVERS\swenum.sys                           
77: fffff88003c7c000  fffff88003cc2000          dxgmms1 \SystemRoot\System32\drivers\dxgmms1.sys                          
78: fffff88003cc2000  fffff88003ccf000          usbuhci \SystemRoot\system32\DRIVERS\usbuhci.sys                          
79: fffff88003ccf000  fffff88003d25000          USBPORT \SystemRoot\system32\DRIVERS\USBPORT.SYS               USBPORT.SYS
7a: fffff88003d25000  fffff88003d48980         E1G6032E \SystemRoot\system32\DRIVERS\E1G6032E.sys             E1G6032E.sys
7b: fffff88003d49000  fffff88003d6d000         HDAudBus \SystemRoot\system32\DRIVERS\HDAudBus.sys             HDAudBus.sys
7c: fffff88003d6d000  fffff88003d7e000          usbehci \SystemRoot\system32\DRIVERS\usbehci.sys                          
7d: fffff88003d7e000  fffff88003d82500           CmBatt \SystemRoot\system32\DRIVERS\CmBatt.sys                           
7e: fffff88003d83000  fffff88003d99000         intelppm \SystemRoot\system32\DRIVERS\intelppm.sys                         
7f: fffff88003d99000  fffff88003da9000     CompositeBus \SystemRoot\system32\DRIVERS\CompositeBus.sys                     
80: fffff88003da9000  fffff88003dbf000         AgileVpn \SystemRoot\system32\DRIVERS\AgileVpn.sys                         
81: fffff88003dbf000  fffff88003de3000          rasl2tp \SystemRoot\system32\DRIVERS\rasl2tp.sys                          
82: fffff88003de3000  fffff88003def000         ndistapi \SystemRoot\system32\DRIVERS\ndistapi.sys                         
83: fffff88003def000  fffff88003df7080         HIDPARSE \SystemRoot\system32\DRIVERS\HIDPARSE.SYS                         
84: fffff88003e00000  fffff88003e3d000          portcls \SystemRoot\system32\drivers\portcls.sys                          
85: fffff88003e3d000  fffff88003e5f000             drmk \SystemRoot\system32\drivers\drmk.sys                             
86: fffff88003e5f000  fffff88003e64200          ksthunk \SystemRoot\system32\drivers\ksthunk.sys                          
87: fffff88003e65000  fffff88003e73000         crashdmp \SystemRoot\System32\Drivers\crashdmp.sys                         
88: fffff88003e73000  fffff88003e7d000    dump_diskdump \SystemRoot\System32\Drivers\dump_diskdump.sys                    
89: fffff88003e7d000  fffff88003e9a000     dump_LSI_SAS \SystemRoot\System32\Drivers\dump_LSI_SAS.sys                     
8a: fffff88003e9a000  fffff88003ead000     dump_dumpfve \SystemRoot\System32\Drivers\dump_dumpfve.sys                     
8b: fffff88003ead000  fffff88003eb9000            Dxapi \SystemRoot\System32\drivers\Dxapi.sys                            
8c: fffff88003eb9000  fffff88003ec7000          monitor \SystemRoot\system32\DRIVERS\monitor.sys                          
8d: fffff88003ec7000  fffff88003ec8f00             USBD \SystemRoot\system32\DRIVERS\USBD.SYS                             
8e: fffff88003ec9000  fffff88003ed7000           hidusb \SystemRoot\system32\DRIVERS\hidusb.sys                           
8f: fffff88003edb000  fffff88003f1e000               ks \SystemRoot\system32\DRIVERS\ks.sys                               
90: fffff88003f1e000  fffff88003f30000            umbus \SystemRoot\system32\DRIVERS\umbus.sys                            
91: fffff88003f30000  fffff88003f8a000           usbhub \SystemRoot\system32\DRIVERS\usbhub.sys                           
92: fffff88003f8a000  fffff88003f9f000          NDProxy \SystemRoot\System32\Drivers\NDProxy.SYS                          
93: fffff88003f9f000  fffff88003ffb000          HdAudio \SystemRoot\system32\drivers\HdAudio.sys                          
94: fffff88004200000  fffff8800420c000       PROCEXP152 \??\C:\Windows\system32\Drivers\PROCEXP152.SYS                    
95: fffff88004217000  fffff88004248000           srvnet \SystemRoot\System32\DRIVERS\srvnet.sys                           
96: fffff88004248000  fffff8800425a000         tcpipreg \SystemRoot\System32\drivers\tcpipreg.sys                         
97: fffff8800425a000  fffff880042c5000             srv2 \SystemRoot\System32\DRIVERS\srv2.sys                             
98: fffff880042c5000  fffff8800435e000              srv \SystemRoot\System32\DRIVERS\srv.sys                              
99: fffff8800435e000  fffff88004389000           vmhgfs \SystemRoot\system32\DRIVERS\vmhgfs.sys                           
9a: fffff88004389000  fffff880043fa000            spsys \SystemRoot\system32\drivers\spsys.sys                            
9b: fffff960000e0000  fffff960003f0000           win32k \SystemRoot\System32\win32k.sys                         win32k.sys
9c: fffff96000570000  fffff9600057a000            TSDDD \SystemRoot\System32\TSDDD.dll                                    
9d: fffff96000610000  fffff96000637000              cdd \SystemRoot\System32\cdd.dll     
```