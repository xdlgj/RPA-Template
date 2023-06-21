from threading import local


out_aa = 1
g = locals()
_cw={}

for l in list(g):
    if l.startswith('out_'):
        _cw[l]=g[l]
print(_cw)

