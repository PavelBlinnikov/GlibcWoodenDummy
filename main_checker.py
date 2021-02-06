import os
import descriptions
import argparse

v23 = ['./glibc_2.23/fastbin_dup_into_stack', './glibc_2.23/fastbin_dup_consolidate', './glibc_2.23/unsafe_unlink', './glibc_2.23/house_of_spirit', './glibc_2.23/poison_null_byte', './glibc_2.23/house_of_lore', './glibc_2.23/overlapping_chunks', './glibc_2.23/overlapping_chunks_2', './glibc_2.23/house_of_force', './glibc_2.23/large_bin_attack', './glibc_2.23/unsorted_bin_attack', './glibc_2.23/unsorted_bin_into_stack', './glibc_2.23/house_of_einherjar', './glibc_2.23/house_of_orange', './glibc_2.23/mmap_overlapping_chunks', './glibc_2.23/fastbin_dup', './glibc_2.23/house_of_roman']
v27 = ['./glibc_2.27/unsafe_unlink', './glibc_2.27/house_of_lore', './glibc_2.27/overlapping_chunks', './glibc_2.27/large_bin_attack', './glibc_2.27/unsorted_bin_attack', './glibc_2.27/unsorted_bin_into_stack', './glibc_2.27/house_of_einherjar', './glibc_2.27/tcache_dup', './glibc_2.27/tcache_poisoning', './glibc_2.27/tcache_house_of_spirit', './glibc_2.27/house_of_botcake', './glibc_2.27/tcache_stashing_unlink_attack', './glibc_2.27/fastbin_reverse_into_tcache', './glibc_2.27/mmap_overlapping_chunks', './glibc_2.27/fastbin_dup', './glibc_2.27/house_of_force', './glibc_2.27/poison_null_byte']
v31 = ['./glibc_2.31/unsafe_unlink', './glibc_2.31/overlapping_chunks', './glibc_2.31/house_of_einherjar', './glibc_2.31/tcache_poisoning', './glibc_2.31/tcache_house_of_spirit', './glibc_2.31/house_of_botcake', './glibc_2.31/tcache_stashing_unlink_attack', './glibc_2.31/fastbin_reverse_into_tcache', './glibc_2.31/mmap_overlapping_chunks', './glibc_2.31/fastbin_dup', './glibc_2.31/large_bin_attack', './glibc_2.31/house_of_lore']

def patch(binary):
    os.system('patchelf --set-interpreter {} {}'.format(ld, binary))

def chmod(binary):
    os.system('chmod +x {}'.format(binary))

def check(binary):
    if os.system('LD_PRELOAD={} {} > /dev/null 2>&1'.format(libc, binary))>>8 == 228:
        print('\x1b[1;32;40m[+] \x1b[0m{}'.format(binary))
        return True
    else:
        if debug == 2:
            print('\x1b[1;31;40m[-] \x1b[0m{}'.format(binary))
        return False
def checker(array):
    for binary in array:
        if not os.path.exists(binary):
            print('\x1b[1;31;40m[-] \x1b[0m {} not found, try to execute: make all'.format(binary))
            exit(0)
        patch('{}'.format(binary))
        if check('{}'.format(binary)):
            print('\t{}'.format(descriptions.descs[os.path.basename(binary)]))

parser = argparse.ArgumentParser(description='Check heap attacks')
parser.add_argument('--ld',
                       metavar='ld_path',
                       type=str,
                       help='path to ld')
parser.add_argument('--libc',
                       metavar='libc_path',
                       type=str,
                       help='path to libc')
parser.add_argument('--debug',
                       metavar='debug level',
                       type=str,
                       help='how much info to give, possible values: 1 or 2')
args = parser.parse_args()
if (not args.libc) or (not args.ld):
    parser.print_help()
    exit(1)
libc = args.libc
if not os.path.exists(libc):
    print('\x1b[1;31;40m[-] \x1b[0m libc path is invalid')
ld = args.ld
if not os.path.exists(ld):
    print('\x1b[1;31;40m[-] \x1b[0m ld path is invalid')
debug = args.debug
if not debug:
    debug = 1
else:
    debug = int(debug)
chmod(ld)
print('\x1b[1;33;40m[*]\x1b[0m 2.23')
checker(v23)
print('\n\x1b[1;33;40m[*]\x1b[0m 2.27')
checker(v27)
print('\n\x1b[1;33;40m[*]\x1b[0m 2.31')
checker(v31)
