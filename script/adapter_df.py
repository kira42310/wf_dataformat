import pandas as pd
import zstandard as zstd

def to_raw_csv( df, filename, index = False, compression = False ):
  if compression:
    df.to_csv( filename, index = index, compression = 'zstd' )
  else:
    df.to_csv( filename, index = index )

def to_hdf( df, filename, key, compression = False, complib = 'blosc:zstd', complevel = 6 ):
  if compression:
    df.to_hdf( filename, key = key, complib = complib, complevel = complevel )
  else:
    df.to_hdf( filename, key = key )

def to_pkl( df, filename, compression = False ):
  if compression:
    df.to_pickle( filename, compression = 'zstd' )
  else:
    df.to_pickle( filename )

def read_csv( filename ):
  # Can read both uncompress and compress file
  return pd.read_csv( filename )

def read_hdf( filename, key ):
  # Can read both uncompress and compress file
  return pd.read_hdf( filename, key = key )

def read_pkl( filename ):
  # Can read both uncompress and compress file
  return pd.read_pickle( filename )
