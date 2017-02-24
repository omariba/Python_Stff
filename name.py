import os

for f in os.listdir('.'):
    if f.endswith(' with English Subbed at Gogoanime.mp4'):
        newname = f[:21]
        ext = '.mp4'
        fname = newname + ext
        os.rename(f, fname)
    elif f.endswith(' with English Subbed at Gogoanime.flv'):
        newname = f[:21]
        ext = '.flv'
        fname = newname + ext
        os.rename(f, fname)
    elif f.startswith('(480P - mp4)') or f.startswith('(360P - mp4)'):
        newname = f[12:]
        os.rename(f, newname)


