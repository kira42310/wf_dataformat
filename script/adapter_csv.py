import csv
import zstandard as zstd

def list_to_csv( data, filename, mode = 'w',  delimiter = ',', compression = False ):
  if compression:
    with zstd.open( filename, mode ) as f:
      writer = csv.writer( f, delimiter = delimiter )
      for row in data:
        writer.writerow( row )
  else:
    with open( filename, mode ) as f:
      writer = csv.writer( f, delimiter = delimiter )
      for row in data:
        writer.writerow( row )

def read_to_list( filename, mode = 'r', delimiter = ',' ):
  data = []
  with open( filename, mode ) as f:
    reader = csv.reader( f, delimiter = delimiter )
    for row in reader:
      data.append( row )
  return data

def read_compress_to_list( filename, mode = 'r', delimiter = ',' ):
  data = []
  with zstd.open( filename, mode ) as f:
    reader = csv.reader( f, delimiter = delimiter )
    for row in reader:
      data.append( row )
  return data

def read_to_list_exper( filename, mode = 'r', delimiter = ',', compression = False ):
  if compression:
    opener = zstd.open
  else:
    opener = open
  data = []
  with opener( filename, mode ) as f:
    reader = csv.reader( f, delimiter = delimiter )
    for row in reader:
      data.append( row )
  return data
