import numpy as np
import zstandard as zstd

def to_csv( data: np.ndarray, filename, mode = 'w', delimiter = ',', dtype = str, fmt = '%s', compression = False ):
  if compression:
    with zstd.open( filename, mode ) as f:
      np.savetxt( f, data.astype( dtype ), delimiter = delimiter, fmt = fmt )
  else:
    np.savetxt( filename, data.astype( dtype ), delimiter = delimiter, fmt = fmt )

def read( filename, mode = 'r', delimiter = ',', dtype = str, compression = False ) -> np.ndarray:
  if compression:
    with zstd.open( filename, mode ) as f:
      return np.loadtxt( f, delimiter = delimiter, dtype = dtype )
  else:
    return np.loadtxt( filename, delimiter = delimiter, dtype = dtype )
