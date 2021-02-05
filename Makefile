V2.23 = glibc_2.23/fastbin_dup_into_stack glibc_2.23/fastbin_dup_consolidate glibc_2.23/unsafe_unlink glibc_2.23/house_of_spirit glibc_2.23/poison_null_byte glibc_2.23/house_of_lore glibc_2.23/overlapping_chunks glibc_2.23/overlapping_chunks_2 glibc_2.23/house_of_force glibc_2.23/large_bin_attack glibc_2.23/unsorted_bin_attack glibc_2.23/unsorted_bin_into_stack glibc_2.23/house_of_einherjar glibc_2.23/house_of_orange glibc_2.23/mmap_overlapping_chunks glibc_2.23/fastbin_dup glibc_2.23/house_of_roman
V2.27 = glibc_2.27/unsafe_unlink glibc_2.27/house_of_lore glibc_2.27/overlapping_chunks glibc_2.27/large_bin_attack glibc_2.27/unsorted_bin_attack glibc_2.27/unsorted_bin_into_stack glibc_2.27/house_of_einherjar glibc_2.27/tcache_dup glibc_2.27/tcache_poisoning glibc_2.27/tcache_house_of_spirit glibc_2.27/house_of_botcake glibc_2.27/tcache_stashing_unlink_attack glibc_2.27/fastbin_reverse_into_tcache glibc_2.27/mmap_overlapping_chunks glibc_2.27/fastbin_dup glibc_2.27/house_of_force glibc_2.27/poison_null_byte
V2.31 = glibc_2.31/unsafe_unlink glibc_2.31/overlapping_chunks glibc_2.31/house_of_einherjar glibc_2.31/tcache_poisoning glibc_2.31/tcache_house_of_spirit glibc_2.31/house_of_botcake glibc_2.31/tcache_stashing_unlink_attack glibc_2.31/fastbin_reverse_into_tcache glibc_2.31/mmap_overlapping_chunks glibc_2.31/fastbin_dup glibc_2.31/large_bin_attack glibc_2.31/house_of_lore

PROGRAMS = $(V2.23) $(V2.27) $(V2.31)

all: $(PROGRAMS)
clean:
		rm -f $(PROGRAMS)
