from ctypes import *

# Legal values for ST_BIND subfield of st_info (symbol binding)
STB_LOCAL  = 0          # Local symbol
STB_GLOBAL = 1          # Global symbol
STB_WEAK   = 2          # Weak symbol
STB_NUM    = 3          # Number of defined types
STB_LOOS   = 10         # Start of OS-specific
STB_HIOS   = 12         # End of OS-specific
STB_LOPROC = 13         # Start of processor-specific
STB_HIPROC = 15         # End of processor-specific

# Legal values for ST_TYPE subfield of st_info (symbol type)
STT_NOTYPE  = 0         # Symbol type is unspecified
STT_OBJECT  = 1         # Symbol is a data object
STT_FUNC    = 2         # Symbol is a code object
STT_SECTION = 3         # Symbol associated with a section
STT_FILE    = 4         # Symbol's name is file name
STT_COMMON  = 5         # Symbol is a common data object
STT_TLS     = 6         # Symbol is thread-local data object
STT_NUM     = 7         # Number of defined types. 
STT_LOOS    = 10        # Start of OS-specific
STT_HIOS    = 12        # End of OS-specific
STT_LOPROC  = 13        # Start of processor-specific
STT_HIPROC  = 15        # End of processor-specific

# Type for a 16-bit quantity
Elf32_Half = c_uint16
Elf64_Half = c_uint16

# Types for signed and unsigned 32-bit quantities
Elf32_Word  = c_uint32
Elf32_Sword = c_int32  
Elf64_Word  = c_uint32 
Elf64_Sword = c_int32  

# Types for signed and unsigned 64-bit quantities
Elf32_Xword  = c_uint64 
Elf32_Sxword = c_int64  
Elf64_Xword  = c_uint64 
Elf64_Sxword = c_int64  

# Type of addresses
Elf32_Addr = c_uint32
Elf64_Addr = c_uint64

# Type of file offsets
Elf32_Off = c_uint32
Elf64_Off = c_uint64

# Type for section indices, which are 16-bit quantities
Elf32_Section = c_uint16
Elf64_Section = c_uint16

# Type for version symbol information
Elf32_Versym = Elf32_Half
Elf64_Versym = Elf64_Half
