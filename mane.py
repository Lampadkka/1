def kk (s):
  adict = {}
  for i in s:
      if adict.get(i,0) !=0:
          adict[i] +=1
      else:
          adict[i] = 1
  for j  in adict:
      print(j,adict[j])

kk('abcdddd')