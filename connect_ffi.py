from cffi import FFI
ffi = FFI()

#Header generated with cpp spotify.h > spotify.processed.h && sed -i 's/__extension__//g' spotify.processed.h
with open("spotify.processed.h") as file:
    header = file.read()

ffi.cdef(header)
ffi.cdef("""
void *malloc(size_t size);
void exit(int status);
""")

C = ffi.dlopen(None)
lib = ffi.verify("""
    #include "spotify.h"
""", include_dirs=['./'],
    library_dirs=['./'],
    libraries=[str('spotify_embedded_shared')])