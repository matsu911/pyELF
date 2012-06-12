from define import *

class Elf64_Ehdr(Structure):
    EI_NIDENT = 16
    _fields_ = [
        ('e_ident', c_ubyte * EI_NIDENT), # Magic number and other info
        ('e_type',      Elf64_Half),      # Object file type
        ('e_machine',   Elf64_Half),      # Architecture
        ('e_version',   Elf64_Word),      # Object file version
        ('e_entry',     Elf64_Addr),      # Entry point virtual address
        ('e_phoff',     Elf64_Addr),      # Program header table file offset
        ('e_shoff',     Elf64_Addr),      # Section header table file offset
        ('e_flags',     Elf64_Word),      # Processor-specific flags
        ('e_ehsize',    Elf64_Half),      # ELF header size in bytes
        ('e_phentsize', Elf64_Half),      # Program header table entry size
        ('e_phnum',     Elf64_Half),      # Program header table entry count
        ('e_shentsize', Elf64_Half),      # Section header table entry size
        ('e_shnum',     Elf64_Half),      # Section header table entry count
        ('e_shstrndx',  Elf64_Half)       # Section header string table index
        ]

class Elf64_Shdr(Structure):
    _fields_ = [
        ('sh_name',      Elf64_Word),  # Section name (string tbl index)
        ('sh_type',      Elf64_Word),  # Section type
        ('sh_flags',     Elf64_Xword), # Section flags
        ('sh_addr',      Elf64_Addr),  # Section virtual addr at execution
        ('sh_offset',    Elf64_Off),   # Section file offset
        ('sh_size',      Elf64_Xword), # Section size in bytes
        ('sh_link',      Elf64_Word),  # Link to another section
        ('sh_info',      Elf64_Word),  # Additional section information
        ('sh_addralign', Elf64_Xword), # Section alignment
        ('sh_entsize',   Elf64_Xword)  # Entry size if section holds table
        ]

class Elf64_Sym(Structure):
    _fields_ = [
        ('st_name',  Elf64_Word),    # Symbol name (string tbl index)
        ('st_info',  c_ubyte),       # Symbol type and binding
        ('st_other', c_ubyte),       # Symbol visibility
        ('st_shndx', Elf64_Section), # Section index
        ('st_value', Elf64_Addr),    # Symbol value
        ('st_size',  Elf64_Xword),   # Symbol size
        ]
