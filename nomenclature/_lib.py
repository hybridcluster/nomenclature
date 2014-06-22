import pkgutil

from cffi import FFI

ffi = FFI()
ffi.cdef(pkgutil.get_data('nomenclature', 'c/cdef.h').decode('ascii'))
lib = ffi.verify(pkgutil.get_data('nomenclature', 'c/verify.h').decode('ascii'),
ext_package='nomenclature',
)

__all__ = ('lib', 'ffi')
