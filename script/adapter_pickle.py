import pickle
import zstandard as zstd

def to_pickle( data, filename, mode = 'wb', compression = False ):
  # If dump numpy use data.astype(str)
  buffers = []
  if compression:
    with zstd.open( filename, mode ) as f:
      pickle.dump( data, f, protocol = pickle.HIGHEST_PROTOCOL, buffer_callback = buffers.append )
  else:
    with open( filename, mode ) as f:
      pickle.dump( data, f, protocol = pickle.HIGHEST_PROTOCOL, buffer_callback = buffers.append )

def read( filename, mode = 'rb', compression = False ):
  if compression:
    with zstd.open( filename, mode ) as f:
      tmp = pickle.load( f )
  else:
    with open( filename, mode ) as f:
      tmp = pickle.load( f )
  return tmp

def read_exper( filename, mode = 'rb', compression = False ):
  buffers = []
  if compression:
    opener = zstd.open
  else:
    opener = open
  with opener( filename, mode ) as f:
    tmp = pickle.load( f, buffers = buffers )
  return tmp
