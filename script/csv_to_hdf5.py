import os
import csv
import pickle
import time
import h5py
import hdf5plugin
import numpy as np
import zstandard as zstd
import pandas as pd
import netCDF4

path = 'resize1g/'
files = os.listdir( path )

def few_print( a ):
  size = len( a )
  print( f'size: {size}' )
  if size > 5:
    for i in range( 5 ):
      print( a[i] )
  else:
    for i in a:
      print( i )

#data = []
#i = files[0]
#with open( path + i, 'r' ) as f: 
#  reader = csv.reader( f, delimiter=',' )
#  for row in reader:
#    data.append( row )
#for i in files[1:]:
#  with open( path + i, 'r' ) as f: 
#    reader = csv.reader( f, delimiter=',' )
#    next( reader )
#    for row in reader:
#      data.append( row )
#few_print( data )

#start = time.time()
#with open( 'test_raw.csv', 'w' ) as f:
#  writer = csv.writer( f, delimiter=',' )
#  for row in data:
#    writer.writerow( row )
#stop = time.time()
#print( f'csv write raw: {stop - start}' )
#print( os.path.getsize( 'test_raw.csv' ) )
#del( data )
#
#data = []
#start = time.time()
#with open( 'test_raw.csv', 'r' ) as f:
#  reader = csv.reader( f, delimiter=',' )
#  for row in reader:
#    data.append( row )
#stop = time.time()
#print( f'csv read raw:  {stop - start}' )
#few_print( data )
#
#start = time.time()
#with zstd.open( 'test_raw.csv.zst', 'w' ) as f:
#  writer = csv.writer( f, delimiter=',' )
#  for row in data:
#    writer.writerow( row )
#stop = time.time()
#print( f'csv write row zst: {stop - start}' )
#print( os.path.getsize( 'test_raw.csv.zst' ) )
#
#try:
#  start = time.time()
#  np_data = np.array( data )
#  with h5py.File( 'test_raw.h5', 'w' ) as f:
#    #f.create_dataset( 'data', data=data.astype('S10') )
#    f.create_dataset( 'data', data=np_data.astype('S10') )
#  stop = time.time()
#  print( f'hdf5 write row: {stop - start}' )
#  print( os.path.getsize( 'test_raw.h5' ) )
#except:
#  print( 'hdf5 raw write fail' )
#del(np_data)
#
#try:
#  start = time.time()
#  np_data = np.array( data )
#  with h5py.File( 'test_raw.h5.gzip', 'w' ) as f:
#    #f.create_dataset( 'data', data=data.astype('S10') )
#    f.create_dataset( 'data', data=np_data.astype('S10'), compression='gzip' )
#  stop = time.time()
#  print( f'hdf5 write row gzip: {stop - start}' )
#  print( os.path.getsize( 'test_raw.h5.gzip' ) )
#except:
#  print( 'hdf5 raw write gzip fail' )
#del(np_data)
#del(data)

#data = []
#start = time.time()
#with zstd.open( 'test_raw.csv.zst', 'r' ) as f:
#  reader = csv.reader( f, delimiter=',' )
#  for row in reader:
#    data.append( row )
#stop = time.time()
#print( f'csv read raw zst: {stop - start}' )
#few_print( data )
#del( data )

#data = []
#try:
#  start = time.time()
#  with h5py.File( 'test_raw.h5', 'r' ) as f:
#    data = f['data'].value
#  stop = time.time()
#  print( f'hdf5 read raw: {stop - start}' )
#  few_print( data )
#except:
#  print( 'hdf5 raw read fail' )
#del( data )
#
##data = []
#try:
#  start = time.time()
#  with h5py.File( 'test_raw.h5.gzip', 'r' ) as f:
#    data = f['data'].value
#  stop = time.time()
#  print( f'hdf5 read raw gzip: {stop - start}' )
#  few_print( data )
#except:
#  print( 'hdf5 raw read gzip fail' )
#del( data )

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

#df = pd.DataFrame()
#for i in files:
#  df = pd.concat( [ df, pd.read_csv( path + i ) ], ignore_index=True )
#print( df )

#start = time.time()
#df.to_csv( 'test_pd.csv', index=False )
#stop = time.time()
#print( f'csv pandas: {stop - start}' )
#print( os.path.getsize( 'test_pd.csv' ) )
#
#start = time.time()
#df.to_csv( 'test_pd.csv.zst', index=False, compression='zstd' )
#stop = time.time()
#print( f'csv write pandas zst: {stop - start}' )
#print( os.path.getsize( 'test_pd.csv.zst' ) )

