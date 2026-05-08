import h5py
import hdf5plugin
import zstandard as zstd
import numpy as np

def list_to_hdf( data, filename, key, mode = 'w', dtype = 'S10', compression = False ):
  np_data = np.array( data )
  if compression:
    with h5py.File( filename, mode ) as f:
      f.create_dataset( key, data = np_data.astype( dtype ), **hdf5plugin.Zstd() )
  else:
    with h5py.File( filename, mode ) as f:
      f.create_dataset( key, data = np_data.astype( dtype ) )

def read_to_list( filename, key, mode = 'r' ):
  # Can read both uncompress and compress
  data = []
  with h5py.File( filename, mode ) as f:
    data = f[ key ][()]
  return data
