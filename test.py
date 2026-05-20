import script.adapter_csv
import script.adapter_df
import script.adapter_hdf5
import script.adapter_netcdf
import script.adapter_np
import script.adapter_pickle

import pandas as pd
import numpy as np

data_dir = "data/"

report = []

try:
  data = script.adapter_csv.read_to_list_exper( data_dir + 'test_noh.csv'  )
  #print( data )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

try:
  script.adapter_csv.list_to_csv( data, data_dir + 'test_noh_.csv' )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

try:
  script.adapter_csv.list_to_csv( data, data_dir + 'test_noh_.csv.zst', compression = True )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

del( data )

########################################

try:
  data = script.adapter_csv.read_to_list_exper( data_dir + 'test_noh_.csv.zst', compression = True )
  #print( data )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

df = pd.DataFrame( data )
#df = script.adapter_df.read_csv( data_dir + 'test_df_noh_.csv' )

########################################

try:
  script.adapter_df.to_raw_csv( df, data_dir + 'test_df_noh_.csv' )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

try:
  script.adapter_df.to_raw_csv( df, data_dir + 'test_df_noh_.csv.zst', compression = True )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

#######################################

try:
  script.adapter_df.to_hdf( df, data_dir + 'test_df_noh_.h5', 'noh' )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

# Failed
try:
  script.adapter_df.to_hdf( df, data_dir + 'test_df_noh_.h5.zst', 'noh', compression = True, complevel = 5 )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

try:
  script.adapter_df.to_pkl( df, data_dir + 'test_df_noh_.pkl' )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

try:
  script.adapter_df.to_pkl( df, data_dir + 'test_df_noh_.pkl.zst', compression = True )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

del( df )

########################################

try:
  df = script.adapter_df.read_csv( data_dir + 'test_noh_.csv' )
  #print( df )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

del( df )

########################################

try:
  df = script.adapter_df.read_csv( data_dir + 'test_df_noh_.csv' )
  #print( df )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

del( df )

########################################

try:
  df = script.adapter_df.read_csv( data_dir + 'test_df_noh_.csv.zst' )
  #print( df )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

del( df )

########################################

try:
  df = script.adapter_df.read_hdf( data_dir + 'test_df_noh_.h5', 'noh' )
  #print( df )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

del( df )

########################################

# Failed: write function failed
try:
  df = script.adapter_df.read_hdf( data_dir + 'test_df_noh_.h5.zst', 'noh' )
  #print( df )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

del( df )

########################################

try:
  df = script.adapter_df.read_pkl( data_dir + 'test_df_noh_.pkl' )
  #print( df )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

del( df )

########################################

try:
  df = script.adapter_df.read_pkl( data_dir + 'test_df_noh_.pkl.zst' )
  #print( df )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

#data = df.values.tolist()
del( df )

########################################

try:
  script.adapter_hdf5.list_to_hdf( data, data_dir + 'test_noh_.h5', 'noh' )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

try:
  script.adapter_hdf5.list_to_hdf( data, data_dir + 'test_noh_.h5.zst', 'noh', compression = True )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

try:
  tmp = script.adapter_hdf5.read_to_list( data_dir + 'test_noh_.h5', 'noh' )
  #print( tmp )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

del( tmp )

########################################

try:
  tmp = script.adapter_hdf5.read_to_list( data_dir + 'test_noh_.h5.zst', 'noh' )
  #print( tmp )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

del( tmp )
#data = script.adapter_csv.read_to_list_exper( data_dir + 'test_noh.csv'  )

# #######################################
# 
# # Failed
# try:
#   script.adapter_netcdf.listmcol_to_netCDF4( data, data_dir + 'test_noh_.nc' )
#   report.append( 1 )
# except Exception as e:
#   print( e )
#   report.append( e )
# print( report )
# 
# #######################################
# 
# # try:
# #   script.adapter_netcdf.listmcol_to_netCDF4( data, data_dir + 'test_noh_.nc.zst', compression = True )
# #   report.append( 1 )
# # except Exception as e:
# #   print( e )
# #   report.append( e )
# 
# ########################################
# 
np_data = np.array( data, dtype = str )
# 
# ########################################
# 
# # Failed
# try:
#   script.adapter_netcdf.npmcol_to_netCDF4( np_data, data_dir + 'test_np_noh_.nc' )
#   report.append( 1 )
# except Exception as e:
#   print( e )
#   report.append( e )
# print( report )
# 
# #######################################
# 
# # try:
# #   script.adapter_netcdf.npmcol_to_netCDF4( np_data, data_dir + 'test_np_noh_.nc', compression = True )
# #   report.append( 1 )
# # except Exception as e:
# #   print( e )
# #   report.append( e )
# 
# ########################################
# 
# 
# ########################################
# 
# # Failed
# try:
#   tmp = script.adapter_netcdf.read_to_list( data_dir + 'test_noh_.nc' )
#   #print( tmp )
#   report.append( 1 )
# except Exception as e:
#   print( e )
#   report.append( e )
# print( report )
# 
# #######################################
# 
# del( tmp )
# 
# #######################################
# 
# # try:
# #   tmp = script.adapter_netcdf.read_to_list( data_dir + 'test_noh_.nc', compression = True )
# #   print( tmp )
# #   report.append( 1 )
# # except Exception as e:
# #   print( e )
# #   report.append( e )
# 
# # ########################################
# 
# # del( tmp )
# 
# # ########################################
# 
# # Failed
# try:
#   tmp = script.adapter_netcdf.read_to_np( data_dir + 'test_np_noh_.nc' )
#   #print( tmp )
#   report.append( 1 )
# except Exception as e:
#   print( e )
#   report.append( e )
# print( report )
# 
# ########################################
# 
# del( tmp )
# 
# ########################################

# try:
#   tmp = script.adapter_netcdf.read_to_np( data_dir + 'test_np_noh_.nc', compression = True )
#   print( tmp )
#   report.append( 1 )
# except Exception as e:
#   print( e )
#   report.append( e )

# ########################################

# del( tmp )

# ########################################

try:
  script.adapter_np.to_csv( np_data, data_dir + 'test_np_noh_.csv' )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

try:
  script.adapter_np.to_csv( np_data, data_dir + 'test_np_noh_.csv.zst', compression = True )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

try:
  tmp = script.adapter_np.read( data_dir + 'test_np_noh_.csv' )
  #print( tmp )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

del( tmp )

########################################

try:
  tmp = script.adapter_np.read( data_dir + 'test_np_noh_.csv.zst', compression = True )
  #print( tmp )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

# del( tmp )

########################################

try:
  script.adapter_pickle.to_pickle( data, data_dir + 'test_noh_.pkl' )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

try:
  script.adapter_pickle.to_pickle( data, data_dir + 'test_noh_.pkl.zst', compression = True )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

try:
  tmp = script.adapter_pickle.read( data_dir + 'test_noh_.pkl' )
  #print( tmp )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

# del( tmp )

########################################

try:
  tmp = script.adapter_pickle.read( data_dir + 'test_noh_.pkl.zst', compression = True )
  #print( tmp )
  report.append( 1 )
except Exception as e:
  print( e )
  report.append( e )
print( report )

########################################

# del( tmp )

########################################

for i, n in enumerate( report ):
  print( i, n )