#start = time.time()
#df.to_hdf( 'test_pd.h5', key='df' )
#stop = time.time()
#print( f'hdf5 write pandas: {stop - start}' )
#print( os.path.getsize( 'test_pd.h5' ) )
#
#start = time.time()
#df.to_hdf( 'test_pd.h5.zst', key='df', complib='blosc:zstd', complevel=6 )
#stop = time.time()
#print( f'hdf5 write pandas zst: {stop - start}' )
#print( os.path.getsize( 'test_pd.h5.zst' ) )
#
#start = time.time()
#df.to_pickle( 'test_pd.pkl' )
#stop = time.time()
#print( f'pickle write pandas: {stop - start}' )
#print( os.path.getsize( 'test_pd.pkl' ) )
#
#start = time.time()
#df.to_pickle( 'test_pd.pkl.zst', compression='zstd' )
#stop = time.time()
#print( f'pickle write pandas zst: {stop - start}' )
#print( os.path.getsize( 'test_pd.pkl.zst' ) )
#

data = pd.read_pickle( 'test_pd.pkl' )
start = time.time()
data = data.to_numpy( dtype='<U10' )
with netCDF4.Dataset( 'test_pd.nc', 'w', format='NETCDF4' ) as f:
  #practice,bnf_code,bnf_name,items,nic,act_cost,quantity
  size = len( data )
  f.createDimension( 'row', size )
  f.createDimension( 'column', 7 )
  data_var = f.createVariable( 'data', str, ('row', 'column') )
  data_var[:] = data
stop = time.time()
print( f'ndtcdf4 raw wirte netcdf4: {stop - start}' )
print( os.path.getsize( 'test_pd.nc' ) )

#del( df )
#
#start = time.time()
#df = pd.read_csv( 'test_pd.csv' )
#stop = time.time()
#print( f'csv read pandas: {stop - start}' )
#print( df )
#del( df )
#
#start = time.time()
#df = pd.read_csv( 'test_pd.csv.zst' )
#stop = time.time()
#print( f'csv read pandas zst: {stop - start}' )
#print( df )
#del( df )
#
#start = time.time()
#df = pd.read_hdf( 'test_pd.h5' )
#stop = time.time()
#print( f'hdf5 read pandas: {stop - start}' )
#print( df )
#del( df )
#
#start = time.time()
#df = pd.read_hdf( 'test_pd.h5.zst' )
#stop = time.time()
#print( f'hdf5 read pandas zst: {stop - start}' )
#print( df )
#del( df )

#start = time.time()
#df = pd.read_pickle( 'test_pd.pkl' )
#stop = time.time()
#print( f'pickle read pandas: {stop - start}' )
#print( df )
#del( df )
#
#start = time.time()
#df = pd.read_pickle( 'test_pd.pkl.zst' )
#stop = time.time()
#print( f'pickle read pandas zst: {stop - start}' )
#print( df )
#del( df )

#np_data = np.genfromtxt( path + files[0], delimiter=',', dtype=str )

#np_data = np.genfromtxt( path + files[0], delimiter=',', dtype=str )
#for f in files[1:]:
#  np_data = np.concatenate( ( np_data, np.genfromtxt( path + f, delimiter=',', dtype=str )[1:] ), axis = 0 )
#few_print( np_data )

#start = time.time()
#np.savetxt( 'test_np.csv', np_data.astype(str), delimiter=',', fmt='%s' )
#stop = time.time()
#print( f'csv write np: {stop - start}' )
#print( os.path.getsize( 'test_np.csv' ) )

#start = time.time()
#with zstd.open( 'test_np.csv.zst', 'w' ) as f:
#  np.savetxt( f, np_data.astype(str), delimiter=',', fmt='%s' )
#stop = time.time()
#print( f'csv write np zstd: {stop - start}' )
#print( os.path.getsize( 'test_np.csv.zst' ) )

#
#start = time.time()
#with h5py.File( 'test_np.h5', 'w' ) as f:
#  f.create_dataset( 'data', data=np_data.astype('S10') )
#stop = time.time()
#print( f'hdf5 write np: {stop - start}' )
#print( os.path.getsize( 'test_np.h5' ) )
#
#start = time.time()
#with h5py.File( 'test_np.h5.gzip', 'w' ) as f:
#  f.create_dataset( 'data', data=np_data.astype('S10'), compression='gzip' )
#stop = time.time()
#print( f'hdf5 write np gzip: {stop - start}' )
#print( os.path.getsize( 'test_np.h5.gzip' ) )
#
#start = time.time()
#with h5py.File( 'test_np.h5.zst', 'w' ) as f:
#  f.create_dataset( 'data', data=np_data.astype('S10'), **hdf5plugin.Zstd() )
#stop = time.time()
#print( f'hdf5 write np zstd: {stop - start}' )
#print( os.path.getsize( 'test_np.h5.zst' ) )

