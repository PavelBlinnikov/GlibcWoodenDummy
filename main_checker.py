import os

v23 = ['./glibc_2.23/fastbin_dup_into_stack', './glibc_2.23/fastbin_dup_consolidate', './glibc_2.23/unsafe_unlink', './glibc_2.23/house_of_spirit', './glibc_2.23/poison_null_byte', './glibc_2.23/house_of_lore', './glibc_2.23/overlapping_chunks', './glibc_2.23/overlapping_chunks_2', './glibc_2.23/house_of_force', './glibc_2.23/large_bin_attack', './glibc_2.23/unsorted_bin_attack', './glibc_2.23/unsorted_bin_into_stack', './glibc_2.23/house_of_einherjar', './glibc_2.23/house_of_orange', './glibc_2.23/mmap_overlapping_chunks', './glibc_2.23/fastbin_dup', './glibc_2.23/house_of_roman']
v27 = ['./glibc_2.27/unsafe_unlink', './glibc_2.27/house_of_lore', './glibc_2.27/overlapping_chunks', './glibc_2.27/large_bin_attack', './glibc_2.27/unsorted_bin_attack', './glibc_2.27/unsorted_bin_into_stack', './glibc_2.27/house_of_einherjar', './glibc_2.27/tcache_dup', './glibc_2.27/tcache_poisoning', './glibc_2.27/tcache_house_of_spirit', './glibc_2.27/house_of_botcake', './glibc_2.27/tcache_stashing_unlink_attack', './glibc_2.27/fastbin_reverse_into_tcache', './glibc_2.27/mmap_overlapping_chunks', './glibc_2.27/fastbin_dup', './glibc_2.27/house_of_force', './glibc_2.27/poison_null_byte']
v31 = ['./glibc_2.31/unsafe_unlink', './glibc_2.31/overlapping_chunks', './glibc_2.31/house_of_einherjar', './glibc_2.31/tcache_poisoning', './glibc_2.31/tcache_house_of_spirit', './glibc_2.31/house_of_botcake', './glibc_2.31/tcache_stashing_unlink_attack', './glibc_2.31/fastbin_reverse_into_tcache', './glibc_2.31/mmap_overlapping_chunks', './glibc_2.31/fastbin_dup', './glibc_2.31/large_bin_attack', './glibc_2.31/house_of_lore']
ld = './ld-2.23.so'
libc = './libc-2.23.so'

def patch(binary):
    os.system('patchelf --set-interpreter {} {}'.format(ld, binary))

def chmod(binary):
    os.system('chmod +x {}'.format(binary))

def check(binary):
    if os.system('LD_PRELOAD={} {} > /dev/null 2>&1'.format(libc, binary))>>8 == 228:
        print('\x1b[1;32;40m[+] \x1b[0m{} succeed '.format(binary))
    else:
        print('\x1b[1;31;40m[-] \x1b[0m{} failed '.format(binary))

chmod(ld)
print('\x1b[1;33;40m[*]\x1b[0m 2.23')
for binary in v23:
    patch('{}'.format(binary))
    check('{}'.format(binary))
print('\x1b[1;33;40m[*]\x1b[0m 2.27')
for binary in v27:
    patch('{}'.format(binary))
    check('{}'.format(binary))
print('\n\x1b[1;33;40m[*]\x1b[0m 2.31')
for binary in v31:
    patch('{}'.format(binary))
    check('{}'.format(binary))
