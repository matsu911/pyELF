from define import *
from struct import *

def get_section_headers(bin_path):
    content            = open(bin_path, "rb").read()
    header             = cast(content, POINTER(Elf64_Ehdr)).contents
    offset             = header.e_shoff
    header_size        = header.e_shentsize
    name_header_offset = offset + header.e_shstrndx * header_size
    name_header        = cast(addressof(header) + name_header_offset, POINTER(Elf64_Shdr)).contents
    names              = addressof(header) + name_header.sh_offset

    return [(string_at(names + h.sh_name), h) for h in
            [cast(addressof(header) + offset + (header_size * i), POINTER(Elf64_Shdr)).contents for i in range(0, header.e_shnum)]]

def get_symbol_names(bin_path, filter_func=None):
    content  = open(bin_path, "rb").read()
    header   = cast(content, POINTER(Elf64_Ehdr)).contents

    section_headers = get_section_headers(bin_path)
    tmp = filter(lambda (name, header): name == ".dynstr", section_headers)
    if not tmp: raise ".dynsym section is not found"
    dynstr = tmp[0][1]
    tmp = filter(lambda (name, header): name == ".dynsym", section_headers)
    if not tmp: raise ".dynstr section is not found"
    dynsym = tmp[0][1]
    if not filter(lambda (name, header): name == ".text", section_headers): raise ".text section is not found"

    symbol_section_offset = dynsym.sh_offset
    symbol_entry_size     = dynsym.sh_entsize
    name_section_offset   = dynstr.sh_offset
    n_entries             = dynsym.sh_size / symbol_entry_size if symbol_entry_size > 0 else 0

    ret = []
    for i in range(0, n_entries): 
        offset               = symbol_section_offset + i * symbol_entry_size
        symbol               = cast(addressof(header) + offset, POINTER(Elf64_Sym)).contents
        name_index           = symbol.st_name
        info                 = symbol.st_info
        section_header_index = symbol.st_shndx
        name                 = string_at(addressof(header) + name_section_offset + name_index)
        if not filter_func or (filter_func(info) and section_headers[section_header_index][0] != ".text"):
            ret.append(name)
    return ret