#start = time.time()
#with open( 'test_np.pkl', 'wb' ) as f:
#  pickle.dump( np_data.astype(str), f )
##  np.save( f, np_data )
##np.save( 'test_np.pkl', np_data )
#stop = time.time()
#print( f'pickle write np: {stop - start}' )
#print( os.path.getsize( 'test_np.pkl' ) )
#
#start = time.time()
#with zstd.open( 'test_np.pkl.zst', 'wb' ) as f:
#  pickle.dump( np_data.astype(str), f )
#  #np.save( f, np_data )
#stop = time.time()
#print( f'pickle write np zstd: {stop - start}' )
#print( os.path.getsize( 'test_np.pkl.zst' ) )

#del( np_data )
#start = time.time()
##np_data = np.genfromtxt( 'test_np.csv', delimiter=',', dtype=str )
#np_data = np.loadtxt( 'test_np.csv', delimiter=',', dtype=str )
#stop = time.time()
#print( f'csv read np: {stop - start}' )
#few_print( np_data )

#del( np_data )
#start = time.time()
#with zstd.open( 'test_np.csv.zst', 'r' ) as f:
#  np_data = np.loadtxt( f, delimiter=',', dtype=str )
#stop = time.time()
#print( f'csv read np: {stop - start}' )
#few_print( np_data )

#del( np_data )
#start = time.time()
#with h5py.File( 'test_np.h5', 'r' ) as f:
#  np_data = f['data'][()]
#stop = time.time()
#print( f'h5 read np: {stop - start}' )
#few_print( np_data )
#
#del( np_data )
#start = time.time()
#with h5py.File( 'test_np.h5.gzip', 'r' ) as f:
#  np_data = f['data'][()]
#stop = time.time()
#print( f'h5 read np gzip: {stop - start}' )
#few_print( np_data )
#
#del( np_data )
#start = time.time()
#with h5py.File( 'test_np.h5.zst', 'r' ) as f:
#  np_data = f['data'][()]
#stop = time.time()
#print( f'h5 read np zstd: {stop - start}' )
#few_print( np_data )
#
#del( np_data )
#start = time.time()
#with open( 'test_np.pkl', 'rb' ) as f:
#  np_data = pickle.load( f )
#stop = time.time()
#print( f'pickle read np: {stop - start}' )
#few_print( np_data )
#
#del( np_data )
#start = time.time()
#with zstd.open( 'test_np.pkl.zst', 'rb' ) as f:
#  np_data = pickle.load( f )
#stop = time.time()
#print( f'pickle read np zstd: {stop - start}' )
#few_print( np_data )

########################################

#with open( 'test.csv', 'r' ) as f:
#  reader = csv.reader( f, delimiter=',' )
#  for i in reader:
#    data.append( i )
#
#few_print( data )

#data = pd.read_csv( 'test.csv', dtype=str )
#print( data )
#data = data.to_numpy( dtype=str )
#few_print( data )
#print( data.dtype )

#start = time.time()
#with open( 'test.csv', 'w' ) as f:
#  writer = csv.writer( f, delimiter=',' )
#  for row in data:
#    writer.writerow( row )
#stop = time.time()
#print( f'csv write: {stop - start}' )
#print( os.path.getsize( 'test.csv' ) )

#start = time.time()
##with open( 'test.pkl', 'wb' ) as f:
#with zstd.open( 'test.pkl.zst', 'wb' ) as f:
#  pickle.dump( data, f )
#stop = time.time()
#print( f'pickle write: {stop - start}' )
#print( os.path.getsize( 'test.pkl' ) )
#

#start = time.time()
#with h5py.File( 'test.h5', 'w' ) as f:
#  #dt = h5py.special_dtype( vlen=str )
#  #f.create_dataset( 'data', data=data, dtype=dt )
#  f.create_dataset( 'data', data=data.astype('S10') )
#stop = time.time()
#print( f'hdf5 write: {stop - start}' )
#print( os.path.getsize( 'test.h5' ) )

#
#
#del( data )
#data = []
#start = time.time()
#with open( 'test.csv', 'r' ) as f:
#  reader = csv.reader( f, delimiter=',' )
#  for row in reader:
#    data.append( row )
#stop = time.time()
#print( f'csv read: {stop - start}' )
#few_print( data )
#
#del( data )
#data = []
#start = time.time()
#with open( 'test.pkl', 'rb' ) as f:
#  data = pickle.load( f )
#stop = time.time()
#print( f'pickle read: {stop - start}' )
#few_print( data )
#
#del( data )
#data = []
#start = time.time()
#with h5py.File( 'test.h5', 'r' ) as f:
#  data = f['data'].value
#stop = time.time()
#print( f'hdf5 read: {stop - start}' )
#few_print( data )
#
