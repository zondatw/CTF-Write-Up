void FUN_0040106b(void)

{
  undefined4 uVar1;
  int iVar2;
  int iVar1;
  undefined4 *first_string;
  undefined4 *second_string;
  undefined4 *first_string_buf_ptr;
  undefined4 *second_string_buf_ptr;
  undefined4 local_140;
  int local_13c [4];
  undefined4 first_string_buf [26];
  undefined4 second_string_buf [26];
  undefined4 local_5c;
  undefined4 local_58;
  undefined4 local_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined4 local_48;
  undefined4 local_44;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c;
  undefined4 local_28;
  undefined4 local_24;
  undefined local_20;
  undefined4 local_1c;
  undefined4 local_18;
  undefined4 local_14;
  undefined4 local_10;
  undefined4 local_c;
  uint local_8;
  
  local_8 = DAT_00413004 ^ (uint)&stack0xfffffffc;
  iVar2 = 0x19;
  local_5c = 0x2c332323;
  local_58 = 0x49643f0e;
  first_string = (undefined4 *)
                                  
                 "nPTnaGLkIqdcQwvieFQKGcTGOTbfMjDNmvibfBDdFBhoPaBbtfQuuGWYomtqTFqvBSKdUMmciqKSGZaosWCSoZlcIlyQpOwkcAgw "
  ;
  first_string_buf_ptr = first_string_buf;
  while (iVar2 != 0
                    /* copy first_string to first_string_buf */) {
    iVar2 = iVar2 + -1;
    *first_string_buf_ptr = *first_string;
    first_string = first_string + 1;
    first_string_buf_ptr = first_string_buf_ptr + 1;
  }
  iVar1 = 0x19;
  local_54 = 0x40a1e0a;
  *(undefined2 *)first_string_buf_ptr = *(undefined2 *)first_string;
  local_50 = 0x1a021623;
  local_4c = 0x24086644;
  second_string =
       (undefined4 *)
              
       "KglPFOsQDxBPXmclOpmsdLDEPMRWbMDzwhDGOyqAkVMRvnBeIkpZIhFznwVylfjrkqprBPAdPuaiVoVugQAlyOQQtxBNsTdPZgDH "
  ;
  second_string_buf_ptr = second_string_buf;
  while (iVar1 != 0) {
    iVar1 = iVar1 + -1;
    *second_string_buf_ptr = *second_string;
    second_string = second_string + 1;
    second_string_buf_ptr = second_string_buf_ptr + 1;
  }
  local_48 = 0x2c741132;
  local_44 = 0xf422d2a;
  local_40 = 0xd64503e;
  local_3c = 0x171b045d;
  local_38 = 0x5033616;
  local_34 = 0x8092034;
  local_30 = 0xe242163;
  local_2c = 0x58341415;
  local_28 = 0x3a79291a;
  local_24 = 0x58560000;
  local_20 = 0x54;
  local_1c = 0x3b020e38;
  local_18 = 0x341b3b19;
  local_14 = 0x3e230c1b;
  local_10 = 0x42110833;
  local_c = 0x731e1239;
  *(undefined2 *)second_string_buf_ptr = *(undefined2 *)second_string;
  FUN_00401000(local_13c,(int)&local_1c,0x14,(int)second_string_buf);
                    /* CreateFile
                       dwDesiredAccess 0x40000000 (GENERIC_WRITE), dwShareMode
                       0x2(FILE_SHARE_WRITE), lpSecurityAttributes 0x0, dwCreationDisposition
                       0x2(CREATE_ALWAYS), dwFlagsAndAttributes 0x80(FILE_ATTRIBUTE_NORMAL),
                       hTemplateFile 0x0 */
  iVar1 = (*(code *)(undefined *)0x12418)(local_13c[0],0x40000000,2,0,2,0x80,0);
  FUN_00401045(local_13c);
  if (iVar1 != -1) {
    local_140 = 0;
    FUN_00401000(local_13c,(int)&local_5c,0x3d,(int)first_string_buf);
                    /* WriteFile */
    (*(code *)(undefined *)0x123f8)(iVar1,local_13c[0],0x3d,&local_140,0);
    FUN_00401045(local_13c);
                    /* CloseHandle */
    (*(code *)(undefined *)0x12426)(iVar1);
    FUN_00401000(local_13c,(int)&local_1c,0x14,(int)second_string_buf);
                    /* ShellExecuteA  */
    (*(code *)(undefined *)0x12442)(0,0,local_13c[0],0,0,0);
    FUN_00401045(local_13c);
  }
                    /* GetCurrentProcess */
  uVar1 = (*(code *)(undefined *)0x123e4)(0xffffffff);
                    /* TerminateProcess */
  (*(code *)(undefined *)0x12404)(uVar1);
  FUN_0040121b();
  return;
}