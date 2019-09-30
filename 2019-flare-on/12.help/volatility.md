```text
λ volatility_2.6_win64_standalone.exe -f help.dmp --profile=Win7SP1x64 crashinfo
Volatility Foundation Volatility Framework 2.6
_DMP_HEADER64:
 Majorversion:         0x0000000f (15)
 Minorversion:         0x00001db1 (7601)
 KdSecondaryVersion    0x00000002
 DirectoryTableBase    0x00187000
 PfnDataBase           0xfffff80002cf7278
 PsLoadedModuleList    0xfffff80002c8d890
 PsActiveProcessHead   0xfffff80002c6f590
 MachineImageType      0x00008664
 NumberProcessors      0x00000001
 BugCheckCode          0x0000007e
 KdDebuggerDataBlock   0xfffff80002c390a0
 ProductType           0x00000001
 SuiteMask             0x00000310
 WriterStatus          0x80000000
 Comment               PAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGEPAGE
 DumpType              Full Dump
 SystemTime            2019-08-02 14:38:33 UTC+0000
 SystemUpTime          0:49:18.389777

Physical Memory Description:
Number of runs: 3
FileOffset    Start Address    Length
00002000      00001000         0009e000
000a0000      00100000         7fde0000
7fe80000      7ff00000         00100000
7ff7f000      7ffff000
```

