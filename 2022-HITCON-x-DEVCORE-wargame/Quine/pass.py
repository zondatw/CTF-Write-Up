import sys
import string
from base64 import b64decode
import subprocess

a = """
                                                                                                                              789cc559
                                                                                                                             5d8f9b46
                                                                                                                            14fd2b53
                                                                                                                           47cdc2ee
                                                                                                                          2ce5ce37
                                                                                                                         72c853a
                                                                                                                        5be2552
                                                                                                                       14a50f9
                                                                                                                      61f6c83
                                                                                                                    37ce3a66
                                                                                                                   0576b68
                                                                                                                  9fae37b                   073b2                               e388a
                     ca7418d9d2189873e19                     e03d6bdc743d3347933c5       91d4e5d                 376b12a              a3d5c73ae22ca6cdb                   e8ee2f8072893313d                    85c43d00d2f339453                 e13d250a118159ae3d054
                     72a0321354a5290e4995e25                4e98c2a835ba3a9963814e       050d430                1c42532            381666068c618cd32984f0             b20398988cd52c47736a9503                 1d9acc9b6dc45c7d938c              f8926e5b6292fc28e5b13
                     df46fabe137e793af92527a67              b3e59573529c86647668a         6b4339               03fc36           8267d4f094e      29665144           03249456615      73c5903f672              2a302d25450ce954190db7            0a98d165432211505ae25e
                    51a50b            514068fb5            3054a61                        2ef1c5e            0dafca6           4a6f93c9             e6e            3e3f55f5              9e3487e5             535dad          caa699a           eebea3
                    3592e9              a5209724           2974a1                         4e5aa2a           ca73f85          78cdb2e1                             e723279                  31b9657            016fab           54916f           5c397f
                    8153be                93c4dcc          f00e2f                          f3f6d9          8af8964          fd779f5                              84f193                    e443b29           ad0c9f           372124f          d7c973
                   bdd997                 d1395bf         4fb4f7e                          38b10d5        e6daba6           8ce28b                              4bddd4                      37f6a7           b32810         290a7ca4           ebf335
                   a2ef4f                 c9c4745         7feb58f0a884f41db4d83            87853d9       a15b37            47e0773                             7b2a2a9                      ca5bf5           a6176379e1f61e8c2f003c            cba30ebc338dd2a483e5
                  59b5d9b                 f01b4eb         5fcd728206d153cdfe0f              4e95eb      42167a             9ff579                              007638                       47917e          64e822090200fc6088b2e             2c9c04b140823c18232cb
                  bb0741                  2c4030         9f2608cb0eac2ca49900               824c88    331c2ba              0b6b27                              413290                      200fc60          89b2e6c9c04a94082                 3c18239c75e1cc49900e
                  24c883                 b12dfab         d3606a                             9932413  4892176               71bd06                              f65e02                     42a0bd5           5efd58     db805e                 430337
                 d700c16               c831f6d1          bd0eb6                              be0681  e42b90                74fda36                             a0d7dec                   0cd4340           2813e1       49db06               f4ba1c
                 b85909              08e5253c6          9db805                               eb3033   747                  01a12c85                2            76d1bd0                 eb79e06            62c209       4b3f0a4              6d037a
                 ad0fdc           fc05843218            9eb46d                               40afff8 19b                    cd80503ec           393b6f          d3fd6eb80            cccd6b402            8b3e149        fb72258            0b9b90d
                086537fc585f2e073037b3c1fe              cb6c3ce6e9f4f12eff7741                29a90fbb6                       8f2b05a91768183dc5724f942           5ebe24c96fb8fd9bec179b2db9              df11c0          fd07bc1           9e40321af49f26d4249f3b1
                dc6ef3f7f5a1a4cdbea80ef                bfc4db52b717e5f9475dd1e                d8c59e                           fda1deb5ab533fcd0b57c                acbae94975f29afb8525e7                9a5bce           a4a79f5          95f29a2be5cdae55370616a
                cd1f30e2c58a3e71d5                     8b046cf3bb0608d9e7760c1                1a3def                              c082357ade81056                      bf4bc030bd6e879                    0716a             cd1f30e         2c58a3fb8db0f5ca9a4462




                                                             dff91d3f7fbe 7bfb    e68f d3fe8b89  7d07f8f83a3d      bef7b391  ff002e3d366e      """
