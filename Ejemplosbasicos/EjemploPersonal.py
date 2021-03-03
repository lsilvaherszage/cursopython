import Personal
from datetime import date
per=Personal.Administrativo("Rubén", "Paz", date(1970, 5, 11))

dir1=Personal.Directivo("dir1", "dir1", date(1980, 2,8))
dir2=Personal.Directivo("dir2", "dir2", date(1999, 5,18))

doc1=Personal.Docente("doc1", "doc1", date(1988, 5, 28), "P5A", dir1)
doc2=Personal.Docente("doc2", "doc2", date(1988, 5, 28), "P6B", dir1)
doc3=Personal.Docente("doc3", "doc3", date(1988, 5, 28), "S1A", dir2)

print(dir2)
dir2.listarPersonal()