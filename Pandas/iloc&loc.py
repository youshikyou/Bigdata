iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. 
So 0:10 will select entries 0,...,9. loc,meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.
