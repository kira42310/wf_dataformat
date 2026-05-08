import netCDF4
import numpy as np
import zstandard as zstd

def list1d_to_netCDF4( data, filename, dtype = '<U8', mode = 'w', format = 'NETCDF4' ):

  np_data = np.array( data, dteyp = dtype )
  row = len( np_data )

  with netCDF4.Dataset( filename, mode, format = format ) as f:
    f.createDimension( 'row', row )
    data_var = f.createVariable( 'data', str, ( 'row', ) )
    data_var[:] = np_data

def list2d_to_netCDF4( data, filename, dtype = '<U8', transpose = False, header = False,  mode = 'w', format = 'NETCDF4' ):
  if header:
    h_data = np.array( data[0], dtype = str )
    np_data = np.array( data[1:], dtype = dtype )
  else:
    np_data = np.array( data, dtype = dtype )

  if transpose:
    np_data = np_data.T
    row = len( np_data[0] )
    column = len( np_data )
  else:
    row = len( np_data[0] )
    column = len( np_data )

  with netCDF4.Dataset( filename, mode, format = format ) as f:
    f.createDimension( 'row', row )
    f.createDimension( 'column', column )
    data_var = f.createVariable( 'data', str, ( 'row', 'column' ) )
    data_var[:] = np_data
    if header:
      header_var = f.createVariable( 'header', str, ( 1, 'column' ) )
      header_var[:] = h_data

def listmcol_to_netCDF4( data, filename, dtype = '<U8', transpose = False, header = False,  mode = 'w', format = 'NETCDF4' ):

  if header:
    h_data = np.array( data[0], dtype = str )
    np_data = np.array( data[1:], dtype = dtype )
  else:
    np_data = np.array( data, dtype = dtype )

  if transpose:
    np_data = np_data.T
    row = len( np_data[0] )
  else:
    row = len( np_data[0] )

  with netCDF4.Dataset( filename, mode, format = format ) as f:
    f.createDimension( 'row', row )
    if not header:
      h_data = np.arange( len( np_data ) ).astype( str )
    for i, h in enumerate( h_data ):
      data_var = f.createVariable( h, str, ( 'row', ) )
      data_var[:] = np_data[i]

def npmcol_to_netCDF4( data, filename, transpose = False, header = False, mode = 'w', format = 'NETCDF4', var_type = 'str' ):
  # if header:
  #   h_data = data[0]
  #   np_data = data[1:]
  
  if transpose:
    np_data = data.T
    row = len( np_data[0] )
  else:
    np_data = data
    row = len( np_data[0] )

  with netCDF4.Dataset( filename, mode, format = format ) as f:
    f.createDimension( 'row', row )
    if not header:
      h_data = np.arange( len( np_data ) ).astype( str )
    for i, h in enumerate( h_data ):
      data_var = f.createVariable( h, var_type, ( 'row', ) )
      data_var[:] = np_data[i]

def read_to_list( filename, mode = 'r' ):
  data = []
  with netCDF4.Dataset( filename, mode ) as f:
    header = f.variables.keys()
    for key in header:
      data.append( f.variables[key][:] )
  return data

def read_to_np( filename, mode = 'r' ):
  # np_data = np.array( [] )
  data = []
  with netCDF4.Dataset( filename, mode ) as f:
    header = f.variables.keys()
    for key in header:
      data.append( f.variables[key][:] )
      # np_data = np.append( np_data, [f.variables[key][:]], axis = 0 )
      # np_data = np.concatenate( ( np_data, f.variables[key][:] ), axis = 0 )
  return np.asarray( data )

# def np_to_netCDF4( ):

#start = time.time()
#np_data = np.array( data, dtype='<U8' )
#with netCDF4.Dataset( 'test_raw.nc', 'w', format='NETCDF4' ) as f:
#  #practice,bnf_code,bnf_name,items,nic,act_cost,quantity
#  size = len( np_data )
#  f.createDimension( 'row', size )
#  f.createDimension( 'column', 7 )
#  data_var = f.createVariable( 'data', str, ('row', 'column') )
#  data_var[:] = np_data
#stop = time.time()
#print( f'ndtcdf4 raw wirte netcdf4: {stop - start}' )
#print( os.path.getsize( 'test_raw.nc' ) )
#del(size)
#del(np_data)
#del(data)

# data = pd.read_pickle( 'test_pd.pkl' )
# start = time.time()
# data = data.to_numpy( dtype='<U10' )
# with netCDF4.Dataset( 'test_pd.nc', 'w', format='NETCDF4' ) as f:
#   #practice,bnf_code,bnf_name,items,nic,act_cost,quantity
#   size = len( data )
#   f.createDimension( 'row', size )
#   f.createDimension( 'column', 7 )
#   data_var = f.createVariable( 'data', str, ('row', 'column') )
#   data_var[:] = data
# stop = time.time()
# print( f'ndtcdf4 raw wirte netcdf4: {stop - start}' )
# print( os.path.getsize( 'test_pd.nc' ) )
