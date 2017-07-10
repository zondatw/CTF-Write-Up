#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

int myindex(char *table, char v)
{
	int i = 0;
	for (i = 0; i < strlen(table); i++)
	{
		if (table[i] == v)
			return i;
	}
	return 0xff;
}

void find_flag(char *check, char *table)
{
	int i = 0;
	for (i = 0; i < strlen(check); i++)
	{
		int idx = myindex(table, check[i] & 0x000000ff);
		printf("%c", idx);
		if (idx == '}')
		{
			printf("\n");
			break;
		}
	}
	exit(0);
}


int ror(unsigned char value, int shift)
{
   return (value >> shift) | (value << (8 - shift)) % 256;
}

void make_table(char first)
{
	unsigned int v1; // eax@1
	int v2; // edx@4
	char v3; // al@5
	char v4; // ST1B_1@7
	char v5; // al@8
	int v6; // eax@10
	int v7; // ecx@10
	int v8; // eax@10
	int v9; // ecx@10
	int v10; // eax@10
	int v11; // ecx@10
	int v12; // eax@10
	int v13; // ecx@10
	char result; // eax@10
	char index; // [sp+1Ah] [bp-Eh]@3
	char v16; // [sp+1Bh] [bp-Dh]@3
	char v17; // [sp+1Bh] [bp-Dh]@7
	int rand_nu; // [sp+1Ch] [bp-Ch]@2
	char table_ptr[256]; 

	*table_ptr = first;
	index = 1;
	v16 = 1;
	do
	{
		v2 = index ^ 2 * index;
		if ( index >= 0 )
		  v3 = 0;
		else
		  v3 = 0x1B;
		index = (v2 ^ v3);
		v4 = 4 * (2 * v16 ^ v16) ^ 2 * v16 ^ v16;
		v17 = 16 * v4 ^ v4;
		if ( v17 >= 0 )
		  v5 = 0;
		else
		  v5 = 9;
		v16 = v17 ^ v5;
		v6 = *table_ptr;
		(v6) = v16 ^ v6;
		v7 = v16;
		(v7) =  ror(v16, 7);
		v8 = v7 ^ v6;
		v9 = v16;
		(v9) = ror(v16, 6);
		v10 = v9 ^ v8;
		v11 = v16;
		(v11) =  ror(v16, 5);
		v12 = v11 ^ v10;
		v13 = v16;
		(v13) = ror(v16, 4);
		result = v13 ^ v12;
		table_ptr[index & 0x000000ff] = result;
	}while ( index != 1 );
	

	//=====check=====
	int i;
	char check[] = {0x95, 0xee, 0xaf, 0x95, 0xef, 0x94, 0x23, 0x49, 0x99, 
					0x58, 0x2f, 0x72, 0x2f, 0x49, 0x2f, 0x72, 0xb1, 0x9a, 
					0x7a, 0xaf, 0x72, 0xe6, 0xe7, 0x76, 0xb5, 0x7a, 0xee, 
					0x72, 0x2f, 0xe7, 0x7a, 0xb5, 0xad, 0x9a, 0xae, 0xb1, 
					0x56, 0x72, 0x96, 0x76, 0xae, 0x7a, 0x23, 0x6d, 0x99, 
					0xb1, 0xdf, 0x4a};

	char c_index[] = "TWCTF{";
	int c = 1;
	for (i = 0; i < strlen(c_index); i++)
	{
		int t = c_index[i];
		if ((check[i] & 0x000000ff) != (table_ptr[t] & 0x000000ff))
			c = 0;
	}
	if (c)
	{
		printf ("find table:<%02x>\n", table_ptr[i] & 0x000000ff);
		find_flag(check, table_ptr);	
		exit(0);
	}
}

int main()
{
	int i = 0;
	for ( i = 0; i < 256; i++)
	{
		make_table(i);
	}
	return 0;
}