D = """I2R    lZmluZ    S8qKi9cCkQoT yxvKWNoYXIqX
                                                             ApxPU8jTyIsI iNvI    lwKK SIsKnAsc  3Nbbzt9CiNpb      mNsdWRlL  yp4eAp4Ki88c      3RkaW8uaD4Ka   W50KGkpP   TAsaj0wCixyP TEyMCxzPTEyM
                                                             AotMTIsbj0wL HgsL    yoKL   S1ER    VZDT                1JFI    S0tC              iove          j0wMDAwMDA  wMAo         7O0Q
                                                                 oIiN     kZWZpbiIKImU   vKio    vXFxEKE8iCiI        sbyl    jaGFyKlxcIgo      icT1PI09cIix cIiI    KIiN vXCJcXClcIiw iCiIqcCxzc1t
                                                                 vO30     jIgoiaW5jbHV   kZS8    qeCIKInh4Ki8        8c3R    kaW8iCiIuaD5      pbnQoaSk9Igo iMCxqPTAscj0 xMiIKIjAscz0 xMjAtMTIiCiI
                                                                 sbj0     wLHg    sLyo   tIgo           iLURF        VkNP           UkUhL             SIKIi 0qL3o9MDAwMD AiCi         IwMD
                                                                 A7O0     QoIi    wxKw o5OSs5MD  ArOTAwMF0KOz      tpbnQobW  FpbikoaW50KC      hmdFB2bwopKS xjaG    FyKi ooKE         N6cHpMeXEpKS
                                                                 l7Cm     Zvci    hzdH J1Y3R7Y2  hhciooTzApOz      sKY2hhci  hvMCk7O3Vuc2      lnbmVkKG8pOw p9Tz    17c3 MsMC         wwfTsqcT8nXy



                                                             c6J18nCj    8rTy    5vMD 8nXyc6J18nPy tpP08ubz0KK0      8ub14qTy5PM  CsrP    DwrO CxPL    m8mP        QoweGZmZ   mYsaS0tLE8ub   zA9
                                                             Kzg6J18n    Cj9w    dXRz KHNzKSxPLm8t MCswLTArMDAK      IT0oK3opPys  wOnB    yaW5 0Zigi   Ly8l       IgoiMTBzIi  wiViIpLGk6J1   8nJ
                                                               jA6       J18n    Cjon Xyc7         KnE/bjwyNz9q      PCty    JiY  qcT8    KKnE 9PSszM  j8qc      SsrOjc/c3Nba SsrX           Qo9
                                                               ajx       zP2o    rKyw rMzI6J18nP2o     rPSs          xCiwqcSsr    Oidf    Jzon Xyc6J18nP24r      Kyw  Kc  i09 MSsoK24lNCE9   MCk
                                                               scz       1yLT    EyLA pzc1tpKytdPT     EwLG          o9MCxuPT0    yNz9    4Cj1 yLTEzLHM9K3g      rLT  Yw  Oid fJzonXycKOid   fJz
                                                               9qP   HI  mJipxPypxPT0        zMj8q     cQor          Kzpq  PnMm   Jmo8cysxMXx8 aj54  P3NzCl      tpK  yt  dPS pxKy
                                                               ssaisrOi  dfJz9zc1sKaS srXT0rMzIsai     srOi          dfJz   onXy  c/bgorKyxyLT 0xKy   huJTQ      hPT  Ap  LHg tPTErCihuJTQ   hPT
                                                               ApLHMrPS  huJTM9PSswKS wKc3NbaSsrXT     0xMC          xqPT    A6J1 8nOidfJwo6Ty 5vMD    9PLm      89T      y5v JjB4ODAwMD8K   Ty5

                                     vPDwxXjB4MTAyMTpPLm88PAoxLE8ubyY9MHhmZmZmLCtPCi5vMC0tOidfJykp"""

s = """print(f"a={b+q+b};D={b+D+b};s={b+sss+b};import_zlib;q=a;a=zlib.decompress(bytes.fromhex(a.replace(chr(10),str()).rep
                                     lace(chr(32),str())));exec(a);exec(s)#{flag}#")"""


flag = "#"*21 if len(sys.argv) < 2 else sys.argv[1]

# DEVCORE{Peek!G0t_Y0U}
base_flag = "DEVCORE{"

# string.printable
bf_simple = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ "

for index in range(len(base_flag) - 2, 19):
    print(f"> {index}: {base_flag}")
    for i in bf_simple:
        flag = base_flag + i
        print(flag)
        sss = s
        s = s.replace(chr(32), str())
        s = s.replace(chr(95), chr(32)).replace(chr(10), str())
        d = [458, 462, 473, 477, 531, 594, 600, 605, 663, 679,
             683, 687, 757, 761, 766, 826, 847, 851, 918, 922, 991]
        d1 = (str(d)+chr(46) if len(str(d)) == 7 else str(d)+chr(46)+chr(48)*(7-len(str(d))) if len(str(d)) != 8 else str(d)
              for d in [6378, 32178, 8439, 830, 43929, 11525, 49462, 36226, 3249, 41004, 33685, 43830, 57874, 52456, 1375, 37161, 5486, 1748, 50558, 52529, 25973])

        d1 = (str(d)+chr(46) if len(str(d)) == 7 else str(d)+chr(46)+chr(48)*(7-len(str(d))) if len(str(d)) != 8 else str(d)
              for d in [6378, 32178, 8439, 830, 43929, 11525, 49462, 36226, 3249, 41004, 33685, 43830, 57874, 52456, 1375, 37161, 5486, 1748, 50558, 52529, 25973])

        b = chr(34)*3
        f = open(".V.c", "wb")
        f.write(b64decode(D.replace(chr(32), str())))
        f.close()
        f = open(".V.c", 'r').read()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[0]+1] = flag[0 % len(flag)]
        dd[d[1]+1] = flag[1 % len(flag)]
        dd[d[2]+1] = flag[2 % len(flag)]
        dd = str().join(dd)
        z = open(f".V0.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[1]+1] = flag[1 % len(flag)]
        dd[d[2]+1] = flag[2 % len(flag)]
        dd[d[3]+1] = flag[3 % len(flag)]
        dd = str().join(dd)
        z = open(f".V1.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[2]+1] = flag[2 % len(flag)]
        dd[d[3]+1] = flag[3 % len(flag)]
        dd[d[4]+1] = flag[4 % len(flag)]
        dd = str().join(dd)
        z = open(f".V2.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[3]+1] = flag[3 % len(flag)]
        dd[d[4]+1] = flag[4 % len(flag)]
        dd[d[5]+1] = flag[5 % len(flag)]
        dd = str().join(dd)
        z = open(f".V3.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[4]+1] = flag[4 % len(flag)]
        dd[d[5]+1] = flag[5 % len(flag)]
        dd[d[6]+1] = flag[6 % len(flag)]
        dd = str().join(dd)
        z = open(f".V4.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[5]+1] = flag[5 % len(flag)]
        dd[d[6]+1] = flag[6 % len(flag)]
        dd[d[7]+1] = flag[7 % len(flag)]
        dd = str().join(dd)
        z = open(f".V5.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[6]+1] = flag[6 % len(flag)]
        dd[d[7]+1] = flag[7 % len(flag)]
        dd[d[8]+1] = flag[8 % len(flag)]
        dd = str().join(dd)
        z = open(f".V6.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[7]+1] = flag[7 % len(flag)]
        dd[d[8]+1] = flag[8 % len(flag)]
        dd[d[9]+1] = flag[9 % len(flag)]
        dd = str().join(dd)
        z = open(f".V7.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[8]+1] = flag[8 % len(flag)]
        dd[d[9]+1] = flag[9 % len(flag)]
        dd[d[10]+1] = flag[10 % len(flag)]
        dd = str().join(dd)
        z = open(f".V8.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[9]+1] = flag[9 % len(flag)]
        dd[d[10]+1] = flag[10 % len(flag)]
        dd[d[11]+1] = flag[11 % len(flag)]
        dd = str().join(dd)
        z = open(f".V9.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[10]+1] = flag[10 % len(flag)]
        dd[d[11]+1] = flag[11 % len(flag)]
        dd[d[12]+1] = flag[12 % len(flag)]
        dd = str().join(dd)
        z = open(f".V10.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[11]+1] = flag[11 % len(flag)]
        dd[d[12]+1] = flag[12 % len(flag)]
        dd[d[13]+1] = flag[13 % len(flag)]
        dd = str().join(dd)
        z = open(f".V11.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[12]+1] = flag[12 % len(flag)]
        dd[d[13]+1] = flag[13 % len(flag)]
        dd[d[14]+1] = flag[14 % len(flag)]
        dd = str().join(dd)
        z = open(f".V12.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[13]+1] = flag[13 % len(flag)]
        dd[d[14]+1] = flag[14 % len(flag)]
        dd[d[15]+1] = flag[15 % len(flag)]
        dd = str().join(dd)
        z = open(f".V13.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[14]+1] = flag[14 % len(flag)]
        dd[d[15]+1] = flag[15 % len(flag)]
        dd[d[16]+1] = flag[16 % len(flag)]
        dd = str().join(dd)
        z = open(f".V14.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[15]+1] = flag[15 % len(flag)]
        dd[d[16]+1] = flag[16 % len(flag)]
        dd[d[17]+1] = flag[17 % len(flag)]
        dd = str().join(dd)
        z = open(f".V15.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[16]+1] = flag[16 % len(flag)]
        dd[d[17]+1] = flag[17 % len(flag)]
        dd[d[18]+1] = flag[18 % len(flag)]
        dd = str().join(dd)
        z = open(f".V16.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[17]+1] = flag[17 % len(flag)]
        dd[d[18]+1] = flag[18 % len(flag)]
        dd[d[19]+1] = flag[19 % len(flag)]
        dd = str().join(dd)
        z = open(f".V17.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[18]+1] = flag[18 % len(flag)]
        dd[d[19]+1] = flag[19 % len(flag)]
        dd[d[20]+1] = flag[20 % len(flag)]
        dd = str().join(dd)
        z = open(f".V18.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[19]+1] = flag[19 % len(flag)]
        dd[d[20]+1] = flag[20 % len(flag)]
        dd[d[0]+1] = flag[21 % len(flag)]
        dd = str().join(dd)
        z = open(f".V19.c", 'w')
        z.write(dd)
        z.close()
        dd = f.replace((chr(48)*8), next(d1))
        dd = list(dd)
        dd[d[20]+1] = flag[20 % len(flag)]
        dd[d[0]+1] = flag[21 % len(flag)]
        dd[d[1]+1] = flag[22 % len(flag)]
        dd = str().join(dd)
        z = open(f".V20.c", 'w')
        z.write(dd)
        z.close()
        k = 0
        k += subprocess.run("gcc .V0.c -o .v && ./.v | tail -n 1 | grep V  > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("0")
            continue
        elif index == 0:
            base_flag = flag
            break
        k += subprocess.run("gcc .V1.c -o .v && ./.v | tail -n 1 | grep V  > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("1")
            continue
        elif index == 1:
            base_flag = flag
            break
        k += subprocess.run("gcc .V2.c -o .v && ./.v | tail -n 1 | grep V  > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("2")
            continue
        elif index == 2:
            base_flag = flag
            break
        k += subprocess.run("gcc .V3.c -o .v && ./.v | tail -n 1 | grep V  > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("3")
            continue
        elif index == 3:
            base_flag = flag
            break
        k += subprocess.run("gcc .V4.c -o .v && ./.v | tail -n 1 | grep V  > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("4")
            continue
        elif index == 4:
            base_flag = flag
            break
        k += subprocess.run("gcc .V5.c -o .v && ./.v | tail -n 1 | grep V  > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("5")
            continue
        elif index == 5:
            base_flag = flag
            break
        k += subprocess.run("gcc .V6.c -o .v && ./.v | tail -n 1 | grep V  > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            continue
        elif index == 6:
            base_flag = flag
            break
        k += subprocess.run("gcc .V7.c -o .v && ./.v | tail -n 1 | grep V  > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("7")
            continue
        elif index == 7:
            base_flag = flag
            break
        k += subprocess.run("gcc .V8.c -o .v && ./.v | tail -n 1 | grep V  > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("8")
            continue
        elif index == 8:
            base_flag = flag
            break
        k += subprocess.run("gcc .V9.c -o .v && ./.v | tail -n 1 | grep V  > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("9")
            continue
        elif index == 9:
            base_flag = flag
            break
        k += subprocess.run("gcc .V10.c -o .v && ./.v | tail -n 1 | grep V > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("10")
            continue
        elif index == 10:
            base_flag = flag
            break
        k += subprocess.run("gcc .V11.c -o .v && ./.v | tail -n 1 | grep V > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("11")
            continue
        elif index == 11:
            base_flag = flag
            break
        k += subprocess.run("gcc .V12.c -o .v && ./.v | tail -n 1 | grep V > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("12")
            continue
        elif index == 12:
            base_flag = flag
            break
        k += subprocess.run("gcc .V13.c -o .v && ./.v | tail -n 1 | grep V > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("13")
            continue
        elif index == 13:
            base_flag = flag
            break
        k += subprocess.run("gcc .V14.c -o .v && ./.v | tail -n 1 | grep V > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("14")
            continue
        elif index == 14:
            base_flag = flag
            break
        k += subprocess.run("gcc .V15.c -o .v && ./.v | tail -n 1 | grep V > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("15")
            continue
        elif index == 15:
            base_flag = flag
            break
        k += subprocess.run("gcc .V16.c -o .v && ./.v | tail -n 1 | grep V > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("16")
            continue
        elif index == 16:
            base_flag = flag
            break
        k += subprocess.run("gcc .V17.c -o .v && ./.v | tail -n 1 | grep V > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("17")
            continue
        elif index == 17:
            base_flag = flag
            break
        k += subprocess.run("gcc .V18.c -o .v && ./.v | tail -n 1 | grep V > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("18")
            continue
        elif index == 18:
            base_flag = flag
            break
        k += subprocess.run("gcc .V19.c -o .v && ./.v | tail -n 1 | grep V > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("19")
            continue
        elif index == 19:
            base_flag = flag
            break
        k += subprocess.run("gcc .V20.c -o .v && ./.v | tail -n 1 | grep V > .z",
                            shell=True, stdout=None, stderr=None).returncode
        if (k != 0):
            print("20")
            continue
        elif index == 20:
            base_flag = flag
            break
print(f"flag: {base_flag}")