```text
λ volatility_2.6_win64_standalone.exe -f help.dmp --profile=Win7SP1x64 modscan
Volatility Foundation Volatility Framework 2.6
Offset(P)          Name                 Base                             Size File
------------------ -------------------- ------------------ ------------------ ----
0x000000007d48ff30 man.sys              0xfffff880033bc000             0xf000 \??\C:\Users\FLARE ON 2019\Desktop\man.sys
0x000000007d693040 BthEnum.sys          0xfffff880032b8000            0x10000 \SystemRoot\system32\DRIVERS\BthEnum.sys
0x000000007d987380 bthport.sys          0xfffff88003200000            0x8c000 \SystemRoot\System32\Drivers\bthport.sys
0x000000007de1e2c0 srvnet.sys           0xfffff88004217000            0x31000 \SystemRoot\System32\DRIVERS\srvnet.sys
0x000000007de28f20 tcpipreg.sys         0xfffff88004248000            0x12000 \SystemRoot\System32\drivers\tcpipreg.sys
0x000000007de892c0 srv.sys              0xfffff880042c5000            0x99000 \SystemRoot\System32\DRIVERS\srv.sys
0x000000007de91160 srv2.sys             0xfffff8800425a000            0x6b000 \SystemRoot\System32\DRIVERS\srv2.sys
0x000000007dfc4630 bthpan.sys           0xfffff880032c8000            0x20000 \SystemRoot\system32\DRIVERS\bthpan.sys
0x000000007e07a760 vmmemctl.sys         0xfffff880032f1000             0xa000 \SystemRoot\system32\DRIVERS\vmmemctl.sys
0x000000007e08fbe0 HTTP.sys             0xfffff880026ea000            0xc9000 \SystemRoot\system32\drivers\HTTP.sys
0x000000007e0a6bd0 BTHUSB.sys           0xfffff88003220000            0x18000 ??嚙遴１?鵂蕞??鴥謍?000????000D??嚙選蕭鵂蕞鼤唾廎?e
0x000000007e171b40 bowser.sys           0xfffff880027b3000            0x1e000 \SystemRoot\system32\DRIVERS\bowser.sys
0x000000007e1748a0 mpsdrv.sys           0xfffff880027d1000            0x18000 \SystemRoot\System32\drivers\mpsdrv.sys
0x000000007e17fc50 mrxsmb.sys           0xfffff88002600000            0x2d000 \SystemRoot\system32\DRIVERS\mrxsmb.sys
0x000000007e184c60 mrxsmb10.sys         0xfffff8800262d000            0x4d000 \SystemRoot\system32\DRIVERS\mrxsmb10.sys
0x000000007e188e90 mrxsmb20.sys         0xfffff8800267a000            0x24000 \SystemRoot\system32\DRIVERS\mrxsmb20.sys
0x000000007e1a8f30 vmhgfs.sys           0xfffff8800435e000            0x2b000 \SystemRoot\system32\DRIVERS\vmhgfs.sys
0x000000007e1fa5c0 peauth.sys           0xfffff88003307000            0xaa000 \SystemRoot\system32\drivers\peauth.sys
0x000000007e1fa6f0 secdrv.SYS           0xfffff880033b1000             0xb000 \SystemRoot\System32\Drivers\secdrv.SYS
0x000000007e219c30 luafv.sys            0xfffff88003bdc000            0x23000 \SystemRoot\system32\drivers\luafv.sys
0x000000007e33cb50 usbccgp.sys          0xfffff88001630000            0x1d000 \SystemRoot\system32\DRIVERS\usbccgp.sys
0x000000007e33ff30 USBD.SYS             0xfffff88003ec7000             0x2000 \SystemRoot\system32\DRIVERS\USBD.SYS
0x000000007e340440 lltdio.sys           0xfffff880026a7000            0x15000 \SystemRoot\system32\DRIVERS\lltdio.sys
0x000000007e35ad40 HIDCLASS.SYS         0xfffff8800164d000            0x19000 \SystemRoot\system32\DRIVERS\HIDCLASS.SYS
0x000000007e35ee10 hidusb.sys           0xfffff88003ec9000             0xe000 \SystemRoot\system32\DRIVERS\hidusb.sys
0x000000007e360e90 HIDPARSE.SYS         0xfffff88003def000             0x9000 \SystemRoot\system32\DRIVERS\HIDPARSE.SYS
0x000000007e36dc00 mouhid.sys           0xfffff880026bc000             0xd000 \SystemRoot\system32\DRIVERS\mouhid.sys
0x000000007e370ba0 rspndr.sys           0xfffff880026c9000            0x18000 \SystemRoot\system32\DRIVERS\rspndr.sys
0x000000007e371d40 vmusbmouse.sys       0xfffff880026e1000             0x9000 \SystemRoot\system32\DRIVERS\vmusbmouse.sys
0x000000007e616b70 TSDDD.dll            0xfffff96000570000             0xa000 \SystemRoot\System32\TSDDD.dll
0x000000007e641ed0 cdd.dll              0xfffff96000610000            0x27000 \SystemRoot\System32\cdd.dll
0x000000007e648f20 PROCEXP152.SYS       0xfffff88004200000             0xc000 \??\C:\Windows\system32\Drivers\PROCEXP152.SYS
0x000000007e80e5c0 npf.sys              0xfffff880032fb000             0xc000 \SystemRoot\system32\drivers\npf.sys
0x000000007eab1220 NDProxy.SYS          0xfffff88003f8a000            0x15000 \SystemRoot\System32\Drivers\NDProxy.SYS
0x000000007eac8220 HdAudio.sys          0xfffff88003f9f000            0x5c000 \SystemRoot\system32\drivers\HdAudio.sys
0x000000007eb28660 drmk.sys             0xfffff88003e3d000            0x22000 \SystemRoot\system32\drivers\drmk.sys
0x000000007eb28d10 portcls.sys          0xfffff88003e00000            0x3d000 \SystemRoot\system32\drivers\portcls.sys
0x000000007eb336e0 ksthunk.sys          0xfffff88003e5f000             0x6000 \SystemRoot\system32\drivers\ksthunk.sys
0x000000007eb45a60 Dxapi.sys            0xfffff88003ead000             0xc000 \SystemRoot\System32\drivers\Dxapi.sys
0x000000007eb69890 dump_dumpfve.sys     0xfffff88003e9a000            0x13000 \SystemRoot\System32\Drivers\dump_dumpfve.sys
0x000000007f01a1a0 raspptp.sys          0xfffff88003c4a000            0x21000 \SystemRoot\system32\DRIVERS\raspptp.sys
0x000000007f0372e0 rassstp.sys          0xfffff88003bc2000            0x1a000 \SystemRoot\system32\DRIVERS\rassstp.sys
0x000000007f0405a0 loop.sys             0xfffff88003c6b000             0x7000 \SystemRoot\system32\DRIVERS\loop.sys
0x000000007f0447c0 swenum.sys           0xfffff88003c72000             0x2000 \SystemRoot\system32\DRIVERS\swenum.sys
0x000000007f060500 ks.sys               0xfffff88003edb000            0x43000 \SystemRoot\system32\DRIVERS\ks.sys
0x000000007f066a60 umbus.sys            0xfffff88003f1e000            0x12000 \SystemRoot\system32\DRIVERS\umbus.sys
0x000000007f0f7d00 usbhub.sys           0xfffff88003f30000            0x5a000 \SystemRoot\system32\DRIVERS\usbhub.sys
0x000000007f206290 BTHUSB.sys           0xfffff880033dc000            0x18000 \SystemRoot\System32\Drivers\BTHUSB.sys
0x000000007f367970 spsys.sys            0xfffff88004389000            0x71000 \SystemRoot\system32\drivers\spsys.sys
0x000000007f36e070 ndiswan.sys          0xfffff88003c00000            0x2f000 \SystemRoot\system32\DRIVERS\ndiswan.sys
0x000000007f3a1070 mouclass.sys         0xfffff88003a68000             0xf000 \SystemRoot\system32\DRIVERS\mouclass.sys
0x000000007f3b8700 usbuhci.sys          0xfffff88003cc2000             0xd000 \SystemRoot\system32\DRIVERS\usbuhci.sys
0x000000007f502970 ndistapi.sys         0xfffff88003de3000             0xc000 \SystemRoot\system32\DRIVERS\ndistapi.sys
0x000000007f50bd50 raspppoe.sys         0xfffff88003c2f000            0x1b000 \SystemRoot\system32\DRIVERS\raspppoe.sys
0x000000007f57b6f0 win32k.sys           0xfffff960000e0000           0x310000 \SystemRoot\System32\win32k.sys
0x000000007f57dc00 dump_storport.sys    0xfffff88003e73000             0xa000 \SystemRoot\System32\Drivers\dump_diskdump.sys
0x000000007f5b3010 dump_LSI_SAS.sys     0xfffff88003e7d000            0x1d000 \SystemRoot\System32\Drivers\dump_LSI_SAS.sys
0x000000007f646c90 rfcomm.sys           0xfffff8800328c000            0x2c000 \SystemRoot\system32\DRIVERS\rfcomm.sys
0x000000007f6c9230 USBPORT.SYS          0xfffff88003ccf000            0x56000 \SystemRoot\system32\DRIVERS\USBPORT.SYS
0x000000007f6d9700 usbehci.sys          0xfffff88003d6d000            0x11000 \SystemRoot\system32\DRIVERS\usbehci.sys
0x000000007f7299a0 CmBatt.sys           0xfffff88003d7e000             0x5000 \SystemRoot\system32\DRIVERS\CmBatt.sys
0x000000007f765f20 intelppm.sys         0xfffff88003d83000            0x16000 \SystemRoot\system32\DRIVERS\intelppm.sys
0x000000007f783110 CompositeBus.sys     0xfffff88003d99000            0x10000 \SystemRoot\system32\DRIVERS\CompositeBus.sys
0x000000007f7a1540 rasl2tp.sys          0xfffff88003dbf000            0x24000 \SystemRoot\system32\DRIVERS\rasl2tp.sys
0x000000007f7ab110 AgileVpn.sys         0xfffff88003da9000            0x16000 \SystemRoot\system32\DRIVERS\AgileVpn.sys
0x000000007f831770 HDAudBus.sys         0xfffff88003d49000            0x24000 \SystemRoot\system32\DRIVERS\HDAudBus.sys
0x000000007f83d6b0 watchdog.sys         0xfffff88001400000            0x10000 \SystemRoot\System32\drivers\watchdog.sys
0x000000007f83f7b0 Beep.SYS             0xfffff880016a2000             0x7000 \SystemRoot\System32\Drivers\Beep.SYS
0x000000007f83fca0 Null.SYS             0xfffff880019f1000             0x9000 \SystemRoot\System32\Drivers\Null.SYS
0x000000007f841640 vmrawdsk.sys         0xfffff880015b0000             0xf000 \SystemRoot\system32\DRIVERS\vmrawdsk.sys
0x000000007f8438a0 RDPCDD.sys           0xfffff88001410000             0x9000 \SystemRoot\System32\DRIVERS\RDPCDD.sys
0x000000007f845610 vga.sys              0xfffff880015bf000             0xe000 \SystemRoot\System32\drivers\vga.sys
0x000000007f8478e0 VIDEOPRT.SYS         0xfffff880015cd000            0x25000 \SystemRoot\System32\drivers\VIDEOPRT.SYS
0x000000007f849330 rdprefmp.sys         0xfffff88001422000             0x9000 \SystemRoot\system32\drivers\rdprefmp.sys
0x000000007f84f5f0 rdpencdd.sys         0xfffff88001419000             0x9000 \SystemRoot\system32\drivers\rdpencdd.sys
0x000000007f851a40 Msfs.SYS             0xfffff880015f2000             0xb000 \SystemRoot\System32\Drivers\Msfs.SYS
0x000000007f8532f0 Npfs.SYS             0xfffff88001236000            0x11000 \SystemRoot\System32\Drivers\Npfs.SYS
0x000000007f857a90 TDI.SYS              0xfffff88001247000             0xd000 \SystemRoot\system32\DRIVERS\TDI.SYS
0x000000007f8597c0 tdx.sys              0xfffff88001072000            0x22000 \SystemRoot\system32\DRIVERS\tdx.sys
0x000000007f861390 afd.sys              0xfffff8800365d000            0x89000 \SystemRoot\system32\drivers\afd.sys
0x000000007f869950 netbt.sys            0xfffff880036e6000            0x45000 \SystemRoot\System32\DRIVERS\netbt.sys
0x000000007f869c70 ws2ifsl.sys          0xfffff8800372b000             0xb000 \SystemRoot\system32\drivers\ws2ifsl.sys
0x000000007f86daf0 pacer.sys            0xfffff8800373f000            0x26000 \SystemRoot\system32\DRIVERS\pacer.sys
0x000000007f86f8e0 netbios.sys          0xfffff88003779000             0xf000 \SystemRoot\system32\DRIVERS\netbios.sys
0x000000007f871ce0 wfplwf.sys           0xfffff88003736000             0x9000 \SystemRoot\system32\DRIVERS\wfplwf.sys
0x000000007f879f30 npcap.sys            0xfffff88003765000            0x14000 \SystemRoot\system32\DRIVERS\npcap.sys
0x000000007f883b20 termdd.sys           0xfffff880037c0000            0x14000 \SystemRoot\system32\DRIVERS\termdd.sys
0x000000007f885500 serial.sys           0xfffff88003788000            0x1d000 \SystemRoot\system32\DRIVERS\serial.sys
0x000000007f885600 wanarp.sys           0xfffff880037a5000            0x1b000 \SystemRoot\system32\DRIVERS\wanarp.sys
0x000000007f893830 rdbss.sys            0xfffff88003600000            0x51000 \SystemRoot\system32\DRIVERS\rdbss.sys
0x000000007f893c60 mssmbios.sys         0xfffff880037d4000             0xb000 \SystemRoot\system32\DRIVERS\mssmbios.sys
0x000000007f89d280 nsiproxy.sys         0xfffff88003651000             0xc000 \SystemRoot\system32\drivers\nsiproxy.sys
0x000000007f8a1290 discache.sys         0xfffff880037df000             0xf000 \SystemRoot\System32\drivers\discache.sys
0x000000007f8a3510 dfsc.sys             0xfffff880011da000            0x1e000 \SystemRoot\System32\Drivers\dfsc.sys
0x000000007f8a54b0 blbdrive.sys         0xfffff880037ee000            0x11000 \SystemRoot\system32\DRIVERS\blbdrive.sys
0x000000007f8a9510 tunnel.sys           0xfffff88003a0c000            0x26000 \SystemRoot\system32\DRIVERS\tunnel.sys
0x000000007f8bd700 i8042prt.sys         0xfffff88003a32000            0x1e000 \SystemRoot\system32\DRIVERS\i8042prt.sys
0x000000007f8c5550 vmmouse.sys          0xfffff88003a5f000             0x9000 \SystemRoot\system32\DRIVERS\vmmouse.sys
0x000000007f8c9ac0 kbdclass.sys         0xfffff88003a50000             0xf000 \SystemRoot\system32\DRIVERS\kbdclass.sys
0x000000007f8d18e0 serenum.sys          0xfffff88003a77000             0xc000 \SystemRoot\system32\DRIVERS\serenum.sys
0x000000007f8d7320 vm3dmp_loader.sys    0xfffff88003a83000             0xa000 \SystemRoot\system32\DRIVERS\vm3dmp_loader.sys
0x000000007f8d78b0 vm3dmp.sys           0xfffff88003a8d000            0x41000 \SystemRoot\system32\DRIVERS\vm3dmp.sys
0x000000007f8dd2a0 crashdmp.sys         0xfffff88003e65000             0xe000 \SystemRoot\System32\Drivers\crashdmp.sys
0x000000007f8f32c0 dxgmms1.sys          0xfffff88003c7c000            0x46000 \SystemRoot\System32\drivers\dxgmms1.sys
0x000000007f8f3c00 dxgkrnl.sys          0xfffff88003ace000            0xf4000 \SystemRoot\System32\drivers\dxgkrnl.sys
0x000000007f9097a0 E1G6032E.sys         0xfffff88003d25000            0x24000 \SystemRoot\system32\DRIVERS\E1G6032E.sys
0x000000007ff15150 monitor.sys          0xfffff88003eb9000             0xe000 \SystemRoot\system32\DRIVERS\monitor.sys
0x000000007ff85f30 cdrom.sys            0xfffff88001678000            0x2a000 \SystemRoot\system32\DRIVERS\cdrom.sys
0x000000007fff7080 intelide.sys         0xfffff88000dd8000             0x8000 \SystemRoot\system32\drivers\intelide.sys
0x000000007fff7170 volmgrx.sys          0xfffff88000e3f000            0x5c000 \SystemRoot\System32\drivers\volmgrx.sys
0x000000007fff7260 volmgr.sys           0xfffff88000e2a000            0x15000 \SystemRoot\system32\drivers\volmgr.sys
0x000000007fff7340 BATTC.SYS            0xfffff88000e1e000             0xc000 \SystemRoot\system32\DRIVERS\BATTC.SYS
0x000000007fff7420 compbatt.sys         0xfffff88000e15000             0x9000 \SystemRoot\system32\DRIVERS\compbatt.sys
0x000000007fff7510 partmgr.sys          0xfffff88000e00000            0x15000 \SystemRoot\System32\drivers\partmgr.sys
0x000000007fff7600 vdrvroot.sys         0xfffff88000fec000             0xd000 \SystemRoot\system32\drivers\vdrvroot.sys
0x000000007fff76f0 pci.sys              0xfffff88000fb9000            0x33000 \SystemRoot\system32\drivers\pci.sys
0x000000007fff77d0 msisadrv.sys         0xfffff88000faf000             0xa000 \SystemRoot\system32\drivers\msisadrv.sys
0x000000007fff78c0 WMILIB.SYS           0xfffff88000fa6000             0x9000 \SystemRoot\system32\drivers\WMILIB.SYS
0x000000007fff79a0 ACPI.sys             0xfffff88000f4f000            0x57000 \SystemRoot\system32\drivers\ACPI.sys
0x000000007fff7a90 WDFLDR.SYS           0xfffff88000f40000             0xf000 \SystemRoot\system32\drivers\WDFLDR.SYS
0x000000007fff7b70 Wdf01000.sys         0xfffff88000e9c000            0xa4000 \SystemRoot\system32\drivers\Wdf01000.sys
0x000000007fff7c70 CI.dll               0xfffff88000d63000            0x75000 \SystemRoot\system32\CI.dll
0x000000007fff7d50 CLFS.SYS             0xfffff88000d05000            0x5e000 \SystemRoot\system32\CLFS.SYS
0x000000007fff7e40 PSHED.dll            0xfffff88000cf1000            0x14000 \SystemRoot\system32\PSHED.dll
0x000000007fff7f20 mcupdate.dll         0xfffff88000ca2000            0x4f000 \SystemRoot\system32\mcupdate_GenuineIntel.dll
0x000000007fffd6c0 kdcom.dll            0xfffff80000bac000            0x2a000 \SystemRoot\system32\kdcom.dll
0x000000007fffd7a0 hal.dll              0xfffff80002a00000            0x49000 \SystemRoot\system32\hal.dll
0x000000007fffd890 ntoskrnl.exe         0xfffff80002a49000           0x5e7000 \SystemRoot\system32\ntoskrnl.exe
0x000000007fffe010 PCIIDEX.SYS          0xfffff88000de0000            0x10000 \SystemRoot\system32\drivers\PCIIDEX.SYS
0x000000007fffe150 pcw.sys              0xfffff8800121b000            0x11000 \SystemRoot\System32\drivers\pcw.sys
0x000000007fffe230 cng.sys              0xfffff88001000000            0x72000 \SystemRoot\System32\Drivers\cng.sys
0x000000007fffe310 \SystemRo...ecdd.sys 0x0000000000000000          0x1200000
0x000000007fffe320 ksecdd.sys           0xfffff88001200000            0x1b000 \SystemRoot\System32\Drivers\ksecdd.sys
0x000000007fffe400 msrpc.sys            0xfffff8800117c000            0x5e000 \SystemRoot\System32\Drivers\msrpc.sys
0x000000007fffe4f0 Ntfs.sys             0xfffff8800125b000           0x1a3000 \SystemRoot\System32\Drivers\Ntfs.sys
0x000000007fffe600 fileinfo.sys         0xfffff88001168000            0x14000 \SystemRoot\system32\drivers\fileinfo.sys
0x000000007fffe6f0 fltmgr.sys           0xfffff8800111c000            0x4c000 \SystemRoot\system32\drivers\fltmgr.sys
0x000000007fffe7e0 amdxata.sys          0xfffff88001111000             0xb000 \SystemRoot\system32\drivers\amdxata.sys
0x000000007fffe8c0 \SystemRo...ahci.sys 0x0000000000000000          0x1106000
0x000000007fffe8d0 msahci.sys           0xfffff88001106000             0xb000 \SystemRoot\system32\drivers\msahci.sys
0x000000007fffe9b0 storport.sys         0xfffff880010a3000            0x63000 \SystemRoot\system32\drivers\storport.sys
0x000000007fffeaa0 lsi_sas.sys          0xfffff88000c7d000            0x1d000 \SystemRoot\system32\drivers\lsi_sas.sys
0x000000007fffeb90 ataport.SYS          0xfffff88000c53000            0x2a000 \SystemRoot\system32\drivers\ataport.SYS
0x000000007fffec70 \SystemRo...tapi.sys 0x0000000000000000           0xc4a000
0x000000007fffec80 atapi.sys            0xfffff88000c4a000             0x9000 \SystemRoot\system32\drivers\atapi.sys
0x000000007fffed60 mountmgr.sys         0xfffff88000c30000            0x1a000 \SystemRoot\System32\drivers\mountmgr.sys
0x000000007fffee40 \SystemRo...sock.sys 0x0000000000000000           0xc19000
0x000000007fffee50 vsock.sys            0xfffff88000c19000            0x17000 \SystemRoot\system32\DRIVERS\vsock.sys
0x000000007fffef30 vmci.sys             0xfffff88000c00000            0x19000 \SystemRoot\system32\DRIVERS\vmci.sys
0x000000007ffff010 Fs_Rec.sys           0xfffff8800122c000             0xa000 \SystemRoot\System32\Drivers\Fs_Rec.sys
0x000000007ffff3e0 CLASSPNP.SYS         0xfffff88001600000            0x30000 \SystemRoot\system32\drivers\CLASSPNP.SYS
0x000000007ffff4d0 disk.sys             0xfffff880019db000            0x16000 \SystemRoot\system32\drivers\disk.sys
0x000000007ffff5b0 fvevol.sys           0xfffff880019a1000            0x3a000 \SystemRoot\System32\DRIVERS\fvevol.sys
0x000000007ffff690 hwpolicy.sys         0xfffff88001998000             0x9000 \SystemRoot\System32\drivers\hwpolicy.sys
0x000000007ffff780 mup.sys              0xfffff88001986000            0x12000 \SystemRoot\System32\Drivers\mup.sys
0x000000007ffff860 rdyboost.sys         0xfffff8800194c000            0x3a000 \SystemRoot\System32\drivers\rdyboost.sys
0x000000007ffff950 spldr.sys            0xfffff88001944000             0x8000 \SystemRoot\System32\Drivers\spldr.sys
0x000000007ffffa30 volsnap.sys          0xfffff880018f8000            0x4c000 \SystemRoot\system32\drivers\volsnap.sys
0x000000007ffffb20 fwpkclnt.sys         0xfffff880018ae000            0x4a000 \SystemRoot\System32\drivers\fwpkclnt.sys
0x000000007ffffc10 tcpip.sys            0xfffff880016aa000           0x204000 \SystemRoot\System32\drivers\tcpip.sys
0x000000007ffffd30 ksecpkg.sys          0xfffff88001584000            0x2c000 \SystemRoot\System32\Drivers\ksecpkg.sys
0x000000007ffffe20 NETIO.SYS            0xfffff88001524000            0x60000 \SystemRoot\system32\drivers\NETIO.SYS
0x000000007fffff10 ndis.sys             0xfffff88001431000            0xf3000 \SystemRoot\system32\drivers\ndis.sys
```